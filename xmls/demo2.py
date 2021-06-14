import xmltodict

stream = open("demo.xml", "r")

xml = xmltodict.parse(stream.read())

for e in xml["Users"]["User"]:
    print(e)