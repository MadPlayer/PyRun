import json_data_table as jdt
from subprocess_manager import SubprocessManager
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
        self.env_data = jdt.JsonDataTable(path=parent_dir + "\\data table\\env_data.json")
        self.script_data = jdt.JsonDataTable(path=parent_dir + "\\data table\\script_data.json")
        self.env_data.load_data_table()
        self.script_data.load_data_table()
        '''
        __subprocess_table is for display
        row_key is pid
        '''
        self.__subprocess_table = jdt.JsonDataTable()
        self.__subprocess_table["format"] = ["script_name",
                                            "env_kind",
                                            "env_name",
                                            "script_location",
                                            ]

        self.__subprocess_manager = SubprocessManager()

    def run_script(self, script_id : str, args=[]):
        '''
        run script has same script_id
        '''
        try:
            data = self.script_data[script_id]
            env_kind = data["env_kind"]
            if env_kind == CONDA_NAME:
                pid = self.__conda_script_run(data, args=args)
                self.__subprocess_table[pid] = data
                return True
            else:
                return False

        except KeyError:
            return False

    def __conda_script_run(self, script_data : dict, args=[]):
        '''only for conda env script'''
        conda_env_data = self.env_data[CONDA_NAME]
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

    def __del__(self):
        self.env_data.save_data_table(overwrite=True)
        self.script_data.save_data_table(overwrite=True)
