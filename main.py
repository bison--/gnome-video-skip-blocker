#! /usr/bin/env python3

from datetime import datetime
from tkinter import *
from tkinter import ttk

EVENTS_TO_MONITOR = [
    "<Key>", "<KeyPress>", "<KeyRelease>",
    "<Button>", "<ButtonPress>", "<ButtonRelease>", "<Motion>",
    "<Enter>", "<Leave>", "<FocusIn>", "<FocusOut>",
    "<Configure>", "<Expose>", "<MouseWheel>",
    "<Destroy>", "<Unmap>", "<Map>", "<Visibility>",
]

def handle_event_debug(event):
    print(f"{datetime.now()}: Event: {event.type}, Widget: {event.widget}, Details: {event.__dict__}")

def open_anti_skip_window_big():
    open_anti_skip_window("290x1")

def open_anti_skip_window(size="10x1"):
    new_window = Toplevel(root)  # Create a new window
    new_window.title("YouTube skip blocker")
    new_window.geometry(size)
    new_window.attributes("-topmost", True)
    if debug_check_state.get() == 1:
        for ev in EVENTS_TO_MONITOR:
            new_window.bind(ev, handle_event_debug)

def check_debug():
    pass

root = Tk()
root.title("gnome-shell video skip blocker")
root.geometry("380x100")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="new smoll skip blocker window", command=open_anti_skip_window).grid(column=1, row=0)
ttk.Button(frm, text="new bigger skip blocker window", command=open_anti_skip_window_big).grid(column=1, row=1)

debug_check_state = IntVar(value=0)
check_button = ttk.Checkbutton(frm, text="log debug", variable=debug_check_state, command=check_debug)
check_button.grid(column=1, row=2)

root.mainloop()
