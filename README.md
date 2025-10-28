.

🔍 Port Scanner (Python)
📘 Project Overview

This project is a multithreaded TCP port scanner written in Python.
It scans a remote host to discover open TCP ports and attempts to identify the service associated with each open port.
The main goals are to learn the basics of network scanning, socket programming, and thread management in Python.

Important: Use this tool only on systems you own or where you have explicit permission. Unauthorized port scanning can be illegal.

⚙️ Key Features

Scan a customizable range of TCP ports.

Attempt to detect the service name (via socket.getservbyport) for open ports.

Multithreaded implementation to speed up scanning (one thread per port).

Graceful handling of exceptions and user interrupts (Ctrl+C).

Reports elapsed time for the full scan.

🧩 Technologies

Python 3

Standard library modules:

socket — network communication

threading — concurrent execution

datetime — timing

subprocess — console cleanup

🖥️ Usage
1. Clone the repository
git clone https://github.com/<your-username>/port-scanner.git
cd port-scanner

2. Run the script
python3 port_scanner.py

3. Enter the requested information

Target IP address

Start port (default: 1)

End port (default: 1024)




