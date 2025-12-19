# Day 24: Password Hashing (bcrypt)

We use the library `bcrypt`. It is the industry standard for password hashing because it is intentionally "slow" (computationally expensive), making it hard for hackers to brute-force guess passwords.


## 1. The Logic

### A. Generating a Hash (Sign-up)

You do this ONCE when the user creates an account.

```Python
import bcrypt

password = "my_secret_password"

bytes = password.encode('utf-8') 

salt = bcrypt.gensalt() 
hashed = bcrypt.hashpw(bytes, salt)

print(hashed) 
```

### B. Checking a Password (Login)

You hash the input and compare it to the stored hash.

```Python

user_input = "wrong_password"
user_bytes = user_input.encode('utf-8')

result = bcrypt.checkpw(user_bytes, stored_hash)
```
---

## 2. Updating secrets.toml

Instead of storing the password directly, we will generate the hash locally, print it, and then paste that hash into `secrets.toml`.