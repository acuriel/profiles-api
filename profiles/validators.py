from django.core.exceptions import ValidationError
from datetime import date

def is_past_date(value):
    if not value < date.today:
        raise ValidationError(
            _('%(value)s is a future date'),
            params={'value': value},
        )