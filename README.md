# Network Scanning Tools

## Project Description
This project contains simple Python programs to perform basic network scanning tasks.  
It includes three tools:

1. Ping Scanner  
2. ARP Scanner  
3. Nmap Scanner  

These tools use Python and system commands to scan and analyze network information.



## Requirements

Before running the programs, make sure the following are installed:

- Python 3
- Nmap




## Installing Nmap

Download and install Nmap from the official website:

https://nmap.org/download.html

After installing, verifying  the installation:

nmap --version





### Run Ping Scanner

Command:

py ping_scanner.py

Example Output:
Enter hostname or IP: google.com
Host is reachable
Average Time: 9ms


---


=== Ping Scanner ===
Enter hostname(s) or IP(s) (separate multiple with commas): google.com, 8.8.8.8, 192.168.1.50

--- Scanning: google.com ---
Status: Reachable
Average Time: 19ms

--- Scanning: 8.8.8.8 ---
Status: Reachable
Average Time: 17ms

--- Scanning: 192.168.1.50 ---
Status: Reachable
Average Time: Could not parse response time

### Run ARP Scanner

Command:

py arp_scanner.py

Example Output:

=== ARP Scanner ===
IP Address      MAC Address
-----------------------------------
192.168.2.1     08-7b-87-9b-89-f4
192.168.2.2     94-18-65-4f-7a-ab
192.168.2.10    28-00-af-d4-ba-13
192.168.2.18    10-98-19-bc-4e-9f
192.168.2.222   28-00-af-d4-b9-ff
192.168.2.247   78-46-5c-5e-2b-4d
192.168.2.255   ff-ff-ff-ff-ff-ff
224.0.0.22      01-00-5e-00-00-16
224.0.0.251     01-00-5e-00-00-fb
224.0.0.252     01-00-5e-00-00-fc
239.255.255.250 01-00-5e-7f-ff-fa
255.255.255.255 ff-ff-ff-ff-ff-ff
192.168.56.255  ff-ff-ff-ff-ff-ff
224.0.0.22      01-00-5e-00-00-16
224.0.0.251     01-00-5e-00-00-fb
224.0.0.252     01-00-5e-00-00-fc
239.255.255.250 01-00-5e-7f-ff-fa

Total entries: 17

--------------

=== ARP Scanner ===

IP Address              MAC Address
---------------------------------------------
192.168.2.1             08-7b-87-9b-89-f4
192.168.2.2             94-18-65-4f-7a-ab
192.168.2.9             6c-f6-da-f2-9c-e8
192.168.2.16            78-46-5c-5e-23-49
192.168.2.19            ac-b4-80-da-73-3f
192.168.2.29            10-98-19-03-7f-8a
192.168.2.47            ac-b4-80-da-74-55
192.168.2.213           ac-b4-80-da-73-27
192.168.2.221           04-f0-ee-19-ec-d1
192.168.2.222           28-00-af-d4-b9-ff
192.168.2.223           24-b2-b9-be-0a-89
192.168.2.225           24-b2-b9-be-39-a9
192.168.2.229           24-b2-b9-be-39-e5
192.168.2.230           04-f0-ee-19-df-8e
192.168.2.234           04-f0-ee-1d-03-99
192.168.2.235           24-b2-b9-be-52-f3
192.168.2.237           04-f0-ee-1b-d0-91
192.168.2.241           10-98-19-17-85-b6
192.168.2.255           ff-ff-ff-ff-ff-ff
224.0.0.22              01-00-5e-00-00-16
224.0.0.99              01-00-5e-00-00-63
224.0.0.251             01-00-5e-00-00-fb
224.0.0.252             01-00-5e-00-00-fc
239.255.255.250         01-00-5e-7f-ff-fa
255.255.255.255         ff-ff-ff-ff-ff-ff
192.168.56.255          ff-ff-ff-ff-ff-ff
224.0.0.22              01-00-5e-00-00-16
224.0.0.251             01-00-5e-00-00-fb
224.0.0.252             01-00-5e-00-00-fc
239.255.255.250         01-00-5e-7f-ff-fa
10.81.234.255           ff-ff-ff-ff-ff-ff
224.0.0.22              01-00-5e-00-00-16
224.0.0.251             01-00-5e-00-00-fb
224.0.0.252             01-00-5e-00-00-fc
239.255.255.250         01-00-5e-7f-ff-fa
255.255.255.255         ff-ff-ff-ff-ff-ff

Total entries: 36

Would you like to save these results to a file? (y/n): y
Enter filename (e.g., arp_results.txt): office_network.txt
Results successfully saved to office_network.txt





### Run Nmap Scanner

Command:

py nmap_scanner.py

Example:

