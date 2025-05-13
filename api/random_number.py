from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/random-number")
def get_random_number():
    number = random.randint(1, 100)
    return {"random_number": number}
