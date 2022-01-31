# Application for automobile store with dict

Automobile = {                                               #dict has two key values pairs
              'store1':{
                        'name':'Engine accessories',          #value has again two dict
                        'parts': [                             # value has list of three dict
                                     { 'name':'cylinder', 'quantity'  : 14},
                                     { 'name': 'piston' ,  'quantity' : 16},
                                     { 'name' : 'crank' ,  'quantity' : 4 }
                                    ]
                        },

              'store2':{
                        'name': 'Engine type',
                        'parts': [
                                   {'name': 'BMW'  , 'quantity' : '400hp'},
                                   {'name': 'porsche' , 'quantity' : '600hp'},
                                   {'name': 'ferrari' , 'quantity' : '300hp'}
                                  ]
                        }
             }
for d in Automobile['store1']['parts']:
    print(d['name'])
for d in Automobile . get('store1').get('parts') :
    if d['name'] == 'crank':
        print(d['quantity'])
for f in Automobile['store2']['parts']:
     if f['name'] == 'ferrari':
            print (list(f.values()))