=== Nmap Scanner ===
Enter target IP: nmap -F scanme.nmap.org
Starting Nmap 7.98 ( https://nmap.org ) at 2026-03-16 18:30 +0530
Nmap scan report for nmap -F scanme.nmap.org (50.116.1.184)
Host is up (0.26s latency).
Other addresses for nmap -F scanme.nmap.org (not scanned): 2600:3c01:e000:3e6::6d4e:7061
rDNS record for 50.116.1.184: ack.nmap.org
Not shown: 993 filtered tcp ports (no-response), 1 filtered tcp ports (admin-prohibited)

PORT      STATE  SERVICE
22/tcp    open   ssh
70/tcp    closed gopher
80/tcp    open   http
113/tcp   closed ident
443/tcp   open   https
31337/tcp closed Elite

--------

=== Nmap Scanner ===
Nmap is installed
Enter target IP or network range: 192.168.1.1

Select scan type:
1. Basic Host Discovery (-sn)
2. Port Scan (default 1-1000)
3. Service Version Detection (-sV)
4. OS Detection (-O)
Enter choice (1-4): 2

Scanning 192.168.1.1... (this may take a while)

Scan Results:

Starting Nmap 7.98 ( https://nmap.org ) at 2026-03-17 15:27 +0530
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.78 seconds



Save results to file? (y/n): y
Enter filename (e.g., nmap_output.txt): scan_results.txt
Results saved to scan_results.txt


### Run Unified Network Scanner (All-in-One)
Command:
py network_scanner.py

This tool provides a central menu to access the Ping, ARP, and Nmap scanners from a single interface.


==============================
   UNIFIED NETWORK SCANNER
==============================
1. Ping Scanner (Reachable & Response Time)
2. ARP Scanner (IP-MAC Table)
3. Nmap Scanner (Port/Service/OS)
4. Exit

Select an option (1-4): 1
Enter hostname(s) or IP(s) (comma-separated): 192.168.10.129

--- Scanning: 192.168.10.129 ---
Status: Reachable
Average Time: 44ms

==============================
   UNIFIED NETWORK SCANNER
==============================
1. Ping Scanner (Reachable & Response Time)
2. ARP Scanner (IP-MAC Table)
3. Nmap Scanner (Port/Service/OS)
4. Exit

Select an option (1-4): 2

IP Address              MAC Address
---------------------------------------------
192.168.2.1             08-7b-87-9b-89-f4
192.168.2.2             94-18-65-4f-7a-ab
192.168.2.9             6c-f6-da-f2-9c-e8
192.168.2.16            78-46-5c-5e-23-49
192.168.2.19            ac-b4-80-da-73-3f
192.168.2.29            10-98-19-03-7f-8a
192.168.2.47            ac-b4-80-da-74-55
192.168.2.213           ac-b4-80-da-73-27
192.168.2.221           04-f0-ee-19-ec-d1
192.168.2.222           28-00-af-d4-b9-ff
192.168.2.223           24-b2-b9-be-0a-89
192.168.2.225           24-b2-b9-be-39-a9
192.168.2.229           24-b2-b9-be-39-e5
192.168.2.230           04-f0-ee-19-df-8e
192.168.2.234           04-f0-ee-1d-03-99
192.168.2.235           24-b2-b9-be-52-f3
192.168.2.237           04-f0-ee-1b-d0-91
192.168.2.241           10-98-19-17-85-b6
192.168.2.255           ff-ff-ff-ff-ff-ff
224.0.0.22              01-00-5e-00-00-16
224.0.0.99              01-00-5e-00-00-63
224.0.0.251             01-00-5e-00-00-fb
224.0.0.252             01-00-5e-00-00-fc
239.255.255.250         01-00-5e-7f-ff-fa
255.255.255.255         ff-ff-ff-ff-ff-ff
192.168.56.255          ff-ff-ff-ff-ff-ff
224.0.0.22              01-00-5e-00-00-16
224.0.0.251             01-00-5e-00-00-fb
224.0.0.252             01-00-5e-00-00-fc
239.255.255.250         01-00-5e-7f-ff-fa
10.81.234.129           00-ff-f8-19-d8-c4
10.81.234.255           ff-ff-ff-ff-ff-ff
224.0.0.22              01-00-5e-00-00-16
224.0.0.251             01-00-5e-00-00-fb
224.0.0.252             01-00-5e-00-00-fc
239.255.255.250         01-00-5e-7f-ff-fa
255.255.255.255         ff-ff-ff-ff-ff-ff

Total entries: 37

Would you like to save these results to a file? (y/n): n

==============================
   UNIFIED NETWORK SCANNER
==============================
1. Ping Scanner (Reachable & Response Time)
2. ARP Scanner (IP-MAC Table)
3. Nmap Scanner (Port/Service/OS)
4. Exit

Select an option (1-4): 3
Enter target IP or network: 192.168.10.129

Select scan type:
1. Basic Host Discovery (-sn)
2. Port Scan (default 1-1000)
3. Service Version Detection (-sV)
4. OS Detection (-O)
Enter choice (1-4): 4

Scanning 192.168.10.129... (this may take a while)

Scan Results:
========================================
Starting Nmap 7.98 ( https://nmap.org ) at 2026-03-17 15:40 +0530
Nmap scan report for 192.168.10.129
Host is up (0.11s latency).
Not shown: 986 filtered tcp ports (no-response)
PORT     STATE SERVICE
53/tcp   open  domain
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl
3389/tcp open  ms-wbt-server
5357/tcp open  wsdapi
5985/tcp open  wsman
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: broadband router|specialized|router
Running (JUST GUESSING): OneAccess embedded (89%), AVtech embedded (88%), Linksys embedded (85%)
OS CPE: cpe:/h:oneaccess:1641
Aggressive OS guesses: OneAccess 1641 router (89%), AVtech Room Alert 26W environmental monitor (88%), Linksys BEFSR41 EtherFast router (85%)
No exact OS matches for host (test conditions non-ideal).

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.44 seconds







## Screenshots

Screenshots of the program outputs are stored in the screenshots folder.


screenshots/ping_output.png  
screenshots/arp_output.png  
screenshots/nmap_output.png  



