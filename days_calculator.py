from datetime import datetime

def calculator():
    now = datetime.now()
    event_date = datetime(day=30, month=3, year=2022)

    days_until = event_date - now
    # print(days_until.days)
    return days_until.days

calculator()


