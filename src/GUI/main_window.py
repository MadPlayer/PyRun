import tkinter as tk
from tkinter import ttk
import json_data_table as jdt
from py_run_gui import MainMenuBar, DataTableListBox
from py_run import PyRun

class MainWindow:
    def __init__(self):
        self.__py_run = PyRun()

        self.__window = tk.Tk()
        self.__window.title("Py-Run")
        self.__window.geometry("640x480+100+100")
        self.__window.resizable(True, True)

        '''frame setting'''
        self.__frame_top = tk.Frame(self.__window)
        self.__frame_bottom = tk.Frame(self.__window)
        self.__frame_top.pack(side="top", fill="both", expand=True)
        self.__frame_bottom.pack(side="bottom", fill="both", expand=True)

        '''main menu bar'''
        self.__menu_bar = MainMenuBar(self.__frame_top)

        '''arg entry'''
        self.__arg_var = tk.StringVar(self.__frame_top)
        self.__arg_entry = tk.Entry(self.__frame_top,
                                    textvariable=self.__arg_var)
        self.__arg_entry.pack(side="top", fill="x", padx=50, pady=10)

        '''run button'''
        self.__run_button = tk.Button(self.__frame_top, text="run")
        self.__run_button.pack(side="top", padx = 50, pady = 10)

        '''list box'''
        self.listbox = DataTableListBox(master=self.__frame_bottom,
                                        data_table=self.__py_run.script_data,
                                        row_tag="script id")
        self.listbox.pack(fill="both")

        self.__gui_bind_init()

        self.__window.config(menu=self.__menu_bar)
        self.__window.mainloop()

    def __gui_bind_init(self):
        '''graphic objects action setting'''
        self.__run_button.config(command=self.__run_activated, repeatdelay=1000,
                                repeatinterval=100)


    def __run_activated(self):
        '''action for run button'''
        try:
            selected_ids = self.listbox.selection()
            if len(selected_ids) > 1:
                for script_id in selected_ids:
                    self.__py_run.run_script(script_id=script_id)
            else:
                entry_args = self.__arg_entry.get().split(" ")
                print(entry_args)
                self.__py_run.run_script(script_id=selected_ids[0],
                                        args=entry_args)
        except IndexError:
            print("select script")

    def __del__(self):
        try:
            self.__window.destroy()
        except Exception:
            print("bye")
