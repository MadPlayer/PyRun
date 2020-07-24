import subprocess
import signal
import json_data_table as jdt

class ProcessManager:
    '''
    spawn subprocess and manage them
    can provide subprocesses states
    subprocess table is dict with (key, val) = (pid, attributes)
    attributes = {"process":(python object)}
    '''
    # row key is pid (ref. json_data_table.py)
    table_format = ["process"]

    def __init__(self):
        self.__process_table = jdt.JsonDataTable(master=self)
        self.__process_table.set_format(self, ProcessManager.table_format)

    def spawn_subprocess(self, *args, **kwargs):
        '''
        spawn subprocess and return pid value
        pid, process object, state value will be registered in table

        args is same as subprocess.Popen object's parameter
        (check docs.python.org)
        '''
        new_subprocess = subprocess.Popen(*args, **kwargs)
        self.__process_table.set_item(self, new_subprocess.pid, {
                                            "process" : new_subprocess,
        })
        return new_subprocess.pid

    def kill(self, pid:str, sig: signal.Signals):
        '''
        send signal to the process
        '''
        self.__process_table[pid].send_signal(sig)

    def broadcast_kill(self, sig: signal.Signals):
        '''
        send signal to every process in table
        '''
        for process in self.__process_table.values():
            process.send_signal(sig)

    def is_running(self, pid:str):
        '''
        return state of subprocess has that pid
        '''
        state = self.__process_table[pid].poll()
        if state == None:
            return True
        else: return False

    def refresh_table(self):
        '''
        renewal subprocess table
        polling every subprocess in table and change states
        '''
        pid_list = self.__process_table.keys()
        delete_list = [False]*len(pid_list)
        for i, pid in enumerate(pid_list):
            if not self.is_running(pid):
                delete_list[i] = True

        for i, delete in enumerate(delete_list):
            if delete:
                del self.__process_table[pid_list[i]]

    def __del__(self):
        '''
        waits for every process
        '''
        for row in self.__process_table.values():
            row["process"].wait()
