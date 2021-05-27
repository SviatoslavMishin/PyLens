'''
Данные функции предназначены для решения следующих задач по работе с каталогами стекол Zemax:
1. Открытие файла-каталога и конвертация его в рабочую переменную-список. 
Элементы списка - строки исходного файла.
2. Поиск марки стекла, запрашиваемой пользователем
3. Извлечение нужных параметров

'''
#Обработка каталога стекла, введенного пользователем.
#Принимает введенное имя каталога CatalogName. 
#Возвращает этот каталог в виде списка строк
def get_GlassCatalog(CatalogName):
	GlassCatFile = open(CatalogName, 'r')
	GlassCatList = GlassCatFile.readlines()
	GlassCatFile.close()
	return GlassCatList

#Ищет в созданном списке марку стекла, введенную пользователем
#Принимает имя марки стела GlassName и каталог стекла, преобразованный в список строк - GlassCatList
#Возвращает номер строки GlassPosition, с которой начинаются данные этого стекла
def get_GlassPosition(GlassName, GlassCatList):
	GlassPosition = 0
	i = 0
	while i <= (len(GlassCatList)-1):
		if (GlassCatList[i].startswith(GlassName)):
			GlassPosition = i
		else:
			pass
		i += 1
	return GlassPosition

#Функция для получения списка всех марок стекол в текущем каталоге
#Принимает каталог стекла, преобразованный в список строк
#Возвращает список всех марок стекол в этом каталоге
def get_Glasses(GlassCatList):
	Glasses=[]
	for item in GlassCatList:
		if item.startswith('NM'):
			TargetList = item.split(' ')
			Glasses.append(TargetList[1])
		else:
			pass
	return Glasses	

#Функция - извлекатель показателя преломления nd для введенной ранее марки стекла
#Принимает номер строки с маркой стекла.
#Возвращает показатель преломления для длины волны d=0.58756180 мкм
def get_dIndex(GlassPosition, GlassCatList):
	TargetString = GlassCatList[GlassPosition] #Исходная строка, в которой находится нужный параметр
	TargetList = TargetString.split(' ')#Разбиваем её на слова по разделителю. Разделитель - символ пробел
	dIndex = float(TargetList[4])
	return dIndex

#Функция - извлекатель числа Аббе vd для введенной ранее марки стекла
#Принимает номер строки с маркой стекла.
#Возвращает число Аббе для длины волны d=0.58756180 мкм
def get_AbbeNumber(GlassPosition, GlassCatList):
	TargetString = GlassCatList[GlassPosition] #Исходная строка, в которой находится нужный параметр
	TargetList = TargetString.split(' ')#Разбиваем её на слова по разделителю. Разделитель - символ пробел
	AbbeNumber = float(TargetList[5])
	return AbbeNumber

#Функция - извлекатель кода дисперсионной формулы для введенной ранее марки стекла
#Принимает номер строки с маркой стекла.
#Возвращает код дисперсионной формулы в обозначениях Zemax
#1 - Schott
#2 - Sellmeier1
#3 - Herzberger
#4 - Sellmeier2
#5 - Conrady
#6 - Sellmeier3
#7 - Handbook1
#8 - Handbook2
#9 - Sellmeier4
#10 - Extended
#11 - Sellmeier5
#12 - Extended2
def get_DispersionCode(GlassPosition, GlassCatList):
	TargetString = GlassCatList[GlassPosition] #Исходная строка, в которой находится нужный параметр
	TargetList = TargetString.split(' ')#Разбиваем её на слова по разделителю. Разделитель - символ пробел
	DispersionCode = float(TargetList[2])
	return DispersionCode

#Функция - извлекатель термического коэффициента расширения TCE
#Принимает номер строки с маркой стекла.
#Возвращает термический коэффициент расширения TCE
def get_TCE(GlassPosition, GlassCatList):
	TargetString = GlassCatList[GlassPosition + 2] #Исходная строка, в которой находится нужный параметр
	TargetList = TargetString.split(' ')#Разбиваем её на слова по разделителю. Разделитель - символ пробел
	TCE = float(TargetList[1])
	return TCE

