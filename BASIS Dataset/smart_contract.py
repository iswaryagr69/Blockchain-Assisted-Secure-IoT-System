class SmartContract:
    def __init__(self):
        self.permissions = {}

    def grant_access(self, node_id, resource):
        if node_id not in self.permissions:
            self.permissions[node_id] = []
        self.permissions[node_id].append(resource)

    def check_access(self, node_id, resource):
        return resource in self.permissions.get(node_id, [])