import xmltodict

stream = open("demo1.xml", "r")

xml = xmltodict.parse(stream.read())

for e in xml["Users"]["User"]:
    print(e)