from fastapi import APIRouter
from models.user import User
from config.db import conn
from shecmas.user import singleUserEntity, listOfUsers

db = conn.local.user

user = APIRouter()


@user.get('/')
async def get_all_users():
    return listOfUsers(db.find())


@user.post('/')
async def add_user(user: User):
    newUser = db.insert_one(dict(user))
    # print(f"{singleUserEntity(newUser)} is the new user")
    return listOfUsers(db.find())
