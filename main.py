from fastapi import FastAPI
from app.routers import auth, hospital

app = FastAPI(title="Predictive Hospital Resource Manager")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(hospital.router, prefix="/hospital", tags=["Hospital"])

@app.get("/")
def read_root():
    return {"message": "API is running"}
