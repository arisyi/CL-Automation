#!/usr/bin/env python3
import netaddr

ip_lo_subnet_spine = '10.0.1.1'
ip_lo_subnet_leaf = '10.0.3.1'
ip_mgmt_spine = '192.168.20.111'
ip_mgmt_leaf = '192.168.20.121'
ip_subnet = '10.0.0.0'
asn_spine = 65101
asn_leaf = 65201
spine = 2
leaf = 6
spine_downlink_port = 1
spine_uplink_port = 0
leaf_uplink_port = 9
leaf_downlink_port = 0
leaf_peerlink_port = 7
leaf_peerlink_count= 2

##START SPINE##
lo_spine = netaddr.IPAddress(ip_lo_subnet_spine)
mgmt =  netaddr.IPAddress(ip_mgmt_spine)
i = 1
print ('interfaces:')
while i <= spine :
  print ('    spine'+str(i)+':')
  print ('        type: "spine"')
  print ('        loopback: "'+str(lo_spine)+'"')
  print ('        mgmt: "'+str(mgmt)+'"')
  print ('        asn: '+str(asn_spine))
  print ('        neighbors:')

#daftar port downlink
  sp_down_port = spine_downlink_port
  ip = netaddr.IPAddress(ip_subnet) + 2*leaf*(i-1)
  j = 1
  while j <= leaf :
    print ('          swp'+str(sp_down_port)+': "'+str(ip)+'/31"')
    j += 1
    sp_down_port += 1
    ip += 2
###end daftar port downlink

  i += 1
  lo_spine += 1 
  asn_spine += 1
  mgmt += 1
##END SPINE###

##START LEAF##
lo_leaf = netaddr.IPAddress(ip_lo_subnet_leaf)
mgmt =  netaddr.IPAddress(ip_mgmt_leaf)
ip = netaddr.IPAddress(ip_subnet) + 1 
i = 1
while i <= leaf :
  print ('    leaf'+str(i)+':')
  print ('        type: "leaf"')
  print ('        loopback: "'+str(lo_leaf)+'"')
  print ('        mgmt: "'+str(mgmt)+'"')
  print ('        asn: '+str(asn_leaf))
  print ('        neighbors:')

#start port uplink
  lf_up_port = leaf_uplink_port
  j = 1
  while j <=  spine :
    print ('            swp'+str(lf_up_port)+': "'+str(ip)+'/31"')
    j += 1
    lf_up_port += 1
    ip += 2
#end port uplink
  print ('        peer_port: "swp'+str(leaf_peerlink_port)+'-'+str(leaf_peerlink_port+1)+'"')
  if (i % 2) == 0 :
    print ('        peer_status: "secondary"')
    print ('        peer_ip: "'+str(mgmt-1)+'"')
  else : 
    print ('        peer_status: "primary"')
    print ('        peer_ip: "'+str(mgmt+1)+'"')
#  print ('           swp'+str(leaf_peerlink_port)+':')
#start port peerlink
#  j = 1
#  lf_peer_port = leaf_peerlink_port
  
#  while j <=  leaf_peerlink_count :
#    print ('            swp'+str(lf_peer_port)+':')
#    j += 1
#    lf_peer_port += 1
#end port peerlink

  i += 1
  lo_leaf += 1
  asn_leaf += 1
  mgmt += 1

##END LEAF##                  
