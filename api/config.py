import os 

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

name = "app.db"

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(root_dir, name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False