#!/usr/bin/env python

"""

library to generate hd account for bitcoin and ethereum
follow https://iancoleman.io/bip39/ patern

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
        network_number = 0
    elif network == 'bitcoin-testnet':
        network_number = 1
    elif network == 'ethereum':
        network_number = 60    
    else:
        print("network should not be" + network) 
        sys.exit("Wrong Network : should be ethereum or bitcoin or bitcoin-testnet!")
    
    account = key.ChildKey(44 + BIP32_HARDEN) \
         .ChildKey(network_number + BIP32_HARDEN) \
         .ChildKey(0 + BIP32_HARDEN) \
         .ChildKey(0) \
         .ChildKey(account_number)
    return account

def gen_bitcoin_account_from_seed(seed,account_number):
    key = rootkey_from_seed(seed,"bitcoin")
    account = account_from_rootkey(key,account_number,"bitcoin")
    return account

def gen_bitcoin_testnet_account_from_seed(seed,account_number):
    key = rootkey_from_seed(seed,"bitcoin-testnet")
    account = account_from_rootkey(key,account_number,"bitcoin-testnet")
    return account

def gen_ethereum_account_from_seed(seed,account_number):
    key = rootkey_from_seed(seed,"ethereum")
    account = account_from_rootkey(key,account_number,"ethereum")
    return account

def bitcoin_data(account):
    private_key = account.PrivateKey()
    wif = account.WalletImportFormat()
    public_key = account.PublicKey()
    address = account.Address()
    return private_key,address,wif,public_key

def ethereum_data(account):
    private_key_eth = account.PrivateKey()
    address_eth = checksum_encode(privtoaddr(private_key_eth))
    return private_key_eth,address_eth

def gen_bitcoin_wallet(seed,account_number):
    account = gen_bitcoin_account_from_seed(seed,account_number)
    return bitcoin_data(account)

def gen_bitcoin_testnet_wallet(seed,account_number):
    account = gen_bitcoin_testnet_account_from_seed(seed,account_number)
    return bitcoin_data(account)

def gen_ethereum_wallet(seed,account_number):
    account = gen_ethereum_account_from_seed(seed,account_number)
    return ethereum_data(account)


if __name__ == '__main__':

    m = Mnemonic('english')
    words = m.generate(strength=256)
    print(words)
    
    
    seed = m.to_seed(words)
    print("************")
    print("Seed " + seed.hex())
    #key = BIP32Key.fromEntropy(seed)
    
    
    print("******************Test Bitcoin********************")
    globalkey = BIP32Key.fromEntropy(seed)
    root = globalkey.ExtendedKey()
    print("Root Key is " + root)
    key = BIP32Key.fromExtendedKey(root)
    bitcoinkey = key.ChildKey(44 + BIP32_HARDEN) \
        .ChildKey(0 + BIP32_HARDEN) \
        .ChildKey(0 + BIP32_HARDEN)
    AccountExtendedPrivateKey = bitcoinkey.ExtendedKey()
    print("Account Extended Private Key is " + AccountExtendedPrivateKey)
    AccountExtendedPublicKey  = bitcoinkey.ExtendedKey(private=False)
    print("Account Extended Public Key is " + AccountExtendedPublicKey)
    bitcoinaccount = bitcoinkey.ChildKey(0)
    BIP32ExtendedPrivateKey = bitcoinaccount.ExtendedKey()
    print("BIP32 Extended Private Key  is : " +  BIP32ExtendedPrivateKey)
    BIP32ExtendedPublicKey = bitcoinaccount.ExtendedKey(private=False)
    print("BIP32 Extended Public Key  is : " +  BIP32ExtendedPublicKey)
    bitcoin0 = bitcoinaccount.ChildKey(0)

        
    print("first private key")
    print(bitcoin0.WalletImportFormat())
    print("first address")
    print(bitcoin0.Address())
    
    
    print("******************Test Bitcoin Testnet********************")
    globalkey = BIP32Key.fromEntropy(seed,testnet=True)
    root = globalkey.ExtendedKey()
    print("Root Key is " + root)
    key = BIP32Key.fromExtendedKey(root)
    bitcoinkey = key.ChildKey(44 + BIP32_HARDEN) \
        .ChildKey(1 + BIP32_HARDEN) \
        .ChildKey(0 + BIP32_HARDEN)
        
    AccountExtendedPrivateKey = bitcoinkey.ExtendedKey()
    print("Account Extended Private Key is " + AccountExtendedPrivateKey)
    AccountExtendedPublicKey  = bitcoinkey.ExtendedKey(private=False)
    print("Account Extended Public Key is " + AccountExtendedPublicKey)
    bitcoinaccount = bitcoinkey.ChildKey(0)
    
    BIP32ExtendedPrivateKey = bitcoinaccount.ExtendedKey()
    print("BIP32 Extended Private Key  is : " +  BIP32ExtendedPrivateKey)
    BIP32ExtendedPublicKey = bitcoinaccount.ExtendedKey(private=False)
    print("BIP32 Extended Public Key  is : " +  BIP32ExtendedPublicKey)
    bitcoin0 = bitcoinaccount.ChildKey(0)
    print("first private key")
    print(bitcoin0.WalletImportFormat())
    print("first address")
    print(bitcoin0.Address())
    
    
    print("******************Test Ethereum********************")

    globalkey = BIP32Key.fromEntropy(seed) 
    root = globalkey.ExtendedKey()
    print("Root Key is " + root)
    key = BIP32Key.fromExtendedKey(root)
    ethereumkey = key.ChildKey(44 + BIP32_HARDEN) \
        .ChildKey(60 + BIP32_HARDEN) \
        .ChildKey(0 + BIP32_HARDEN)
    
    AccountExtendedPrivateKey = ethereumkey.ExtendedKey()
    print("Account Extended Private Key is " + AccountExtendedPrivateKey)
    AccountExtendedPublicKey  = ethereumkey.ExtendedKey(private=False)
    print("Account Extended Public Key is " + AccountExtendedPublicKey)
    ethereumaccount = ethereumkey.ChildKey(0)
    BIP32ExtendedPrivateKey = ethereumaccount.ExtendedKey()
    print("BIP32 Extended Private Key  is : " +  BIP32ExtendedPrivateKey)
    BIP32ExtendedPublicKey = ethereumaccount.ExtendedKey(private=False)
    print("BIP32 Extended Public Key  is : " +  BIP32ExtendedPublicKey)
    ethereum0 = ethereumaccount.ChildKey(0)
    private_key_eth = ethereum0.PrivateKey()
    print("first private key")
    print(private_key_eth.hex())
    address_eth = checksum_encode(privtoaddr(private_key_eth))
    print("first address")
    print(address_eth) 
