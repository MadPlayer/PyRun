import tkinter as tk
from GUI.data_table_list_box import DataTableListBox
from json_data_table import JsonDataTable

class SFRBottomFrame(tk.Frame):


    def __init__(self, master, env_table: JsonDataTable):
        super().__init__(master)

        self.__okay_button = tk.Button(self, text="Ok", command=None)
        self.__okay_button.grid(row=1, sticky="e", padx=100, pady=10)

        self.__env_listbox = DataTableListBox(self, env_table, "env_id")
        self.__env_listbox.grid(row=0, sticky="news", padx=5, pady=10)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

    def set_okay_action(self, func):
        self.__okay_button.config(command=func)

    def get_selection(self):
        '''return selected item's id'''
        try:
            return self.__env_listbox.selection()[0]
        except IndexError:
            raise Exception("select value")
