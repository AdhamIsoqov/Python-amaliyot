# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:52:56 2023

@author: Lider_Isoqov
"""

# =============================================================================
# python_dictonary = {
#     'integer' : 'butun son',
#     'float' : 'kasr son',
#     'string' : 'matn',
#     'boolean' : 'mantiqiy qiymat',
#     'for' : 'uchun',
#     'in' : 'malum bir narsa ichida',
#     'if' : 'agar',
#     'else' : 'aks holda',
#     'range' : 'malum bir qiymatdan ma`lum bir qiymatgacha'
#     }
# for key, value in sorted(python_dictonary.items()):
#     print(f'{key.title()}-{value.title()}')
# =============================================================================

# =============================================================================
# davlatlar_shaharlar = {
#     "o'zbekiston" : "toshkent",
#     'aqsh' : 'washington',
#     'italiya' : 'rim',
#     'angliya' : 'london',
#     'rossiya' : 'moskva',
#     'hindiston' : 'dehli',
#     'xitoy' : 'pekin',
#     'turkiya' : 'istanbul',
#     'germaniya' : 'berlin'
#     }
# print('Dunyo davlatlari:')
# for davlat in sorted(davlatlar_shaharlar.keys()):
#     print(davlat.upper())
# print('\nDavlatlarning poytaxtlari:')
# for poytaxt in sorted(davlatlar_shaharlar.values()):
#     print(poytaxt.title())
# =============================================================================

# =============================================================================
# davlatlar_shaharlar = {
#     "o'zbekiston" : "toshkent",
#     'aqsh' : 'washington',
#     'italiya' : 'rim',
#     'angliya' : 'london',
#     'rossiya' : 'moskva',
#     'hindiston' : 'dehli',
#     'xitoy' : 'pekin',
#     'turkiya' : 'istanbul',
#     'germaniya' : 'berlin'
#     }
# davlat = input('Qaysi davlatning poytaxtini blishni istaysiz?: ').lower()
# if davlat in davlatlar_shaharlar:
#     print(f'{davlat.upper()}ning poytaxti {davlatlar_shaharlar[davlat].title()} shahri')
# else:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')
# =============================================================================

# =============================================================================
# taomlar_menu = {
#     'osh' : 18_000,
#     'manti' : 18_000,
#     'non' : 2_000,
#     'kabob' : 5_000,
#     'somsa' : 25_000,
#     'chuchvara' : 20_000,
#     'qazi' : 40_000,
#     'tandir kobob' : 75_000,
#     'tabaka' : 25_000,
#     'norin' : 15_000,
#     'shorva' : 12_000
#     }
# taomlar = []
# print('3 ta taom buyurma bering.')
# for taom in range(3):
#     taomlar.append(input(f'{taom+1}-taom: ').lower())
# for taom in taomlar:
#     if taom in taomlar_menu:
#         print(f'{taom.title()} {taomlar_menu[taom]}')
#     else:
#         print(f'Kechirasiz, bizda {taom} yo\'q')
# =============================================================================