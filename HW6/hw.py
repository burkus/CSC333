#HW6
# Diffie-Hellman Key Agreement
from random import randrange

def keyAgreement():
    Alice = {}
    Bob = {}
    Eve = {}
    Alice['p'] = 43897539013
    Alice['r'] = 2
    Bob['p'] = 43897539013
    Bob['r'] = 2
    Eve['p'] = 43897539013
    Eve['r'] = 2

    #Alice generates her private key
    Alice['a'] = randrange(2 ** 16)
    print("Alice generates her private key:{}".format(Alice['a']))

    #Bob generates his private key
    Bob['b'] = randrange(2 ** 16)
    print("Bob generates his private key:{}".format(Bob['b']))


    #Alice makes her public key
    Alice['A'] = (Alice['r'] ** Alice['a']) % Alice['p']

    #Alice sends her public key to Bob
    print("Alice -> Bob A:{}".format(Alice['A']))
    Bob['A'] = Alice['A']
    Eve['A'] = Alice['A']
    
    #Bob Calculates his public key
    Bob['B'] = (Bob['r'] ** Bob['b']) % Bob['p']

    #Bob sends his public key to Alice
    print("Bob -> Alice B:{}".format(Bob['B']))
    Alice['B'] = Bob['B']
    Eve['B'] = Bob['B']

    #Alice calculates her secret
    Alice['s'] = (Alice['B'] ** Alice['a']) % Alice['p']

    #Bob calculates his secret
    Bob['s'] = (Bob['A'] ** Bob['b']) % Bob['p']

    print("Do their secrets match?")
    print("Alice's secret:{}, Bob's secret:{}".format(Alice['s'], Bob['s']))
    
