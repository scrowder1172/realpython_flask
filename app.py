from flask import Flask
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)


@app.route("/")
def index():
    secret_key = app.config.get('SECRET_KEY')
    debug_level = app.config.get('DEBUG')
    development = app.config.get('DEVELOPMENT')
    return f"Hello world! My super secret key is: {secret_key}. This code is running as {env_config}. " \
           f"Debug level is: {debug_level}. Development is {development}"


if __name__ == "__main__":
    app.run()
