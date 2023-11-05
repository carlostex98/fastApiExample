import os
from dotenv import load_dotenv

load_dotenv()
# configuracion bucket s3
URL_BUCKET = os.getenv('URL_BUCKET')
S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
S3_SECRET_KEY = os.getenv('S3_SECRET_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')

# configuracion BD
DATABASE = os.getenv('DATABASE')
DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_USER = os.getenv('DATABASE_USER')

# configuracion correo_electronico
SMTP_PORT = os.getenv('SMTP_PORT')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_SENDER_EMAIL = os.getenv('SMTP_SENDER_EMAIL')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
