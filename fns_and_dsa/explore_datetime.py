from datetime import datetime, timedelta

def display_current_datetime():
    current = datetime.now()
    format_date_time = current.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {format_date_time}")
    
display_current_datetime()


add_day = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    now = datetime.now()
    current_date = now.date()
    delta = timedelta(days = add_day)
    future_date = current_date + delta
    format_date = future_date.strftime("%Y-%m-%d")
    print(format_date)
calculate_future_date()