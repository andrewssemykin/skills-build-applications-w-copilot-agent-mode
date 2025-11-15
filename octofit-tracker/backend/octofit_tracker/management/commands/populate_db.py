from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models


from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User = get_user_model()
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, distance=5)
        Activity.objects.create(user=users[1], type='cycle', duration=60, distance=20)
        Activity.objects.create(user=users[2], type='swim', duration=45, distance=2)
        Activity.objects.create(user=users[3], type='run', duration=50, distance=10)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', team=marvel)
        Workout.objects.create(name='Strength Training', description='Strength for DC heroes', team=dc)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

# Models for reference (to be created in octofit_tracker/models.py):
# class Team(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#
# class Activity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     duration = models.IntegerField()
#     distance = models.FloatField()
#
# class Workout(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#
# class Leaderboard(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     points = models.IntegerField()
