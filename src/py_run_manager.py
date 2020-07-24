import json_data_table as jdt
from process_manager import ProcessManager
import subprocess
import os

CONDA_NAME = "conda"

class PyRunManager:
    '''
    link data flow and manage events
    '''
    def __init__(self):
        parent_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(parent_dir)
        self.__env_table = jdt.JsonDataTable(master=self)
        self.__script_table = jdt.JsonDataTable(master=self)
        self.__env_table.load_data_table(path=parent_dir + "\\data table\\env_data.json")
        self.__script_table.load_data_table(path=parent_dir + "\\data table\\script_data.json")
        '''
        __subprocess_table is for display
        row_key is pid
        self.__subprocess_table = jdt.JsonDataTable(master=self)
        self.__subprocess_table["format"] = ["script_name",
                                            "env_kind",
                                            "env_name",
                                            "script_location",
                                            ]
                                            '''

        self.__subprocess_manager = ProcessManager()

    def run_script(self, script_id : str, args=[]):
        '''
        run script has same script_id
        '''
        try:
            data = self.__script_table[script_id]
            env_kind = data["env_kind"]
            if env_kind == CONDA_NAME:
                pid = self.__conda_script_run(data, args=args)
                '''self.__subprocess_table[pid] = data'''
                return True
            else:
                return False

        except KeyError:
            return False

    def __conda_script_run(self, script_data : dict, args=[]):
        '''only for conda env script'''
        conda_env_data = self.__env_table[CONDA_NAME]
        command = conda_env_data["env_location"] + conda_env_data["command"]
        command = command.format(env_name=script_data["env_name"],
                                script_location=script_data["script_location"],
                                script_name=script_data["script_name"])

        ''' who gonna manage pid '''
        command = command.split("~")
        command.extend(args)
        print(command)
        return self.__subprocess_manager.spawn_subprocess(command,
                                    creationflags=subprocess.CREATE_NEW_CONSOLE
                                    )

    def get_env_table(self):
        return self.__env_table

    def get_script_table(self):
        return self.__script_table

    def save_tables(self, path=""):
        self.__env_table.save_data_table(path)
        self.__script_table.save_data_table(path)
