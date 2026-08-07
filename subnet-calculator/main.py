import ipaddress

def main_menu():
    numbers = [1, 2, 3]
    print("=" * 45)
    print("Welcome to the Subnet Calculator".center(45))
    print("=" * 45)
    print("") 
    choice = int(input(
    '1. Network Information\n'
    ''
    '2. Subnet Calculator\n'
    ''
    '3. Exit\n'
    ''       
    'Choice:'))
    print("")
    if choice not in numbers:
        print("Please choose 1, 2 or 3")
    else:
        return choice

def get_network(): #takes user_input
    while True:
        try:
            user_input = input("Please input an ip address (CIDR format): ") #asks user for an ip-address
            print("")
            network = ipaddress.IPv4Network(user_input, strict=False)
            address = user_input.split("/") #get the ip address
            ip = address[0]
            ip_address = ipaddress.IPv4Address(ip)
            return network, ip_address #returns network object and ip_address
        
        except ValueError:
            print("")
            print("wrong input! Please enter a valid ip_address...")
            continue

def calculate_informations(network, ip_addr): #calculates informations for display
    private_status = "No"
    if ip_addr.is_private:
        private_status = "Yes" #checks, if address is part of the private ip address range 
    network_address = network.network_address
    network_class = "."
    first_octet = int(str(network_address).split(".")[0])
    broadcast_address = network.broadcast_address
    subnet_mask = network.netmask
    wildcard_mask = network.hostmask
    prefix = network.prefixlen
    first_host = network.network_address + 1
    last_host = network.broadcast_address - 1
    usable_hosts = network.num_addresses - 2

    if first_octet >= 1 and first_octet < 127:
        network_class = "A"
    elif first_octet >= 128 and first_octet <= 191:
        network_class = "B"
    elif first_octet >= 192 and first_octet <= 223:
        network_class = "C"
    elif first_octet >= 224 and first_octet <= 239:
        network_class = "D"
    else:
        network_class = "E"
    
    if network.prefixlen == 32:
        usable_hosts = 1
        first_host = broadcast_address
        last_host = broadcast_address
    elif network.prefixlen == 31:
        usable_hosts = 2
        last_host = broadcast_address
        first_host = network_address

    return {
    "network_address": network_address,
    "broadcast_address": broadcast_address,
    "subnet_mask": subnet_mask,
    "wildcard_mask": wildcard_mask,
    "prefix": prefix,
    "first_host": first_host,
    "last_host": last_host,
    "usable_hosts": usable_hosts,
    "private_status": private_status,
    "network_class": network_class
    }

def display_informations(data): #displays Values
    print("=" * 39)
    print("Subnet Information".center(39))
    print("=" * 39)
    print(f"{'Network Address':<20}: {data['network_address']}") 
    print(f"{'Broadcast':<20}: {data['broadcast_address']}") 
    print(f"{'Subnet Mask':<20}: {data['subnet_mask']}") 
    print(f"{'Wildcard Mask':<20}: {data['wildcard_mask']}") 
    print(f"{'CIDR Prefix':<20}: {data['prefix']}") 
    print(f"{'First Host':<20}: {data['first_host']}") 
    print(f"{'Last Host':<20}: {data['last_host']}") 
    print(f"{'Usable Hosts':<20}: {data['usable_hosts']}") 
    print(f"{'Private Address':<20}: {data['private_status']}") 
    print(f"{'Network class':<20}: {data['network_class']}") 

while True:
    choice = main_menu()
   
    if choice == 1:
        network_info = get_network() 
        network, ip_addr = network_info #tuple unpackaging 
        data = calculate_informations(network, ip_addr)
        display_informations(data)
        print("")
        finish = input(f"Press Enter to return")
        print("")
        continue
        
    elif choice == 3:
        break
    
