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
    private_status = "No"
    if ip_addr.is_private:
        private_status = "Yes"
    print("=" * 39)
    print("Subnet Information".center(39))
    print("=" * 39)
    network_address = network.network_address
    broadcast_address = network.broadcast_address
    subnet_mask = network.netmask
    prefix = network.prefixlen
    first_host = network.network_address + 1
    last_host = network.broadcast_address - 1
    usable_hosts = network.num_addresses - 2
    if network.prefixlen == 32:
        usable_hosts = 1
        first_host = broadcast_address
        last_host = broadcast_address
    elif network.prefixlen == 31:
        usable_hosts = 2
        last_host = broadcast_address
        first_host = network_address

    print(f"{'Network Address':<20}: {network_address}") #display network address
    print(f"{'Broadcast':<20}: {broadcast_address}") #display broadcast address
    print(f"{'Subnet Mask':<20}: {subnet_mask}") #display netmask
    print(f"{'CIDR Prefix':<20}: {prefix}") #CIDR representation of the netmask
    print(f"{'First Host':<20}: {first_host}") #display first host address
    print(f"{'Last Host':<20}: {last_host}") #display last host address
    print(f"{'Usable Hosts':<20}: {usable_hosts}") #display max. number of hosts 
    print(f"{'Private Address':<20}: {private_status}") #checks, if address is part of the private ip address range 

display_information(network, ip_addr)
