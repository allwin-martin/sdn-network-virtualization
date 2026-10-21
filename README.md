# SDN Network Virtualization — Mininet Lab

Educational two-switch, four-host OpenFlow lab. **Not** a completed EVPN/VXLAN or OpenDaylight deployment.

## Static test
```bash
python -m unittest discover -p "test_*.py"
python validate_topology.py
```

## Live lab (Linux VM)
Install Mininet, Open vSwitch and a compatible OpenFlow controller. Start the controller on TCP port 6653, then:
```bash
sudo mn --custom topology.py --topo lab --controller remote,ip=127.0.0.1,port=6653 --switch ovsk
```
At the Mininet prompt: `net`, `nodes`, `pingall`. If forwarding fails, verify the controller and switch OpenFlow versions.

## Demo talking points
Control plane versus data plane; topology links; switch-to-controller connection; packet forwarding. Live controller connectivity has not been validated here.
