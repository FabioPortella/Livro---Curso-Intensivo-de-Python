file_name = "Cap10\learning_python.txt"

with open(file_name) as file_object:
    linhas = file_object.readlines()

for linha in linhas:
    print(linha.replace("python", "Delphi"))