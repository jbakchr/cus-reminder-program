#!/usr/bin/env python3 -W ignore::DeprecationWarning

from datetime import date
import tkinter as tk
from tkinter import ttk


def get_last_run_date():
    with open("/Users/jonasphillipson/MyDocuments/Python/01-udemy/03-gui-dev-w-py-and-tkinter/own-trials/03-reminder-script/last_run.txt", "r") as file:
        return file.read()


def update_last_run_date():
    with open("/Users/jonasphillipson/MyDocuments/Python/01-udemy/03-gui-dev-w-py-and-tkinter/own-trials/03-reminder-script/last_run.txt", "w") as file:
        file.write(str(current_date))
    root.destroy()


def start_reminder_app():
    # App
    root.title("Reminder!")
    root.protocol("WM_DELETE_WINDOW", root.destroy)

    # Frame
    main_frame = main_frame = ttk.Frame(root, padding=(10, 10))
    main_frame.pack()

    # Label
    label = ttk.Label(
        main_frame, text="Har du husket at tage din medicin?")
    label.pack(padx=100, pady=20)

    # No button
    no_button = ttk.Button(
        main_frame, text="Nej", command=root.destroy)
    no_button.pack(side="left")
    no_button.focus()

    # Yes button
    right_button = ttk.Button(main_frame, text="Ja",
                              command=update_last_run_date)
    right_button.pack(side="right")

    root.mainloop()


# Get Tkinter root
root = tk.Tk()

# Get latest run date
last_run = get_last_run_date()

# Get current date
current_date = str(date.today())

# Check for reminder
if last_run != current_date:
    start_reminder_app()
