task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority not in ["high", "medium", "low"] or time_bound not in["yes", "no"]:
    print("cant handle that")
else:
    match time_bound:
        case "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        case "no":
            print(f"Note: '{task}' is a {priority} priority task. consider completing it when you have freetime.")
        case _:
            print("Invalid input")

#match priority:
#        case "high":
#           if time_bound == "yes":
#                print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
#            else:
#                print(f"Note: '{task}' is a {priority} priority task. consider completing it when you have freetime.")
#        case "medium":
#            if time_bound == "yes":
#                print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
#            else:
#                print(f"Note: '{task}' is a {priority} priority task. consider completing it when you have freetime.")
#        case "low":
#            if time_bound == "yes":
#               print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
#            else:
#                print(f"Note: '{task}' is a {priority} priority task. consider completing it when you have freetime.")"""
        