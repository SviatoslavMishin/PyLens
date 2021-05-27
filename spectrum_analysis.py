"""
В данном файле представлены функции для расчета 
интегральных значений спектральных характеристик
Дополнительно используется функция simps из библиотеки SciPy

"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.integrate import simps


def load_spectrum_file(file_name):
    """
    Обработка файла со спектральными характеристиками, введенного пользователем
    Функция принимает введенное имя исходного файла и возвращает список строк этого файла
    """
    with open(file_name, 'r') as spectrum_file:
        current_file = spectrum_file.readlines()
    return current_file


def get_info(current_file):
    """
    Извлечение из открытого файла информации об измерении
    Принимает прочитанный построчно файл с результатами измерений
    Возвращает список, содержащий слова в нулевой строке файла измерений
    """
    info = current_file[0].split('\t')
    return info

def get_waves(current_file):
    """
    Извлечение данных о длинах волн
    Принимает открытый файл спектра, который был возвращен в виде построчного списка
    функцией load_spectrum_file
    """

    # Убираем первые 2 строки со служебной информацией
    temp_list = current_file[2:]
    # Создаем список, в который будем записывать нужные значения
    waves = []
    for i in temp_list:
        if not i:
            continue
        # Из каждой строчки исходного файла-списка берем только длину волны
        waves.append(i.split('\t')[1])
    waves = [float(i) for i in waves]
    return waves

def get_data(current_file):
    """
    Извлечение данных о значениях спектральных коэффициентов
    Принимает открытый файл спектра, который был возвращен в виде построчного списка
    функцией load_spectrum_file
    """
    # Убираем первые 2 строки со служебной информацией
    temp_list = current_file[2:]
    spectrum_data = []  # Создаем список, в который будем записывать нужные значения
    for i in temp_list:
        if not i:
            continue
        # Из каждой строчки исходного файла-списка берем только длину волны
        spectrum_data.append(i.split('\t')[3])
    spectrum_data = [float(i) for i in spectrum_data]
    return spectrum_data

def calc_integral_coeff(spectrum_data, waves, min_wave, max_wave):
    """
    Вычисление интегрального коэффициента 
    Принимает список с данными о спектральных коэффициентах, список с соотв. длинами волн,
    а также нижнюю и верхнюю границу интегрирования - границы интересующего участка спектра
    Возвращает интегральный коэффициент
    """
    # Фильтрация исходных массивов данных
    min_wave_position = 0
    max_wave_position = 0
    i = 0
    while i <= (len(waves) - 1):
        if (waves[i] <= min_wave):
            min_wave_position = i
            i += 1
        elif (min_wave < waves[i] <= max_wave):
            max_wave_position = i
            i += 1
        else:
            break
    # Нужный участок массива коэффициентов
    spectrum_data = spectrum_data[min_wave_position:max_wave_position + 1]
    # Нужный участок массива длин волн
    waves = waves[min_wave_position:max_wave_position + 1]
    integral = simps(spectrum_data, waves)  # Интеграл
    # Интегральный коэффициент
    integral_coeff = integral / (waves[-1] - waves[0])
    return integral_coeff


def draw_plot(waves, spectrum_data, mode, min_wave, max_wave):
    """
    Рисование графика спектральной характеристики
    """

    # На рисунке fig с системами координат axes у нас будет один график
    fig, axes = plt.subplots(1)
    axes.plot(waves, spectrum_data)  # График зависимости спектр. коэффициента
    fig.subplots_adjust(left=0.125, right=0.9, top=0.9, bottom=0.15)
    # На полученном графике обозначим диапазон, для которого будем считать интегральный коэффициент
    rect = patches.Rectangle((min_wave, 0), (max_wave - min_wave), 100, linewidth=1,
                             edgecolor='green', facecolor='green', fill=True, color='green', alpha=0.5)
    axes.add_patch(rect)
    # Введем сетку, названия осей и название графика
    # Добавим светло серую сетку с прозрачностью 0,5
    axes.grid(True, c='lightgrey', alpha=0.5)
    axes.set_xlabel('Wavelength, nm', fontsize=8)  # Название оси х
    axes.set_ylim(0, 100)  # Пределы значений по оси y - от 0 до 100%
    # Если режим измерения R, то название графика - Spectral Reflection и по оси y - к-т отражения
    # Если режим измерения T, то название графика - Spectral Transmission и по оси y - к-т пропускания
    if mode == 'Mode: R':
        axes.set_title('Spectral Reflection', fontsize=10)
        axes.set_ylabel('R, %', fontsize=8)
    elif mode == 'Mode: T':
        axes.set_title('Spectral Transmission', fontsize=10)
        axes.set_ylabel('T, %', fontsize=8)
    return fig


'''
# Код проверки
#Ввод исходных данных: имя файла спектра, граничные длины волн для анализа
file_name = input('Введите имя файла спектра: ')
print(get_mode(file_name))
spectrum_data = get_spectrum_data(file_name)
waves = get_waves(file_name)
min_wave = float(input('Введите начальную длину волны: '))
max_wave = float(input('Введите конечную длину волны: '))

#Вычисление интегрального коэффициента
coeff = calc_integral_coeff(spectrum_data, waves, min_wave, max_wave)
print(coeff)

#Рисуем график, на котором изображены спектр из файла и диапазон анализа (красный rect)
fig, ax = plt.subplots(1)
ax.plot(waves, spectrum_data)
rect = patches.Rectangle((min_wave, 0), (max_wave - min_wave), 100, linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(rect)
plt.show()
'''


# Все работает
