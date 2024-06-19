# Pet project - "Tasker".

> [!TIP]
## Stack:
- `Deploy`: docker
- `Database`: sqlite
- `Local host`: uvicorn
- `Patterns`: repository
- `Web framework`: FastAPI
- `Programming language`: Python >= 3.9
- `Modules`: sqlalchemy, typing, pydantic

> [!NOTE]
## Files:
- `.dockerignore`: using this file, you can set rules for excluding files from the build context, which means reducing 
the time required to assemble the tar archive and send it to the server.
- `.gitignore`: a file specifies intentionally untracked files that Git should ignore.
- `Dockerfile`: a dockerfile is a text document that contains all the commands a user could call on the command line to 
assemble an image.
- `README.md`: is used to generate the html summary you see at the bottom of projects. 
- `data.py`: contains all other information for the project.
- `database.py`: contains classes and methods for working with the database.
- `main.py`: the main file of the application launch.
- `repository.py`: repository pattern file for working with the database.
- `requirements.txt`: serves as a list of items to be installed by pip, when using pip install.
- `router.py`: contains the main routers to work with application.
- `schema.py`: contains a description of data structures.
