from datetime import date , timedelta

WEEKDAYS = ['monday' , 'tuesday' , 'wednessday' , 'thursday' , 'friday' ,'saturday' , 'sunday']

def parse_due(text):
    text = text.strip().lower()
    today = date.today()
    if text=='today':
        return today
    if text=='tommarow':
        return today+timedelta(days=1)
    if text in WEEKDAYS:
        ahead = (WEEKDAYS.index(text) - today.weekday()) % 7 or 7
        return today+timedelta(days=ahead)
    return date.fromisoformat(text)
