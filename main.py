from chain import Chain


def describe_block(block):
    """Print the three ingredients that are hashed into a block."""
    print(f"previous hash: {block.previous_hash}")
    print(f"message:       {block.message}")
    print(f"nonce:         {block.nonce}")
    print(f"block hash:    {block.H.hexdigest()}")
    print()


def main():
    difficulty = 10
    chain = Chain(difficulty)

    print(f"Created genesis block with difficulty {difficulty}.")
    describe_block(chain.blockchain[-1])

    for _ in range(5):
        message = input("Type your message: ")
        chain.queue(message)  # add message to the mining queue

        block = chain.mine()
        if block is None:
            print("No message was mined.")
            continue

        describe_block(block)


if __name__ == "__main__":
    main()
