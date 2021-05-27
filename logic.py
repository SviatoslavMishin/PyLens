'''
Тестовый файл с функциями, описывающими логику программы
'''

from collections import Counter
from operator import itemgetter



def add_info(lens_variations):
    '''
    Добавляет в вариант объектива значение фокального отрезка
    и значение воздушного промежутка между линзами 
    на основе данных об известных вариантах, находящихся в каталоге.
    Каталог известных вариантов объективов - lens_base.txt
    '''
    for lens in lens_variations:
        with open('lens_base.txt') as lens_base:
            for line in lens_base:
                info = line.split()
                if lens[0] == float(info[0]) and lens[1] == float(info[1]):
                    lens.append(float(info[2]))
                    lens.append(float(info[3]))
    return lens_variations


def lens_variations(main_parts, secondary_parts):
    '''
    Определяет все уникальные варианты объектива, которые можно составить
    из всех возможных 001 линз - main_parts и 103(104) линз - secondary parts.
    main_parts - список, содержащий уникальные толщины 001 линз и их количество.
    Толщина и количество линз с этой толщиной лежат в списке в форме кортежей 
    secondary_parts - списоксписок, содержащий уникальные толщины 103(104) линз 
    и их количество.Толщина и количество линз с этой толщиной лежат в списке 
    в форме кортежей

    '''
    lens_variations = []  # Создаем пустой список для вариантов объектива
    for main_part in main_parts:
        for secondary_part in secondary_parts:
            lens = [main_part[0], secondary_part[0], main_part[1] if (
                main_part[1] <= secondary_part[1]) else secondary_part[1]]
            lens_variations.append(lens)
    return lens_variations


def find_match(left_lens, right_lens_variations):
    '''
    Для выбранного 000 объектива находит подходящий ему 000-01 объектив.
    Критерий поиска: delta_bfl = S'_000 - S'_000-01 разность должна быть минимальной.
    Если найдено несколько подходящих вариантов, то выбирается вариант,
    который может быть сформирован в большем количестве.
    Входные параметры:
    left_lens - вариант объектива 000, для которого нужно найти пару;
    right_lens_variations - список всех возможных вариантов 000-01 объектива.
    Выдает - подходящий вариант 000-01 объектива - right_lens.
    '''
    match_lenses = list(right_lens_variations)
    for lens_variation in match_lenses: #для каждого варианта 000-01 объектива считаем разность отрезков delta_bfl
    	delta_bfl = abs(left_lens[3] - lens_variation[3])
    	lens_variation.append(delta_bfl)
    match_lenses = sorted(match_lenses, key=itemgetter(5))	#Сначала сортируем варианты 000-01 объектива по delta_bfl от наименьшей к наибольшей
    sorted(match_lenses, key=itemgetter(2), reverse=True) #Затем отсортированные варианты распределим по частоте, чтобы из нескольких вариантов с наименьшей разностью отрезков выбрать вариант с большим возможным количеством
    match_lens = match_lenses[0][0:5] #Подходящий вариант 

    return match_lens



def kitmaker(parts_001, parts_103, parts_104):
    '''
    Комплектует пары объективов 000 + 000-01.
    Исходные данные - толщины 001, 103 и 104 линз по комплектовочному листу
    Результат список с парами объективов объективов 000 + 000-01 
    '''
    lens_kits = []  # Создаем пустой список для комплектов

    # Защитим исходные списки линз, создав их рабочие копии
    tmp_parts_001 = list(parts_001)
    tmp_parts_103 = list(parts_103)
    tmp_parts_104 = list(parts_104)

    while True:
        # Считаем частоты каждой из линз и выполняем сортировку:
        # от самых часто встречающихся до самых редких
        main_parts = Counter(tmp_parts_001).most_common()
        left_secondary_parts = Counter(tmp_parts_103).most_common()
        right_secondary_parts = Counter(tmp_parts_104).most_common()

        # Составляем список всех возможных вариантов 000 объектива 
        left_lens_variations = lens_variations(
            main_parts, left_secondary_parts)

        #Сортируем эти варианты по убыванию их возможного количества
        left_lens_variations = sorted(
            left_lens_variations, key=itemgetter(2), reverse=True)

        #Дополняем их информацией из базы данных lens_base.txt
        left_lens_variations = add_info(left_lens_variations)

        #Берем самый часто встречающийся вариант 000 объектива
        left_lens = left_lens_variations[0]

        #Удаляем из списка имеющихся линз 001-ю линзу и 103-ю линзу, которые вошли в этот вариант
        tmp_parts_001.remove(left_lens[0])
        main_parts = Counter(tmp_parts_001).most_common() #Заново отсортировали 001 линзы
        tmp_parts_103.remove(left_lens[1])

        #Из оставшихся 001 линз и 104 линз составляем список всех возможных вариантов 000-01 объектива
        right_lens_variations = lens_variations(main_parts, right_secondary_parts)

        # Полученные варианты 000-01 объектива сверяем с базой данных 
        right_lens_variations = add_info(right_lens_variations)    
        
        #Ищем среди них подходящую пару для выбранного варианта 000 объектива
        right_lens = find_match(left_lens, right_lens_variations)

        #Удаляем из списка имеющихся линз 001-ю линзу и 104-ю линзу, которые вошли в этот вариант
        tmp_parts_001.remove(right_lens[0])
        tmp_parts_104.remove(right_lens[1])
       
        #Готовим информацию к выводу: удаляем сведения о количестве.
        #Оставляем только толщины линз, отрезок и промежуток
        del left_lens[2]
        del right_lens[2]
        #Преобразуем выбранные объективы из списков в строки и заполняем список вывода
        lens_kit = ' '.join(map(str, left_lens))+' and '+' '.join(map(str, right_lens))
        lens_kits.append(lens_kit)
        
        #Проверим число оставшихся линз. Если число 001 линз меньше 2 или закончились какие-либо из 103 или 104, то прерываем цикл
        if len(tmp_parts_001) < 2 or not tmp_parts_103 or not tmp_parts_104:
        	break

    return lens_kits

