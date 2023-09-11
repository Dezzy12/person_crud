# Person API

## Description
The Person API allows you to manage and retrieve information about a person, including their name, age, and email addresse.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Starting the API](#starting-the-api)
  - [API Endpoints](#api-endpoints)

## Getting Started
Follow the instructions below to get the Person API up and running on your local machine.

### Prerequisites
- Python 3.9 or higher
- Django 3.2 or higher
- Django REST Framework 3.12 or higher

### Installation
1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/person-api.git
2. Change into the project directory:
    ```shell
    cd person-api
3. Create and activate a virtual environment:
    hange into the project directory:
    ```shell
    python3 -m venv venv
    source venv/bin/activate
4. Install the required dependencies:
    ```shell
    pip install -r requirements.txt
5. Apply database migrations:
    ```shell
    python manage.py migrate
## Usage
### Starting the API
1. Run the following command to start the API:
    ```shell
    python manage.py runserver
2. The API will be accessible at https://endpoint-dez.onrender.com/api/

### API Endpoints
- POST /api/: Creates a new person.
- GET /api/{id}/: Retrieves a specific person by their id.
- PUT /api/{id}/: Updates an existing person.
- DELETE /api/{id}/: Deletes a person.

Please refer to the API documentation or interact with the API using tools like Postman to explore these endpoints in detail. Use this to link to access the test script on postman: https://documenter.getpostman.com/view/25680408/2s9YC1XuMF

### NB:
- Lastly, images for  the UML and ER Diagram are in root directory with the base name `person` 