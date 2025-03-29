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

## API Endpoints
- **Patients**: `POST /patients`, `GET /patients/{id}`, `PUT /patients/{id}`, `DELETE /patients/{id}`
- **Doctors**: `POST /doctors`, `GET /doctors/{id}`, `PUT /doctors/{id}`, `DELETE /doctors/{id}`
- **Appointments**: `POST /appointments`, `GET /appointments/{id}`, `PUT /appointments/{id}`, `DELETE /appointments/{id}`

## Contributing
Feel free to fork this repository and submit pull requests.

## License
MIT License
