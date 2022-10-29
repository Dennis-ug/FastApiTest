from fastapi import APIRouter
from models.payment_models import Payment, Subcription
from config.db import conn

db = conn.ChurchDb.docs

media=APIRouter(tags=['Media'])

@media.get('/summons')
def get_summons():
    return{"test":"owk"}


@media.get('/events')
def get_events():
    return{"test":"owk"}