# API for kindergartens

A FastAPI-based CRUD system designed for managing parents and children records in a kindergarten setting. The project uses PostgreSQL as the database and provides a robust foundation for future extensions like database migrations and unit testing. The system has integrated SMTP functionality for email notifications. You can configure the SMTP server details in your environment variables and use it for sending emails asynchronously through background tasks.

# Technologies Used

Backend: FastAPI  
Database: PostgreSQL with SQLAlchemy and asyncpg  
Testing: Pytest, HTTPX, and ASGI Lifespan for unit tests  
Settings and Configurations: Managed with python-dotenv  
Logging: Powered by Loguru  

# Installation
Clone the repository:
```bash
git clone https://github.com/C0nst4nta/kindergarten-online-system.git  
cd kindergarten-online-system
```  
Create a virtual environment and activate it:  
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```  
Install dependencies:  
```bash
pip install -r requirements.txt
```


# Run with Docker
Build and start the containers:
```bash
docker-compose up --build
```
Access the application at http://localhost:8000.  
Explore the API documentation:  
Swagger UI: http://localhost:8000/docs  
ReDoc: http://localhost:8000/redoc  



### Project Structure
```bash
src
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
└    
```


