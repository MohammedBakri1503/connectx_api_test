# 🧪 ConnectX Junior Automation Engineer – API Testing Exercise

This project demonstrates an automated testing strategy for RESTful APIs using the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) fake API. The focus is on validating core CRUD functionality, edge cases, and verifying proper API behavior using Python with `requests` and `pytest`.

---

## ✅ Objective

To test the `/posts` endpoint by validating:

- Response structure
- Status codes
- Data integrity
- Proper handling of positive and negative test scenarios
- RESTful CRUD operations

---

## 🧠 Testing Strategy & Objectives

**Test Plan Overview:**

We focus on verifying basic API behavior through:

1. **Positive Testing** – Valid inputs and expected outcomes  
2. **Negative Testing** – Invalid input (e.g., non-existent ID, missing fields)  
3. **Data Validation** – Ensuring the API returns fields with correct types and values  
4. **CRUD Coverage**:
   - `GET /posts` – List all posts
   - `GET /posts/{id}` – Retrieve a single post
   - `POST /posts` – Create a new post
   - `PUT /posts/{id}` – Update an existing post
   - `DELETE /posts/{id}` – Delete a post

**Assertions include:**

- Status codes (200, 201, 404, 500)
- Response schema structure
- Required fields (`id`, `title`, `body`, `userId`)
- Type checking (e.g., strings, integers)

---

## 🧰 Tools & Libraries Used

- [`requests`](https://pypi.org/project/requests/): To send HTTP requests
- [`pytest`](https://docs.pytest.org/): To define and run test cases

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/connectx-api-tests.git
cd connectx-api-tests

pip install -r requirements.txt

pytest



PS C:\Users\lennovo\Desktop\connectx_api_test> pytest
==============================================================================
platform win32 -- Python 3.7.6, pytest-7.4.3
collected 31 items

tests\posts_create_test.py .......                                                                                     [ 22%]
tests\posts_delete_test.py .....                                                                                       [ 38%]
tests\posts_get_test.py .......                                                                                        [ 61%]
tests\posts_update_test.py ............                                                                                [100%]

============================================================================== 31 passed in 8.27s ==============================================================================



🧠 Challenges & Interesting Findings
🔍 Challenges Faced
Unrealistic API Behavior:
JSONPlaceholder is a mock API that does not validate request payloads. It accepts:

Missing required fields

Incorrect data types

None or invalid JSON (like plain strings)

This made negative testing non-standard, requiring flexible assertions.

Ambiguous Edge Case Responses:
Some scenarios (e.g., GET /posts/"") returned the full list instead of an error.
Posting an empty dict ({}) still resulted in a 201 Created with an auto-generated ID.

Limited Error Handling:
The API often returned 200 OK even for inputs that would realistically cause 400 Bad Request or 500 Internal Server Error.

🌟 Interesting Findings
Echo Behavior:
JSONPlaceholder echoes back extra/unexpected fields in the response — unlike real APIs which usually reject or ignore them.

Static ID Generation:
Every new post created using POST gets an id of 101, regardless of payload. This shows there's no backend persistence.

Hardcoded Data:
The data in GET /posts is static — so data validation tests must account for that and not assume dynamic state changes.