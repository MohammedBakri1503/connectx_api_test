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

- **Positive Tests** – Valid inputs returning expected results  
- **Negative Tests** – Invalid data types, IDs, missing fields, malformed JSON  
- **Data Validation** – Verifying the presence and types of response fields  
- **Edge Cases** – Empty payloads, null IDs, and unexpected fields

### Key Assertions

- Status codes: `200 OK`, `201 Created`, `404 Not Found`, `500 Internal Server Error`
- JSON schema: presence of fields like `id`, `title`, `body`, `userId`
- Correct data types: integers for `id` and `userId`, strings for `title` and `body`

---

## 🛠 Tech Stack

| Tool             | Purpose                       |
|------------------|-------------------------------|
| `pytest`         | Test runner                   |
| `requests`       | Sending HTTP requests         |
| `JSONPlaceholder`| Fake REST API for testing     |
| `allure-pytest`  | Test reporting and visualization |

---

##  Setup Instructions

### 1.  Clone the Repository

```bash
git clone https://github.com/MohammedBakri1503/connectx_api_test?tab=readme-ov-file
```
```bash
cd connectx-api-tests
```


### 2.  Install Dependencies

```bash
pip install -r requirements.txt
```

If using Allure for reporting, also install:

```bash
pip install allure-pytest
```


---

##  Run the Tests

```bash
pytest
```

---

##  Generate Allure Report

### Step 1: Run Tests with Allure

```bash
pytest --alluredir=allure-results
```

### Step 2: Generate the Report

```bash
allure generate allure-results --clean -o allure-report
```

### Step 3: Open the Report in Browser

```bash
allure open allure-report
```

---

##  Sample Test Output

```bash
platform win32 -- Python 3.7.6, pytest-7.4.3
collected 31 items

tests\posts_create_test.py .......                                                                                     [ 22%]
tests\posts_delete_test.py .....                                                                                       [ 38%]
tests\posts_get_test.py .......                                                                                        [ 61%]
tests\posts_update_test.py ............                                                                                [100%]

============================================================================== 31 passed in 8.27s ==============================================================================
```

---

##  Challenges & Interesting Findings

###  Challenges

- **Unrealistic API Behavior**  
  JSONPlaceholder is a mock API, so it doesn't validate data. It accepts:
  - Payloads missing required fields
  - Wrong data types
  - `None` or invalid JSON

- **Edge Case Behavior**  
  - `POST {}` returns 201 Created
  - `GET /posts/""` returns the full list, not an error
  - Invalid requests often return 200 OK

- **Error Handling Gaps**  
  The API returns 200 even when 400 or 500 would be expected in production.

###  Interesting Findings

- **Echo Behavior**  
  JSONPlaceholder returns unknown fields in the response.

- **Static ID Generation**  
  Every post created with `POST` returns `id = 101`.

- **Immutable Data**  
  `GET /posts` always returns the same 100 static records.

---
