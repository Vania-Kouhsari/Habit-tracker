from flask import jsonify, render_template, request, redirect
from app.models import get_all_habits, add_habit, update_streak, delete_habit, last_completed_date, update_completion_date ,DATABASE
from datetime import datetime
import sqlite3

# Initialize routes
def init_routes(app):
    # Home route, connects with db and fetches all habits
    @app.route('/')
    def index():
        habits = get_all_habits()
        return render_template('index.html', habits=habits)

    # Add habit route, adds a new habit to the database
    @app.route('/add', methods=['POST'])
    def add_habit():
        name = request.form['name']
        description = request.form['description']
        color = request.form['color']
        start_date = datetime.now().strftime("%Y-%m-%d")

        with sqlite3.connect(DATABASE) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO habits (name, description, color, start_date) VALUES (?, ?, ?, ?)",
                    (name, description, color, start_date))
            conn.commit()

        return redirect('/')

    # Delete habit route, deletes a habit from the db
    @app.route('/delete/<int:habit_id>', methods=['POST'])
    def delete_habit_route(habit_id):
        delete_habit(habit_id)
        return redirect('/')

    # integrate the "update_completion_date" in models.py
    @app.route('/update_streak/<int:habit_id>', methods=['POST'])
    def update_habit_streak(habit_id):
        # Check if the habit can be updated (completed today or not)
        success = update_streak(habit_id)

        if success:
            # If the streak update was successful, update the completion date
            update_completion_date(habit_id)
            return redirect('/')  # Habit streak updated successfully
        else:
            # Fetch the habit details to check its streak
            with sqlite3.connect(DATABASE) as conn:
                cur = conn.cursor()
                cur.execute("SELECT streak FROM habits WHERE id = ?", (habit_id,))
                habit = cur.fetchone()

            if habit and habit[0] == 0:
                # If streak is 0 update the streak
                return jsonify({"message": "First-time completion! Streak updated."}), 200
            else:
               return redirect('/')

    # Opening the calendar 
    @app.route('/calendar/<int:habit_id>', methods=['GET'])
    def view_calendar(habit_id):
        with sqlite3.connect('habit_tracker.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT name, description, start_date, streak, completion_dates, color FROM habits WHERE id = ?", (habit_id,))
            habit = cur.fetchone()

        if habit:
            # Parse completion dates (split the comma-separated string into a list)
            completion_dates = habit[4].split(',') if habit[4] else []

        return render_template('calendar.html', habit={
            'name': habit[0],
            'description': habit[1],
            'start_date': habit[2],
            'streak': habit[3],
            'color': habit[5]  
        }, dates=completion_dates)
        return "Habit not found", 404