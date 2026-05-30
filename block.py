from hashlib import sha256


class Block:
    """A minimal proof-of-work block.

    Each block stores the previous block's hash, a message payload, and a
    nonce. Mining searches for a nonce that makes this block's hash small
    enough for the requested difficulty.
    """

    def __init__(self, message: str, previous_hash: str):
        self.previous_hash = previous_hash
        self.H = sha256()  # hash object containing the latest mined hash
        self.message = message
        self.nonce = 0

    def __str__(self) -> str:
        # This is the exact text that is hashed. Keeping the format stable
        # matters: changing it changes every block hash.
        return f"{self.previous_hash}{self.message}{self.nonce}"

    def compute_hash(self) -> sha256:
        """Return a fresh SHA-256 hash object for the current block content."""
        H = sha256()
        H.update(str(self).encode("utf-8"))
        return H

    def mine(self, difficulty: int) -> None:
        """Increment the nonce until the hash satisfies the difficulty target."""
        target = 2 ** (256 - difficulty)

        self.H = self.compute_hash()
        while int(self.H.hexdigest(), 16) >= target:
            self.nonce += 1
            self.H = self.compute_hash()
