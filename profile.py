"""A profile to create a CloudLab infrastructure with two compute nodes: webserver and observer.

The webserver node runs an Apache web server with a public IP address.
The observer node runs an NFS server without a public IP address.
Both nodes are connected to the same network.
"""

import geni.portal as portal
import geni.rspec.pg as rspec

# Create a request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

# Define the webserver node
webserver = request.RawPC('webserver')
webserver.hardware_type = 'c220g5'
webserver.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD'
webserver.Site('Site 1')

# Define the observer node
observer = request.RawPC('observer')
observer.hardware_type = 'c220g5'
observer.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD'
observer.Site('Site 1')

# Define a link between the two nodes
link = request.Link(members=[webserver, observer])

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
