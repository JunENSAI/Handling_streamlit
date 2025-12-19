import bcrypt

password = "tocard@35"
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
print(hashed.decode()) 