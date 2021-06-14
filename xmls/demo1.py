from lxml import etree as ET

stream = open("demo.xml", "r")

xml = ET.parse(stream)

root = xml.getroot()

for e in root:
    print(e.get("id"))
    print("*" * 30)
    print(ET.tostring(e))
    print("*" * 30)
    print("")
