# Leadership Self Assessment

A full-stack self assessment web application built using Django that allows users to evaluate their leadership and personal development skills through a dynamic questionnaire system. The application calculates scores automatically, displays assessment results instantly, and sends a detailed email report along with a downloadable PDF report.

## Features

- Dynamic self-assessment questionnaire
- Automatic score calculation
- Instant result display
- Email report delivery
- PDF report generation and attachment
- Clean and responsive user interface
- Error handling for failed email delivery

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Django

### Database
- PostgreSQL

### Additional Tools
- WeasyPrint (PDF generation)
- SMTP Email Integration

## Project Structure

```bash
leadership-self-assessment/
│
├── assessment/
├── leadership_project/
├── static/
├── templates/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Keerthan-17/leadership-self-assessment
cd leadership-self-assessment
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the root directory.

```env
SECRET_KEY=your_secret_key
DEBUG=True

EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
```

## Run the Project

```bash
python manage.py migrate
python manage.py runserver
```

Open in browser:

```bash
http://127.0.0.1:8000/
```

## Screenshots

<img width="1366" height="676" alt="image" src="https://github.com/user-attachments/assets/34cca5bc-61cb-4204-9525-8efb8294428a" />

<img width="1343" height="677" alt="image" src="https://github.com/user-attachments/assets/57391440-bf8e-40b5-a4b5-6dcf3e3ee4e7" />


## Future Enhancements

- User authentication system
- Admin dashboard analytics
- Database-driven questionnaires
- Result history tracking
- Deployment with Docker
- AI-based performance insights

## Author

**Keerthan M**

## License

This project is developed for educational and learning purposes.
