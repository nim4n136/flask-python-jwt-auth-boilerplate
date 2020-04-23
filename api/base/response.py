class Response():

    data = []
    
    def __init__(self, data = []):
        self.data = data

    def success(self, message="Success", code=200):
        return {
            "data": self.data,
            "message": message,
            "code": code,
            "error": False
        }, code
    
    def error(self, message="Someting wrong", code=500, errorMessage=""):
        return {
            "data": self.data,
            "message": message,
            "errorMessage": errorMessage,
            "code": code,
            "error": True
        }, code



