# connectx_api_test


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

- Status codes (200, 201, 404)
- Response schema structure
- Required fields (`id`, `title`, `body`, `userId`)
- Type checking (e.g., strings, integers)

---

## 🧰 Tools & Libraries Used

- [`requests`](https://pypi.org/project/requests/): To send HTTP requests
- [`pytest`](https://docs.pytest.org/): To define and run test cases

---

## 🧱 Setup Instructions

### 1. 📦 Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)

### 2. 📁 Clone this project

```bash
git clone https://github.com/yourusername/connectx-api-tests.git
cd connectx-api-tests


======================= test session starts ========================
collected 7 items

tests/test_posts_api.py::test_get_all_posts PASSED
tests/test_posts_api.py::test_get_single_post_valid[1] PASSED
tests/test_posts_api.py::test_get_single_post_valid[50] PASSED
tests/test_posts_api.py::test_get_single_post_valid[100] PASSED
tests/test_posts_api.py::test_get_single_post_invalid PASSED
tests/test_posts_api.py::test_create_post PASSED
tests/test_posts_api.py::test_delete_post PASSED
...
