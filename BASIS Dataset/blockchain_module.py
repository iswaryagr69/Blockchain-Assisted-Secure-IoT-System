import hashlib
import time

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class PoABlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.authorized_nodes = set()

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def register_node(self, node_id):
        self.authorized_nodes.add(node_id)

    def add_block(self, data, node_id):
        if node_id not in self.authorized_nodes:
            raise Exception("Unauthorized node!")

        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].prev_hash != self.chain[i-1].hash:
                return False
        return True