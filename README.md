# Kindergarten CRUD System

A FastAPI-based CRUD system designed for managing parents and children records in a kindergarten setting. The project uses PostgreSQL as the database and provides a robust foundation for future extensions like database migrations and unit testing.

# Technologies Used

Backend: FastAPI  
Database: PostgreSQL with SQLAlchemy and asyncpg  
Testing: Pytest, HTTPX, and ASGI Lifespan for unit tests  
Settings and Configurations: Managed with python-dotenv  
Logging: Powered by Loguru  




### Project Structure
```bash
├───app
│   ├───api
│   │   ├───dependencies        # FastAPI dependency injection 
│   │   └───routes              # endpoint definintions
│   ├───core                    # settings
│   ├───db
│   │   ├───models              # SQLAlchemy models
│   │   └───repositories        # CRUD related stuff
│   ├───models                  
│   │   ├───domain              # schemas related to domain entities
│   │   └───utility_schemas     # schemas for other validation
│   └───services                # not just CRUD related stuff
├───migrations
│   └───versions
└───tests
    ├───fixtures                # where test specific fixtures live
    └───unit_tests                
        └───test_api            # testing endpoints
```

# Future Enhancements

Database Migrations  
Unit Testing  
Frontend Integration  

