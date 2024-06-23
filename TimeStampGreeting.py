# ============================TIMESTAMP GREETING ON TURTLE================================
import time
import turtle as t

# Setup the screen
t.bgcolor('black')
t.color('white')
t.hideturtle()
t.penup()
t.speed(0)

def update_time():
    while True:
        # Get current time
        current_time = time.strftime("%I:%M:%S %p")  # Note the change to colons

        # Determine the appropriate greeting
        hour = int(time.strftime("%I"))
        period = time.strftime("%p")
        
        if period == "AM":
            if 6 <= hour < 12:
                greeting = "Good Morning  ⁠❤"
            else:
                greeting = "Good Night ⁠♡ "
        elif period == "PM":
            if hour == 12 or hour < 5:
                greeting = "Good Afternoon 💕"
            elif 5 <= hour < 8:
                greeting = "Good Evening 💫✨ "
            else:
                greeting = "⁠Good Night ⁠💕🥰 "

        # Clear the screen and write the time and greeting
        t.clear()
        t.goto(0, 30)  # Position for the time
        t.write(current_time, align="center", font=("Bell MT", 70, 'bold'))
        t.goto(0, -30)  # Position for the greeting
        t.write(greeting, align="center", font=("Segoe Script", 30, 'bold'))
        
        time.sleep(1)  # Wait for 1 second

# Start updating the time
update_time()



# ⁠♡ (◕⁠ᴗ◕⁠) ⁠♡  ⁠✿  ⁠❤(⁠◕⁠ᴗ⁠◕⁠)⁠❤  😘  🫶🏻
# =========================TIMESTAMP GREETING ON TERMINAL================================
# import time

# def print_greeting():
#     hour = int(time.strftime("%I"))
#     period = time.strftime("%p")
        
#     if period == "AM":
#         if 6 <= hour < 12:
#             print("Good Morning!")
#         else:
#             print("Good Night!")
#     elif period == "PM":
#         if hour == 12 or hour < 5:
#             print("Good Afternoon!")
#         elif 5 <= hour < 8:
#             print("Good Evening!")
#         else:
#             print("Good Night!")

# def update_time():
#     while True:
#         global greeting
#         greeting = time.strftime("%I-%M-%S %p")
#         print(greeting, end='\r')  # Print on the same line
#         time.sleep(1)  # Wait for 1 second

# print_greeting()
# update_time()



# =======================TIMESTAMP GREETING BY OWN============================
# import time

# current_time = time.strftime("%I:%M:%S %p")
# hour = int(time.strftime('%I'))
# period = time.strftime('%p')

# if period == 'AM':
#     if 6 <= hour < 12:
#         greeting = "Good Morning"
#     else:
#         greeting = "Good Night"
# else:
#     if 12 >= hour > 5:
#         greeting = "Good Afternoon"
#     elif 5 <= hour < 8:
#         greeting = "Good Evening"
#     else:
#         greeting = "Good Night"

# print(current_time)
# print(greeting)




# import this