import sys.argv as args
from cloudlink import server

if len(sys.argv) < 3:
    print("Error: Please provide an IP and a port.")
    print("Usage: python greet.py <IP> <port>")
    sys.exit(1)

ipa = sys.argv[1]
porta = int(sys.argv[2])

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
server.run(ip=ipa, port=porta)
