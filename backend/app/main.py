from fastapi import FastAPI
from app.routes.import_route import router as import_router
from app.core.db import DB

app = FastAPI(title="Shared Expense App")

@app.on_event("startup")
def startup():
    DB.init()

app.include_router(import_router)

@app.get("/")
def health():
    return {"status": "running"}