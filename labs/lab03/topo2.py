#flag que forca a utilizacao do python2 para executar o script
#!/usr/bin/evn python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost, Host, Node
from mininet.nodelib import NAT

#criacao da classe que contem a topologia
class Linear(Topo):

    #aqui, o construtor da nossa classe, chama o construtor de topologias do mininet, para construir a rede
    def __init__(self):
        Topo.__init__(self)


        #declaracao dos hosts na mesma subrede, onde o ultimo eh do tipo NAT
        h1 = self.addHost('h1', ip='10.1.1.1', defaultRoute='via 10.1.1.254')
        h2 = self.addHost('h2', ip='10.1.1.2', defaultRoute='via 10.1.1.254')
        h3 = self.addHost('h3', ip='10.1.1.3', defaultRoute='via 10.1.1.254')
        h4 = self.addHost('h4', ip='10.1.1.4', defaultRoute='via 10.1.1.254')
        h5 = self.addHost('h5', ip='10.1.1.5', defaultRoute='via 10.1.1.254')

        #declaracao dos switches openFlow
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')

        #criacao dos links entre hosts-switches e switches-switches
        self.addLink(h1, s1)       
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)
        self.addLink(h5, s5)
        
        #self.addLink(nat1, s3)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s1, s4)
        self.addLink(s4, s3)
        self.addLink(s3, s5)
        self.addLink(s4, s5)

#dicionario da topologia, utilizado como parametro no momento da execucao no ambinente mininet
topos = { 'linear': ( lambda: Linear() ) }