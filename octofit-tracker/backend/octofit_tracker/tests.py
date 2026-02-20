from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=30)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')

    def test_activity_str(self):
        self.assertEqual(str(self.activity), 'testuser - Run')

    def test_leaderboard_str(self):
        self.assertEqual(str(self.leaderboard), 'testuser - 100')
