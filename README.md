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

To generate 24 words and mnemonic
```
./walletgen --mnemonic 
output : 
  24 words
  equivalent master seed 
```
To generate 24 words

```
./walletgen --words
output : rate latin vicious music pig physical fix number raven session leaf festival indicate wrap umbrella federal begin grocery crop unfair task submit two payment
```

To generate seed

```
./walletgen --seed
output : 7376da6f43b6e8fe46897c6343b8f14f05581b65f6b6cb296ef4098258a3a29c61073180cc0f348b9934f6abf299c107d9ecf9215ce212f7f6fea791147d8462
```

To generate seed from 24 words

```
./walletgen --seedfromwords "24words" 
```
example:
```
./walletgen --seedfromwords "cannon lucky try weasel lawn private object forward tortoise pet wasp shine mad verb dinner summer idea make notable suffer family license bless story"
output :189751cf217140241754eb9825f1343fb69b74201001fbad448fb5fb91bf25d832e04bd8af89892cc5a87e07f61c4afe7b6fdae96b68c68d977a9253ae425801
```

To derivate account from seed
```
./walletgen --datafromseed

enter the seed

enter network (ethereum or bitcoin or bitcoin-testnet)

enter the account number you want to generate

output:
  private key
  wif (only bitcoin and bitcoin-testnet)
  public key (only bitcoin and bitcoin-testnet)
  address
```  


To derivate account from 24 words
```
./walletgen --data

enter the mnemonic 24 words

enter network (ethereum or bitcoin or bitcoin-testnet)

enter the account number you want to generate

output:
  private key
  wif (only bitcoin and bitcoin-testnet)
  public key (only bitcoin and bitcoin-testnet)
  address
  
  
```

To derivate privatekey from seed
```
./walletgen --key SEED NETWORK ACCOUNT_NUMBER
(example) :
./walletgen --key 7376da6f43b6e8fe46897c6343b8f14f05581b65f6b6cb296ef4098258a3a29c61073180cc0f348b9934f6abf299c107d9ecf9215ce212f7f6fea791147d8462 ethereum 2
output : 145bb45fb5588d44800e0461cf5b0bfdda2a44f3767d583180c9984233c6c7f8
```

To derivate address from seed
```
./walletgen --address SEED NETWORK ACCOUNT_NUMBER
(example) :
./walletgen --address 7376da6f43b6e8fe46897c6343b8f14f05581b65f6b6cb296ef4098258a3a29c61073180cc0f348b9934f6abf299c107d9ecf9215ce212f7f6fea791147d8462 ethereum 2
output : 0x8FaF0bc74b0b4be7384f7d6921FD538D0Df11a07
```
