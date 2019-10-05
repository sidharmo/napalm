from napalm import get_network_driver

driver = get_network_driver("ios")
ios_r1 = driver("10.10.10.1","dharmo","dharmo")
ios_r1.open()

r1_ip = ios_r1.get_interfaces_ip()
print r1_ip

ios_r1.close()
