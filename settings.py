import os 

if os.path.exists("env.py"):
    import env


SECRET_KEY = os.environ.get('SECRET_KEY', 'any_secret_key_1')