# REST API Ticketing System

Welcome to the REST API Ticketing System! This system allows you to manage tickets and assign them to individuals based on the Round Robin Principle.

## Getting Started

To use this system, follow the instructions below to perform different actions using the provided API endpoints.

### Assigning a Ticket

To assign a new ticket based on the Round Robin Principle, follow these steps:

1. Open a tool like Postman or a web browser.
2. Enter the URL of your deployed app.
   Example: `http://saikiran112.pythonanywhere.com`
3. Make a POST request to the following URL to assign a ticket:
   - URL: `http://saikiran112.pythonanywhere.com/assign_ticket`
   - Request Body: JSON object with "issue_description" and "raised_by" fields.
   - Example Request Body: `{"issue_description": "Sample issue", "raised_by": "User123"}`

### Viewing People

To view the list of people and their assigned tickets, follow these steps:

1. Open a tool like Postman or a web browser.
2. Enter the URL of your deployed app.
   Example: `http://saikiran112.pythonanywhere.com`
3. Navigate to the following URL to view people details:
   - URL: `http://saikiran112.pythonanywhere.com/people`

### Viewing Tickets

To view the list of all tickets that have been assigned, follow these steps:

1. Open a tool like Postman or a web browser.
2. Enter the URL of your deployed app.
   Example: `http://saikiran112.pythonanywhere.com`
3. Navigate to the following URL to view ticket details:
   - URL: `http://saikiran112.pythonanywhere.com/tickets`

## Notes

- Each endpoint corresponds to a specific method of the REST API.
- For more information on request formats, responses, and other details, refer to the API documentation.
