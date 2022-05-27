# userName: str
#     email: str
#     contact: int
#     password: str
#     genger: str

def singleUserEntity(userObject) -> dict:
    return{
        'id': str(userObject['_id']),
        'userName': userObject['userName'],
        'email': userObject['email'],
        'contact': userObject['contact'],
        'password': userObject['password'],
        'gender': userObject['gender'],
    }


def listOfUsers(userEntity) -> list:
    return[singleUserEntity(i) for i in userEntity]
