from fastapi import APIRouter, UploadFile, File
import pandas as pd
from app.services.import_service import ImportService

router = APIRouter(prefix="/import", tags=["Import"])

@router.post("/csv")
async def import_csv(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    service = ImportService()
    result = service.process(df)

    return result