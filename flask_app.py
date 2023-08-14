# A very simple Flask Hello World app for you to get started with...
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
people = [
    {"id": "#1", "name": "Person A", "tickets": []},
    {"id": "#2", "name": "Person B", "tickets": []},
    {"id": "#3", "name": "Person C", "tickets": []},
    {"id": "#4", "name": "Person D", "tickets": []},
    {"id": "#5", "name": "Person E", "tickets": []}
]

tickets = []
ticket_id_counter = 1
person_counter = 0

@app.route("/assign_ticket", methods=["POST"])
def assign_ticket():
    global ticket_id_counter, person_counter

    # Get the next person in the round-robin sequence
    current_person = people[person_counter % len(people)]
    person_counter += 1

    # Get data from the request
    data = request.get_json()
    if "issue_description" not in data or "raised_by" not in data:
        return jsonify({"error": "Issue description and raised by are required fields"}), 400

    issue_description = data["issue_description"]
    raised_by = data["raised_by"]

    # Create a new ticket and assign it to the current person
    new_ticket = {
        "id": ticket_id_counter,
        "issue_description": issue_description,
        "assigned_to": current_person["id"],
        "raised_by": raised_by
    }
    current_person["tickets"].append(new_ticket)

    tickets.append(new_ticket)
    ticket_id_counter += 1

    return jsonify({"message": "Ticket assigned successfully"})

@app.route("/people", methods=["GET"])
def get_people():
    return jsonify(people)

@app.route("/tickets", methods=["GET"])
def get_tickets():
    return jsonify(tickets)

if __name__ == "__main__":
    from waitress import serve
    serve(app,port=4000)
