import tkinter as tk
from tkinter import ttk

class MainTopFrame(tk.Frame):


    def __init__(self, master):
        super().__init__(master)
        self.__run_button = tk.Button(self, text="Run")
        self.__delete_button = tk.Button(self, text="Delete")
        self.__args_entry = tk.Entry(self)

        self.__args_entry.pack(side="left", padx=10, pady=10, expand=True, fill="x")
        self.__run_button.pack(side="left", padx=10)
        self.__delete_button.pack(side="bottom", padx=10, pady=10)

    def set_run_action(self, command):
        self.__run_button.config(command=command,
                                repeatdelay=1000,
                                repeatinterval=100)
        self.__args_entry.bind("<Return>", lambda e: command())

    def set_del_action(self, command):
        self.__delete_button.config(command=command,
                                    repeatdelay=1000,
                                    repeatinterval=100)

    def get(self):
        return self.__args_entry.get()
