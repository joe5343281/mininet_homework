#!/usr/bin/env python

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import Link, TCLink, Intf

if '__main__' == __name__:
    """Create Topo"""
    net = Mininet(link=TCLink)
    
    """Host Adding"""
    h1 = net.addHost('h1', ip="192.168.1.1/24", mac="00:00:00:00:00:01")
    h2 = net.addHost('h2', ip="192.168.2.1/24", mac="00:00:00:00:00:02")

    """Router Adding"""
    r1 = net.addHost('r1')
    r2 = net.addHost('r2')
    r3 = net.addHost('r3')
    r4 = net.addHost('r4')

    """Node Linking"""
    net.addLink(h1, r1)
    net.addLink(r1, r2)
    net.addLink(h2, r2)
    net.addLink(r1, r3)
    net.addLink(r3, r4)
    net.addLink(r4, r2)
    
    net.build()

    """Router IP & MAC Configuration"""
    r1.cmd("ifconfig r1-eth0 192.168.1.2 netmask 255.255.255.0")
    r1.cmd("ifconfig r1-eth1 192.168.3.1 netmask 255.255.255.0")
    r1.cmd("ifconfig r1-eth2 192.168.6.2 netmask 255.255.255.0")

    r2.cmd("ifconfig r2-eth0 192.168.2.2 netmask 255.255.255.0")
    r2.cmd("ifconfig r2-eth1 192.168.5.2 netmask 255.255.255.0")
    r2.cmd("ifconfig r2-eth2 192.168.6.1 netmask 255.255.255.0")

    r3.cmd("ifconfig r3-eth0 192.168.3.2 netmask 255.255.255.0")
    r3.cmd("ifconfig r3-eth1 192.168.4.1 netmask 255.255.255.0")

    r4.cmd("ifconfig r4-eth0 192.168.4.2 netmask 255.255.255.0")
    r4.cmd("ifconfig r4-eth1 192.168.5.1 netmask 255.255.255.0")

    h1.cmd("ip route add default via 192.168.1.2 dev h1-eth0")
    h2.cmd("ip route add default via 192.168.2.2 dev h2-eth0")

    CLI(net)
    net.stop()
