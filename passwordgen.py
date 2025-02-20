import random


path = input("Enter the path to the location which the passwords should be saved to (make sure to change \ to /)")
abc = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBMN!@#$%^&*"
#accounts change this to what accounts you need
accounts = ["Google", "Youtube", "Facebook", "Gmail"]
#passwordai = passwords
passwordai = {account: "".join(random.choices(abc, k=12)) for account in accounts}

#location of the passwords
file_path = path

with open(file_path, 'w') as f:
    for account, password in passwordai.items():
        f.write(f"{account}: {password}\n")

#passwordai = passwords
print(passwordai)
print("Passwords saved to", file_path)

    