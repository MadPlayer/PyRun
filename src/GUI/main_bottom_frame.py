import tkinter as tk
from tkinter import ttk
from GUI.data_table_list_box import DataTableListBox

class MainBottomFrame(tk.Frame):


    def __init__(self, master, script_table):
        super().__init__(master)
        self.__listbox = DataTableListBox(master=self,
                                            data_table=script_table,
                                            row_tag="script id")
        self.__listbox.pack(fill="both")

    def get_selection(self):
        return self.__listbox.selection()

    def add_item(self, script_id, script_data):
        self.__listbox.insert('', 'end', iid=script_id,
                                text=script_id,
                                values=tuple(script_data.values())
                                )

    def remove_item(self):
        for script_id in self.get_selection():
            self.__listbox.delete(script_id)
