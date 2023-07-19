from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from models import User
import models

from database import (
	fetch_one_user,
	fetch_all_users,
	create_user,
	remove_user,
	logInUser,
	addUserToLocation,
	createNewUser,
	getAllLocations,
	getLocation,
)

# current user
currUser = None
currLoco = None
# app object
app = FastAPI()

origins = ["http://localhost:3000"]

# middleware acts as a bridge between database
#   and application
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

#logging in the user
@app.get("/api/user/{email}")
async def logIn(email):
	currUser = logInUser(email)


@app.get("/")
async def read_root():
	return {"Hello": "World"}


@app.get("/api/user")
async def get_user():
	response = await fetch_all_users()
	return response

#creating a new user
@app.post("/api/user/", response_model=User)
async def new_user(name, email):
	response = await createNewUser(email,name)
	if response:
		return response
	raise HTTPException(400, "Something went wrong")

#joining a location
@app.put("/api/user/{locationid}")
async def joinLocation(locationid):
	response = await addUserToLocation(currUser,locationid)
	if response:
		return response
	raise HTTPException(400, "Something went wrong")


#removing a user from a location
@app.delete("/api/user/")
async def delete_user():
	response = await remove_user(currUser)
	if response:
		return "Successfully deleted user"
	raise HTTPException(404, f"There is no user with the name {currUser.getName()}")

#getting all locations
@app.get("/api/user")
async def getLocations():
	response = await getAllLocations()
	return response

#creates an object for a specific location 
@app.get("/api/user/{locationid}")
async def getCurrLocation(locationid):
	currLoco = getLocation(locationid)

# gets all users at a location
@app.get("/api/user/")
async def getUsersAtLoco(locationid):
	return currLoco.getCurrentUsers()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True
    )