from fastapi import APIRouter
from models.payment_models import Payment, Subcription
from config.db import conn

db = conn.ChurchDb.docs

payments = APIRouter(tags=['Payments'])

@payments.post('/subscription')
def subcription(sub: Subcription):
    return {'test':''}


@payments.post('/normal_pay')
def normal_payments(pay:Payment):
    return {'test':''}