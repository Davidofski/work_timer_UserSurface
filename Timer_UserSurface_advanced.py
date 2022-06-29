# work timer advanced

# import
from pickle import TRUE
import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter.messagebox import showinfo
import time, _thread
from time import strftime

# definition of vars
timer_starttime = 0
timer_time = 0
timer_paused = False
timer_pausetime = 0

# start clicked
def start_clicked():
    timer_starttime = time.time()
    signin.destroy()

    # calculation of time since start
    timer_time = time.time() - timer_starttime

    # ground timer label
    ground_timer_label = ttk.Label(counting, text = ground_timer.get() + ':')
    ground_timer_label.pack(fill='x', expand=True)

    # ground timer value
    ground_timer_value = ttk.Label(counting, text = time.strftime("%H:%M:%S", time.gmtime(timer_time)))
    ground_timer_value.pack(fill='x', expand=True)
    ground_timer_value.after(1000, time)

    # refresh clicked
    def refresh_clicked():
        timer_time = time.time() - timer_starttime
        ground_timer_value["text"] = time.strftime("%H:%M:%S", time.gmtime(timer_time))

    # end clicked
    def end_clicked():
        root.destroy()

    # add clicked
    def add_clicked():
        counting.destroy()

    # pause clicked
    def pause_clicked():
        if timer_paused == False:
            timer_time = time.time() - timer_starttime
            timer_paused = True
        else:
            timer_starttime = time.time() - timer_time
            timer_paused = False


    # refresh button
    refresh_button = ttk.Button(counting, text="Refresh", command=refresh_clicked)
    refresh_button.pack(fill='x', expand=True, pady=10)

    # pause button
    pause_button = ttk.Button(counting, text="Pause", command=pause_clicked)
    pause_button.pack(fill='x', expand=True, pady=10)

    # add button
    add_button = ttk.Button(counting, text="Add timer", command=add_clicked)
    add_button.pack(fill='x', expand=True, pady=10)

    # end button
    end_button = ttk.Button(counting, text="END", command=end_clicked)
    end_button.pack(fill='x', expand=True, pady=10)

# root window
root = tk.Tk()
root.geometry("250x250")
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

