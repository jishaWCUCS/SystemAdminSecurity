import geni.portal as portal
import geni.rspec.pg as rspec
         
# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

prefixForIP = "192.168.1."
link = request.LAN("lan")

# Create a XenVM
for i, node_name in enumerate(["webserver", "observer"]):
    node = request.XenVM(node_name)
    
    if node_name == "webserver":
        node.routable_control_ip = True
        node.addService(rspec.Execute(shell="sh", command="sudo bash /local/repository/setup_apache.sh"))
    else:
        node.routable_control_ip = False
        node.addService(rspec.Execute(shell="sh", command="sudo apt-get update && sudo apt-get install -y nfs-kernel-server"))

    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
    iface = node.addInterface("if" + str(i))
    iface.component_id = "eth1"
    iface.addAddress(rspec.IPv4Address(prefixForIP + str(i + 1), "255.255.255.0"))
    link.addInterface(iface)
    
# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
