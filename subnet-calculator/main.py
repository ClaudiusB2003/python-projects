import ipaddress 

def get_network():
    while True:
        try:
            user_input = input("Please input an ip address (CIDR format): ") #asks user for an ip-address
            ip_address = ipaddress.IPv4Network(user_input, strict=False)
            return ip_address #returns network object
        
        except ValueError:
            print("wrong input! Please enter a valid ip_address...")
            continue

get_network()