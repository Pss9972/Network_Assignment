import ping_scanner
import arp_scanner
import nmap_scanner

def main():
    while True:
        print("\n" + "="*30)
        print("   UNIFIED NETWORK SCANNER")
        print("="*30)
        print("1. Ping Scanner (Reachable & Response Time)")
        print("2. ARP Scanner (IP-MAC Table)")
        print("3. Nmap Scanner (Port/Service/OS)")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == '1':
            target = input("Enter hostname(s) or IP(s) (comma-separated): ")
            ping_scanner.ping_host(target)
        elif choice == '2':
            arp_scanner.get_arp_table()
        elif choice == '3':
            target = input("Enter target IP or network: ")
            nmap_scanner.run_scan(target)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()