from hashlib import sha256
from block import Block


class Chain:
    """A tiny educational blockchain with a single local miner."""

    def __init__(self, difficulty: int):
        self.difficulty = difficulty  # difficulty is chain-wide in this code
        self.blockchain = []
        self.messages = []

        # The genesis block anchors the chain. The message mirrors Bitcoin's
        # genesis-block newspaper headline, and the previous hash is the hash
        # of the empty string because there is no earlier block.
        message = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks."
        H = sha256()
        H.update("".encode("utf-8"))
        hexdigest = H.hexdigest()
        genesis = Block(message, hexdigest)
        genesis.mine(self.difficulty)
        self.blockchain.append(genesis)

    def is_valid_next_block(self, block: Block) -> bool:
        """Validate proof-of-work and linkage for a candidate next block."""
        H_temp = block.compute_hash()

        # Proof of work: with difficulty d, the hash must be below 2^(256-d).
        # Equivalently, it has roughly d leading zero bits.
        target = 2 ** (256 - self.difficulty)
        has_valid_work = int(H_temp.hexdigest(), 16) < target

        # Chain linkage: the block must point to the current chain tip.
        points_to_tip = block.previous_hash == self.blockchain[-1].H.hexdigest()

        return has_valid_work and points_to_tip

    def pow(self, block: Block) -> bool:
        """Backward-compatible alias for the next-block proof-of-work check."""
        return self.is_valid_next_block(block)

    def queue(self, message: str) -> None:
        """Store a message until the miner packages it into a block."""
        self.messages.append(message)

    def mine(self) -> Block | None:
        """Mine one queued message and append the block if it validates."""
        if not self.messages:
            return None

        message = self.messages.pop(0)
        block = Block(message, self.blockchain[-1].H.hexdigest())
        block.mine(self.difficulty)

        if self.is_valid_next_block(block):
            self.blockchain.append(block)
            return block

        return None
