# work timer advanced

# import
from pickle import TRUE
import tkinter as tk
from tkinter import ttk
from tkinter import *
import time

# definition of vars
timer_starttime = 0
timer_time = 0
timer_paused = False
timer_pausetime = 0
timer_totaltime = 0

# start clicked
def start_clicked():
    global timer_starttime
    timer_starttime = time.time()
    signin.destroy()

    # calculation of time since start
    timer_time = 0

    # ground timer label
    ground_timer_label = ttk.Label(counting, text = ground_timer.get() + ':')
    ground_timer_label.pack(fill='x', expand=True)

    # ground timer value
    ground_timer_value = ttk.Label(counting, text = time.strftime("%H:%M:%S", time.gmtime(timer_time)))
    ground_timer_value.pack(fill='x', expand=True)

    # refresh window every 1 second
    def refresh_window():
        global timer_starttime
        global timer_time
        global timer_totaltime
        global timer_pausetime
        global timer_paused
        timer_totaltime = time.time() - timer_starttime
        if timer_paused == True:
            timer_pausetime = timer_totaltime - timer_time
        else:
            timer_time = timer_totaltime - timer_pausetime
            ground_timer_label["text"] = ground_timer.get() + ':'
            ground_timer_value["text"] = time.strftime("%H:%M:%S", time.gmtime(timer_time))
        root.after(1000, refresh_window)

    # end clicked
    def end_clicked():
        root.destroy()

    # pause clicked
    def pause_clicked():
        global timer_paused
        if timer_paused == False:
            timer_paused = True
            ground_timer_label["text"] = ground_timer.get() + ': PAUSED'          
        else:
            timer_paused = False
            refresh_window()

    # pause button
    pause_button = ttk.Button(counting, text="pause/continue", command=pause_clicked)
    pause_button.pack(fill='x', expand=True, pady=10)

    # end button
    end_button = ttk.Button(counting, text="END", command=end_clicked)
    end_button.pack(fill='x', expand=True, pady=10)

    # automatic start of refreshing the window
    refresh_window()

# root window
root = tk.Tk()
root.geometry("200x150")
root.resizable(True, True)
root.title('Work Timer')

# store email address and password
ground_timer = tk.StringVar()

# frame to name timer
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# ground timer label + entry
ground_timer_label = ttk.Label(signin, text="Enter name of timer: ")
ground_timer_label.pack(fill='x', expand=True)

ground_timer_entry = ttk.Entry(signin, textvariable=ground_timer)
ground_timer_entry.pack(fill='x', expand=True)
ground_timer_entry.focus()

# start button
start_button = ttk.Button(signin, text="Start", command=start_clicked)
start_button.pack(fill='x', expand=True, pady=10)

# frame to run the timer
counting = ttk.Frame(root)
counting.pack(padx=10, pady=10, fill='x', expand=True)

root.mainloop()

