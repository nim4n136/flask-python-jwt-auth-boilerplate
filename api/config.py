import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    
    # General Config
    DEBUG =  (os.getenv("DEBUG", True).lower() == "true")
    SECRET_KEY = os.getenv("SECRET_KEY", "ANUDS8w7dwf9a9vlv-w.tlfr9k8rwcqo2")

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_BINDS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False