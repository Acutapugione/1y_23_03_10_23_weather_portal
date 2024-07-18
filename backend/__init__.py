from os import getenv
from dotenv import load_dotenv
from flask import Flask

# from flask_mail import Mail, Message
# from flask_cors import CORS
from .config import Config
from .utils import WeatherApiETL

load_dotenv()

app = Flask(
    __name__,
    static_folder=Config.static_folder,
    template_folder=Config.template_folder,
)
app.config.from_object(Config)
etl = WeatherApiETL(api_key=getenv("API_KEY"))

# CORS(app)
from . import routes

if __name__ == "__main__":
    app.run(debug=int(getenv("DEBUG")), port=int(getenv("PORT")))
