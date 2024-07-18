from dotenv import load_dotenv
from os import getenv

load_dotenv()


class Config:
    DEBUG = int(getenv("DEBUG"))
    PORT = int(getenv("PORT"))
    static_folder = "../frontend/static/"
    template_folder = "../frontend/templates/"
    # template_folder = "../frontend/templates/"
    # STATIC_FOLDER = "frontend/static/"
    # template_folder = "frontend/templates"
