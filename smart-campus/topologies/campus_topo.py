from mininet.topo import Topo
class CampusTopo(Topo):
    def build(self):
        core= self.addSwitch('s1')
        s2=self.addSwitch('s2')
        s3=self.addSwitch('s3')
        s4=self.addSwitch('s4')

        hosts={
            'h1' : '10.0.0.1/24' ,
            'h2' : '10.0.0.2/24' ,
            'h3' : '10.0.0.3/24' ,
            'h4' : '10.0.0.4/24' ,
            'h5' : '10.0.0.5/24' ,
            'h6' : '10.0.0.6/24' ,
            }
        host_obj={}
        for host,ip in hosts.items():
            host_obj[host]=self.addHost(host,ip=ip)
        self.addLink(core,s2)
        self.addLink(core,s3)
        self.addLink(core,s4)
        self.addLink(s2,host_obj['h1'])
        self.addLink(s2,host_obj['h2'])
        self.addLink(s3,host_obj['h3'])
        self.addLink(s3,host_obj['h4'])
        self.addLink(s4,host_obj['h5'])
        self.addLink(s4,host_obj['h6'])
topos = {
    'campusTopo': CampusTopo
}
