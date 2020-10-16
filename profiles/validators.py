from django.core.exceptions import ValidationError
from datetime import date

def is_past_date(value):
    print(value)
    if value > date.today():
        raise ValidationError(f'{value} is a future date')