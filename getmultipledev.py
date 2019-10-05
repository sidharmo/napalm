from napalm import get_network_driver
import json

router_list = ["10.10.10.1", "10.10.10.2"]
for router in router_list:
  driver = get_network_driver("ios")
  ios_r = driver(router,"dharmo","dharmo")
  ios_r.open()

  r_fact = ios_r.get_facts()
  hostname = r_fact['hostname']
  uptime = r_fact['uptime']
  print "{} sudah hidup selama {} second".format(hostname, uptime)

  ios_r.close()
