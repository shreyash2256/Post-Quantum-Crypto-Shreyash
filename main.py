import numpy as np

# Parameters
n = 4
q = 97

# Generate secret key
def generate_secret():
    return np.random.randint(0, q, n)

# Generate public key
def generate_public(secret):
    A = np.random.randint(0, q, (n, n))
    e = np.random.randint(-1, 2, n)
    b = (A @ secret + e) % q
    return A, b

# Encrypt message (0 or 1)
def encrypt(A, b, message):
    r = np.random.randint(0, 2, n)
    u = (r @ A) % q
    v = (r @ b + message * (q // 2)) % q
    return u, v

# Decrypt
def decrypt(secret, u, v):
    x = (v - u @ secret) % q
    return 1 if x > q//4 else 0


# MAIN
secret = generate_secret()
A, b = generate_public(secret)

message = 1
u, v = encrypt(A, b, message)

decrypted = decrypt(secret, u, v)

print("Original Message:", message)
print("Decrypted Message:", decrypted)