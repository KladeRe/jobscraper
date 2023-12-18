class ConnectionError(Exception):
    def __init__(self, url, code, *args):
        super().__init__(args)
        self.url = url
        self.code = code
    
    def __str__(self):
        return f"Unable to connect to {self.url}, error code: {self.code}"

class ClassnameError(Exception):
    def __init__(self, class_name, url, *args):
        super().__init__(args)
        self.class_name = class_name
        self.url = url
    
    def __str__(self):
        return f"Unable to find class '{self.class_name}' on {self.url}"


    