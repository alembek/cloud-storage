from fastapi import FastAPI

from app.routes import router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://185.182.219.45:5173/"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(upload.router)

@app.get("/")
def read_root():
	return {"message":"Cloud Storage API is working"}

