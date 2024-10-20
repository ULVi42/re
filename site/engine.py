from sqlmodel import create_engine,SQLModel


engine = create_engine('sqlite:///database.db')

SQLModel.metadata.create_all(engine)