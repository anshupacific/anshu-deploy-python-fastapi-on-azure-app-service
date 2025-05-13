from fastapi import APIRouter

router = APIRouter()

@router.get("/info")
def get_static_info():
    return {
        "project": "Azure FastAPI Integration",
        "version": "1.0",
        "maintainer": "Anshu"
    }
