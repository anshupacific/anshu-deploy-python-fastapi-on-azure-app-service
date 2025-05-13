from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import static_info, random_number, user_input

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(static_info.router, prefix="/api")
app.include_router(random_number.router, prefix="/api")
app.include_router(user_input.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Test FastAPI app is running 🚀"}
