# FAQ Management System

This is a Django-based FAQ management system that lets you create, edit, and manage FAQs with multilingual support. It includes caching for better performance and a WYSIWYG editor to make editing easy. The system also provides a RESTful API to interact with FAQs programmatically.

## Table of Contents

- [Installation Steps](#installation-steps)
- [Creating a Superuser](#creating-a-superuser)
- [API Usage](#api-usage)
- [Additional Information](#additional-information)

## Installation Steps

Follow these steps to set up and run the FAQ Management System on your local machine.

### 1. Clone the Repository

First, clone the project from GitHub:

```bash
git clone https://github.com/procoding2022/multilingual_faq_backend.git
cd multilingual_faq_backend
```

### 2. Set Up a Virtual Environment

It's best to use a virtual environment to manage dependencies.

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

Install the required packages:

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

## Creating a Superuser

To access the admin panel and manage FAQs, you need to create a superuser.

```bash
python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password. Once created, log in to the admin panel at:

`http://localhost:8000/admin/`

After logging in, you can add, edit, and manage FAQs. The API endpoints will also start working as expected.

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

### 2. Get FAQs in a Specific Language

Fetch FAQs in Hindi (`hi`) or Bengali (`bn`):

```bash
curl http://localhost:8000/api/faqs/?lang=hi
curl http://localhost:8000/api/faqs/?lang=bn
```

### 3. Create a New FAQ

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
### 4. Update an FAQ

Update an existing FAQ:

```bash
curl -X PUT http://localhost:8000/api/faqs/1/ -H "Content-Type: application/json" -d '{
    "question": "What is the FAQ system?",
    "answer": "This system allows you to manage FAQs easily.",
    "language": "en"
}'
```
### 5. Delete an FAQ

Delete an FAQ entry:

```bash
curl -X DELETE http://localhost:8000/api/faqs/1/
```

## Additional Notes
Admin Panel: Available at `http://localhost:8000/admin/`.

Testing: Unit tests are provided in `faq/tests.py` using `pytest`.

For any questions, feel free to reach out.

`Name: Anant Agarwal
 Email: anantagarwal1512@gmail.com`
