# 🔐 One-Time Secret Sharing Platform

A secure, one-time secret sharing web application built with **Flask**, **MongoDB Compass**, **Python Cryptography**, and **Email/QR support**. Share messages and files that **self-destruct** after one view or a time limit.

---

## 💡 Features

- ✉️ Send secrets and optional files via one-time links
- ⏳ Links auto-expire after first view or time limit
- 🔒 AES encryption using Python's `cryptography` library
- 🧾 File download only after viewing secret
- 📧 Email notifications to recipient (optional)
- 📷 QR code for quick access to secrets
- 🖼️ Beautiful, responsive UI with animated buttons and gradients
- ❌ Prevent recipient from navigating back to home page

---

## 🚀 Live Demo (Optional)
> Coming Soon (If you deploy on Vercel, Render, etc.)

---

## 📦 Tech Stack

| Layer         | Tech                             |
|---------------|----------------------------------|
| Backend       | Flask (Python)                   |
| Frontend      | HTML, CSS, Jinja, JavaScript     |
| Database      | MongoDB (via MongoDB Compass)    |
| Encryption    | cryptography (Fernet AES)        |
| Email         | Gmail SMTP with App Password     |
| QR Code       | `qrcode` Python library          |

---

## 🛠 Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/your-username/secret-share-app.git
cd secret-share-app
✅ 2. Install Dependencies
Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # On Windows use `venv\Scripts\activate`
Then install:

bash
Copy
Edit
pip install -r requirements.txt
✅ 3. Setup MongoDB Compass
Download MongoDB Compass

Create a DB called: one_time_secret_database

It will auto-create the secrets collection on first insert.

✅ 4. Configure Your config.py
Create a file named config.py:

python
Copy
Edit
# config.py

from cryptography.fernet import Fernet
fernet = Fernet(b'your-generated-key')

EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-gmail-app-password"
💡 Generate Fernet key using:

python
Copy
Edit
from cryptography.fernet import Fernet
print(Fernet.generate_key())
✅ 5. Run the App
bash
Copy
Edit
python app.py
Visit http://localhost:5000

📁 Folder Structure
arduino
Copy
Edit
.
├── app.py
├── config.py
├── uploads/
├── templates/
│   ├── index.html
│   ├── success.html
│   ├── view.html
│   └── error.html
├── static/
│   ├── style.css
│   └── qr_xxxxx.png (dynamic)
├── requirements.txt
└── README.md
✨ Screenshots
Page	Preview
Home	Form to enter secret + file
Success	Shows link + QR code + copy button
View Secret	Displays secret + download file button
Expired	Shows error message with restart link
🛡️ Security Notes
All secrets and files are encrypted using AES symmetric key (Fernet)

Secrets are deleted (marked as viewed) after first access

Files are stored with UUID + original name to avoid conflicts

QR codes are locally generated and not shared externally

📬 Email Notes
You must enable 2FA in your Gmail account

Generate a Gmail App Password (like psoj hfyi lwrl hkkj)

Add this to config.py under EMAIL_PASSWORD

📱 Mobile Responsive?
✅ Yes! The entire UI is designed to work on both desktop and mobile.

🚀 Future Improvements
✅ PWA support (installable app)

✅ Secret analytics dashboard

✅ Password protection for secrets

✅ Expire after custom events (e.g. 1 hour)

✅ Dark mode

💬 Support
Feel free to open an issue or reach out to yourname@domain.com