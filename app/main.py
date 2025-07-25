from fastapi import FastAPI
from app.routes.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              
    allow_credentials=True,
    allow_methods=["*"],               
    allow_headers=["*"],               
)


app.include_router(chat_router)
