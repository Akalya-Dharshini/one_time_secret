# app.py
import os
import uuid
import base64
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, send_file
from pymongo import MongoClient
from config import fernet, EMAIL_USER, EMAIL_PASSWORD
import smtplib
from email.mime.text import MIMEText
import qrcode
from io import BytesIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client.one_time_secret_database
secrets_collection = db.secrets

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def send_email_notification(to_email, access_link):
    try:
        msg = MIMEText(f"You've received a one-time secret! Click here to view it: {access_link}")
        msg['Subject'] = '🔐 You’ve Received a One-Time Secret!        It will expire after one view or the set time limit.'
        msg['From'] = EMAIL_USER
        msg['To'] = to_email

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print("Email error:", e)

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route("/create", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        secret = request.form["secret"]
        expire_minutes = int(request.form["expire"])
        email = request.form.get("email")
        uploaded_file = request.files.get("file")

        # Encrypt the secret
        encrypted_secret = fernet.encrypt(secret.encode()).decode()

        # Handle file if uploaded
        file_name = None
        encrypted_file = None
        if uploaded_file and uploaded_file.filename:
            file_data = uploaded_file.read()
            encrypted_file = fernet.encrypt(file_data)
            file_name = uploaded_file.filename

        secret_id = str(uuid.uuid4())
        expire_time = datetime.utcnow() + timedelta(minutes=expire_minutes)

        # Save to DB
        secrets_collection.insert_one({
            "_id": secret_id,
            "secret": encrypted_secret,
            "expire_at": expire_time,
            "viewed": False,
            "file": encrypted_file,
            "file_name": file_name,
            "email": email
        })

        link = request.url_root + "view/" + secret_id

        # Generate QR code
        qr = qrcode.make(link)
        qr_io = BytesIO()
        qr.save(qr_io, 'PNG')
        qr_data = base64.b64encode(qr_io.getvalue()).decode()
        qr_url = f"data:image/png;base64,{qr_data}"

        # Send notification
        if email:
            send_email_notification(email, link)

        return render_template("success.html", link=link, qr_url=qr_url)
    return render_template("index.html")

@app.route("/view/<secret_id>")
def view_secret(secret_id):
    data = secrets_collection.find_one({"_id": secret_id})

    if not data or data["viewed"] or data["expire_at"] < datetime.utcnow():
        return render_template("view.html", secret=None)

    # Mark as viewed
    secrets_collection.update_one({"_id": secret_id}, {"$set": {"viewed": True}})

    # Decrypt secret
    decrypted_secret = fernet.decrypt(data["secret"].encode()).decode()

    # Decrypt file if exists
    file_data = None
    file_name = None
    if data.get("file"):
        decrypted_file = fernet.decrypt(data["file"])
        file_data = "data:application/octet-stream;base64," + base64.b64encode(decrypted_file).decode()
        file_name = data.get("file_name")

    # QR not needed here, but you can re-display if you want
    return render_template("view.html", secret=decrypted_secret, file_data=file_data, file_name=file_name, qr_url=None)

if __name__ == "__main__":
    app.run(debug=True)
