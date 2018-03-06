#!/usr/bin/env python

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import Link, TCLink, Intf

if '__main__' == __name__:
    
    net = Mininet(link=TCLink)
    
    h1 = net.addHost('h1', ip="192.168.10.2/24", mac="00:00:00:00:00:01")
    h2 = net.addHost('h2')
    h3 = net.addHost('h3', ip="192.168.20.2/24", mac="00:00:00:00:00:03")
    
    net.addLink(h1, h2)
    net.addLink(h2, h3)
    
    net.build()

    h2.cmd('ifconfig h2-eht0 192.168.10.1 netmask 255.255.255.0')
    h2.cmd('ifconfig h2-eht1 192.168.20.1 netmask 255.255.255.0')
    
    h2.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")

    #h1.cmd("ifconfig h1-eth0 0") # Clear interface config
    #h3.cmd("ifconfig h3-eth0 0") 

    #h1.cmd("ip address add 192.168.10.2/24 dev h1-eth0")
    h1.cmd("ip route add default via 192.168.10.1 dev h1-eth0")

    #h3.cmd("ip address add 192.168.20.2/24 dev h3-eth0")
    h3.cmd("ip route add default via 192.168.20.1 dev h3-eth0")

    CLI(net)
    net.stop()
