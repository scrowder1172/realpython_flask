# Background
Flask tutorial series from RealPython

# Link
https://realpython.com/learning-paths/flask-by-example/

## Version 1
The first version of the app creates a basic web page that returns
a secret key from an environment variable, describes the code 
environment, describes the debug level, and tells whether the code 
is for development or not.

dotenv is imported to load environment variables from .env
However this may not be required as environment variables were read
without calling load_dotenv()

config.py contains some "configuration" information for the script 
that really doesn't do anything, but it provides an example of how 
to store configuration data in a project file.

If there isn't an environment variable defined in .env for 
APP_SETTING, the program defaults to the DevelopmentConfig. 
When setting APP_SETTING, be sure to match it to one of the classes in 
config.py or else the application will fail and/or won't load.

If SECRET_KEY is not defined in .env, then a default key will be returned


