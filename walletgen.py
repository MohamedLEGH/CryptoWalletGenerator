from mnemonic import Mnemonic
from bip32utils import BIP32Key
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

print(key.ChildKey(44 + BIP32_HARDEN) \
     .ChildKey(0 + BIP32_HARDEN) \
     .ChildKey(0 + BIP32_HARDEN) \
     .ChildKey(0) \
     .ChildKey(0) \
.Address())
