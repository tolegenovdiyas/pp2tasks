'''
import json
with open('sample-data.json') as file:
    data = json.load(file)
'''
print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU')  
print('-------------------------------------------------- --------------------  ------  ------') 
'''
for i in data['imdata']: 
    print(i['l1PhysIf']['attributes']['dn'],'       ',i['PhysIf']['attributes']['descr'],
          i['l2PhysIf']['attributes']['spped'],'     ',i['PhysIf']['attributes']['mtu'] )
    
print(data['imdata'])    
'''