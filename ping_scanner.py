import subprocess
import platform
import re
import sys

def ping_host(hosts_input):
    """
    Pings one or more hosts and parses the output for reachability and response time.
    Supports comma-separated input for multiple hosts.
    """
    # Detect the operating system to set the correct ping parameter [cite: 85, 87]
    os_type = platform.system().lower()
    
    # Windows uses '-n', while Linux/Mac use '-c' [cite: 88, 89]
    param = "-n" if os_type == "windows" else "-c"

    # Split the input string into a list of hosts and remove whitespace 
    hosts = [h.strip() for h in hosts_input.split(',')]

    for host in hosts:
        print(f"\n--- Scanning: {host} ---")
        try:
            # Execute the ping command using subprocess [cite: 23, 73]
            # Sends 4 packets with a 10-second timeout [cite: 75, 79]
            result = subprocess.run(
                ["ping", param, "4", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=10
            )

            output = result.stdout

            # Check if the host is reachable based on return code [cite: 24, 81]
            if result.returncode == 0:
                print(f"Status: Reachable")

                # Extract average response time using Regex [cite: 25, 91]
                # Regex matches 'Average = Xms' (Windows) or 'avg/X' (Linux/Mac)
                if os_type == "windows":
                    match = re.search(r"Average = (\d+)ms", output)
                else:
                    # Typical Linux/Mac format: min/avg/max/mdev = 10.123/15.456/...
                    match = re.search(r"avg/(\d+\.\d+)", output)

                if match:
                    avg_time = match.group(1)
                    print(f"Average Time: {avg_time}ms")
                else:
                    print("Average Time: Could not parse response time")

            else:
                print(f"Status: Not reachable")

        except subprocess.TimeoutExpired:
            print(f"Error: Ping request for {host} timed out") [cite: 61]
        except Exception as e:
            print(f"An error occurred while scanning {host}: {e}") [cite: 62]

if __name__ == "__main__":
    print("=== Ping Scanner ===")
    # Accepts hostname or IP address as input [cite: 22, 65]
    user_input = input("Enter hostname(s) or IP(s) (separate multiple with commas): ")
    
    if user_input.strip():
        ping_host(user_input)
    else:
        print("Error: No input provided.")