'''
Данная программа вычисляет показатель преломления
по одной из дисперсионных формул
'''
#Определим функции вычисления по дисперсионным формулам
# Schott
def schott(Wave, a0, a1, a2, a3, a4, a5):
	index = a0 + a1*pow(Wave, 2) + a2*pow(Wave, -2) + a3*pow(Wave, -4) + a4*pow(Wave, -6) + a5*pow(Wave, -8)
	return pow(index, 0.5)

#Sellmeier 1
def sellmeier1(Wave, K1, L1, K2, L2, K3, L3):
	index = 1 + (K1*pow(Wave, 2))/(pow(Wave, 2)-L1) + (K2*pow(Wave, 2))/(pow(Wave, 2)-L2) + (K3*pow(Wave, 2))/(pow(Wave, 2)-L3)
	return pow(index, 0.5)

#Herzberger
def herzberger(Wave, A, B, C, D, E, F):
	L = 1/(pow(Wave, 2) - 0.028)
	index = A + B*L + C*pow(L, 2) + D*pow(Wave, 2) + E*pow(Wave, 4) + F*pow(Wave, 6)
	return index

#Sellmeier 2
def sellmeier2(Wave, A, B, C, D, E):
	index = A + (B*pow(Wave, 2))/(pow(Wave, 2)-pow(C, 2)) + D/(pow(Wave, 2)-pow(E, 2))
	return pow(index, 0.5)

#Conrady
def conrady(Wave, n0, A, B):
	index = n0 + A/Wave + B/(pow(Wave, 3.5))
	return index

#Sellmeier 3
def sellmeier3(Wave, K1, L1, K2, L2, K3, L3, K4, L4):
	index = 1 + (K1*pow(Wave, 2))/(pow(Wave, 2)-L1) + (K2*pow(Wave, 2))/(pow(Wave, 2)-L2) + (K3*pow(Wave, 2))/(pow(Wave, 2)-L3) + (K4*pow(Wave, 2))/(pow(Wave, 2)-L4)
	return pow(index, 0.5)

#Handbook 1
def handbook1(Wave, A, B, C, D):
	index = A + B/(pow(Wave, 2) - C) - D*pow(Wave, 2)
	return pow(index, 0.5)

#Handbook 2
def handbook2(Wave, A, B, C, D):
	index = A + (B*pow(Wave, 2))/(pow(Wave, 2) - C) - D*pow(Wave, 2)
	return pow(index, 0.5)

#Sellmeier 4
def sellmeier4(Wave, A, B, C, D, E):
	index = A + (B*pow(Wave, 2))/(pow(Wave, 2) - C) + (D*pow(Wave, 2))/(pow(Wave, 2) - E)
	return pow(index, 0.5)

#Extended
def extended(Wave, a0, a1, a2, a3, a4, a5, a6, a7):
	index = a0 + a1*pow(Wave, 2) + a2*pow(Wave, -2) + a3*pow(Wave, -4) + a4*pow(Wave, -6) + a5*pow(Wave, -8) + a6*pow(Wave, -12) + a7*pow(Wave, -14)
	return pow(index, 0.5)

#Sellmeier 5
def sellmeier5(Wave, K1, L1, K2, L2, K3, L3, K4, L4, K5, L5):
	index = 1 + (K1*pow(Wave, 2))/(pow(Wave, 2)-L1) + (K2*pow(Wave, 2))/(pow(Wave, 2)-L2) + (K3*pow(Wave, 2))/(pow(Wave, 2)-L3) + (K4*pow(Wave, 2))/(pow(Wave, 2)-L4) + (K5*pow(Wave, 2))/(pow(Wave, 2)-L5)
	return pow(index, 0.5)

#Extended 2
def extended2(Wave, a0, a1, a2, a3, a4, a5, a6, a7):
	index = a0 + a1*pow(Wave, 2) + a2*pow(Wave, -2) + a3*pow(Wave, -4) + a4*pow(Wave, -6) + a5*pow(Wave, -8) + a6*pow(Wave, 4) + a7*pow(Wave, 6)
	return pow(index, 0.5)

#Все функции работают
