import ipaddress
def get_network(): #takes user_input
    while True:
        try:
            user_input = input("Please input an ip address (CIDR format): ") #asks user for an ip-address
            network = ipaddress.IPv4Network(user_input, strict=False)
            address = user_input.split("/") #get the ip address
            ip = address[0]
            ip_address = ipaddress.IPv4Address(ip)
            return network, ip_address #returns network object and ip_address
        
        except ValueError:
            print("wrong input! Please enter a valid ip_address...")
            continue

network_info = get_network() 
network, ip_addr = network_info #tuple unpackaging 

def display_information(network, ip_addr): #displays informations of the network
    print("=" * 33)
    print("Subnet Information".center(33))
    print("=" * 33)
    print(f"{'Network Address':<20}: {network.network_address}") #display network address
    print(f"{'Broadcast':<20}: {network.broadcast_address}") #display broadcast address
    print(f"{'Subnet Mask':<20}: {network.netmask}") #display netmask
    print(f"{'Usable Hosts':<20}: {network.num_addresses - 2}") #display max. number of hosts 
    print(f"{'Private Address':<20}: {ip_addr.is_private}") #checks, if address is part of the private ip address range 

display_information(network, ip_addr)
