from suds.client import Client

client = Client('http://localhost:8000/?wsdl', cache=None)

print("Service #1")
user_info = client.service.get_information("www.google.com")
# print(user_info)
print('\n'.join(user_info[0]))
print()

print("Service #2")
dns = client.service.dns_records("twitter.com")
# print(dns)
print('\n'.join(dns[0]))
print()

print("Service #3")
disk = client.service.disk_usage()
# print(disk)
print('\n'.join(disk[0]))
print()

print("Service #4")
block = client.service.block_domain("facebook.com", "unblock")
# print(block)
print('\n'.join(block[0]))

