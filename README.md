# Lab: Contractors Lab

---

## Overview

Now it is time for you to build your own request responses!

You are working for a company that manages contracts between two parties. You need to manage sensitive data, and as such, you need to build two requests:

- One for **customer information**
- One for **contract information**

You will be using two new response codes:

- **204**: Successful response but no data to send (e.g., confirming a customer exists without sharing data).
- **404**: Not found — we cannot find the requested data.

---

## Tasks

### Task 1: Define the Problem

Build the following routes:

- `/contract/<id>`
- `/customer/<customer_name>`

---

### Task 2: Determine the Design

#### App Routes:

- `GET /contract/<id>`
  - **200**: Contract found — return contract information.
  - **404**: Contract not found.

- `GET /customer/<customer_name>`
  - **204**: Customer found — no information returned (sensitive).
  - **404**: Customer not found.

---

### Task 3: Develop the Code

- Initialize Flask
- Set up routes
- Configure responses

---

### Task 4: Test and Refine

- Debug and test during development using the provided test suite and Flask instance.

---

### Task 5: Document and Maintain

- Commit as you go with meaningful messages.
- Push commit history to GitHub periodically and when the lab is complete.

---

## Tools and Resources

- **GitHub Repo**: [https://github.com/walbeck85/python-flask-contracts-lab]
- **Flask Quickstart**: [https://flask.palletsprojects.com/en/stable/quickstart/](https://flask.palletsprojects.com/en/stable/quickstart/)

---

## Instructions

### Set Up

Before coding:

1. **Fork and Clone**
   - Go to the provided GitHub repository link: 
   - Fork the repository to your GitHub account.
   - Clone the forked repository to your local machine.

2. **Open and Run**
   - Open the project in VSCode.
   - Run `pipenv install` to install dependencies.
   - Run `pipenv shell` to activate the Python shell.

---

### Task 1: Define the Problem

Build the following routes:

- `/contract/<id>`
- `/customer/<customer_name>`

---

### Task 2: Determine the Design

#### App Routes:

- `/contract/<id>`
  - **200**: Contract found — return information
  - **404**: Contract not found

- `/customer/<customer_name>`
  - **204**: Customer found — return no information
  - **404**: Customer not found

---

### Task 3: Develop, Test, and Refine the Code

1. Create a **feature branch**.
2. Build the following routes:

#### `/contract/<id>`

- If the contract ID is found in the given array:
  - Return contract information with a **200** response.
- If not found:
  - Return a **404** response.

#### `/customer/<customer_name>`

- If the customer name is found:
  - Return a **204** response with an empty body.
- If not found:
  - Return a **404** response.

3. Push the feature branch and open a PR on GitHub.
4. Merge into `main`.

---

### Task 4: Document and Maintain

#### Best Practices:

- Add comments to explain logic and purpose.
- Clarify code intent for other developers.
- Include a screenshot of completed work in the README.
- Update the README to reflect functionality using [https://makeareadme.com](https://makeareadme.com).
- Delete stale branches on GitHub.
- Remove unnecessary or commented-out code.
- Update `.gitignore` if needed to exclude sensitive data

# Lab Submission: Routes Request-Response Cycle – Managing Contractors

This repository contains my implementation of the Flatiron School Course 8, Module 2 lab on the Flask request–response cycle.  
The goal is to demonstrate correct route handling, response creation, and HTTP status codes using Flask.  
This lab builds on the previous technical lesson and focuses on managing contract and customer data with clear, testable routes.

---

## Features

- Implements two dynamic Flask routes:
  - `/contract/<id>` returns contract data or a 404 error.
  - `/customer/<customer_name>` confirms the customer exists with a 204 “No Content” response or a 404 if not found.
- Uses in-memory sample data to simulate a small API.
- Demonstrates Flask best practices for response handling with `make_response()`.
- Applies HTTP status codes correctly for success (200, 204) and failure (404).
- Code is fully documented with purpose-driven comments and follows Flatiron’s structure for readability and maintainability.

---

## Environment

- Python 3.11 (tested locally on macOS)
- Flask installed via Pipenv virtual environment

The same setup applies on Windows or Linux; only the activation command differs.

---

## Setup

Clone and enter the project directory:

```bash
git clone <repo-url>
cd python-flask-contracts-lab
```

Create and activate the virtual environment:

```bash
pipenv install
pipenv shell
```

If Flask is not installed automatically, you can install it directly:

```bash
pip install flask
```

Run the development server:

```bash
python server/app.py
```

The Flask app will start on port `5555` by default.

---

## File Structure

```
.
├── CONTRIBUTING.md
├── LICENSE.md
├── Pipfile
├── Pipfile.lock
├── README.md
├── pytest.ini
└── server/
    ├── app.py
    └── testing/
        └── codegrade_test.py
```

---

## How to Run and Test Routes

With the app running at `http://127.0.0.1:5555`, test each endpoint in your browser or terminal.

### Contract Route
**Example 1 — Contract Found (200 OK):**
```bash
curl -i http://127.0.0.1:5555/contract/1
```
Response:
```
HTTP/1.0 200 OK
Content-Type: application/json
{
  "id": 1,
  "vendor": "Acme Security",
  "value": 120000
}
```

**Example 2 — Contract Not Found (404 Not Found):**
```bash
curl -i http://127.0.0.1:5555/contract/999
```

---

### Customer Route
**Example 3 — Customer Found (204 No Content):**
```bash
curl -i http://127.0.0.1:5555/customer/alice
```

**Example 4 — Customer Not Found (404 Not Found):**
```bash
curl -i http://127.0.0.1:5555/customer/zoe
```

---

## Notes on Status Codes

- **200 OK** – Successful response with content.
- **204 No Content** – Successful response confirming existence but returning no body (used for sensitive customer info).
- **404 Not Found** – Indicates the requested contract or customer was not found.

This structure demonstrates a complete, working request–response cycle aligned with real-world API design.

---

## Branch and Pull Request Workflow

I followed Flatiron’s recommended Git workflow:
- Created a feature branch `contracts_lab`.
- Committed work in small, meaningful increments.
- Opened a Pull Request into `main` for review before merging.
- Maintained a clean main branch for submission and grading.

---

## Screenshot of Working Routes

Below is a placeholder for the screenshot showing the app output in the browser.  
*(Replace this with your own screenshot before submission.)*

```
![App Screenshot – Successful 200 and 204 Responses](./screenshot.png)
```

---

## Instructor Checklist

- [ ] Activate the Pipenv shell and run `python server/app.py`.
- [ ] Visit or `curl` `/contract/1` and `/customer/alice` to confirm correct responses.
- [ ] Verify HTTP 200, 204, and 404 behavior aligns with the rubric.
- [ ] Check the comments in `server/app.py` for clear documentation of purpose and logic.
- [ ] Confirm code passes the CodeGrade test suite.

---

## Acknowledgments

This work follows the structure and objectives provided in Flatiron’s **Lab: Routes Request-Response Cycle – Managing Contractors** module.