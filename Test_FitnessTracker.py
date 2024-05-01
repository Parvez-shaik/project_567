import unittest
from unittest.mock import patch, MagicMock
from FitnessTracker import FitnessTracker

class TestFitnessTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = FitnessTracker()
        self.tracker.username = "test_user"
        self.tracker.password = "test_password"

    def test_register(self):
        with patch('code.messagebox.showinfo') as mocked_showinfo:
            self.tracker.register("test_user", "test_password")
            mocked_showinfo.assert_called_once_with("Registration", "Registration successful!")

    def test_login(self):
        with patch('code.messagebox.showinfo') as mocked_showinfo:
            self.tracker.login("test_user", "test_password")
            mocked_showinfo.assert_called_once_with("Login", "Login successful!")

    def test_logout(self):
        self.tracker.logout()
        self.assertFalse(self.tracker.logged_in)

    def test_track_workout(self):
        with patch('code.messagebox.showinfo') as mocked_showinfo:
            self.tracker.logged_in = True
            self.tracker.track_workout("Running", 30, 400)
            mocked_showinfo.assert_called_once_with("Workout Tracked", "Workout tracked successfully!")

    def test_view_workout_history(self):
        with patch('code.messagebox.showinfo') as mocked_showinfo:
            self.tracker.logged_in = True
            self.tracker.view_workout_history()
            mocked_showinfo.assert_called_once_with("Workout History", "Workout History:\n\n")

if __name__ == '__main__':
    unittest.main()
