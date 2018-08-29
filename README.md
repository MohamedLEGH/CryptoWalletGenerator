Command line interface to generate mnemonic hd wallet in python3

Can be used to create bitcoin, bitcoin-testnet or ethereum account

Follow same pattern as this website : https://iancoleman.io/bip39/

# Before install
pip3 install mnemonic 

pip3 install bip32utils

pip3 install ethereum

# install

git clone https://github.com/MohamedLEGH/CryptoWalletGenerator
cd CryptoWalletGenerator

chmod u+x walletgen

# Usage

To generate a new mnemonic (24 words)
```
./walletgen --new mnemonic 
output : 
  24 words
  equivalent master seed 

To derivate account from mnemonic

./walletgen --new account

enter network (ethereum or bitcoin or bitcoin-testnet)

enter the account number you want to generate

enter the mnemonic 24 words

output:
  private key
  wif (only bitcoin and bitcoin-testnet)
  public key (only bitcoin and bitcoin-testnet)
  address
  
  
```
example :
```

./walletgen --new mnemonic 

output :

Your 24 mnemonic words are: 

stairs patrol mimic memory scorpion lady arctic second mouse punch nature humor strong valid fat father great game tattoo cat unaware twist near vessel

The equivalent master seed is: 

557531277f3b1b5b5e9225011b34bfbd7df99911150ecae731342742971698f87613b3ff1d2106f230bbc57ba729cedacbad15551154c8b93dfe541a8104fc6f


./walletgen --new account
Please enter network (bitcoin, bitcoin-testnet or ethereum) : bitcoin
Please enter account number :0
Please input 24 mnemonic words :
stairs patrol mimic memory scorpion lady arctic second mouse punch nature humor strong valid fat father great game tattoo cat unaware twist near vessel

output:
 ********** Account Data ********** 

private key : e6661ad4ac28bd03406a54851bbcda1cb18e7854dd3418ea1fa57894d5c431a8

WIF : L4waNN1cK3UJUMAzeWp31BfMwdciQ7QbX4rrJP4SamBUnydjJGQ5

public key : 02b7b73b2fe2362933724437bb37c40167192a3ab88236c45492405ac258674954

address : 19jnnAWWv2rP968cAjaYqDHSLZ5Waz3DLZ
```
