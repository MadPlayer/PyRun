import tkinter as tk
from GUI.data_table_list_box import DataTableListBox
from json_data_table import JsonDataTable

class EWBottomFrame(tk.Frame):


    def __init__(self, master, env_table: JsonDataTable):
        super().__init__(master)

        self.__env_listbox = DataTableListBox( master=self,
                                             data_table=env_table,
                                             row_tag="env id")
        self.__env_listbox.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.__delete_button = tk.Button(self, text="Delete")
        self.__delete_button.pack(side="bottom", anchor="e", padx=10, pady=10)

    def set_delete_activated(self, func):
        self.__delete_button.config(command=func)

    def get_selection(self):
        return self.__env_listbox.selection()

    def add_item(self, env_id, env_data):
        self.__env_listbox.insert('', 'end', iid=env_id,
                                text=env_id,
                                values=tuple(env_data.values())
                                )

    def remove_item(self):
        for env_id in self.get_selection():
            self.__env_listbox.delete(env_id)
