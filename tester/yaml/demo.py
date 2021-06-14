import yaml
from yaml import load, load_all

stream = open("demo.yaml", "r")

documents = load_all(stream, Loader=yaml.FullLoader)

print(type(documents))
print(" ")

for document in documents:
    for users in document["Users"]:
        print(users)
