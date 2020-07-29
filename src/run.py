from GUI.main_window import MainWindow
from py_run_manager import PyRunManager

if __name__=="__main__":
    pyrun = PyRunManager()
    window = MainWindow(pyrun)
    # pyrun.save_tables()
