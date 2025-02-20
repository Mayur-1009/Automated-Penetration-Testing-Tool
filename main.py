from modules.reconnaissance import whois_lookup, subdomain_scan, scan_ports
from modules.vulnerability_scan import sql_injection_scan, xss_scan, csrf_scan
from modules.exploitation import brute_force_ssh, directory_traversal_scan
from modules.reporting import generate_report

def main():
    print("\n🔍 Automated Penetration Testing Tool")
    print("1️⃣ Reconnaissance")
    print("2️⃣ Vulnerability Scanning")
    print("3️⃣ Exploitation")
    print("4️⃣ Generate Report")
    
    choice = input("\nSelect an option (1-4): ")

    if choice == "1":
        target = input("Enter target domain/IP: ")
        print(whois_lookup(target))
        print(subdomain_scan(target))
        print(scan_ports(target))

    elif choice == "2":
        url = input("Enter URL for vulnerability scan: ")
        sql_injection_scan(url)
        xss_scan(url)
        print(csrf_scan(url))

    elif choice == "3":
        target = input("Enter target IP: ")
        username = input("Enter username: ")
        password_list = input("Enter password list file: ")
        brute_force_ssh(target, username, password_list)
        directory_traversal_scan(target)

    elif choice == "4":
        generate_report("pentest_report.pdf", {"Recon": "Success", "Vulns": "High", "Exploits": "Attempted"})
        print("✅ Report saved as pentest_report.pdf")

    else:
        print("❌ Invalid option!")

if __name__ == "__main__":
    main()
