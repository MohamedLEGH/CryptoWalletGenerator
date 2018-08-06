from mnemonic import Mnemonic
from bip32utils import BIP32Key

from ethereum.utils import privtoaddr,checksum_encode # for ethereum derivation

m = Mnemonic('english')
words = m.generate(strength=256)
print(words)
seed = m.to_seed(words)
print("************")
print("Seed " + seed.hex())
#key = BIP32Key.fromEntropy(seed)

xprv = BIP32Key.fromEntropy(seed).ExtendedKey()
print("Root Key is " + xprv)

key = BIP32Key.fromExtendedKey(xprv)
from bip32utils import BIP32_HARDEN
"""
print(key.ChildKey(44 + BIP32_HARDEN) \
     .ChildKey(0 + BIP32_HARDEN) \
     .ChildKey(0 + BIP32_HARDEN) \
     .ChildKey(0) \
     .ChildKey(0) \
.Address())
"""
"""
privatekeybitcoin0.Address(
privatekeybitcoin0.C
privatekeybitcoin0.CKDpriv(
privatekeybitcoin0.CKDpub(
privatekeybitcoin0.ChainCode(
privatekeybitcoin0.ChildKey(
privatekeybitcoin0.ExtendedKey(
privatekeybitcoin0.Fingerprint(
privatekeybitcoin0.Identifier(
privatekeybitcoin0.K
privatekeybitcoin0.PrivateKey(
privatekeybitcoin0.PublicKey(
privatekeybitcoin0.SetPublic(
privatekeybitcoin0.WalletImportFormat(
privatekeybitcoin0.depth
privatekeybitcoin0.dump(
privatekeybitcoin0.fromEntropy(
privatekeybitcoin0.fromExtendedKey(
privatekeybitcoin0.hmac(
privatekeybitcoin0.index
privatekeybitcoin0.k
privatekeybitcoin0.parent_fpr
privatekeybitcoin0.public
privatekeybitcoin0.testnet

"""

print("******************Test Bitcoin********************")

bitcoin0 = key.ChildKey(44 + BIP32_HARDEN) \
     .ChildKey(0 + BIP32_HARDEN) \
     .ChildKey(0 + BIP32_HARDEN) \
     .ChildKey(0) \
     .ChildKey(0)
print(bitcoin0.WalletImportFormat())

print(bitcoin0.Address())

print("******************Test Ethereum********************")
"""
print(key.ChildKey(44 + BIP32_HARDEN) \
     .ChildKey(60 + BIP32_HARDEN) \
     .ChildKey(0 + BIP32_HARDEN) \
     .ChildKey(0) \
     .ChildKey(0) \
.Address())
"""

ethereum0 = key.ChildKey(44 + BIP32_HARDEN) \
     .ChildKey(60 + BIP32_HARDEN) \
     .ChildKey(0 + BIP32_HARDEN) \
     .ChildKey(0) \
     .ChildKey(0)
private_key_eth = ethereum0.PrivateKey()
print(private_key_eth.hex())
address_eth = checksum_encode(privtoaddr(private_key_eth))
print(address_eth) 
