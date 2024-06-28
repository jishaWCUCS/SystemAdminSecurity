"""CloudLab Profile for constructing a profile with 2 nodes.
Assignment 2 profile

Instructions:
Wait for the profile instance to start, and then log in to the host via the
ssh port specified below.
"""

# Import the necessary libraries
import geni.portal as portal
import geni.rspec.pg as pg

# Create a request object to start building the RSpec
request = portal.context.makeRequestRSpec()

# Define the webserver node
webserver = request.RawPC("webserver")
webserver.hardware_type = "m510"
webserver.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD"
webserver.addService(pg.Execute(shell="sh", command="sudo apt-get update && sudo apt-get install -y apache2"))
webserver.routable_control_ip = True

# Define the observer node
observer = request.RawPC("observer")
observer.hardware_type = "m510"
observer.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD"
observer.addService(pg.Execute(shell="sh", command="sudo apt-get update && sudo apt-get install -y nfs-kernel-server"))

# Link the nodes together
link = request.Link(members=[webserver, observer])
link.bandwidth = 1000000  # 1 Gbps

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
