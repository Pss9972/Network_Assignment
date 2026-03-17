import subprocess
import os

# Update this path if Nmap is installed in a different location
NMAP_PATH = r"C:\Program Files (x86)\Nmap\nmap.exe"

def check_nmap():
    """Checks if Nmap is installed and accessible."""
    try:
        subprocess.run([NMAP_PATH, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def run_scan(target):
    """Provides a menu for different scan types and executes the selected Nmap scan."""
    print("\nSelect scan type:")
    print("1. Basic Host Discovery (-sn)")
    print("2. Port Scan (default 1-1000)")
    print("3. Service Version Detection (-sV)")
    print("4. OS Detection (-O)")
    
    choice = input("Enter choice (1-4): ")
    
    # Mapping user choice to Nmap arguments
    scan_options = {
        "1": ["-sn"],
        "2": ["-p", "1-1000"],
        "3": ["-sV"],
        "4": ["-O"]
    }
    
    args = scan_options.get(choice, [])
    
    # Build the command list
    command = [NMAP_PATH] + args + [target]
    
    print(f"\nScanning {target}... (this may take a while)")
    
    try:
        # Execute the scan with a timeout as per assignment requirements
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=300  # 5-minute timeout
        )
        
        if result.returncode == 0:
            print("\nScan Results:")
            print("========================================")
            print(result.stdout)
            print("========================================")
            
            # Save to file feature
            save_choice = input("\nSave results to file? (y/n): ").lower()
            if save_choice == 'y':
                filename = input("Enter filename (e.g., nmap_output.txt): ")
                with open(filename, "w") as f:
                    f.write(result.stdout)
                print(f"Results saved to {filename}")
        else:
            print("Error: Nmap execution failed.")
            print(result.stderr)

    except subprocess.TimeoutExpired:
        print("Error: The scan timed out.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("=== Nmap Scanner ===")
    
    if not check_nmap():
        print("Error: Nmap is not installed or the path is incorrect.")
        print(f"Current path check: {NMAP_PATH}")
    else:
        print("Nmap is installed")
        target_ip = input("Enter target IP or network range: ")
        if target_ip.strip():
            run_scan(target_ip)
        else:
            print("Error: Target IP cannot be empty.")