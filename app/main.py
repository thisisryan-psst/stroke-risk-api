from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chat, predict

app = FastAPI(title="Stroke Risk Prediction API")

# ✅ ADD THIS (required for HTML + JS frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # OK for local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(predict.router, tags=["Prediction"])

@app.get("/")
def root():
    return {"message": "Stroke Risk API is running"}
