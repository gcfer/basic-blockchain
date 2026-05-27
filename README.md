# Basic Blockchain

A compact Python implementation of a proof-of-work blockchain. The code is
intended as a readable educational example rather than a production blockchain.

## Files

| File | Description |
| --- | --- |
| `block.py` | Defines a block, including the previous hash, message, nonce, and mining loop. |
| `chain.py` | Defines the blockchain, creates the genesis block, queues messages, mines new blocks, and checks proof of work. |
| `main.py` | Interactive demo that asks for messages and appends mined blocks to the chain. |

## How to run

This example uses only the Python standard library.

```bash
python3 main.py
```

The demo uses a fixed difficulty of `10`. It asks for five messages, mines a
block for each message, and prints a compact representation of the latest block.

## Notes

This is a minimal model of the main ideas: linked hashes, nonces, and
proof-of-work. It does not implement networking, transactions, wallets,
consensus between peers, or persistent storage.
