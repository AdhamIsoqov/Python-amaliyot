# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:19:05 2023

@author: Lider_Isoqov
"""
# =============================================================================
# son = float(input('Juft son kiriting: '))
# if son % 2 == 0:
#     print('Rahmat!')
# else:
#     print('Bu juft son emas.')
# =============================================================================

# =============================================================================
# yosh = int(input('Yoshingiz nechada\n>>>'))
# if yosh <= 4 or yosh >= 60:
#     narx = 'Kirish bepul'
# elif yosh <= 18:
#     narx = 10_000
# elif yosh >= 18:
#     narx = 20_000
# print(narx)
# =============================================================================

# =============================================================================
# son_1 = float(input('Istalgan son kiriting:'))
# son_2 = float(input('Istalgan son kiriting:'))
# if son_1 < son_2:
#     print(son_1,'<',son_2)
# elif son_1 > son_2:
#     print(son_1,'>',son_2)
# else:
#     print(son_1,'=',son_2)
# =============================================================================

# =============================================================================
# mahsulotlar = ['olma', 'sabzi', 'nok', 'apelsin', 'mandarin', 'ananas', 'banan', 'anor', 'xurmo', 'gilos']
# savat = []
# for mahsulot in range(5):
#     savat.append(input(f'Savatga {mahsulot+1}-mahsulotni qoshing: '))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f'Do\'konimizda {mahsulot} bor')
#     else:
#         print(f'Do\'konimizda {mahsulot} yo\'q')
# =============================================================================

# =============================================================================
# mahsulotlar = ['olma', 'sabzi', 'nok', 'apelsin', 'mandarin', 'ananas', 'banan', 'anor', 'xurmo', 'gilos']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# n = 0
# for mahsulot in range(5):
#     savat.append(input(f'Savatga {mahsulot+1}-mahsulotni qoshing: '))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if len(mavjud_emas) == 0:
#     print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor!')
# else:
#     print('Do\'konimizda quyidagi mahsulotlar yo\'q:')
#     for mahsulot in range(len(mavjud_emas)):
#         print(mavjud_emas[mahsulot])
# =============================================================================

# =============================================================================
# foydalanuvchilar = ['axror', 'firdavs', 'mahmud', 'anvar', 'shuhrat']
# foydalanuvchi = input('Yangi Login kiriting: ')
# if foydalanuvchi.lower() in foydalanuvchilar:
#     print('Login band, yangi login tanlang!')
# else:
#     print('Xush kelibsiz', foydalanuvchi)
# =============================================================================

# =============================================================================
# son = int(input('Istalgan son kiriting: '))
# for i in range(son):
#     if son % (i + 2) == 0:
#         print(f'{son} soni {i+2} ga qoldiqsiz bo\'linadi')
# =============================================================================