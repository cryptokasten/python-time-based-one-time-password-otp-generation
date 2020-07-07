import pyotp

seed = "<CODE_FROM_SERVICE>"

pin = pyotp.totp.TOTP(seed).now()
pin

print(pin)