# Тестирование

'''
#Пошаговое тестирование
# 1. Вводим линзы из комплектовочного листа
print('Данные 001 линз:')
parts_001 = parts_input()
print('Данные 103 линз:')
parts_103 = parts_input()
print('Данные 104 линз:')
parts_104=parts_input()


# 2 Для каждой группы линз посчитаем число вхождений каждой толщины
main_parts = Counter(parts_001).most_common()
left_secondary_parts = Counter(parts_103).most_common()
right_secondary_parts = Counter(parts_104).most_common()
print('Отсортированные 001 линзы')
print(main_parts)
print('Отсортированные 103 линзы')
print(left_secondary_parts)
print('Отсортированные 104 линзы')
print(right_secondary_parts)

# 3.1 Составим возможные варианты для 000 и 000-01 объектива
left_lens_variations = lens_variations(main_parts, left_secondary_parts)
print('Варианты 000 объектива' + '\n')
print(left_lens_variations)

right_lens_variations = lens_variations(main_parts, right_secondary_parts)
print('Варианты 000-01 объектива' + '\n')
print(right_lens_variations)

# 3.2 Ставим к каждой паре соответствующее значение заднего отрезка back_focal_length
print('Добавим в них значения S и d' + '\n')
print('Варианты 000 объектива' + '\n')
left_lens_variations = add_info(left_lens_variations)
print(left_lens_variations)

print('Варианты 000-01 объектива' + '\n')
right_lens_variations = add_info(right_lens_variations)
print(right_lens_variations)

# 3.5 Отсортируем варианты объектива по наибольшему количеству
print('Отсортированные по наибольшему количеству варианты' + '\n')
print('Варианты 000 объектива' + '\n')
left_lens_variations = sorted(
    left_lens_variations, key=itemgetter(2), reverse=True)
print(left_lens_variations)
print('Варианты 000-01 объектива' + '\n')
right_lens_variations = sorted(right_lens_variations, key=itemgetter(2), reverse=True)
print(right_lens_variations)

#3.6 Берем вариант 000 объектива, который может быть сформирован в наибольшем количестве.
# Ищем ему в пару 000-01 объектив
left_lens = left_lens_variations[0]
right_lens = find_match(left_lens, right_lens_variations)
print('Наиболее подходящий 000-01 объектив:' + '\n') 
print(right_lens)
lens_kit = ' '.join(map(str, (left_lens_variations[0][0:2]+left_lens_variations[0][3:]) ))+' and '+' '.join(map(str, (right_lens[0:2]+right_lens[3:])))
print('Комплект объективов:'+'\n')
print(lens_kit)
print('ООО объектив\n')
print(left_lens[0])
print('ООО-01 объектив\n')
print(right_lens[0])

parts_001.remove(left_lens[0])
parts_001.remove(right_lens[0])
parts_103.remove(left_lens[1])
parts_104.remove(right_lens[1])

print('\nОставшиеся 001 линзы')
print(parts_001)
print('\nОставшиеся 103 линзы')
print(parts_103)
print('\nОставшиеся 001 линзы')
print(parts_104)



#Общее тестрование
print('Данные 001 линз:')
parts_001 = parts_input()
print('Данные 103 линз:')
parts_103 = parts_input()
print('Данные 104 линз:')
parts_104=parts_input()

print('\nСкомплектованные наборы:\n')
lens_kits=kitmaker(parts_001, parts_103, parts_104)
for lens_kit in lens_kits:
	print('\n'+lens_kit)
'''