# Simple Reminder App

while True:
    answer = input("Have you submitted your assignment? ").lower()
    
    if answer == "done":
        print("Great job! ")
        break
    else:
        print("Still waiting... Submit it already!")