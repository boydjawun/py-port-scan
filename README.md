# 👣Welcome to Port Recon Pro!
<img width="1000" height="241" alt="Port Recon Pro" src="https://github.com/user-attachments/assets/82687b8a-966e-4dc2-8256-72c119537dfa" />

>Port Recon Pro is a simple port scanner. A Port Scanner is a program that probes a target host (via its IP address) to check which network ports are open, closed, or filtered. It does this by attempting connections (typically TCP) to a range of ports and analyzing responses—open ports usually indicate services listening for connections (e.g., web servers on port 80 or SSH on 22). This specific port scanner is used for **basic reconnaissance** to identify open ports on a target IP address within a user-specified range, helping reveal potentially exposed services.

# 💻Software + Modules Used:
- Windows 11 Host
- Python v3.13.1
- PyCharm 2025.3.2.1
- sys — for flushing stdout during scanning (to show progress in real time)
- socket — for creating network connections and probing ports
- pyfiglet — for generating fancy ASCII art banners(May have to install using apt or pip)
- time — for adding delays (e.g., pauses during verification or scanning feedback)

# 🔗The socket library in Python

>The socket module in Python provides a low-level interface to the BSD socket API, enabling network communication. It allows programs to create endpoints (sockets) for sending and receiving data across networks using protocols like TCP or UDP.

### Common ways it can be used:

>Building client-server applications (e.g., simple web servers, chat apps, or remote control tools)

>Creating TCP clients that connect to remote servers (like fetching web pages or connecting to databases)

>Implementing TCP servers that listen for and accept incoming connections

>Sending/receiving UDP datagrams for lightweight, connectionless communication (e.g., DNS queries, streaming, or gaming)

>Performing network probes/scans (like checking if ports are open)

>Handling low-level socket options (timeouts, binding to addresses, etc.)

# 🔗The sys library in Python
>The sys module provides access to variables and functions that interact closely with the Python interpreter and runtime environment. It's a built-in module for system-specific parameters and control.

### Common ways it can be used:

>Accessing command-line arguments via sys.argv

>Exiting the program cleanly with sys.exit()

>Flushing output buffers (e.g., sys.stdout.flush()) for real-time console updates

>Redirecting or manipulating standard input/output/error streams (sys.stdin, sys.stdout, sys.stderr)

>Querying Python version, platform, or interpreter details (e.g., sys.version, sys.platform)

>Modifying the module search path (sys.path)


# 👣Port Recon Pro Walkthrough
This is an interactive, console-based TCP port scanner named "Port Recon Pro" with a stylish ASCII banner (using pyfiglet). It runs in a loop until the user types "quit".
Here's a step-by-step breakdown of how it works:

### User IP Address Input and IPv4 Validation

- Displays fancy banners with pyfiglet.
- Asks for an IP address (loops until valid or "quit").
- Validates the input as a proper IPv4 address:
- Splits by dots → must have exactly 4 parts.
- Each part must be an integer between 0–255.

### User Port Specifications and TCP Connection

- Prompts for a starting port (portA) and ending port (portZ).
- Prints a message indicating the scan range.
- Defines a helper function probe_port(ip, port):
- Creates a TCP socket (socket.AF_INET, socket.SOCK_STREAM).
- Sets a short 0.5-second timeout.
- Uses connect_ex() which returns 0 if the connection succeeds (port is open), otherwise nonzero.
- Closes the socket and returns the result.
  
### Check each port that was provided

- Loops through every port in the range (from portA to portZ inclusive).
- Calls probe_port() for each.
- If open (response == 0), adds the port to a list.
- Flushes stdout for smoother console feedback.

- After scanning, prints sorted open ports (if any) or a sad message if none found.
- Loops back to ask for a new IP (or quit).

It's a straightforward, basic scanner focused on TCP connect scans (full handshake attempts), useful for learning or quick local checks—but note that scanning remote hosts without permission can be illegal or against terms of service.

# ⚠️ Disclaimer

**For educational and research purposes only.**

Do NOT use any code or technique in this repository against systems you do not own or have explicit written permission to test.

Unauthorized use is illegal and may result in criminal charges.

The author(s) are not liable for any misuse or damage caused by this project.
