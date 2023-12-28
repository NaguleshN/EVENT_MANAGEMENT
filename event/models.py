from django.db import models

# Create your models here.

mode_choice=(('online','online'),('offline','offline'))
varieties=(('technical','technical'),('non-technical','non-technical'))
class Event(models.Model):
    event_name=models.CharField( max_length=20)
    instruction=models.CharField(max_length=1000)
    category=models.CharField(max_length=14,choices=varieties)
    date=models.DateField()
    mode=models.CharField( max_length=10,  choices=mode_choice)
    registration_fee=models.IntegerField()
    prize_amount=models.IntegerField()
    contact_number=models.BigIntegerField()
    time=models.TimeField()
    venue=models.CharField(max_length=50)
    def __str__(self):
        return self.event_name
    
# class registeration(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     event=models.CharField(max_length=30)
