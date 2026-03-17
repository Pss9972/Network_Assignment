import subprocess
import re
import platform

def get_arp_table():
    try:
        # Execute the system 'arp -a' command [cite: 202, 271]
        result = subprocess.run(
            ["arp", "-a"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout
        
        # Regex pattern to extract IP address and MAC address [cite: 203, 265]
        pattern = r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]{11,17})"
        matches = re.findall(pattern, output)

        # Prepare the display table [cite: 204]
        header = "IP Address\t\tMAC Address"
        separator = "-" * 45
        print(f"\n{header}")
        print(separator)

        results_text = f"{header}\n{separator}\n"

        for ip, mac in matches:
            line = f"{ip}\t\t{mac}"
            print(line)
            results_text += line + "\n"

        # Count total entries [cite: 205]
        footer = f"\nTotal entries: {len(matches)}"
        print(footer)
        results_text += footer

        # Save to file feature (Bonus Point Opportunity) [cite: 206, 334]
        save_choice = input("\nWould you like to save these results to a file? (y/n): ").lower()
        if save_choice == 'y':
            filename = input("Enter filename (e.g., arp_results.txt): ")
            with open(filename, "w") as f:
                f.write(results_text)
            print(f"Results successfully saved to {filename}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("=== ARP Scanner ===")
    get_arp_table()