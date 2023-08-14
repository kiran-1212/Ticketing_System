# Ticketing_System
A RESTAPI Ticketing Server ti assign tickets on basis of Round Robin Principle
## Accessing Different API Endpoints

Our REST API Ticketing System provides various endpoints to perform different actions. Here's how to access each of them:

### Assigning a Ticket

To assign a new ticket based on the Round Robin Principle, follow these steps:

1. Open a web browser.
2. Enter the URL of your deployed app.
   Example: https://your-app-domain.com
3. Make a POST request to the following URL to assign a ticket:
   - URL: https://your-app-domain.com/assign_ticket
   - Request Body: JSON object with "issue_description" and "raised_by" fields.
   - Example Request Body: {"issue_description": "Sample issue", "raised_by": "User123"}
   
### Viewing People

To view the list of people and their assigned tickets, follow these steps:

1. Open a web browser.
2. Enter the URL of your deployed app.
   Example: https://your-app-domain.com
3. Navigate to the following URL to view people details:
   - URL: https://your-app-domain.com/people

### Viewing Tickets

To view the list of all tickets that have been assigned, follow these steps:

1. Open a web browser.
2. Enter the URL of your deployed app.
   Example: https://your-app-domain.com
3. Navigate to the following URL to view ticket details:
   - URL: https://your-app-domain.com/tickets

Please note that each endpoint corresponds to a specific method of our REST API. For more information on request formats, responses, and other details, refer to the API documentation.
