import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class FitnessTracker:
    def __init__(self):
        self.username = None
        self.password = None
        self.logged_in = False
        self.workout_history = []

    def register(self, username, password):
        self.username = username
        self.password = password
        messagebox.showinfo("Registration", "Registration successful!")

    def login(self, username, password):
        if username == self.username and password == self.password:
            self.logged_in = True
            messagebox.showinfo("Login", "Login successful!")
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")

    def logout(self):
        self.logged_in = False

    def track_workout(self, workout_type, duration, calories):
        if self.logged_in:
            workout_entry = {'type': workout_type, 'duration': duration, 'calories': calories, 'date': datetime.now()}
            self.workout_history.append(workout_entry)
            messagebox.showinfo("Workout Tracked", "Workout tracked successfully!")
        else:
            messagebox.showerror("Authentication Error", "You need to log in to track workouts.")

    def view_workout_history(self):
        if self.logged_in:
            history_text = "Workout History:\n\n"
            for entry in self.workout_history:
                history_text += f"Date: {entry['date']}, Type: {entry['type']}, Duration: {entry['duration']} minutes, Calories: {entry['calories']}\n"
            messagebox.showinfo("Workout History", history_text)
        else:
            messagebox.showerror("Authentication Error", "You need to log in to view workout history.")

class FitnessAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Tracker")

        self.tracker = FitnessTracker()

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1)

        self.register_button = tk.Button(root, text="Register", command=self.register)
        self.register_button.grid(row=2, column=0)
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=1)
        self.logout_button = tk.Button(root, text="Logout", command=self.logout)
        self.logout_button.grid(row=2, column=2)

        self.workout_type_label = tk.Label(root, text="Workout Type:")
        self.workout_type_label.grid(row=3, column=0)
        self.workout_type_entry = tk.Entry(root)
        self.workout_type_entry.grid(row=3, column=1)

        self.duration_label = tk.Label(root, text="Duration (minutes):")
        self.duration_label.grid(row=4, column=0)
        self.duration_entry = tk.Entry(root)
        self.duration_entry.grid(row=4, column=1)

        self.calories_label = tk.Label(root, text="Calories Burned:")
        self.calories_label.grid(row=5, column=0)
        self.calories_entry = tk.Entry(root)
        self.calories_entry.grid(row=5, column=1)

        self.track_button = tk.Button(root, text="Track Workout", command=self.track_workout)
        self.track_button.grid(row=6, column=0)

        self.view_history_button = tk.Button(root, text="View Workout History", command=self.view_workout_history)
        self.view_history_button.grid(row=6, column=1)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.tracker.register(username, password)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.tracker.login(username, password)

    def logout(self):
        self.tracker.logout()

    def track_workout(self):
        workout_type = self.workout_type_entry.get()
        duration = int(self.duration_entry.get())
        calories = int(self.calories_entry.get())
        self.tracker.track_workout(workout_type, duration, calories)

    def view_workout_history(self):
        self.tracker.view_workout_history()

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessAppGUI(root)
    root.mainloop()
