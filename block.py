import hashlib
import json

class Block:
    def __init__(self, index, product_movements, timestamp, previous_hash):
        self.index = index
        self.product_movements = product_movements
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0  # Nonce used for the proof-of-work
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def proof_of_work(self, difficulty):
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1
            self.hash = self.compute_hash()
        return self.hash
