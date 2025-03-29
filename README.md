# Healthcare Appointment Scheduling System

## Overview
This project is a Flask-based backend for a healthcare appointment scheduling system. It efficiently manages patient data, doctor availability, and appointment scheduling while ensuring security and performance.

## Features
- **Patient Management**: Register and manage patient profiles, including contact details and insurance information.
- **Doctor Management**: Maintain doctor profiles with specializations and manage availability schedules.
- **Appointment Scheduling**: Schedule appointments, prevent conflicts, and manage status updates.
- **Security**: Implement authentication and role-based access control using OAuth 2.0.
- **Performance Optimizations**: Asynchronous processing and message queuing using Redis.

## Technology Stack
- **Backend**: Flask (Python)
- **Database**: PostgreSQL/MySQL
- **Authentication**: OAuth 2.0
- **Asynchronous Processing**: Redis
- **API Documentation**: Swagger/OpenAPI

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- PostgreSQL/MySQL
- Redis (for asynchronous processing)
- Virtual environment tool (optional but recommended)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/healthcare-scheduling.git
   cd healthcare-scheduling
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   Create a `.env` file and configure the following:
   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   DATABASE_URL=postgresql://user:password@localhost/healthcare_db
   SECRET_KEY=your_secret_key
   REDIS_URL=redis://localhost:6379/0
   ```
5. Initialize the database:
   ```sh
   flask db upgrade
   ```
6. Run the application:
   ```sh
   flask run
   ```

## API Endpoints
- **Patients**: `POST /patients`, `GET /patients/{id}`, `PUT /patients/{id}`, `DELETE /patients/{id}`
- **Doctors**: `POST /doctors`, `GET /doctors/{id}`, `PUT /doctors/{id}`, `DELETE /doctors/{id}`
- **Appointments**: `POST /appointments`, `GET /appointments/{id}`, `PUT /appointments/{id}`, `DELETE /appointments/{id}`

Full API documentation is available at `http://localhost:5000/docs` (Swagger UI).

## Testing
Run unit tests with:
```sh
pytest
```

## Deployment
Use Docker for deployment:
```sh
docker-compose up --build
```

## Contributing
Feel free to fork this repository and submit pull requests.

## License
MIT License
