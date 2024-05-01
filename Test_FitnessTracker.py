import unittest
from FitnessTracker import FitnessTracker

class TestFitnessTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = FitnessTracker()
        self.tracker.register("test_user", "test_password")
        self.tracker.login("test_user", "test_password")

    def test_register(self):
        self.assertEqual(self.tracker.username, "test_user")
        self.assertEqual(self.tracker.password, "test_password")

    def test_login(self):
        self.assertTrue(self.tracker.logged_in)

    def test_logout(self):
        self.tracker.logout()
        self.assertFalse(self.tracker.logged_in)

    def test_track_workout(self):
        self.tracker.track_workout("Running", 30, 400)
        self.assertEqual(len(self.tracker.workout_history), 1)

    def test_view_workout_history(self):
        self.tracker.track_workout("Running", 30, 400)
        history = self.tracker.view_workout_history()
        self.assertIn("Running", history)

if __name__ == '__main__':
    unittest.main()
