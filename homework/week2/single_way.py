#!/usr/bin/env python

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import Link, TCLink, Intf

if '__main__' == __name__:
    """Create Topo"""
    net = Mininet(link=TCLink)
    
    """Host Adding"""
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    """Router Adding"""
    r1 = net.addHost('r1')
    r2 = net.addHost('r2')
    r3 = net.addHost('r3')
    r4 = net.addHost('r4')

    """Node Linking"""
    net.addLink(h1, r1)
    net.addLink(h2, r2)
    net.addLink(r1, r2)
    net.addLink(r1, r3)
    net.addLink(r2, r4)
    net.addLink(r3, r4)
    
    net.build()

    """Router IP & MAC Configuration"""
    r1.cmd('ifconfig r1-eth0 192.168.1.1 netmask 255.255.255.0')
    r1.cmd('ifconfig r1-eth1 192.168.12.1 netmask 255.255.255.0')
    r1.cmd('ifconfig r1-eth2 192.168.13.1 netmask 255.255.255.0')

    r2.cmd('ifconfig r2-eth0 192.168.2.1 netmask 255.255.255.0')
    r2.cmd('ifconfig r2-eth1 192.168.12.2 netmask 255.255.255.0')
    r2.cmd('ifconfig r2-eth2 192.168.24.2 netmask 255.255.255.0')

    r3.cmd('ifconfig r3-eth0 192.168.13.3 netmask 255.255.255.0')
    r3.cmd('ifconfig r3-eth1 192.168.34.3 netmask 255.255.255.0')

    r4.cmd('ifconfig r4-eth0 192.168.24.4 netmask 255.255.255.0')
    r4.cmd('ifconfig r4-eth1 192.168.34.4 netmask 255.255.255.0')

    h1.cmd('ifconfig h1-eth0 192.168.1.2 netmask 255.255.255.0')
    h2.cmd('ifconfig h2-eth0 192.168.2.2 netmask 255.255.255.0')

    """Host Default Gateway"""
    r1.cmd('ip route add default via 192.168.13.3 dev r1-eth2')
    r2.cmd('ip route add default via 192.168.12.1 dev r2-eth1')
    r3.cmd('ip route add default via 192.168.34.4 dev r3-eth1')
    r4.cmd('ip route add default via 192.168.24.2 dev r4-eth0')

    h1.cmd('ip route add default via 192.168.1.1 dev h1-eth0')
    h2.cmd('ip route add default via 192.168.2.1 dev h2-eth0')

    """Forwarding"""
    r1.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
    r2.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
    r3.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
    r4.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')

    """Disable Reverse Path"""
    r1.cmd('echo 0 > /proc/sys/net/ipv4/conf/all/rp_filter')
    r1.cmd('echo 0 > /proc/sys/net/ipv4/conf/r1-eth0/rp_filter')
    r1.cmd('echo 0 > /proc/sys/net/ipv4/conf/r1-eth1/rp_filter')
    r1.cmd('echo 0 > /proc/sys/net/ipv4/conf/r1-eth2/rp_filter')
   
    r2.cmd('echo 0 > /proc/sys/net/ipv4/conf/all/rp_filter')
    r2.cmd('echo 0 > /proc/sys/net/ipv4/conf/r2-eth0/rp_filter')
    r2.cmd('echo 0 > /proc/sys/net/ipv4/conf/r2-eth1/rp_filter')
    r2.cmd('echo 0 > /proc/sys/net/ipv4/conf/r2-eth2/rp_filter')
    
    r3.cmd('echo 0 > /proc/sys/net/ipv4/conf/all/rp_filter')
    r3.cmd('echo 0 > /proc/sys/net/ipv4/conf/r3-eth0/rp_filter')
    r3.cmd('echo 0 > /proc/sys/net/ipv4/conf/r3-eth1/rp_filter')
   
    r4.cmd('echo 0 > /proc/sys/net/ipv4/conf/all/rp_filter')
    r4.cmd('echo 0 > /proc/sys/net/ipv4/conf/r4-eth0/rp_filter')
    r4.cmd('echo 0 > /proc/sys/net/ipv4/conf/r4-eth1/rp_filter')

    CLI(net)
    net.stop()
