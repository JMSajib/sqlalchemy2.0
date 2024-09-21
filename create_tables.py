from models import Base, User, Comment
from connect import engine


print("******* Createing Tables ******")
Base.metadata.create_all(bind=engine)