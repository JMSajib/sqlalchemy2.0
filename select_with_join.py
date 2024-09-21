from main import session
from models import User, Comment
from sqlalchemy import select


statement = select(User).join(User.comments).where(User.username == 'Sajib').where(Comment.text == 'Hello World')

result = session.scalars(statement).one()

if result.comments:
    for comment in result.comments:
        print(comment)