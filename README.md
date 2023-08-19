**Running Grouper in Dev Mode:**
- start Mongo server using Mongo Compass or command line (may need to add IP address)
- cd to grouper backend folder, run `python main.py`
- in a separate console, cd to grouper frontend folder, run `npm start`

*FARM Stack Resources:*
- https://www.mongodb.com/developer/languages/python/farm-stack-fastapi-react-mongodb/
- https://www.freecodecamp.org/news/learn-the-farm-stack-fastapi-reactjs-mongodb/

*Things to do:*

1. Choose a language
2. Find a database
3. Connect to the database
4. Create a group in the database
5. Allow for a user to add and remove their name from a group in the database
6. Allow the user to create new groups (Groups could be public at first)
7. Make groups private to users in the group (individual sign in)
8. Allow the adding of users to a group




Code Style Convention:
camelCase for variables
CapWords for classes
kebab_case for functions
ALL_CAPS for global constants
no unused variables
no unnecessary print statements (ex: testing statements)
comments above functions to tell what they do
expected input and output
overall description of purpose of function
tab (4 spaces) to indent
spaces between operators (ex: i = 0)
opening curly brace on same line as definition (ex: for(){ )
classes should have their own file
  including testing code
