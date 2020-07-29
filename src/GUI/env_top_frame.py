import tkinter as tk
import tkinter.filedialog as tkfile
from py_run_manager import PyRunManager

class EWTopFrame(tk.Frame):


    def __init__(self, master):
        super().__init__(master)

        env_kind_label = tk.Label(self, text="enviroment kind")
        env_kind_label.grid(row=0, column=0, sticky="w", padx=5, pady=10)
        self.__env_kind_entry = tk.Entry(self)
        self.__env_kind_entry.grid(row=0, column=1, sticky="we", padx=5, pady=10)

        env_name_label = tk.Label(self, text="enviroment name")
        env_name_label.grid(row=1, column=0, sticky="w", padx=5, pady=10)
        self.__env_name_entry = tk.Entry(self)
        self.__env_name_entry.grid(row=1, column=1, sticky="we", padx=5, pady=10)

        self.__location_entry = tk.Entry(self)
        self.__location_entry.grid(row=2, column=0, columnspan=2, sticky="we", padx=50, pady=10)

        self.__seek_button = tk.Button(self, text="Seek", command=self.__seek_activated)
        self.__seek_button.grid(row=2, column=1, sticky="e", padx=10, pady=10)

        self.__regist_button = tk.Button(self, text="Regist")
        self.__regist_button.grid(row=3, column=1, sticky="e", padx=5)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

    def __seek_activated(self):
        #action for seek button
        full_path = tkfile.askdirectory()
        self.__location_entry.delete(0, "end")
        self.__location_entry.insert(0, full_path)

    def set_regist_activated(self, func):
        self.__regist_button.config(command=func)

    def get_env_data(self):
        "tag: env_data.json"
        env_data = {
            "env_kind": self.__env_kind_entry.get(),
            "env_name": self.__env_name_entry.get(),
            "python_location": self.__location_entry.get()
        }
        return env_data
