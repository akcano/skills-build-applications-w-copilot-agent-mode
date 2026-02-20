from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Clear data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
        wonderwoman = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password')
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password')

        # Activities
        Activity.objects.create(user='ironman', type='Running', duration=30)
        Activity.objects.create(user='batman', type='Cycling', duration=45)
        Activity.objects.create(user='wonderwoman', type='Swimming', duration=60)
        Activity.objects.create(user='spiderman', type='Yoga', duration=20)

        # Leaderboard
        Leaderboard.objects.create(user='ironman', points=100)
        Leaderboard.objects.create(user='batman', points=120)
        Leaderboard.objects.create(user='wonderwoman', points=150)
        Leaderboard.objects.create(user='spiderman', points=90)

        # Workouts
        Workout.objects.create(name='HIIT', description='High Intensity Interval Training')
        Workout.objects.create(name='Strength', description='Strength training workout')
        Workout.objects.create(name='Cardio', description='Cardio workout')
        Workout.objects.create(name='Flexibility', description='Flexibility and stretching')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
