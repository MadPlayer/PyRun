import tkinter as tk
import tkinter.filedialog as tkfile

class SFRTopFrame(tk.Frame):
    '''top frame for script file register'''

    def __init__(self, master):
        super().__init__(master)
        self.__func = lambda : None

        location_entry_label = tk.Label(master=self, text="Script File Location")
        location_entry_label.grid(row=0, column=0, sticky="w", padx=5, pady=10)

        self.__location_entry = tk.Entry(master=self)
        self.__location_entry.grid(row=0, column=1, sticky="we", pady=10)

        self.__seek_button = tk.Button( master=self,
                                        command=self.__seek_activated,
                                        text="Seek"
                                        )
        self.__seek_button.grid(row=0, column=2, sticky="e", padx=5, pady=10)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

    def get(self):
        return self.__location_entry.get()

    def __seek_activated(self):
        #action for seek button
        full_path = tkfile.askopenfilename()
        self.__location_entry.delete(0, "end")
        self.__location_entry.insert(0, full_path)
        self.__func()

    def set_seek_action(self, func):
        self.__func = func
