from napalm import get_network_driver
import json
driver = get_network_driver("ios")
ios_r1 = driver("10.10.10.1","dharmo","dharmo")
ios_r1.open()

r1_fact = ios_r1.get_facts()
print json.dumps(r1_fact, indent=4)

ios_r1.close()
