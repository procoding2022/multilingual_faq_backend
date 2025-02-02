# FAQ Management System

This is a Django-based FAQ management system with multilingual support, caching, and a WYSIWYG editor for managing FAQ entries. It provides a RESTful API for interacting with FAQs.

## Table of Contents

- [Installation Steps](#installation-steps)
- [API Usage Examples](#api-usage-examples)
- [Additional Notes](#additional-notes)

## Installation Steps

Follow these steps to set up and run the FAQ Management System locally.

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/procoding2022/multilingual_faq_backend.git
cd multilingual_faq_backend
```
### 2. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install the Required Dependencies

Install the dependencies listed in requirements.txt:

```bash
pip install -r requirements.txt
```
 ### 4. Set Up the Database

 Run migrations to set up your database:

 ```bash
python manage.py migrate
```
### 5. Run the Development Server

Start the development server:

```bash
python manage.py runserver
```

Now, your application should be running at `http://localhost:8000`.

## API Usage Examples

### 1. Get All FAQs

Fetch all the FAQs:

```bash
curl http://localhost:8000/api/faqs/
```

Response

```json
[
    {
        "id": 1,
        "question": "What is the FAQ management system?",
        "answer": "This system allows users to manage FAQs.",
        "language": "en"
    },
    ...
]
```

### 2. Create a New FAQ

Post a new FAQ entry:

```bash
curl -X POST http://localhost:8000/api/faqs/ -H "Content-Type: application/json" -d '{
    "question": "How do I use the FAQ system?",
    "answer": "You can add, edit, and delete FAQs via the admin panel.",
    "language": "en"
}'
```

Response:

```json
{
    "id": 2,
    "question": "How do I use the FAQ system?",
    "answer": "You can add, edit, and delete FAQs via the admin panel.",
    "language": "en"
}
```
### 3. Update an FAQ

Update an existing FAQ:

```bash
curl -X PUT http://localhost:8000/api/faqs/1/ -H "Content-Type: application/json" -d '{
    "question": "What is the FAQ system?",
    "answer": "This system allows you to manage FAQs easily.",
    "language": "en"
}'
```
### 4. Delete an FAQ

Delete an FAQ entry:

```bash
curl -X DELETE http://localhost:8000/api/faqs/1/
```

## Additional Notes
WYSIWYG Editor: This project uses django-ckeditor for editing FAQ answers.
Caching: Redis caching is used for faster API responses.
Multi-language Support: The system supports multiple languages, and FAQ answers can be translated accordingly.
Testing: Unit tests are provided in faq/tests.py using pytest.

`Name: Anant Agarwal
 Email: anantagarwal1512@gmail.com`
