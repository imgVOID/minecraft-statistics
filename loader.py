from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url='/api/minecraft/docs', redoc_url='/api/minecraft/redoc')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)