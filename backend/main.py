from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
import uvicorn

from models import CreateUserRequest

from database import (
	create_new_user,
	log_in_user,
	getAllLocations,
)

# current user
global currUser
currUser = None
# currLoco = None


# app object
app = FastAPI()



origins = ["http://localhost:3000","http://localhost:3000/","https://localhost:3000", "https://localhost:3000/",]


# middleware acts as a bridge between database and application

app.add_middleware(
	CORSMiddleware,
	#allow_origins=["http://localhost:3000"],
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


#creating a new user
@app.post("/api/user/")
async def new_user(request: CreateUserRequest):
	response = await create_new_user(request.email, request.name)
	print(response)
	if response:
		return response
	raise HTTPException(status_code=400, detail="Failed to create a new user")

#logging in the user
@app.get("/api/user/{email}")
async def log_in(email: str):
	currUser = await log_in_user(email)
	print(currUser.getEmail())
	return currUser.getId()


@app.get("/")
async def read_root():
	return {"Hello": "World"}

#getting all locations
@app.get("/api/location/")
async def getLocations():
	response = await getAllLocations()
	return response


# @app.get("/api/user")
# async def get_user():
# 	response = await fetch_all_users()
# 	return response

'''
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
'''

'''
#creates an object for a specific location
@app.get("/api/user/{locationid}")
async def getCurrLocation(locationid):
	currLoco = getLocation(locationid)


# gets all users at a location
@app.get("/api/user/")
async def getUsersAtLoco(locationid):
	return currLoco.getCurrentUsers()
'''

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True
    )
    
