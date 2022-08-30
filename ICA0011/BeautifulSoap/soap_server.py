import subprocess
import shutil
import netifaces as nf
import platform
import dns.resolver as d_r

import socket as s
from ipwhois import IPWhois
import os

from spyne import Application, rpc, ServiceBase, Iterable, Unicode

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class UserInformation(ServiceBase):
    """Get information about user OS, IP, Network connection."""

    @staticmethod
    def ping_host(host):
        """Ping host and understand does users net could reach it or not."""
        response = subprocess.call(['ping', '-c', '2', host])
        if response == 0:
            return host + ' is reachable'
        return host + ' is not reachable'

    @staticmethod
    def define_os():
        """Define users current operating system."""
        return "I am using " + platform.system() + " Platform"

    @staticmethod
    def define_public_ip():
        """Define users public IP."""
        interface = list(filter(lambda x: "enp" in x, nf.interfaces()))[0]
        user_current_ip = nf.ifaddresses(interface)[nf.AF_INET][0]['addr']
        return 'My IP address is ' + user_current_ip

    @rpc(Unicode, _returns=Iterable(Unicode))
    def get_information(ctx, reachable_host='www.google.com'):
        """Return information about users system"""
        self = UserInformation()
        user_os = self.define_os()
        ip = self.define_public_ip()
        reach = self.ping_host(reachable_host)
        yield user_os
        yield ip
        yield reach


class DiskUsage(ServiceBase):
    """Get information about total, used and free memory in disk."""

    @staticmethod
    def convert_to_gb(memory_in_bytes: int) -> str:
        """Converts memory to gb."""
        bytes_per_gb = 1024 * 1024 * 1024
        in_gb = float('%.2f' % (memory_in_bytes / bytes_per_gb))
        return str(in_gb)

    @rpc(_returns=Iterable(Unicode))
    def disk_usage(ctx):
        """Find how many memory is total/free/used."""
        self = DiskUsage
        disk_usage: tuple = shutil.disk_usage('/home')
        total = "Total: " + self.convert_to_gb(disk_usage[0]) + "GB"
        used = "Used: " + self.convert_to_gb(disk_usage[1]) + "GB"
        free = "Free: " + self.convert_to_gb(disk_usage[2]) + "GB"
        yield total
        yield used
        yield free


class DnsResolver(ServiceBase):
    """Get information dns records of a domain."""

    @staticmethod
    def get_records(name: str, record_type: str) -> list:
        """Find specific site dns records."""
        resolver = d_r.Resolver()
        records = resolver.resolve(name, record_type)
        result = [record.to_text() for record in records]
        return result

    @rpc(Unicode, _returns=Iterable(Unicode))
    def dns_records(ctx, name):
        """Return site A, MX, NS dns records"""
        self = DnsResolver()
        mail = self.get_records(name, 'MX')
        a = self.get_records(name, 'A')
        ns = self.get_records(name, 'NS')
        yield u"The Name Servers (NS) of %s:" % name
        for ns_record in ns:
            yield u"%s" % ns_record
        yield " "
        yield u"The DNS A Record of %s:" % name
        for a_record in a:
            yield u"%s" % a_record
        yield " "
        yield u"The MX Records of %s:" % name
        for mail_record in mail:
            yield u"%s" % mail_record


class BlockDomain(ServiceBase):
    """Block/Unblock specific domain by name."""

    @staticmethod
    def get_cidr(domain: str):
        """Return domain CIDR."""
        ip = s.gethostbyname(domain)
        cidr = IPWhois(ip).lookup_whois(ip)['asn_cidr']
        return cidr

    @staticmethod
    def block(domain: str, subnet_ip: str, action):
        """Block/Unblock subnet by ip address, domain by name xxx.y."""
        act = 'A' if action in 'block' else 'D'
        os.system(f'sudo iptables -{act} OUTPUT -p tcp -d {domain} -j DROP')
        os.system(f'sudo iptables -{act} OUTPUT -p tcp -d www.{domain} -j DROP')
        os.system(f'sudo iptables -{act} OUTPUT -p tcp -d {subnet_ip} -j DROP')

    @rpc(Unicode, Unicode,  _returns=Iterable(Unicode))
    def block_domain(ctx, domain, action):
        """
        Return site A, MX, NS dns records
        :param domain domain name to block/unblock
        :param action block/unblock subnet.
        """
        self = BlockDomain
        cidr = self.get_cidr(domain)
        self.block(domain, cidr, action)
        yield u"CIDR of %s is %s" % (domain, cidr)
        yield u"Subnet %s and domain %s is %sed" % (cidr, domain, action)


services = [UserInformation, DnsResolver, DiskUsage, BlockDomain]
application = Application(services, 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()
