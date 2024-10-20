from sqlmodel import SQLModel,Field,Relationship
from passlib.context import CryptContext
from typing import List
from engine import engine

SQLModel.metadata.create_all(engine)

qwert= CryptContext(schemes=["bcrypt"],deprecated="auto")

class User(SQLModel,table=True):
    id: int=Field(default=None,primary_key=True)
    username: str=Field(default=None)
    hashed_password: str=Field(default=None)
    role: str=Field(default="user")

    def hashing_password(password):
        hashed_password=qwert.hash(password)
        
    def verify_password(hashed_password):
        password=qwert.hash(hashed_password)   

    posts: List["Post"]=Relationship(back_populates="owner")
    comments: List["Comment"]=Relationship(back_populates="owner")
    reactions: List["Reaction"]=Relationship(back_populates="owner")
    responses: List["Response"]=Relationship(back_populates="owner")


class Post(SQLModel,table=True):
    id: int=Field(default=None,primary_key=True)
    title: str
    image_link: str
    text: str
    owner_id: int = Field(foreign_key="user.id")

    owner: User=Relationship(back_populates="posts")
    comments: List["Comment"]=Relationship(back_populates="post")
    reactions: List["Reaction"]=Relationship( back_populates="post")



class Comment(SQLModel,table=True):
    id: int=Field(default=None,primary_key=True)
    text: str 
    owner_id: int = Field(foreign_key="user.id")
    post_id: int = Field(foreign_key="post.id")

    owner: User=Relationship(back_populates="comments")
    responses: List["Response"]=Relationship(back_populates="comment")
    post: Post=Relationship(back_populates="comments")

class Response(SQLModel,table=True):
    id: int=Field(default=None,primary_key=True)
    text: str 
    owner_id: int = Field(foreign_key="user.id")
    comment_id: int = Field(foreign_key="comment.id")

    owner: User=Relationship(back_populates="responses")
    comment: Comment=Relationship(back_populates="responses")

class Reaction(SQLModel,table=True):
    id: int=Field(default=None,primary_key=True)
    text: str 
    owner_id: int = Field(foreign_key="user.id")
    post_id: int = Field(foreign_key="post.id")

    owner: User=Relationship(back_populates="reactions")
    post: Post=Relationship(back_populates="reactions")

    

