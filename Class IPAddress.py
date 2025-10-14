# An IP address is a unique address that identifies a device on the Internet or a local network. 
# IP addresses are a set of four integers separated by dots. For example, 192.158.1.38. 
# Each number in the set belongs to the range of 0 to 255. Therefore, the full range of IP addresses is from 0.0.0.0 to 255.255.255.255.

# Implement an IPAddress class that describes an IP address. When instantiated, the class should accept one argument:

# ipaddress — an IP address represented in one of the following formats:
# a string of four integers separated by dots
# a list or tuple of four integers

class IPAddress:
    def __init__(self, ipadress) -> None:
        if isinstance(ipadress, str):
            self.ipadress = [el for el in ipadress.split('.')]
        else:
            self.ipadress = [str(el) for el in ipadress]

    def __str__(self) -> str:
        return '.'.join(self.ipadress)
    
    def __repr__(self) -> str:
        return f"IPAddress('{'.'.join(self.ipadress)}')"

ip = IPAddress((1, 1, 11, 11))

# Sample Input 1:

ip = IPAddress('8.8.1.1')

print(str(ip))
print(repr(ip))
# Sample Output 1:

# 8.8.1.1
# IPAddress('8.8.1.1')
# Sample Input 2:

ip = IPAddress([1, 1, 10, 10])

print(str(ip))
print(repr(ip))
# Sample Output 2:

# 1.1.10.10
# IPAddress('1.1.10.10')