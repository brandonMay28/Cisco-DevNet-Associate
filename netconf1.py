from ncclient import manager
import xml.dom.minidom

router = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "user": "developer",
    "pass": "C1sco12345",
    "port": "830"
}

netconfFilter = """
    <filter>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name></name>
            </interface>
        </interfaces>
    </filter>
"""


with manager.connect(host=router["host"], port=router["port"], username=router["user"],
 password=router["pass"], hostkey_verify=False) as m:
    
    for capabiltity in m.server_capabilities:
        print(" ")
        print(capabiltity)
        print("*" * 50)

        interface_netconf = m.get(netconfFilter)
        xmldom = xml.dom.minidom.parseString(str(interface_netconf))
        print(xmldom.toprettyxml(indent="  "))
        print("*" * 25 + "Break" + "*" * 25)

    