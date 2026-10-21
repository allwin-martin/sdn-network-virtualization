"""Two-switch Mininet topology; requires Linux, Mininet and Open vSwitch."""
from mininet.topo import Topo

class LabTopo(Topo):
    def build(self):
        s1 = self.addSwitch("s1")
        s2 = self.addSwitch("s2")
        for i in (1, 2):
            self.addLink(self.addHost(f"h{i}"), s1)
        for i in (3, 4):
            self.addLink(self.addHost(f"h{i}"), s2)
        self.addLink(s1, s2)

topos = {"lab": LabTopo}
