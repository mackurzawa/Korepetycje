# Tutoring App Readme

Welcome to the Tutoring App repository! This application is designed to assist my students in their learning journey by providing two main functionalities - homework assignements and equation generator. App is hosted on Streamlit Community Cloud. You can access it here and try it yourself:

https://korepetycje.streamlit.app/  (as name use "test")

## Features

### Homework Assignment
Students can quickly complete homework assignments using the app, and the system promptly evaluates their submissions. Users have the opportunity to review their performance and make corrections.

### Random Equation Generator
The app includes a random equation generator feature. Users can solve randomly generated arithmetic problems. The system checks the answers, and users can review and correct their solutions.

## Important Note

All user responses are automatically saved in a Google Sheets spreadsheet. The spreadsheet contains the following information:

- Student's name
- Task content
- Correct answer
- User's response
- Time taken to solve the problem
- Execution time

This feature ensures that both students and tutors can track progress and identify areas for improvement.

## Technology Stack

The application is implemented using Streamlit in Python, providing a user-friendly interface for seamless interaction.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/tutoring-app.git
cd tutoring-app
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app locally:
```
streamlit run main.py
```

4. Access the app through your web browser at http://localhost:8501.
