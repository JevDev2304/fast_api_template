
from fastapi import APIRouter , HTTPException, Depends
from typing import List
from app.database.models.fibonacci import FibonacciRequest, FibonacciDatabaseDB
from app.services.fibonacci_service import linear_fibbo_with_seeds
from app.utils.time_utils import extract_fibbo_params
from app.utils.html_utils import render_fibonacci_html
from app.services.email_service import  send_email_mailersend
from app.database.db import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/fibonacci_email", tags=["fibonacci_email"])

@router.get("/")
async def list_items(db: Session = Depends(get_db)):
    try:
        fibonacci_entries = db.query(FibonacciDatabaseDB).all()

        if not fibonacci_entries:
            raise HTTPException(status_code=404, detail="No Fibonacci records found.")

        # Convertir los registros a la estructura esperada por Pydantic
        return [FibonacciDatabaseDB(hour=entry.hour, fibonacci_sequence=entry.fibonacci_sequence) for entry in fibonacci_entries]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", status_code=201)
async def create_item(fibonacci_request: FibonacciRequest,db: Session = Depends(get_db)):
    seed_one, seed_two, count = extract_fibbo_params(fibonacci_request.hour)
    fibonacci_list = linear_fibbo_with_seeds(count, seed_one, seed_two)
    if fibonacci_request.email:
        try:
            send_email_mailersend(to_email=fibonacci_request.email,
                                  subject=fibonacci_request.subject,
                                  html_body=render_fibonacci_html(fibonacci_list,f"{fibonacci_request.hour}"),
                                  from_email="MS_OUkALR@test-z0vklo66op7l7qrx.mlsender.net ",
                                  from_name="Your Fibonacci Sequence")
            
        except Exception as e:
            raise e
        db.add(FibonacciDatabaseDB(hour=fibonacci_request.hour, fibonacci_sequence=fibonacci_list))
        db.commit()
    return {"fibonacci_sequence":fibonacci_list}
