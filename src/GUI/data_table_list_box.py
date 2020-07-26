import tkinter as tk
from tkinter import ttk
from json_data_table import JsonDataTable

class DataTableListBox(ttk.Treeview):
    '''
    * display json_data_table
    '''
    def __init__(self, master, data_table: JsonDataTable, row_tag: str):
        '''
        load the json_data_table to listbox
        '''
        table_columns = data_table["format"]
        super().__init__(master, columns=tuple(
            ["#" + str(i + 1) for i in range(len(table_columns))]
        ))
        self.heading("#0", text=row_tag)

        for i, tag in enumerate(table_columns):
            self.heading("#" + str(i + 1), text=tag)

        for row_key in data_table.keys():
            data = data_table[row_key]
            self.insert('', 'end', iid=row_key,
                        text=row_key,
                        values=tuple(data.values()))
