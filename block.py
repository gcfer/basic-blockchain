from hashlib import sha256

class Block():
    def __init__(self, message, _hexdigest):
        self._hexdigest = _hexdigest  # digest of the previous block (hex)
        self.H = sha256()  # hash object of this block
        self.message = message
        self.nonce = 0

    def __str__(self):
        return "{}{}{}".format(self._hexdigest, self.message, self.nonce)

    def mine(self, difficulty):
        while int(self.H.hexdigest(), 16) > 2**(256 - difficulty):
            self.nonce += 1
            self.H = sha256()
            bytes_to_hash = str(self).encode('utf-8')  # the encode part converts to bytes
            self.H.update(bytes_to_hash)
