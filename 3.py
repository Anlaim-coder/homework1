import random as r

password_letters = r.choices("QAZWSXEDCRFVTGBYHNUJMIKOLP",k=3)
password_numbers = r.choices("0123456789",k=3)
password_symbols = r.choices("!@#$%^&*",k=2)

password = password_letters + password_numbers + password_symbols
r.shuffle(password)
password = "".join(password)

print(password)