#Функция - извлекатель плотности стекла
#Принимает номер строки с маркой стекла.
#Возвращает плотность стекла в г/см3
def get_Density(GlassPosition, GlassCatList):
	TargetString = GlassCatList[GlassPosition + 2] #Исходная строка, в которой находится нужный параметр
	TargetList = TargetString.split(' ')#Разбиваем её на слова по разделителю. Разделитель - символ пробел
	Density = float(TargetList[3])
	return Density

#Функция - извлекатель частной дисперсии dPgF
#Принимает номер строки с маркой стекла.
#Возвращает частную дисперсию dPgF
def get_PartDispersion(GlassPosition, GlassCatList):
	TargetString = GlassCatList[GlassPosition + 2] #Исходная строка, в которой находится нужный параметр
	TargetList = TargetString.split(' ')#Разбиваем её на слова по разделителю. Разделитель - символ пробел
	PartDispersion = float(TargetList[4])
	return PartDispersion

#Функция - извлекатель коэффициентов дисперсионной формулы
#Принимает номер строки с маркой стекла.
#Возвращает список, состоящий из коэффициентов дисперсионной формулы
def get_DispCoeffs(GlassPosition, GlassCatList):
	TargetString = GlassCatList[GlassPosition + 3] #Исходная строка, в которой находится нужный параметр
	DispCoeffs = TargetString.split(' ')#Разбиваем её на слова по разделителю. Разделитель - символ пробел
	DispCoeffs = DispCoeffs[1:]#Берем все, кроме первого слова, которое будет CD
	DispCoeffs = [float(i) for i in DispCoeffs]#Преобразуем все элементы в тип float
	return DispCoeffs

#Функция - извлекатель термооптических коэффициентов
#Принимает номер строки с маркой стекла.
#Возвращает список, состоящий из термооптических коэффициентов
def get_ThermalIndexCoeffs(GlassPosition, GlassCatList):
	TargetString = GlassCatList[GlassPosition + 4] #Исходная строка, в которой находится нужный параметр
	ThermalIndexCoeffs = TargetString.split(' ')#Разбиваем её на слова по разделителю. Разделитель - символ пробел
	ThermalIndexCoeffs = ThermalIndexCoeffs[1:]#Берем все, кроме первого слова, которое будет CD
	ThermalIndexCoeffs = [float(i) for i in ThermalIndexCoeffs]#Преобразуем все элементы в тип float
	return ThermalIndexCoeffs

#Функция - извлекатель коротковолновой границы рабочего спектрального диапазона стекла
#Принимает номер строки с маркой стекла.
#Возвращает длину волны коротковолновой границы рабочего спектрального диапазона стекла в мкм
def get_MinWave(GlassPosition, GlassCatList):
	TargetString = GlassCatList[GlassPosition + 6] #Исходная строка, в которой находится нужный параметр
	TargetList = TargetString.split(' ')#Разбиваем её на слова по разделителю. Разделитель - символ пробел
	MinWave = float(TargetList[1])
	return MinWave

#Функция - извлекатель длинноволновой границы рабочего спектрального диапазона стекла
#Принимает номер строки с маркой стекла.
#Возвращает длину волны длинноволновой границы рабочего спектрального диапазона стекла в мкм
def get_MaxWave(GlassPosition, GlassCatList):
	TargetString = GlassCatList[GlassPosition + 6] #Исходная строка, в которой находится нужный параметр
	TargetList = TargetString.split(' ')#Разбиваем её на слова по разделителю. Разделитель - символ пробел
	MaxWave = float(TargetList[2])
	return MaxWave

'''
#Проверка работы
CatalogName = input('Введите имя открываемого файла-каталога: ')
GlassCatList = get_GlassCatalog(CatalogName)
print(get_Glasses(GlassCatList))


GlassName = 'NM ' + input('Введите марку стекла: ')
GlassNumber = get_GlassPosition(GlassName, GlassCatList)
print('Ваше стекло находится в строке № '+ str(GlassNumber))
print('Ваш параметр = ' + str(get_MaxWave(GlassNumber, GlassCatList)))
'''



