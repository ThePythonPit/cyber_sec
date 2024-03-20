# test_dotenv.py
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("SQLALCHEMY_DATABASE_URI"))
