import tkinter as tk
from tkinter import ttk
import json_data_table as jdt
from GUI.data_table_list_box import DataTableListBox
from GUI.menu_bar import MenuBar
from GUI.script_file_register import ScriptFileRegister
from py_run import PyRun

class MainWindow:
    def __init__(self):
        '''for init main menu bar'''
        main_menu_init_data = {
        "script register" : self.__register_script_activated,
        "register enviroment" : lambda : None,
        "process manager" : lambda : None
        }


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
        self.__main_menu = MenuBar(self.__frame_top, menu_name="Menu",
                                label_to_command=main_menu_init_data)

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

        self.__window.config(menu=self.__main_menu)
        self.__window.mainloop()

    def __gui_bind_init(self):
        '''graphic objects action setting'''
        '''run script'''
        self.__run_button.config(command=self.__run_activated, repeatdelay=1000,
                                repeatinterval=100)
        self.__arg_entry.bind("<Return>", func=lambda event : self.__run_activated())

        '''register script menu'''


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

    def __register_script_activated(self):
        new_script_data = {}
        script_data_table = self.__py_run.script_data
        env_data_table = self.__py_run.env_data

        ''' must be modified!!!!'''
        tmp = ScriptFileRegister(self.__window, script_data=new_script_data,
                            env_name_list=["base", "crawler"],
                            env_kind_list=["conda"]
                            )
        if new_script_data:
            new_script_id = str(len(script_data_table))
            script_data_table[new_script_id] = new_script_data
            self.listbox.insert('', "end", iid=new_script_id,
            values=tuple(new_script_data.values())
            )

    def __del__(self):
        try:
            self.__window.destroy()
        except Exception:
            print("bye")
