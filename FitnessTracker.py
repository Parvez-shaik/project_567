class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.distance = 0.0
        self.calories_burned = 0
        self.goals = {
            'steps': 10000,
            'distance': 5.0,
            'calories': 500
        }

    def track_steps(self, steps):
        self.steps += steps
        self.update_progress()

    def track_distance(self, distance):
        self.distance += distance
        self.update_progress()

    def track_calories(self, calories):
        self.calories_burned += calories
        self.update_progress()

    def update_progress(self):
        if self.steps >= self.goals['steps'] and \
                self.distance >= self.goals['distance'] and \
                self.calories_burned >= self.goals['calories']:
            print("Congratulations! You've reached all your fitness goals.")

    def set_goals(self, steps, distance, calories):
        self.goals['steps'] = steps
        self.goals['distance'] = distance
        self.goals['calories'] = calories

    def view_progress(self):
        print(f"Steps: {self.steps}")
        print(f"Distance: {self.distance} miles")
        print(f"Calories burned: {self.calories_burned}")

    def log_workout(self, workout_type, duration, calories):
        print(f"Logged {workout_type} workout for {duration} minutes, burned {calories} calories")


# Example usage
if __name__ == "__main__":
    tracker = FitnessTracker()
    tracker.track_steps(5000)
    tracker.track_distance(2.5)
    tracker.track_calories(300)
    tracker.view_progress()
    tracker.set_goals(15000, 10.0, 1000)
    tracker.track_steps(10000)
    tracker.track_distance(5.0)
    tracker.track_calories(600)
    tracker.view_progress()
    tracker.log_workout("Running", 30, 400)
