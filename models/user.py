from pydantic import BaseModel
from datetime import datetime, date
from typing import Dict, List, Set, Tuple


class DeviceInfo(BaseModel):
    deviceName: str
    serialNumber: str
    ip: str


class User(BaseModel):
    userName: str
    email: str
    contact: List[int]
    password: str
    # profilePic: str
    gender: str
    church_branch: str
    roles: List[str]
    date_of_birth: datetime
    date_of_going: datetime
    deviceInfo: DeviceInfo


class Transactions(BaseModel):
    user_tracting: str
    amt: str
    trans_type: str
    desc: str


class Donation(BaseModel):
    title: str
    description: str
    target_amount: str


class Event(BaseModel):
    title: str
    description: str
    target_amount: str
