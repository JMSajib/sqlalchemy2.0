from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///sample.db", echo=True)
# engine = create_engine("postgresql://postgres:mysecretpassword@127.0.0.1:5432/sql2", echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))
    print(result.all())