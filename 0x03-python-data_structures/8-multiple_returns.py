#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)

    if (n == 0):
        sent = (n, None)
    else:
        sent = (n, sentence[0])

    return (sent)
