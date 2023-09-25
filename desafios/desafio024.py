cid = str(input('Em que cidade você nasceu: ')).strip().lower().split()
if 'santo' in cid[0]:
    print('A palavra Santo está em primeiro')
else:
    print('A palavra Santo não está em primeiro')
