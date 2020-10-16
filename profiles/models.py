from django.db import models
from datetime import date


class UserProfile(models.Model):
    firstname       = models.CharField(max_length=50)
    lastname        = models.CharField(max_length=50)
    birthdate       = models.DateField()
    picture         = models.ImageField(upload_to='profile', null=True)

    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'
    
    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.mont, self.birthdate.day))
    