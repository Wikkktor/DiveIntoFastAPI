# FastAPI cheat sheet
## Repository contains fundamental structure of a fastapi project:
- Schema pydentic classes
- Models with sqlalchemy orm
- Routers to separate endpoints
- Authentication & Authorization with generated JWT
- Migrations with alembic
- Database connection with postgreSQL with foreignkeys used
- CRUD of every model

<br>

### To run locally this project, after cloning you must create passwords.py file in the main directory with you database postgreSQL credentials
<br>

### Example: 
database = "postgresql://user:pass@host/dbname" 
