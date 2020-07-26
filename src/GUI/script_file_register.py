import tkinter as tk
from GUI.sfr_top_frame import SFRTopFrame
from GUI.sfr_bottom_frame import SFRBottomFrame
from os.path import dirname, basename
from json_data_table import JsonDataTable

class ScriptFileRegister(tk.Toplevel):
    '''
    reaction for main menu bar's script register
    '''
    def __init__(self, master, script_data : dict, env_table: JsonDataTable):
        '''
        script_data is going to be output
        After user fill out the entries and its contents will be written in
        dictionary script_data.
        '''
        super().__init__(master)
        self.__script_data = script_data
        self.title("script file register")
        self.geometry("720x480+100+100")

        self.__top_frame = SFRTopFrame(self)
        self.__top_frame.set_seek_action(self.__seek_activated)
        self.__top_frame.pack(side="top", fill="both")

        self.__env_table = env_table
        self.__bottom_frame = SFRBottomFrame(self, env_table)
        self.__bottom_frame.set_okay_action(self.__okay_button_activated)
        self.__bottom_frame.pack(side="bottom", fill="both")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

    def __seek_activated(self):
        path = self.__top_frame.get()
        self.__script_data["script_name"] = basename(path)
        self.__script_data["script_location"] = dirname(path)

    def __okay_button_activated(self):
        '''need more exception handling'''
        try:
            self.__script_data["env_id"] = self.__bottom_frame.get_selection()
        except Exception:
            self.__script_data = {}
            
        self.destroy()
