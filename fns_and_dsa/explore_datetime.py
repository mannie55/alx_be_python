from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current = datetime.now()
    print(f"Current date and time: {current.year}-{current.month:02d}-{current.day:02d} {current.hour:02d}:{current.minute:02d}:{current.second:02d}")
display_current_datetime()


add_day = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    now = datetime.now()
    current_date = now.date()
    delta = timedelta(days = add_day)
    future_date = current_date + delta
    print(future_date)
calculate_future_date()




#