from django import template
from datetime import datetime
from django.utils import timezone

register=template.Library()

@register.filter
def humanized_date(valu):
    if valu:
        today=datetime.now().date()
        valu=timezone.localtime(valu)
        
        if valu.date()==today:
            return f"Today At {valu.strftime('%I:%M %p')}"
        if valu.date()==today.replace(day=today.day-1):
            return f"Yesterday At {valu.strftime('%I:%M %p')}"
        else:
            return f"{valu.date().strftime('%B %d'),valu.strftime('%I:%M %p')}"
    return "No Login Record Available"
            