# BizNOS
Cumulus Linux Generator Ansible for Spine Leaf Clos Network with BGP-EVPN

network-generator.py : generate variable for ansible
```
python3 network-generator.py > group_vars/all
```

topology_generator.py : generate topology.dot for PTM
```
python3 topology-generator.py > topology.dot
```

factory-default.yaml : ansible-playbook for factory default switch
```
# ansible-playbook -u cumulus factory-default.yaml
```
