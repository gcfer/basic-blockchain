from hashlib import sha256
from block import Block


class Chain():
    def __init__(self, difficulty):
        self.difficulty = difficulty  # difficulty is chain-wide in this code
        self.blockchain = []
        self.messages = []
        # genesis
        message = 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.'
        H = sha256()
        H.update(''.encode('utf-8'))
        hexdigest = H.hexdigest()
        genesis = Block(message, hexdigest)
        genesis.mine(self.difficulty)
        self.blockchain.append(genesis)
        

    def pow(self, block):
        H_temp = sha256()
        H_temp.update(str(block).encode('utf-8'))
        # proof of work
        cond_1 = int(H_temp.hexdigest(), 16) < 2**(256 - self.difficulty)
        # check if the hash of the previous block is equal to the first hash of this block
        cond_2 = block._hexdigest == self.blockchain[-1].H.hexdigest()
        # check all of them
        return cond_1 and cond_2


    def queue(self, message):
        self.messages.append(message)


    def mine(self):
        if self.queue:
            message = self.messages.pop()
            block = Block(message, self.blockchain[-1].H.hexdigest())
            block.mine(self.difficulty)
            if self.pow(block):
                self.blockchain.append(block)
