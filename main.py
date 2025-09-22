# Import the GUI python library
import tkinter as tk
# Import a library for a message that pops up and keeps user informed
from tkinter import messagebox
# Import time library to help with timer functionality
# import time as time


# Global variable to keep track of time left on the timer in seconds
total_seconds = 0
timer_started = False
time_id = None

# Timer display/formatting functions **************************************
# Calculate hrs, mins, secs and format them to always be two digits
def format_time(seconds):
    hrs = seconds // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hrs:02}:{mins:02}:{secs:02}"

# Update the timer display
def update_timer_display():
    timer_value.set(format_time(total_seconds))

# Countdown function to decrease the timer every second
def countdown():
    global total_seconds, timer_started, time_id
    if total_seconds > 0 and timer_started:
        total_seconds -= 1
        update_timer_display()
        # Schedule countdown again after 1 second
        time_id = root.after(1000, countdown)
    elif total_seconds == 0:
        timer_started = False
        update_timer_display()
        messagebox.showinfo("Info", "Time's up!")


# Functions for the buttons ***************************************
def add_ten_minutes():
    try:
        global total_seconds
        total_seconds += 600
        update_timer_display()
    except Exception as e:
        print(f"An error occurred: {e}")

def add_one_minute():
    try:
        global total_seconds
        total_seconds += 60
        update_timer_display()
    except Exception as e:
        print(f"An error occurred: {e}")

def reset_timer():
    try:
        global total_seconds, timer_started, time_id
        # Reset the timer to 0 seconds
        total_seconds = 0
        # Reset the timer started flag
        timer_started = False
        # Cancel any scheduled countdown calls
        if time_id is not None:
            root.after_cancel(time_id)
            time_id = None
        update_timer_display()
    except Exception as e:
        print(f"An error occurred: {e}")

def pause_timer():
    try:
        global timer_started, time_id
        # Pause if the timer is currently running
        if timer_started:
            # Set the timer started flag to False
            timer_started = False
            # Cancel any scheduled countdown calls so timer stops
            if time_id is not None:
                # Cancel the scheduled countdown call
                root.after_cancel(time_id)
                time_id = None        
    except Exception as e:
        print(f"An error occurred: {e}")

def start_timer():
    try:
        global timer_started, time_id
        # Start the timer if it is not already running
        if not timer_started and total_seconds > 0:
            # Set the timer started flag to True
            timer_started = True
            # Start the countdown
            time_id = root.after(1000, countdown)
    except Exception as e:
        print(f"An error occurred: {e}")

# Make the main window for the Pomodoro timer *******************************
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("400x250")
# Prevent the window from being resized for minimalistic design
root.resizable(False, False)


# Create frames to organize the layout of the GUI *********************
top_frame = tk.Frame(root)
middle_frame = tk.Frame(root)
bottom_frame = tk.Frame(root)

# Top frame will hold the title label and timer display
top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
timer_value = tk.StringVar()
# Initialize the timer value with the formatted time
timer_value.set(value=format_time(total_seconds))

timer_display = tk.Label(top_frame, textvariable=timer_value, font=("Helvetica", 48))
# Center the timer display and add some vertical padding
timer_display.pack(anchor=tk.CENTER, pady=5, expand=True)

# Middle frame will hold the +10 Min and +1 Min buttons
middle_frame.grid_columnconfigure(0, weight=1)
middle_frame.grid_columnconfigure(1, weight=1)
# Place the middle frame below the top frame with some horizontal padding
middle_frame.pack(side=tk.TOP, padx=10, fill=tk.X)

# Bottom frame will hold the Reset, Pause, and Start buttons
bottom_frame.grid_columnconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(1, weight=1)
bottom_frame.grid_columnconfigure(2, weight=1)
# Place the bottom frame below the middle frame with some padding
bottom_frame.pack(side=tk.BOTTOM, padx=10, pady=10, fill=tk.X)


# Create buttons and place them in the appropriate frames *************************
# Make the buttons expand to fill their grid cell with sticky="nesw"

# A button for adding 10 minutes
add_ten_button = tk.Button(middle_frame, text="+10 Min", pady=5, command=add_ten_minutes)
add_ten_button.grid(row=0, column=0, sticky="nesw")

# A button for adding 1 minute
add_minute_button = tk.Button(middle_frame, text="+1 Min", pady=5, command=add_one_minute)
add_minute_button.grid(row=0, column=1, sticky="nesw")

# A button to reset the timer
reset_button = tk.Button(bottom_frame, text="Reset", pady=5, command=reset_timer)
reset_button.grid(row=0, column=0, sticky="nesw")

# A button to pause the timer
pause_button = tk.Button(bottom_frame, text="Pause", pady=5, command=pause_timer)
pause_button.grid(row=0, column=1, sticky="nesw")

# A button to start the timer
start_button = tk.Button(bottom_frame, text="Start", pady=5, command=start_timer)
start_button.grid(row=0, column=2, sticky="nesw")


# Run the main loop to keep the window open ******************************
root.mainloop()
