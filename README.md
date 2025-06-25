#  ConnectX Junior Automation Engineer – API Testing Exercise

This project demonstrates a structured approach to automated testing of RESTful APIs using [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — a free online REST API for testing and prototyping. The main goal is to validate core CRUD functionality, response behavior, and edge cases using `pytest` and `requests`.

---

##  Objective

To test the `/posts` endpoint for:

- Correct **HTTP status codes**
- Proper **response structure**
- **Data integrity** and consistency
- Coverage of both **positive** and **negative** test scenarios
- Full **CRUD operations**:
  - `GET /posts` – List all posts
  - `GET /posts/{id}` – Retrieve a specific post
  - `POST /posts` – Create a new post
  - `PUT /posts/{id}` – Update a post
  - `DELETE /posts/{id}` – Delete a post

---

##  Testing Strategy

### Test Approach

This project includes comprehensive test coverage for:

-  **Positive Tests** – Valid inputs returning expected results  
-  **Negative Tests** – Invalid data types, IDs, missing fields, malformed JSON  
-  **Data Validation** – Verifying the presence and types of response fields  
-  **Edge Cases** – Empty payloads, null IDs, and unexpected fields

### Key Assertions

- Status codes: `200 OK`, `201 Created`, `404 Not Found`, `500 Internal Server Error`
- JSON schema: presence of fields like `id`, `title`, `body`, `userId`
- Correct data types: integers for `id` and `userId`, strings for `title` and `body`

---

##  Tech Stack

| Tool             | Purpose                       |
|------------------|-------------------------------|
| `pytest`         | Test runner                   |
| `requests`       | Sending HTTP requests         |
| `JSONPlaceholder`| Fake REST API for testing     |

---

##  Setup Instructions

### 1.  Clone the Repository

```bash
git clone https://github.com/yourusername/connectx-api-tests.git
cd connectx-api-tests
```

### 2.  Install Dependencies

```bash
pip install -r requirements.txt
```

### 3.  Run the Tests

```bash 
pytest
```

---

##  Sample Test Output

```bash
PS C:\Users\lennovo\Desktop\connectx_api_test> pytest
============================================================================== test session starts ==============================================================================
platform win32 -- Python 3.7.6, pytest-7.4.3
collected 31 items

tests\posts_create_test.py .......                                                                                     [ 22%]
tests\posts_delete_test.py .....                                                                                       [ 38%]
tests\posts_get_test.py .......                                                                                        [ 61%]
tests\posts_update_test.py ............                                                                                [100%]

============================================================================== 31 passed in 8.27s ==============================================================================
```

---

## Challenges & Interesting Findings

###  Challenges Faced

- **Unrealistic API Behavior**  
  JSONPlaceholder is a mock API, so it doesn't validate data. It accepts:
  - Payloads missing required fields
  - Wrong data types (e.g., `title` as number, `userId` as string)
  - `None` or invalid JSON like plain strings

- **Edge Case Behavior**  
  - `POST {}` returns 201 Created, even if no meaningful fields are provided
  - `GET /posts/""` returns the entire post list, not an error
  - Many invalid cases return 200 OK or unexpected responses

- **Error Handling Limitations**  
  The API often returns 200 OK for cases that would realistically yield `400 Bad Request` or `500 Internal Server Error` in real applications.

###  Interesting Findings

- **Echo Behavior**  
  JSONPlaceholder **echoes extra or unknown fields** back in the response. Real-world APIs would reject or silently ignore them.

- **Static ID Generation**  
  All new posts created via `POST` return an `id` of `101`, regardless of how many times you call the endpoint — proving there's no persistent storage.

- **Hardcoded Dataset**  
  The `GET /posts` response always contains the same 100 static items. So test cases must not assume dynamic changes like deletions or updates persist.

---

