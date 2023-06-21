from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from models import User

from database import (
	fetch_one_user,
	fetch_all_users,
	create_user,
	remove_user,
)


# app object
app = FastAPI()

origins = ["https://localhost:3000"]

# middleware acts as a bridge between database
#   and application
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/")
async def read_root():
	return {"Hello": "World"}


@app.get("/api/user")
async def get_user():
	response = await fetch_all_users()
	return response

@app.post("/api/user/", response_model=User)
async def post_user(user):
	response = await create_user(user.dict())
	if response:
		return response
	raise HTTPException(400, "Something went wrong")

@app.delete("/api/user/{name}")
async def delete_user(name):
	response = await remove_user(name)
	if response:
		return "Successfully deleted user"
	raise HTTPException(404, f"There is no user with the name {name}")



if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True
    )