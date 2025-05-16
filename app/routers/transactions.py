from fastapi import APIRouter

from models import Transaction

router = APIRouter()

@router.get('/transactions', tags=['transactions'])
async def read_transaction(transaction_data: Transaction):
    return transaction_data