import datetime

def current_date_time():
    current = datetime.datetime.today()
    print(f"Current date and time: {current.year}-{current.month:02d}-{current.day:02d} {current.hour:02d}:{current.minute:02d}:{current.second:02d}")
current_date_time()


add_day = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    current_date = datetime.date.today()
    delta = datetime.timedelta(days = add_day)
    future_date = current_date + delta
    print(future_date)
calculate_future_date()




#