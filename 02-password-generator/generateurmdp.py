import random, string

long = int(input("combien de caractere vous voulez pour votre mot de passe: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(long):
  password += random.choice(characters)
print(password)