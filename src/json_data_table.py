import json

# row key is script_id
script_data_table_format = [
        "script_name",
        "env_kind", # conda or venv ...
        "env_name", # for conda ex base

        # script_location has absolute path to dictionary contains script file
        "script_location",
]

# row key is env_name
env_data_table_format = [
        # env_location has absolute path to enviroment path
        "env_location",

        "command",
]

class JsonDataTable(dict):
    '''
    data table for json file format (json_data_table format)
    shape is like this
    {
        "format" : [
            "format_key1",
            "format_key2",
            ...
        ],
        row_key1 : {
            format_key1 : data,
            format_key2 : data,
            ...
        },
        row_key2 : {
            format_key1 : data,
            format_key2 : data,
            ...
        },
        ...
    }
    '''

    def __init__(self, **kwargs):
        '''
        "path" contains the file's absolute path
        "data" is a dictionary satisfies format
        '''
        super().__init__(self)
        self.__path = ""

        if "data" in kwargs.keys():
            data = kwargs["data"]
            if "format" not in data.keys():
                key = list(data.keys())[0]
                self["format"] = [format_key for format_key in data[key].keys()]
            #read data
            for key, val in data.items():
                self[key] = val

        if "path" in kwargs.keys():
            self.__path = kwargs["path"]

    def load_data_table(self, path = ""):
        '''
        load data table file
        file must be json_data_table !!!format!!!
        '''
        if path != "":
            self.__load_data_table(path)
        elif self.__path != "":
            self.__load_data_table(self.__path)

        else:
            raise ValueError("Nothing was happened!!!")

    def __load_data_table(self, path : str):
        with open(path, "r") as json_file:
            json_data = json.load(json_file)
            self.__init__(data = json_data, path = self.__path)

    def save_data_table(self, path = "", overwrite = False):
        '''
        write data table file
        file will be json file
        '''
        str_self = json.dumps(self, indent=4)
        if path == "" and overwrite:
            with open(self.__path, "w") as new_save_file:
                new_save_file.write(str_self)

        elif path != "":
            print(path)
            with open(path, "w") as new_save_file:
                new_save_file.write(str_self)
        else:
            raise ValueError("Nothing was happened!!!")

    def keys(self):
        ''' exclude 'format' part from table '''
        jdt_keys = list(super().keys())
        try:
            jdt_keys.remove("format")
        except Exception:
            pass

        return jdt_keys

    def values(self):
        ''' exclude 'format' part from table '''
        jdt_values = list(super().values())
        try:
            del jdt_values[0]
        except IndexError:
            raise IndexError("empty data table")

        return jdt_values

    def __str__(self):
        return json.dumps(self, indent=4)

    def __setitem__(self, key, val:dict):
        '''
        Every data must satisfies format.
        To use this method, Data has "proper format" is mendatory.
        Obviously, Value also has "proper format".
        '''
        if key != "format":
            if set(self["format"]) == set(val.keys()):
                super().__setitem__(key, val)
            else:
                raise ValueError("data format unmattched")
        else:
            super().__setitem__(key, list(val) )

    def __iter__(self):
        yield from list(self.keys())[1:]
