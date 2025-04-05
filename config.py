#from cryptography.fernet import Fernet

# Generate a key ONCE and keep it safe.
# Use Fernet.generate_key() in Python to get this key.
#KEY = b'9L4H7pVYEWI7F8JgE4MAW0O1UbBnX4lil2bwJoeFOZk='  # Replace with your actual key
#fernet = Fernet(KEY)

# Email credentials for sending notifications
#EMAIL_USER = "p69875565@gmail.com"  # Replace with your email address
#EMAIL_PASSWORD = "psoj hfyi lwrl hkkj"  # Your Gmail app password

# App name or secret identifier (can be used for branding or internal purposes)
#APP_NAME = "secret"

# Paths or directories (ensure these exist in your project folder)
#UPLOAD_FOLDER = 'uploads'
#QR_CODE_FOLDER = 'static/qr_codes'

# Database configuration (MongoDB example, if using MongoDB)
#DB_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
#DB_NAME = "one_time_secret_database"  # Database name
#SECRET_COLLECTION = "secrets"  # MongoDB collection for storing secrets

# Optional: Set up logging (for debugging or error tracking)
#import logging
#logging.basicConfig(level=logging.DEBUG)  # Set to ERROR in production

# Optional: Set your secret expiry time (e.g., 24 hours)
#SECRET_EXPIRY_TIME = 24 * 60 * 60  # 24 hours in seconds






from cryptography.fernet import Fernet

# Your encryption key (generate using Fernet.generate_key())
SECRET_KEY = b'9L4H7pVYEWI7F8JgE4MAW0O1UbBnX4lil2bwJoeFOZk='
fernet = Fernet(SECRET_KEY)

# Email settings
EMAIL_USER = "p69875565@gmail.com"
EMAIL_PASSWORD = "psoj hfyi lwrl hkkj"  # Gmail App Password
APP_NAME = "secret"
