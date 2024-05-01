import unittest

class TestFitnessTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = FitnessTracker()

    def test_track_steps(self):
        self.tracker.track_steps(5000)
        self.assertEqual(self.tracker.steps, 5000)

    def test_track_distance(self):
        self.tracker.track_distance(2.5)
        self.assertEqual(self.tracker.distance, 2.5)

    def test_track_calories(self):
        self.tracker.track_calories(300)
        self.assertEqual(self.tracker.calories_burned, 300)

    def test_set_goals(self):
        self.tracker.set_goals(15000, 10.0, 1000)
        self.assertEqual(self.tracker.goals['steps'], 15000)
        self.assertEqual(self.tracker.goals['distance'], 10.0)
        self.assertEqual(self.tracker.goals['calories'], 1000)

    def test_log_workout(self):
        self.tracker.log_workout("Running", 30, 400)
        # You can add assertions to verify the output if necessary

if __name__ == '__main__':
    unittest.main()
