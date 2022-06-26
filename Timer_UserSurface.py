from pickle import TRUE
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import time, _thread

# Definition of variables
timers = {}
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
mtimer = 0
dont_print = False

# Displayed texts
separator = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

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
root.geometry("300x150")
root.resizable(False, False)
root.title('Sign In')

# store email address and password
email = tk.StringVar()
password = tk.StringVar()


def login_clicked():
    """ callback when the login button clicked
    """
    msg = f'You entered email: {email.get()} and password: {password.get()}'
    showinfo(
        title='Information',
        message=msg
    )




#   Start of program

# Header
print("Timer with 4 threads which can be defined")
print("Please define your timers\n")

# Definition of timers
## Name 'e' can't be given
print("How many timers would you like to use?")

i = 0
while i == 0:                                                   #Enterign the amount of timers wished
    try:
        m0 = input()
        timers_number = int(m0)
        i = 1
        break
    except:
        print("Please enter a number!")

if timers_number < 1:
    timers_number = 1

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






# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# email
email_label = ttk.Label(signin, text="Email Address:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)


root.mainloop()