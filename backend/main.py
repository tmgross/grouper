from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from models import *
from database import *

# current user
global currUser, currLoco
currUser = None
currLoco = None

# app object
app = FastAPI()



origins = ["http://localhost:3000","http://localhost:3000/","https://localhost:3000", "https://localhost:3000/",]


# middleware acts as a bridge between database and application

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
	global currUser
	currUser = await log_in_user(email)
	print(currUser.getEmail())
	if currUser.getId():
		return currUser.getId()
	raise HTTPException(status_code=404, detail="User")

#creating a new group
@app.post("/api/group/")
async def new_group(request: CreateGroupRequest):
	response = await create_new_group(request.group)
	print(response)
	if response:
		return response
	raise HTTPException(status_code=400, detail="Failed to create a new group")

# #getting all locations
# @app.get("/api/location/")
# async def getLocations():
# 	response = await getAllLocations()
# 	return response

#getting all locations
@app.get("/api/location/")
async def getLocations():
	response = await getAllLocations()
	return response

#creates an object for a specific location
@app.get("/api/user/loco/{locationId}")
async def getCurrLocation(locationId):
	global currLoco
	currLoco = await getLocation(locationId)
	return currLoco

@app.get("/api/user/location/loconame")
async def getLocoName():
	if not currLoco:
		return "Error"
	return currLoco.getName()

@app.get("/api/username")
async def getUserName():
	if not currUser:
		return "invalid user"
	else:
		return currUser.getName()

@app.get("/api/location/users")
async def getLocationUsers():
	users = await currLoco.getCurrentUsers()
	return users

#removing a user from a location
@app.delete("/api/user/remove")
async def delete_user():
	response = await removeUser(currUser,currLoco)
	if response:
		return "Successfully deleted user"
	raise HTTPException(404, f"There is no user with the name {currUser.getName()}")

# adding a user to a location
@app.put("/api/user/adduser")
async def joinLocation():
	response = await addUserToLocation(currUser,currLoco)
	if response:
		return response
	raise HTTPException(400, "Something went wrong")
  
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

