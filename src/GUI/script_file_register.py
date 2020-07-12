import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as tkfile
from os.path import dirname

class ScriptFileRegister(tk.Toplevel):
    '''
    reaction for main menu bar's script register
    '''
    def __init__(self, master, script_data : dict, env_name_list : list, env_kind_list : list):
        '''
        script_data is going to be output
        After user fill out the entries and its contents will be written in
        dictionary script_data.
        '''
        super().__init__(master)
        self.__script_data = script_data
        self.title("script file register")
        self.__on_destroy = lambda : None

        #for script location entries
        self.__script_location = tk.StringVar(self)
        self.__env_kind = tk.StringVar(self)
        self.__env_name = tk.StringVar(self)

        location_entry_label = tk.Label(self, text="Script File Location")
        location_entry_label.grid(row=0, column=0, sticky="w", padx=5, pady=10)

        self.__location_entry = tk.Entry(self, textvariable=self.__script_location)
        self.__location_entry.grid(row=0, column=1, sticky="we", pady=10)

        self.__seek_button = tk.Button(self, text="Seek", command=self.__seek_activate)
        self.__seek_button.grid(row=0, column=2, padx=5, pady=10)

        #for env kind combobox
        env_kind_label = tk.Label(self, text="enviroment kind")
        env_kind_label.grid(row=1, column=0, padx=5, pady=10)

        self.__env_kind_combobox = ttk.Combobox(self, height=len(env_kind_list),
                                                values=env_kind_list,
                                                textvariable=self.__env_kind)
        self.__env_kind_combobox.grid(row=1, column=1, sticky="w", padx=5, pady=10)

        #for env name combobox
        env_name_label = tk.Label(self, text="enviroment name")
        env_name_label.grid(row=2, column=0, padx=5, pady=10)

        self.__env_name_combobox = ttk.Combobox(self, height=len(env_name_list),
                                                values=env_name_list,
                                                textvariable=self.__env_name)
        self.__env_name_combobox.grid(row=2, column=1, sticky="w", padx=5, pady=10)

        # okay button
        self.__okay_button = tk.Button(self, text="Okay", command=self.__okay_button_activated)
        self.__okay_button.grid(row=3, column=2, sticky="e", padx=5, pady=10)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

    def __seek_activate(self):
        ask_outcome = tkfile.askopenfilename()
        self.__script_location.set(ask_outcome)

        script_file_location = dirname(ask_outcome).replace("/", "\\") + "\\"
        script_file_name = ask_outcome[len(script_file_location):]

        self.__script_data["script_name"] = script_file_name
        self.__script_data["script_location"] = script_file_location

    def __okay_button_activated(self):
        '''need more exception handling'''
        self.__script_data["env_kind"] = self.__env_kind_combobox.get()
        self.__script_data["env_name"] = self.__env_name_combobox.get()
        self.destroy()
