# Week 2- Using FastAPI and adding custom Starlette to add endpoints, middleware and updated docs
 
  ###  The project package contains middlewares, http exceptions, routers in its api, currently using fastapi and use CRUD operations on users (/users) and hospital tasks (/tasks)


## Key Features

*  Creating, reading, updating and deleting users on the app
*  Creating, reading, updating and deleting tasks just as well
*  Uses pydantic and exceptions to clean out the proper looking error messages
*  Built in id_number as we assign users and tasks and user the id number to read, update or delete the information. 
* Starlette middleware to record response time, method, path etc

## Requirements

* Requirements.txt


## End point Documentation 
* http://127.0.0.1:8000/users/{user_1}  This for example gives you the user's details if their id_number is 1. Simply replacing users and {users_1} with projects and tasks which give you the details for said task for project
for e.g.
* http://127.0.0.1:8000/tasks/1
 * http://127.0.0.1:8000/projects/1
* http://127.0.0.1:8000/projects
* http://127.0.0.1:8000/tasks
* http://127.0.0.1:8000/users
 * http://127.0.0.1:8000/users/1