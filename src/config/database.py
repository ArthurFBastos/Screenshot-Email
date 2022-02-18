import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "login": os.getenv("login"),
    "password": os.getenv("senha"),



}