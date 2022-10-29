from models.user import User, DeviceInfo
# userName: str
#     email: str
#     contact: int
#     password: str
#     genger: str


# def deviceEntity(device) -> dict:
#     deviceName: 'deviceName'
#     serialNumber: 'serialNumber'
#     ip: 'ip'


def singleUserEntity(userObject: User) -> dict:
    return{
        'id': str(userObject['_id']),
        'userName': userObject['userName'],
        'email': userObject['email'],
        'contact': userObject['contact'],
        'password': userObject['password'],
        'gender': userObject['gender'],
        'deviceInfo': userObject['deviceInfo']

    }


def listOfUsers(userEntity) -> list:
    return[singleUserEntity(i) for i in userEntity]


# Data writers

def userDoc(userObject: User) -> dict:
    return{

        'userName': userObject.userName,
        'email': userObject.email,
        'contact': userObject.contact,
        'password': userObject.password,
        'gender': userObject.gender,
        'deviceInfo': {'deviceName': userObject.deviceInfo.deviceName,
                       'serialNumber': userObject.deviceInfo.serialNumber,
                       'ip': userObject.deviceInfo.ip,
                        }
    }
