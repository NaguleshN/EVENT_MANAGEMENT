from django.db import models

# Create your models here.

mode_choice=(('online','online'),('offline','offline'))
class Event(models.Model):
    event_name=models.CharField( max_length=20)
    instruction=models.CharField(max_length=1000)
    category=models.ForeignKey(varieties,on_delete=models.CASCADE)
    date=models.DateField()
    mode=models.CharField( max_length=10,  choices=mode_choice)
    registration_fee=models.IntegerField()
    prize_amount=models.IntegerField()
    contact_number=models.BigIntegerField()
    duration=models.TimeField()
    venue=models.CharField(max_length=50)
    def __str__(self):
        return self.event_name
    
class registeration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event=models.CharField(max_length=30)
