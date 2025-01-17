import sqlite3
from datetime import datetime

DATABASE = 'habit_tracker.db'

# Function to initialize the database
def init_db():
    with sqlite3.connect('habit_tracker.db') as conn:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,  
            color TEXT DEFAULT #FF5733,
            start_date TEXT NOT NULL,
            streak INTEGER DEFAULT 0,
            last_completed_date TEXT,
            completion_dates TEXT 
        )''')
        conn.commit()

# Function to get all habits
def get_all_habits():
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM habits")
        return cur.fetchall()

# Function to add a habit to the database
def add_habit(name, description, color, start_date): 
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute('''INSERT INTO habits (name, description, color, start_date) 
                       VALUES (?, ?, ?, ?)''', (name, description, color, start_date))
        conn.commit()

# Function to update the streak of a habit
def update_streak(habit_id):
    today = datetime.now().strftime('%Y-%m-%d')
    
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()

        # Get the habit's last completed date and streak
        cur.execute("SELECT last_completed_date, streak FROM habits WHERE id = ?", (habit_id,))
        habit = cur.fetchone()
        
        if habit:
            last_completed_date, streak = habit

            # If the habit has been completed today, return False (no need to increment streak)
            if last_completed_date == today:
                return False  # Habit has already been completed today

            # If it's the first time completion (streak == 0), set streak to 1
            if streak == 0:
                cur.execute("UPDATE habits SET streak = 1, last_completed_date = ? WHERE id = ?", (today, habit_id))
            else:
                # For subsequent completions, increment the streak by 1
                cur.execute("UPDATE habits SET streak = streak + 1, last_completed_date = ? WHERE id = ?", (today, habit_id))
            conn.commit()

    return True  # Habit marked as completed and streak updated successfully

# Function to delete a habit
def delete_habit(habit_id):
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
        conn.commit()

# Function to get last completed date (for updating streaks)
def last_completed_date():
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT last_completed_date FROM habits WHERE last_completed_date IS NOT NULL")
        completed_dates = cur.fetchall()

    # Convert dates from tuple format to list of strings
    completed_dates = [date[0] for date in completed_dates]
    return completed_dates

#retrieves all completion dates
def update_completion_date(habit_id):
    with sqlite3.connect('habit_tracker.db') as conn:
        cur = conn.cursor()
        # Get today's date
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Get the existing completion dates for this habit
        cur.execute("SELECT completion_dates FROM habits WHERE id = ?", (habit_id,))
        result = cur.fetchone()
        
        if result:
            completion_dates = result[0] if result[0] else ''
            # Append today's date to the existing completion dates (comma-separated)
            new_dates = completion_dates + ',' + today if completion_dates else today
            # Update the habit with the new completion dates
            cur.execute("UPDATE habits SET completion_dates = ? WHERE id = ?", (new_dates, habit_id))
            conn.commit()