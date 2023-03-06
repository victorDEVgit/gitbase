capital = {
    'Abia' : 'Umuahia',
    'Adamawa' : 'Yola',
    'Akwa Ibom' : 'Uyo',
    'Benue' : 'Markurdi',
    'Lagos' : 'Ikeja',
    'Ogun' : 'Abeokuta',
    'Borno' : 'Maiduguri'
}
print("Lagos state capital is: " , capital['Lagos'])
for state, city in list(capital.items()):
    print(f"Nigeria has {state} state, and its capital is {city}")