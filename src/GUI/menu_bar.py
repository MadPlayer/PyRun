import tkinter as tk

class MenuBar(tk.Menu):
    '''
    py_run's main menu bar
    '''
    def __init__(self, master, menu_name : str, label_to_command : dict):
        '''
        label_to_command = {
        "label text" : command, #func to be activated when label is clicked
        ...
        }
        '''
        super().__init__(master)
        self.__menu = tk.Menu(master, tearoff=0)
        for label_text, command in label_to_command.items():
            self.__menu.add_command(label=label_text, command=command)

        self.add_cascade(label=menu_name, menu=self.__menu)
