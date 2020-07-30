import json_data_table as jdt
from process_manager import ProcessManager
import subprocess
import os


class PyRunManager:
    '''
    link data flow and manage events
    '''
    def __init__(self):
        parent_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(parent_dir).replace("\\", "/")
        self.__env_table = jdt.JsonDataTable(master=self)
        self.__script_table = jdt.JsonDataTable(master=self)
        self.__env_table.load_data_table(path=parent_dir + "/data table/env_data.json")
        self.__script_table.load_data_table(path=parent_dir + "/data table/script_data.json")
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
            script_data = self.__script_table[script_id]
            env_id = script_data["env_id"]
            env_data = self.__env_table[env_id]
            pid = self.__script_run(
                        script_data,
                        env_data["python_location"],
                        args=args)
            '''self.__subprocess_table[pid] = data'''
            return True

        except KeyError:
            return False

    def __script_run(self, script_data : dict, python_location, args=[]):
        #command = [python_location, script_location, args]
        command = []
        command.append(python_location + "/python.exe")
        command.append(script_data["script_location"] + "/" +
                            script_data["script_name"])
        command.extend(args)

        ''' who gonna manage pid '''
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
