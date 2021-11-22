from chain import Chain

difficulty = 10
chain = Chain(difficulty)

for _ in range(5):
    message = input('Type your message: ')
    chain.queue(message)  # add message to the chain queue

    chain.mine()

    s = str(chain.blockchain[-1])
    print(s[0:64] + ' ' + s[64:64+len(message)] + ' ' + s[-len(message)+1:])
