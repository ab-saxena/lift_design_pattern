class Server:
    def __init__(self, server_num):
        self.server_num = server_num
        self.cache = dict()
        self.status = True

    def get_response(self, key):
        if key in self.cache:
            return self.cache[key]
        resp = self.get_response_database(key)
        if resp:
            self.cache[key] = resp
        return resp

    @staticmethod
    def get_response_database(key):
        return 'resp'

