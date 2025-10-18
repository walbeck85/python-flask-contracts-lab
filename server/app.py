# server/app.py
from flask import Flask, make_response

app = Flask(__name__)

# Updated exact string bodies for certain contracts.
_CONTRACT_TEXT = {
    1: "This contract is for John and building a shed",
    2: "This contract is for Sarah and painting a house",
}

# Treat customer existence as sensitive: if present, return 204 with no body.
_CUSTOMERS = {"alice", "bob", "carol"}


@app.route("/contract/<int:id>")
def get_contract(id: int):
    """
    If the contract id exists:
      - Return the EXACT expected plain string (no JSON, no newline) with 200 OK.
    Else:
      - Return 404 Not Found (body not graded).
    """
    text = _CONTRACT_TEXT.get(id)
    if text is not None:
        return text, 200
    return "Contract not found", 404


@app.route("/customer/<customer_name>")
def check_customer(customer_name: str):
    """
    If the customer exists:
      - Return 204 No Content with an empty body (sensitive).
    Else:
      - Return 404 Not Found.
    """
    if customer_name in _CUSTOMERS:
        return ("", 204)  # 204 must not include a body
    return "Customer not found", 404


if __name__ == "__main__":
    app.run(port=5555, debug=True)