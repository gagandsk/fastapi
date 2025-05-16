from fastapi import APIRouter

from models import Invoice

router = APIRouter()

@router.get('/invoices', tags=['invoices'])
async def read_invoice(invoice_data: Invoice):
    return invoice_data