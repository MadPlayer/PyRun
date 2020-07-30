import tkinter as tk
from GUI.data_table_list_box import DataTableListBox
from json_data_table import JsonDataTable

class SFRBottomFrame(tk.Frame):


    def __init__(self, master, env_table: JsonDataTable):
        super().__init__(master)

        self.__env_listbox = DataTableListBox( master=self,
                                             data_table=env_table,
                                             row_tag="env_id")
        self.__env_listbox.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.__okay_button = tk.Button(self, text="Ok")
        self.__okay_button.pack(side="bottom", anchor="e", padx=10, pady=10)


    def set_okay_action(self, func):
        self.__okay_button.config(command=func)

    def get_selection(self):
        '''return selected item's id'''
        try:
            return self.__env_listbox.selection()[0]
        except IndexError:
            raise Exception("select value")
