import pandas as pd
import numpy as np
data = [[2,4,5],
        [2,4,1],
        [4,7,2],
        [4,1,4],
        [6,3,2],
        [5,4,7]]
print(data)

cum1 = int(input('nhap mau cho cum 1:'))
while (cum1 < 0 or cum1 >len(data)):
  print('cum duoc chon phai nam trong mau da cho')
  cum1 = int(input('nhap mau cho cum 1:'))
cum2 = int(input('nhap mau cho cum 2:'))
while (cum2 < 0 or cum2 >len(data) or cum2 == cum1):
  print('cum duoc chon phai nam trong mau da cho va khac cum1')
  cum2 = int(input('nhap mau cho cum 2:'))
cum3 = int(input('nhap mau cho cum 3:'))
while (cum3 < 0 or cum3 >len(data) or cum2 == cum1 or cum3 == cum2):
  print('cum duoc chon phai nam trong mau da cho va khac cum1 va cum2')
  cum2 = int(input('nhap mau cho cum 3:'))

tt1 = data[cum1]
tt2 = data[cum2]
tt3 = data[cum3]
print(tt1)
print(tt2)
print(tt3)

def kcach(x,y):
  kc = 0
  for i in range(len(x)):
    kc = kc + np.power(x[i]-y[i],2)
  return kc

def phan_cum(data, t1, t2,t3):
  c1 =[]
  c2 =[]
  c3 = []
  for i in range(len(data)):
    if(kcach(data[i], tt1) <= kcach(data[i], tt2) and kcach(data[i], tt1) <= kcach(data[i], tt3)):
      c1.append(data[i])
    elif (kcach(data[i], tt2) < kcach(data[i], tt1) and kcach(data[i], tt2) < kcach(data[i], tt3)):
      c2.append(data[i])
    else:
      c3.append(data[i])
  return c1 ,c2,c3
c1, c2,c3 = phan_cum(data, tt1, tt2,tt3)

def cap_nhat_tt(a):
  a = np.array(a)
  tt_new = np.mean(a, axis=0)
  tt_new = tt_new.tolist()
  return tt_new

while ((tt1 != cap_nhat_tt(c1))  or (tt2 != cap_nhat_tt(c2)) or (tt3 != cap_nhat_tt(c3))):
  tt1 = cap_nhat_tt(c1)
  tt2 = cap_nhat_tt(c2)
  tt3 = cap_nhat_tt(c3)
  print(tt1)
  print(tt2)
  print(tt3)
  phan_cum(data, tt1, tt2,tt3)
  c1, c2,c3 = phan_cum(data, tt1, tt2,tt3)
c1, c2,c3 = phan_cum(data, tt1, tt2,tt3)
print('vang: ', c1)
print('bac: ', c2)
print('dong: ', c3)
print('trong tam c1 duoc cap nhat la:', cap_nhat_tt(c1))
print('trong tam c2 duoc cap nhat la:', cap_nhat_tt(c2))
print('trong tam c3 duoc cap nhat la:', cap_nhat_tt(c3))
