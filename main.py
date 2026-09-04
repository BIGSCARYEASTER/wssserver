from cloudlink import server
import os
# Read Render's assigned port string, use 10000 if running locally
port_env = int(os.environ.get("PORT", 10000))
# Import protocols

from cloudlink.server.protocols import clpv4, scratch



# Instantiate the server object
server = server()

# Set logging level
server.logging.basicConfig(
    level=server.logging.INFO # See python's logging library for details on logging levels.
)

# Load protocols
clpv4 = clpv4(server)
scratch = scratch(server)

# Start the server!
server.run(ip="0.0.0.0", port=10000)
