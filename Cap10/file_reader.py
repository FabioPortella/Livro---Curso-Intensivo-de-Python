file_name = 'cap10\pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()

niver = input("Entre com a data de seu aniversário: ddmmaa => ")
if niver in pi_string:
    print("Seu aniverário está no primeiro milhão de digitos de PI !")
else:
    print("Seu aniverário NÃO está no primeiro milhão de digitos de PI !")