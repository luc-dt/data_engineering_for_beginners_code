class DataExtractor:
    def __init__(self, some_value):
        self.some_value = some_value 

    def get_connection(self):
        pass 

    def close_connection(self):
        pass 

de_object = DataExtractor(10)
print(de_object.some_value)