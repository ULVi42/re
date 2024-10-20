from models import User,Post,Reaction,Response,Comment
from sqlmodel import Session,select
from fastapi import status,HTTPException
from fastapi_jwt_auth import AuthJWT


def get_users(session: Session):
    users=session.exec(select(User)).all()
    return  users

def get_user_by_id(id,session: Session):
    user=session.exec(select(User).where(User.id==id)).first()
    if user==None:
        HTTPException(status_code=404,detail="User not found")
    return  user



def login(username,password,session: Session):
    hashed_password=User.hashing_password(password=password)
    user=User(username=username,hashed_password=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)

def sign_in(username,password,session: Session):
    user=session.exec(select(User).where(User.username==username)).first()
    if user==None:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    hashed_password=User.verify_password(password)
    if not hashed_password!=user.hashed_password:
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorect password")
    access_token = AuthJWT.create_access_token(subject=user.username)
    D={
        status: status.HTTP_200_OK,
        "data":{
            "access_token": access_token,
            "token_type":"bearer"
        }
    }
    return user

def update_user(id,username,password,session: Session):
    user=session.exec(select(User).where(User.id==id)).first()
    if user==None:
       HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    if username:
        user.username=username
    if password:
        user.hashed_password=User.hashing_password(password)
    session.add(user)
    session.commit()
    session.refresh(user)

def delete_user(id,session:Session):
    user=session.exec(select(User).where(User.id==id)).first()
    if user==None:
       HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    session.delete(user)
    session.commit()

def add_post(post: Post,session:Session):
    session.add(post)
    session.commit()
    session.refresh(post)

def add_reaction_to_post(id,react:Reaction,session:Session):
    post=session.exec(select(Post).where(Post.id==id)).first()
    react.post=post
    session.add(react)
    session.commit()
    session.refresh(react)

def add_comment_to_post(id,comment:Reaction,session:Session):
    post=session.exec(select(Post).where(Post.id==id)).first()
    comment.post=post
    session.add(comment)
    session.commit()
    session.refresh(comment)


def delete_post(id,session:Session):
    post=session.exec(select(Post).where(Post.id==id)).first()
    if post==None:
       HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    session.delete(post)
    session.commit()
    
def delete_Reaction(id,session:Session):
    Reaction=session.exec(select(Reaction).where(Reaction.id==id)).first()
    if Reaction==None:
       HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    session.delete(Reaction)
    session.commit()

def delete_comment(id,session:Session):
    comment=session.exec(select(Comment).where(Comment.id==id)).first()
    if comment==None:
       HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    session.delete(comment)
    session.commit()
 


    


    
