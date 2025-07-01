# Task-6_Elevate_Labs

Portfolio Website with Flask. This project was created as part of Task 6 for the Elevate Labs Internship.

## Objective
Create a personal portfolio website using Python, Flask, HTML, and CSS. The site includes personal info, a projects page, and a contact form.

## Features
- Home, About, Projects, and Contact pages
- Responsive design with custom CSS
- Contact form with email sending (Flask-Mail)
- Environment variables managed with a .env file (python-dotenv)

## Setup Instructions
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root:
   ```env
   APP_KEY=your_secret_key_here
   EMAIL=your_email@example.com
   PASSWORD=your_email_password
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open your browser at [http://localhost:5000](http://localhost:5000)

## Project Structure
```
Task-6_Elevate_Labs/
├── app.py
├── requirements.txt
├── .env
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── about.html
    ├── projects.html
    └── contact.html
```

## Security Note
- **Never commit your `.env` file to version control.**
- Add `.env` to your `.gitignore` to keep your secrets safe.

## Customization
- Edit `templates/index.html` for your info and skills
- Edit `templates/projects.html` to showcase your work
- Edit `static/css/style.css` for custom styles
