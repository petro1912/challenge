from web3 import Web3
import re

def get_ether_balance(address):
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/bc9e864d4dcb4fcea20b32230aabcf29'))

    balance = w3.eth.get_balance(address)
    ether_balance = w3.from_wei(balance, 'ether')

    return ether_balance

def is_valid_ethereum_address(address):
    if len(address) == 42 and address.startswith('0x'):
        return True
    else:
        return False