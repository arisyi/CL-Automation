#!/usr/bin/env python3

spine = 2
spine_port = 1
leaf = 6
leaf_up_port = 9
leaf_peer_port = 7
leaf_peer_port_count = 2



print ('graph vx {')

i=1
k=leaf_up_port
print(' # Leaf - Spine Connections')
while i <= spine :
  j=1
  while j <= leaf : 
    print(' "leaf'+str(j)+'":"swp'+str(k)+'" -- "spine'+str(i)+'":"swp'+str(j)+'"')
    j += 1
  i += 1
  k += 1

print('')

i=1
print(' # Leaf Peerlink Connections')
while i <= leaf :
  j=1
  k=leaf_peer_port
  while j <= leaf_peer_port_count : 
    print(' "leaf'+str(i)+'":"swp'+str(k)+'" -- "leaf'+str(i+1)+'":"swp'+str(k)+'"')
    j += 1
    k += 1
  i += 2
print('}')

