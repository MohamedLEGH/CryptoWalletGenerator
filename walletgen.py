from mnemonic import Mnemonic
from bip32utils import BIP32Key
m = Mnemonic('english')
words = m.generate(strength=256)
print(words)
seed = m.to_seed(words)
print("************")
print("Seed " + seed.hex())
key = BIP32Key.fromEntropy(seed)
xprv = BIP32Key.fromEntropy(seed).ExtendedKey()
print("Root Key is " + xprv)
