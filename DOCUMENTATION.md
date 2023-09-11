# Person API Documentation

## Standard Formats

### Requests
- Endpoint: `/api/{id}/`
   - Method: `GET`
   - Description: Retrieves a specific person by their ID.
   - Example Request:
     ```http
     GET /api/123/ HTTP/1.1
     Host: localhost:8000
     ```

- Endpoint: `/api`
   - Method: `POST`
   - Description: Creates a new person.
   - Example Request:
     ```http
     POST /api HTTP/1.1
     Host: localhost:8000
     Content-Type: application/json

     {
       "name": "John Doe",
       "age": 30,
       "email": "johndoe@example.com"
     }
     ```

- Endpoint: `/api/{id}/`
   - Method: `PUT`
   - Description: Updates an existing person.
   - Example Request:
     ```http
     PUT /api/123/ HTTP/1.1
     Host: localhost:8000
     Content-Type: application/json

     {
       "name": "Jane Smith",
       "age": 35,
       "email": "janesmith@example.com"
     }
     ```

- Endpoint: `/api/{id}/`
   - Method: `DELETE`
   - Description: Deletes a person.
   - Example Request:
     ```http
     DELETE /api/123/ HTTP/1.1
     Host: localhost:8000
     ```

### Responses
- Success Response:
   - Status Code: `200 OK`
   - Example Response:
     ```json
     {
       "id": 123,
       "name": "John Doe",
       "age": 30,
       "email": "johndoe@example.com"
     }
     ```

- Error Response:
   - Status Code: `404 Not Found`
   - Example Response:
     ```json
     {
       "detail": "Person not found."
     }
     ```

## Sample Usage

### Create a New Person
- Endpoint: `/api`
- Request:
   ```http
    POST /api/persons/ HTTP/1.1
    Host: localhost:8000
    Content-Type: application/json

    {
        "name": "Alice Johnson",
        "age": 25,
        "email": "alicejohnson@example.com"
    }
    ```
- Response:
    ```json
    {
        "id": 3,
        "name": "Alice Johnson",
        "age": 25,
        "email": "alicejohnson@example.com"
    }
    ```
## Known Limitations and Assumptions
- The API assumes that a person has a unique ID and requires that ID for specific operations like updating or deleting a person.
- The API currently supports only basic CRUD operations (Create, Read, Update, Delete) for persons.