#!/usr/bin/env python

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import Link, TCLink, Intf

if '__name__ == __main__':
    
    net = Mininet(link=TCLink)
   
    # Adding Devices
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    h5 = net.addHost('h5')

    # All Devices Linking Topo
    Link(h1, h5)
    Link(h2, h5)
    Link(h3, h5)
    Link(h4, h5)
    net.build()
   
    # All Devices setting
    ## vlan tag setting
    h1.cmd("vconfig add h1-eth0 10")
    h2.cmd("vconfig add h2-eth0 10")
    h3.cmd("vconfig add h3-eth0 20")
    h4.cmd("vconfig add h4-eth0 20")
    
    h5.cmd("vconfig add h5-eth0 10")
    h5.cmd("vconfig add h5-eth1 10")
    h5.cmd("vconfig add h5-eth2 20")
    h5.cmd("vconfig add h5-eth3 20")
    ## vlan if up
    h1.cmd("ifconfig h1-eth0.10 up")
    h2.cmd("ifconfig h2-eth0.10 up")
    h3.cmd("ifconfig h3-eth0.20 up")
    h4.cmd("ifconfig h4-eth0.20 up")
    
    h5.cmd("ifconfig h5-eth0.10 up")
    h5.cmd("ifconfig h5-eth1.10 up")
    h5.cmd("ifconfig h5-eth2.20 up")
    h5.cmd("ifconfig h5-eth3.20 up")
    
    ## br if adding & setting
    h5.cmd("brctl addbr br10")
    h5.cmd("brctl addbr br20")
    
    h5.cmd("brctl addif br10 h5-eth0.10")
    h5.cmd("brctl addif br10 h5-eth1.10")
    h5.cmd("brctl addif br20 h5-eth2.20")
    h5.cmd("brctl addif br20 h5-eth3.20")

    h5.cmd("ifconfig br10 up")
    h5.cmd("ifconfig br20 up")
    
    h1.cmd("ip addr add 10.0.1.1/24 brd + dev h1-eth0.10")
    h2.cmd("ip addr add 10.0.1.2/24 brd + dev h2-eth0.10")
    h3.cmd("ip addr add 10.0.1.3/24 brd + dev h3-eth0.20")
    h4.cmd("ip addr add 10.0.1.4/24 brd + dev h4-eth0.20")

    CLI(net)
    net.stop()
