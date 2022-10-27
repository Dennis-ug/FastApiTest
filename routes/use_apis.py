from fastapi import APIRouter
from models.user import User
from config.db import conn
from shecmas.user import singleUserEntity, listOfUsers, userDoc

db = conn.ChurchDb.docs

user = APIRouter(tags='Users')


@user.get('/')
async def get_all_users():
    return listOfUsers(db.find())


@user.post('/')
async def add_user(user: User):
    newUser = db.insert_one(dict(userDoc(user)), True)
    db.f
    print(newUser.inserted_id)
    # print(f"{singleUserEntity(newUser)} is the new user")
    print()
    return singleUserEntity(db.find_one({"userName": user.userName}))
