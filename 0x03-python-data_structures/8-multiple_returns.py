#!/usr/bin/python3
def multiple_returns(sentence):
    None_sent = ""
    if sentence == None_sent:
        x = (len(sentence), None)
    else:
        x = (len(sentence), sentence[0])
    return x
