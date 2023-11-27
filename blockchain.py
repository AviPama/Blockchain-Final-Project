from block import Block
import time

class Blockchain:
    difficulty = 2  # Difficulty level of the PoW

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.proof_of_work(Blockchain.difficulty)
        self.chain.append(genesis_block)

    def add_new_movement(self, product_id, movement_details, user):
        product_movement = {
            'product_id': product_id,
            'movement_details': movement_details,
            'timestamp': time.time(),
            'added_by': user.username
        }
        if self.chain:
            previous_block = self.chain[-1]
            new_block = Block(previous_block.index + 1, [product_movement], time.time(), previous_block.hash)
            new_block.proof_of_work(Blockchain.difficulty)
            self.chain.append(new_block)

    def get_product_history(self, product_id):
        history = []
        for block in self.chain:
            for movement in block.product_movements:
                if movement['product_id'] == product_id:
                    history.append(movement)
        return history
