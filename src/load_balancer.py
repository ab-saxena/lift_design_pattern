class LoadBalancer:
    def __init__(self, servers_map: dict, replica_factor: int):
        self.servers = list()
        self.servers_map = servers_map
        self.replica_factor = replica_factor

    def get_hash_server(self, key):
        return key % len(self.servers)

    def get_server(self, key):
        server_id = self.get_hash_server(key)
        if self.servers[server_id].status:
            return self.servers[server_id]

        iter_server = server_id
        while self.servers[iter_server].status:
            iter_server = (iter_server + 1) % len(self.servers)
            if iter_server == server_id:
                return None
        return self.servers[iter_server]


