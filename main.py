from fastapi import FastAPI
from app.routers import auth, patients, beds, resources, predictions
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Predictive Hospital Resource Management")

app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(beds.router)
app.include_router(resources.router)
app.include_router(predictions.router)
