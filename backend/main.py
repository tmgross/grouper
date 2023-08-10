from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from models import *
from database import *
from invite import *
from friendInvite import *
from location import *

# current user
global currUser, currLoco, selectedGroupIvt
currUser = None
currLoco = None
selectedGroupIvt = None

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
	global currUser
	currUser = await log_in_user(request.email)
	if response:
		return response
	raise HTTPException(status_code=400, detail="Failed to create a new user")

#logging in the user
@app.get("/api/user/{email}")
async def log_in(email: str):
	global currUser
	currUser = await log_in_user(email)
	print(currUser.get_email())
	if currUser.get_id():
		return currUser.get_id()
	raise HTTPException(status_code=404, detail="User")

#creating a new group
@app.post("/api/group/")
async def new_group(request: CreateGroupRequest):
	response = await create_new_group(request.group)
	loco = await get_location(response)
	#adding the current users access to the group
	access = await add_user_access(currUser,loco)
	print(access)
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
	response = await currUser.get_locations()
	#response = await get_all_locations(currUser)
	return response

#creates an object for a specific location
@app.get("/api/user/loco/{locationId}")
async def getCurrLocation(locationId):
	global currLoco
	currLoco = await get_location(locationId)
	return currLoco

@app.get("/api/user/location/loconame")
async def getLocoName():
	if not currLoco:
		return "Error"
	return currLoco.get_name()

@app.get("/api/username")
async def getUserName():
	if not currUser:
		return "invalid user"
	else:
		return currUser.get_name()

@app.get("/api/email")
async def getUserEmail():
	if not currUser:
		return "invalid user"
	else:
		return currUser.get_email()

@app.get("/api/location/users")
async def getLocationUsers():
	users = await currLoco.get_current_users()
	return users

#removing a user from a location
@app.delete("/api/user/remove")
async def delete_user():
	response = await remove_user(currUser,currLoco)
	if response:
		return "Successfully deleted user"
	raise HTTPException(404, f"There is no user with the name {currUser.get_name()}")

# adding a user to a location
@app.put("/api/user/adduser")
async def joinLocation():
	response = await add_user_to_location(currUser,currLoco)
	if response:
		return response
	raise HTTPException(400, "Something went wrong")


@app.get("/api/friends/")
async def get_friends():
	friendsList = await currUser.get_friends()
	return friendsList

@app.get("/api/invites/friends")
async def get_friend_invites():
	return await currUser.get_friend_invites()

@app.get("/api/invites/get/groups")
async def get_group_invites():
	invites = await currUser.get_group_invites()
	ivts = {}
	for i in range (len(invites)):
	#for invite in invite:
		#ivts[invite.getFromId()]=invite.getFromName()
		ivts[invites[i].get_from_id()]=invites[i].get_group_name()
	return ivts

@app.post("/api/invite/group/set/{groupId}")
async def set_selected_group(groupId):
	global selectedGroupIvt
	invites = await currUser.get_group_invites()
	for i in range (len(invites)):
		if(invites[i].get_from_id()==groupId):
			global selectedGroupIvt
			selectedGroupIvt = invites[i]
	return selectedGroupIvt != None

@app.put("/api/invite/group/accept")
async def accept_group_invite():
	if(selectedGroupIvt!=None):
		newid = await selectedGroupIvt.accept_invite()
		return newid
	else:
		return "invalid object"

@app.put("/api/invite/group/reject")
async def accept_group_invite():
	if(selectedGroupIvt!=None):
		await selectedGroupIvt.reject_invite()
		return "rejected"
	else:
		return "invalid object" 

@app.put("/api/invite/group/{toEmail}")
async def new_group_invite(toEmail):
	ivt = GroupInvite(currLoco.get_id(),str(toEmail))
	return await ivt.add_invite()  


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

