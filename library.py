#!/usr/bin/env python

"""

library to generate hd account for bitcoin and ethereum
follo https://iancoleman.io/bip39/ patern

"""
import sys

from mnemonic import Mnemonic
from bip32utils import BIP32Key
from bip32utils import BIP32_HARDEN

from ethereum.utils import privtoaddr,checksum_encode # for ethereum derivation

coins = ['bitcoin','bitcoin-testnet','ethereum']

"""
bytes.fromhex("stuff")
"""
def create_words():
    m = Mnemonic('english')
    words = m.generate(strength=256)
    return words

def create_seed(words):
    m = Mnemonic('english')
    seed = m.to_seed(words)
    return seed

def create_mnemonic():
    words = create_words()
    seed = create_seed(words)
    return words,seed

def rootkey_from_seed(seed,network):
    if network == 'bitcoin' or network == 'ethereum':
        xprv = BIP32Key.fromEntropy(seed).ExtendedKey()
    elif network == 'bitcoin-testnet':
        xprv = BIP32Key.fromEntropy(seed,testnet=True).ExtendedKey()    
    else:
        print("network should not be" + network) 
        sys.exit("Wrong Network : should be ethereum or bitcoin or bitcoin-testnet!")
    rootkey = BIP32Key.fromExtendedKey(xprv)
    return rootkey

def account_from_rootkey(key,account_number,network):
    if network == 'bitcoin':
        account = key.ChildKey(44 + BIP32_HARDEN) \
            .ChildKey(0 + BIP32_HARDEN) \
            .ChildKey(0 + BIP32_HARDEN) \
            .ChildKey(0) \
            .ChildKey(account_number)
    elif network == 'bitcoin-testnet':
        account = key.ChildKey(44 + BIP32_HARDEN) \
            .ChildKey(1 + BIP32_HARDEN) \
            .ChildKey(0 + BIP32_HARDEN) \
            .ChildKey(0) \
            .ChildKey(account_number)
    elif network == 'ethereum':
        account = key.ChildKey(44 + BIP32_HARDEN) \
            .ChildKey(60 + BIP32_HARDEN) \
            .ChildKey(0 + BIP32_HARDEN) \
            .ChildKey(0) \
            .ChildKey(account_number)
    else:
        print("network should not be" + network) 
        sys.exit("Wrong Network : should be ethereum or bitcoin or bitcoin-testnet!")
    return account        

def bitcoin_data(account):
    private_key = account.PrivateKey()
    wif = account.WalletImportFormat()
    public_key = account.PublicKey()
    address = account.Address()
    return private_key,wif,public_key,address

def ethereum_data(account):
    private_key_eth = acccount.PrivateKey()
    address_eth = checksum_encode(privtoaddr(private_key_eth))
    return private_key_eth,address_eth

if __name__ == '__main__':

    m = Mnemonic('english')
    words = m.generate(strength=256)
    print(words)
    
    
    seed = m.to_seed(words)
    print("************")
    print("Seed " + seed.hex())
    #key = BIP32Key.fromEntropy(seed)
    
    
    print("******************Test Bitcoin********************")
    xprv = BIP32Key.fromEntropy(seed).ExtendedKey()
    print("Root Key is " + xprv)
    key = BIP32Key.fromExtendedKey(xprv)
    bitcoin0 = key.ChildKey(44 + BIP32_HARDEN) \
        .ChildKey(0 + BIP32_HARDEN) \
        .ChildKey(0 + BIP32_HARDEN) \
        .ChildKey(0) \
        .ChildKey(0)
        
    print("first private key")
    print(bitcoin0.WalletImportFormat())
    print("first address")
    print(bitcoin0.Address())
    
    
    print("******************Test Bitcoin Testnet********************")
    xprv = BIP32Key.fromEntropy(seed,testnet=True).ExtendedKey()
    print("Root Key is " + xprv)
    key = BIP32Key.fromExtendedKey(xprv)
    bitcoin0 = key.ChildKey(44 + BIP32_HARDEN) \
        .ChildKey(1 + BIP32_HARDEN) \
        .ChildKey(0 + BIP32_HARDEN) \
        .ChildKey(0) \
        .ChildKey(0)
    print("first private key")
    print(bitcoin0.WalletImportFormat())
    print("first address")
    print(bitcoin0.Address())
    
    
    print("******************Test Ethereum********************")

    xprv = BIP32Key.fromEntropy(seed).ExtendedKey()
    print("Root Key is " + xprv)
    key = BIP32Key.fromExtendedKey(xprv)
    ethereum0 = key.ChildKey(44 + BIP32_HARDEN) \
        .ChildKey(60 + BIP32_HARDEN) \
        .ChildKey(0 + BIP32_HARDEN) \
        .ChildKey(0) \
        .ChildKey(0)
    private_key_eth = ethereum0.PrivateKey()
    print("first private key")
    print(private_key_eth.hex())
    address_eth = checksum_encode(privtoaddr(private_key_eth))
    print("first address")
    print(address_eth) 
