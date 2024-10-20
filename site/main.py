from fastapi import FastAPI,HTTPException
import uvicorn
from engine import engine
import functions
from sqlmodel import Session
 
app=FastAPI(docs_url="/docs")

from sqlmodel import SQLModel

SQLModel.metadata.create_all(engine)

@app.get("/get/users")
def  GetUsers():
    return functions.get_users(session=Session(engine))

@app.get("/get/user/{id}")
def  GetUserByID(id):
    return functions.get_user_by_id(id,session=Session(engine))

@app.post("/login")
def  Login(username,password):
    return functions.login(username,password,session=Session(engine))

@app.post("/singin")
def signin(username,password):
    return functions.sign_in(username,password,session=Session(engine))

@app.put("/update/user/{id}")
def  updateUser(id,username,password):
    return functions.update_user(id,username,password,session=Session(engine))

@app.delete("/delete/user/{id}")
def  DeleteUser(id):
    return functions.delete_user(id,session=Session(engine))

if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8080,reload=True)
