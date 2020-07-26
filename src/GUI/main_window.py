import tkinter as tk
from tkinter import ttk
from GUI.data_table_list_box import DataTableListBox
from GUI.menu_bar import MenuBar
from GUI.script_file_register import ScriptFileRegister
from GUI.main_top_frame import MainTopFrame
from GUI.main_bottom_frame import MainBottomFrame
from py_run_manager import PyRunManager

class MainWindow:
    def __init__(self, pyrun: PyRunManager):
        '''for init main menu bar'''
        main_menu_init_data = {
        "script register" : self.__register_script_activated,
        "register enviroment" : lambda : None,
        "process manager" : lambda : None
        }


        self.__py_run = pyrun

        self.__window = tk.Tk()
        self.__window.title("Py-Run")
        self.__window.geometry("720x480+100+100")
        self.__window.resizable(True, True)

        '''frame setting'''
        self.__frame_top = MainTopFrame(self.__window)
        self.__frame_bottom = MainBottomFrame(self.__window, self.__py_run.get_script_table())
        self.__frame_top.pack(side="top", fill="both", expand=True)
        self.__frame_bottom.pack(side="bottom", fill="both", expand=True)

        '''main menu bar'''
        self.__main_menu = MenuBar(self.__window, menu_name="Menu",
                                label_to_command=main_menu_init_data)

        self.__gui_bind_init()

        self.__window.config(menu=self.__main_menu)
        self.__window.mainloop()

    def __gui_bind_init(self):
        '''graphic objects action setting'''
        '''run script'''
        self.__frame_top.set_run_action(self.__run_activated)

        '''register script menu'''

    def __run_activated(self):
        '''action for run button'''
        try:
            selected_ids = self.__frame_bottom.get_selection()
            if len(selected_ids) > 1:
                for script_id in selected_ids:
                    self.__py_run.run_script(script_id=script_id)
            else:
                entry_args = self.__frame_top.get().split(" ")
                print(entry_args)
                self.__py_run.run_script(script_id=selected_ids[0],
                                        args=entry_args)
        except IndexError:
            print("select script")

    def __register_script_activated(self):
        new_script_data = {}
        script_data_table = self.__py_run.get_script_table()
        env_data_table = self.__py_run.get_env_table()

        ''' must be modified!!!!'''
        self.__window.wait_window(ScriptFileRegister(self.__window,
                            script_data=new_script_data,
                            env_table=env_data_table
                            ))
        if new_script_data:
            print(new_script_data)
            new_script_id = str(len(script_data_table))
            script_data_table.set_item(self.__py_run, new_script_id, new_script_data)
            self.__bottom_frame.add_item(new_script_id, new_script_data)
