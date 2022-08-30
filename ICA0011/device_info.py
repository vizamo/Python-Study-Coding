"""Get information about Cisco Router or Switch."""
import re
from netmiko import ConnectHandler
import csv

device_IOS_XR_ONE = {
    'address': 'sbx-iosxr-mgmt.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    "ssh_port": 8181,
    "device_type": "cisco_ios"
}
device_IOS_XE_ONE = {
    "address": "ios-xe-mgmt.cisco.com",
    "ssh_port": 8181,
    "username": "root",
    "password": "D_Vay!_10&",
    "device_type": "cisco_ios"
}
device_IOS_XE_TWO = {
    "address": "ios-xe-mgmt-latest.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "device_type": "cisco_ios"
}

conn_IOS_XR_ONE = ConnectHandler(ip=device_IOS_XR_ONE["address"],
                                 port=device_IOS_XR_ONE["ssh_port"],
                                 username=device_IOS_XR_ONE["username"],
                                 password=device_IOS_XR_ONE["password"],
                                 device_type=device_IOS_XR_ONE["device_type"])

conn_IOS_XE_ONE = ConnectHandler(ip=device_IOS_XE_ONE["address"],
                                 port=device_IOS_XE_ONE["ssh_port"],
                                 username=device_IOS_XE_ONE["username"],
                                 password=device_IOS_XE_ONE["password"],
                                 device_type=device_IOS_XE_ONE["device_type"])

conn_IOS_XE_TWO = ConnectHandler(ip=device_IOS_XE_TWO["address"],
                                 username=device_IOS_XE_TWO["username"],
                                 password=device_IOS_XE_TWO["password"],
                                 device_type=device_IOS_XE_TWO["device_type"])


class ObtainInformation:

    def __init__(self, device, ios):
        """."""
        self.connected_device = device
        self.ios = ios

        self.run = self.send_command('show run')
        self.version = self.send_command('show version')
        self.ip_data = self.send_command('show ip int brief')
        self.ssh_data = self.send_command('show ssh')

        self.hostname = self.regex('hostname (.+)', self.run)
        self.domain_name = self.regex('domain name (.+)', self.run)

        self.last_conf_change = self.regex('Last configuration change at (.+)', self.run)
        self.lcc_time, self.lcc_user = self.last_conf_change.split(' by ')
        self.uptime = self.regex('uptime is (.+)', self.version)

    def send_command(self, command):
        response = self.connected_device.send_command(command)
        return response

    @staticmethod
    def regex(pattern, text):
        return re.findall(pattern, text)[0]

    def ip_packets(self):
        ip_packets = self.send_command('show ip traffic')
        sent = int(self.regex(r'Sent: (\d+)', ip_packets))
        received = int(self.regex(r'Rcvd:  (\d+)', ip_packets))
        return str(sent + received)

    def int_info(self):
        lines = [re.sub(r'\s+', ' ', line) for line in self.ip_data.split('\n') if
                 line and '-----' not in line]
        lines = lines[1:] if self.ios == 'xe' else lines[2:]
        interfaces_count = str(len(lines))
        enabled_int = []
        for interface in lines:
            interface = interface.split(" ")
            if interface[3] in ['Up', 'up'] or interface[5] in ['Up', 'up']:
                int_info = self.send_command(f'show int {interface[0]}')
                int_ip = interface[1] if interface[1] != 'unassigned' else 'Interface does not have IP address'

                mac = re.findall(r'Hardware is .+, address is (....\.....\.....)', int_info)
                int_mac = mac[0] if len(mac) > 0 else 'Interface does not have MAC address'

                int_output = {interface[0]: {'ip_address': int_ip, 'mac_address': int_mac}}
                enabled_int.append(int_output)
        return enabled_int, interfaces_count

    def ssh(self):
        sessions = str(len(re.findall(r'Session | SESSION', self.ssh_data)))
        ssh_ip = self.send_command('show ip ssh')
        ssh_r = re.findall(r'SSH Enabled|SSH version :', ssh_ip)
        if len(ssh_r) > 0 or sessions:
            status = 'enabled'
        else:
            status = 'disabled'

        ssh_clients = []
        if self.ios == 'xr':
            lines = [re.sub(r'\s+', ' ', line) for line in self.ssh_data.split('\n') if
                     line and '-----' not in line]
            lines = lines[4:-1]
            for line in lines:
                line = line.split(" ")
                ssh_clients.append({line[0]: line[6]})
        return status, sessions, ssh_clients

    def terminal_output(self):
        """Print found information to terminal"""
        print("Device Hostname is: " + self.hostname)
        print("Device Domain Name is: " + self.domain_name)
        print("System last configuration change was at " + self.lcc_time +
              " by " + self.lcc_user)
        print("System last boot was " + self.uptime + " ago")

        interfaces: tuple = self.int_info()
        print("System have " + interfaces[1] + " interfaces. "
              + str(len(interfaces[0])) + " is enabled")
        print("Enabled interfaces in system:")
        for interface in interfaces[0]:
            name = str(list(interface.keys())[0])
            ip = interface[name]['ip_address']
            mac = interface[name]['mac_address']
            print("    " + name +
                  " (IP: " + ip +
                  ", MAC: " + mac + ")")

        ssh = self.ssh()
        print('SSH client is ' + ssh[0])
        print("Currently open " + ssh[1] + " SSH sessions:")
        for client in ssh[2]:
            name = str(list(client.keys())[0])
            ip = client[name]
            print(name + " with ip: " + ip)

        ip_packets = self.ip_packets()
        print("Total number of send and received IP packets: " + ip_packets)

    def csv_output(self):
        with open(f'device_{self.hostname}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Device Hostname is: " + self.hostname])
            writer.writerow(["Device Domain Name is: " + self.domain_name])
            writer.writerow(["System last configuration change was at " + self.lcc_time +
                             " by " + self.lcc_user])
            writer.writerow(["System last boot was " + self.uptime + " ago"])
            interfaces: tuple = self.int_info()
            writer.writerow(["System have " + interfaces[1] + " interfaces. "
                             + str(len(interfaces[0])) + " is enabled"])
            writer.writerow(["Enabled interfaces in system:"])
            for interface in interfaces[0]:
                name = str(list(interface.keys())[0])
                ip = interface[name]['ip_address']
                mac = interface[name]['mac_address']
                writer.writerow(["    " + name + " (IP: " + ip + ", MAC: " + mac + ")"])
            ssh = self.ssh()
            writer.writerow(['SSH client is ' + ssh[0]])
            writer.writerow(["Currently open " + ssh[1] + " SSH sessions: "])
            for client in ssh[2]:
                name = str(list(client.keys())[0])
                ip = client[name]
                writer.writerow(["    " + name + " with ip: " + ip])
            ip_packets = self.ip_packets()
            writer.writerow(["Total number of send and received IP packets: " + ip_packets])


print("------------First device information------------")
print()
ObtainInformation(conn_IOS_XR_ONE, 'xr').terminal_output()
print()
print("------------Second device information------------")
print()
ObtainInformation(conn_IOS_XE_ONE, 'xe').terminal_output()
print()
print("------------Third device information------------")
print()
ObtainInformation(conn_IOS_XE_TWO, 'xe').terminal_output()

ObtainInformation(conn_IOS_XR_ONE, 'xr').csv_output()
ObtainInformation(conn_IOS_XE_ONE, 'xe').csv_output()
ObtainInformation(conn_IOS_XE_TWO, 'xe').csv_output()
