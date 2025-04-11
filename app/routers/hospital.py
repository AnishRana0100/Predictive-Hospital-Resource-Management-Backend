from fastapi import APIRouter
from app.services.prediction import predict_resources

router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    return predict_resources(data)
