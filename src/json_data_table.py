import json

class JsonDataTable(dict):
    '''
    master is ref var of owner class
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

    def __init__(self, master, data={}):
        '''
        "data" is a dictionary satisfies format
        '''
        super().__init__(self)
        self.__path = ""
        self.__master = master

        if data:
            if "format" not in data.keys():
                key = list(data.keys())[0]
                super().__setitem__("format",[format_key for format_key in data[key].keys()])
            #read data
            for key, val in data.items():
                super().__setitem__(key, val)

    def load_data_table(self, path):
        with open(path, "r") as json_file:
            json_data = json.load(json_file)
            self.__init__(master=self.__master, data=json_data)
            self.__path = path

    def save_data_table(self, path = ""):
        '''
        write data table file
        file will be json file
        '''
        str_self = json.dumps(self, indent=4)
        if path == "":
            print(self.__path)
            with open(self.__path, "w") as new_save_file:
                new_save_file.write(str_self)
        else:
            with open(path, "w") as new_save_file:
                new_save_file.write(str_self)

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

    def set_item(self, master, key, item: dict):
        '''
        Every data must satisfies format.
        To use this method, Data has "proper format" is mendatory.
        Obviously, Value also has "proper format".
        '''
        if self.__master != master or key == "format":
            return False

        format = self["format"]
        if set(format) == set(item.keys()):
            # sort properly
            values = [item[key] for key in format]
            item = dict(zip(format, values))
            super().__setitem__(key, item)
            return True
        else:
            raise ValueError("data format unmattched")

    def set_format(self, master, format: list):
        if master == self.__master:
            super().__setitem__("format", format)

    def delete_item(self, master, key: str):
        if master == self.__master:
            super().__delitem__(key)

    def __iter__(self):
        yield from list(self.keys())[1:]

    def __setitem__(self, key, val:dict):
        raise Exception("No data is inserted JsonDataTable __setitem__")

    def __delete__(self, key):
        raise Exception("No data is deleted JsonDataTable __delete__")
