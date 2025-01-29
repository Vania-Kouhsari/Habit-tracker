# Habit Tracker  

## Description  
Habit Tracker is a simple web application that helps users track and manage their daily habits. Users can add, mark complete, or delete habits, and each habit can be customized with a name, description, and color. The app provides an easy way to maintain consistency in habit-building.

## Features  
- Add a habit  
- Mark a habit as complete  
- View activity (dates completed and habit description)  
- Delete a habit  
- Switch between dark mode and light mode  

## Tech Stack  
- Frontend: HTML, CSS, JavaScript  
- Backend: Python, Flask, SQLite  
- Dependencies: Flask-SQLAlchemy  

## Usage  
- Add a habit: Click on the "+" button, fill out the form, and click "Add Habit".  
- Mark as complete: Click "Mark as complete" to mark it as completed.  
- View activity: Click "View Activity" to see completed dates and the habit description.  
- Delete a habit: Click the "delete" button on a habit card.  
- Switch theme: Click the "moon icon" (top left) for dark mode and the "sun icon" (top left) for light mode.  

## Run the Habit Tracker App
1. Clone the GitHub repository to your local machine using the following command:

git clone https://github.com/Vania-Kouhsari/Habit-tracker
cd Habit-tracker


2. Create a virtual environment to isolate the project’s dependencies using the following command:

python -m venv venv


3. Activate the Virtual Environment
		On Windows:

venv\Scripts\activate


		On Mac/Linux:

source venv/bin/activate


4. Install the required dependencies listed in requirements.txt using the following command:

pip install -r requirements.txt 


5. Run the Flask app using the following command:

python app.py

The application should now be running at http://127.0.0.1:5000/.

## Folder Structure
```bash
habit-tracker/
├── pycache/
│   ├── app.cpython39.pyc
│   └── app.cpython313.pyc
├── app/
│   ├── pycache/
│   ├── init.py
│   ├── models.py
│   └── routes.py
├── docs_phase3/
│   └── Habit-Tracker-Vid.mp4
├── static/
│   ├── calendar.js
│   ├── darkmode.js
│   ├── script.js
│   └── styles.css
├── templates/
│   ├── calendar.html
│   └── index.html
├── README.md
├── app.py
├── habit_tracker.db
└── requirements.txt
```
