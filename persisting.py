from models import User, Comment
from main import session


user1 = User(
    username="Sajib",
    email_address="sajib@gamil.com",
    comments = [
        Comment(text="Hello World"),
        Comment(text="Please Subscribe")
    ]
)

user2 = User(
    username=" Jahidul Sajib",
    email_address="jahidul@gamil.com",
    comments = [
        Comment(text="Hello World77"),
        Comment(text="Please Subscribe77")
    ]
)

session.add_all([user1,user2])
session.commit()