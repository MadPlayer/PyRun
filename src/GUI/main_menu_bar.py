import tkinter as tk

class MainMenuBar(tk.Menu):
    '''
    py_run's main menu bar
    '''
    def __init__(self, master):
        '''
        ---------------
        register script
        ---------------
        register enviroment
        ---------------
        process manager
        ---------------
        '''
        super().__init__(master)
        self.__menu = tk.Menu(master, tearoff=0)
        self.__menu.add_command(label="register script")
        self.__menu.add_command(label="register enviroment")
        self.__menu.add_command(label="process manager")
        self.add_cascade(label="Menu", menu=self.__menu)
