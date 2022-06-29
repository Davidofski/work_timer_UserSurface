# import
from pickle import TRUE
import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter.messagebox import showinfo
import time, _thread

# Definition of variables
timers = {}
empty_labels = ['lb1', 'lb2', 'lb3', 'lb4', 'lb5', 'lb6', 'lb7', 'lb8', 'lb9']
lbcount = 0
timers_totaltime = 0
timers_starttime = 0
active_timer = 0
nonactive_timer_sum = 0
timers_count = 0

# Memory
m0 = 0
m1 = 0
m2 = 0
m3 = 0
x = 0
timers_starttime = 0
now = time.time()

# Definition of time thread
def display_timers():
    sum_inactive_timers = 0
    for i in carrier:                                       #Summing up inactive timers to deduct from the active
        if i !=  active_timer:
            sum_inactive_timers = sum_inactive_timers + timers[i]
    if dont_print == False:
        print("Actual time:")

    for i in carrier:                                       #Calculation of active timer
        timers_totaltime = time.time() - timers_starttime
        if i == active_timer:
            timers[i] = timers_totaltime - sum_inactive_timers
            print("ACTIVE")
        if dont_print == False:
            print(time.strftime("%H:%M:%S", time.gmtime(timers[i])), " : ", i)

# root window
root = tk.Tk()
root.geometry("300x300")
root.resizable(True, True)
root.title('Work Timer')

# store email address and password
ground_timer = tk.StringVar()
password = tk.StringVar()

# open timer window when 'start' has been clicked
def start_clicked():
    timers_starttime = time.time()

# add timer when 'add' has been clicked
def add_clicked(lbcount):
    if lbcount < 10:
        new_label = empty_labels[lbcount]
        lbcount = lbcount + 1
    else:
        msg = f'You reached the max amount of timer!'
        showinfo(
            title='Information',
            message=msg
        )

# get time during runnign program @refresh
def get_time():
    now = time.time()
    timers[1] = now - timers_starttime
    ground_timer_label["text"] = "Timer 1: " + time.strftime("%H:%M:%S", time.gmtime(timers[1]))

# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# ground timer
ground_timer_label = ttk.Label(signin, text="Timer 1: " + time.strftime("%H:%M:%S", time.gmtime(now)))
ground_timer_label.pack(fill='x', expand=True)

ground_timer_entry = ttk.Entry(signin, textvariable=ground_timer)
ground_timer_entry.pack(fill='x', expand=True)
ground_timer_entry.focus()

# start button
start_button = ttk.Button(signin, text="Start", command=start_clicked)
start_button.pack(fill='x', expand=True, pady=10)

# add button
add_button = ttk.Button(signin, text="Add timer", command=add_clicked)
add_button.pack(fill='x', expand=True, pady=10)

# refresh button
refresh_button = ttk.Button(signin, text="Refresh", command=get_time)
refresh_button.pack(fill='x', expand=True, pady=10)

root.mainloop()




#   Start of program

# Definition of timers

while i < timers_number + 1:                        #Filling the amount of timeres into the library
    timers[i] = 0
    i = i+1
i = 1
while i < timers_number + 1:                        #Naming of each timer
    print("Define timer", i)
    m1 = input()
    if m1 == 'e':
        print("\n'e' canb't be given! 'e'is a commmand\n")
        print("Try again!\n")
        # m1 = 'TimerX'
    if m1 != 'e':
        timers[m1] = timers[i]
        del timers[i]
        i = i+1
carrier = timers.keys()                                     #Find the keys of timers

# Definition of active timer
## If only one timer, then jump over and activate the only timer
if timers_number > 1:
    print("Activate one of your timers!")
    print("Which one shall it be?")
    timer_found = False
    while timer_found == False:                         #Loop to find if timer is exists
        active_timer = input()
        for i in carrier:
            if i == active_timer:
                print("Timer found\n")
                print(separator)
                timer_found = True
            else:
                print("Input not equal to timer:", i)
        if timer_found == False:
            print("Try again!")
else:
    active_timer = m1

timers_count = len(timers)

#Start of timers
timers_run = True
timers_starttime = time.time()
display_timers()




