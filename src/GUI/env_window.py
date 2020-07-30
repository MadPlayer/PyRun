import tkinter as tk
from hash_func import hash_crc32_data
from py_run_manager import PyRunManager
from GUI.env_top_frame import EWTopFrame
from GUI.env_bottom_frame import EWBottomFrame

class EnvWindow(tk.Toplevel):


    def __init__(self, master, py_run: PyRunManager):
        super().__init__(master)

        self.title("Enviroment Window")

        self.__py_run = py_run
        self.__top_frame = EWTopFrame(self)
        self.__top_frame.pack(side="top", fill="both")

        self.__bottom_frame = EWBottomFrame(self, py_run.get_env_table())
        self.__bottom_frame.pack(side="bottom", fill="both", expand=True)

        self.__top_frame.set_regist_activated(self.__regist_env)
        self.__bottom_frame.set_delete_activated(self.__delete_env)

    def __delete_env(self):
        env_ids = self.__bottom_frame.get_selection()
        env_table = self.__py_run.get_env_table()

        # remove data from env table
        for env_id in env_ids:
            env_table.delete_item(self.__py_run, env_id)

        # remove from listbox
        self.__bottom_frame.remove_item()

    def __regist_env(self):
        env_data = self.__top_frame.get_env_data()
        if env_data["python_location"] != "":
            env_table = self.__py_run.get_env_table()
            env_id = str(hash_crc32_data(env_data))
            try:
                self.__bottom_frame.add_item(env_id, env_data)
                env_table.set_item(self.__py_run, env_id, env_data)
            except Exception:
                '''compare these data and judge them'''
                print("same id")
