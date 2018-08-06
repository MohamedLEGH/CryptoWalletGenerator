from mnemonic import Mnemonic

m = Mnemonic('english')
words = m.generate(strength=256)
print(words)
