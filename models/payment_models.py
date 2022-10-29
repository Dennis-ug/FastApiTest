from pydantic import BaseModel
from datetime import datetime, date
from typing import Dict, List, Set, Tuple


class DeviceInfo(BaseModel):
    deviceName: str
    serialNumber: str
    ip: str

class Payment(BaseModel):
    payer_name:str
    title:str
    date_of_payment:datetime
    amount:int



class Subcription(Payment):
    deviceInfo:DeviceInfo
