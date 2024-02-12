import os
from dotenv import load_dotenv

class Settings:
    load_dotenv()
    token=os.getenv("TOKEN")

settings=Settings()