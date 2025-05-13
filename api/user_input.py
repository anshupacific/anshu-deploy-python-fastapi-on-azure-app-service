from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/echo-input")
def echo_user_input(message: str = Query(..., description="Your input message")):
    return {"response": f"Hey, your input is '{message}'"}
