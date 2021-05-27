# -*- coding: utf-8 -*-
'''

'''
import sys
import os
import app_gui
import spectrum_analysis as spectr
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from plot_to_widget import MyCanvas


class AppWin(QtWidgets.QMainWindow):
    current_file = []

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = app_gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.load_file)
        self.ui.pushButton_2.clicked.connect(self.calc)

    def load_file(self):
        # Выбор файла через диалог "Открыть файл" и отображение имени этого файла
        # Получаем имя файла измерений
        file_name = QtWidgets.QFileDialog.getOpenFileName()[0]
        # Принимаем данный файл для использования
        AppWin.current_file = spectr.load_spectrum_file(file_name)
        # Отображаем имя выбранного файла
        self.ui.lineEdit.setText(os.path.basename(file_name))

        # Заполнение полей в разделе Measurement Info
        # Дата измерения
        date = spectr.get_info(AppWin.current_file)[0]
        self.ui.label_2.setText(date)
        self.ui.label_2.adjustSize()

        # Время измерения
        time = spectr.get_info(AppWin.current_file)[1]
        self.ui.label_3.setText(time)
        self.ui.label_3.adjustSize()

        # Режим измерения: R - отражение, T - пропускание
        mode = spectr.get_info(AppWin.current_file)[2]
        self.ui.label_4.setText(mode)
        self.ui.label_4.adjustSize()

        # Поляризация
        polarization = spectr.get_info(AppWin.current_file)[4]
        self.ui.label_5.setText(polarization)
        self.ui.label_5.adjustSize()

        # Предельные длины волн в измерении
        waves = spectr.get_waves(AppWin.current_file)
        self.ui.label_6.setText('Min. wave: ' + str(min(waves)) + ' nm')
        self.ui.label_6.adjustSize()
        self.ui.label_7.setText('Max. wave: ' + str(max(waves)) + 'nm')
        self.ui.label_7.adjustSize()

        # Заполнение ComboBox'ов с начальной (From) и конечной (To) длиной волны для вычислений

        # Начальная длина волны From
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(str(i) for i in waves)
        self.ui.comboBox.setEnabled(True)

        # Конечная длина волны To в зависимости от выбранной во From
        start_wave_index = self.ui.comboBox.findText(
            self.ui.comboBox.currentText())
        self.ui.comboBox_2.addItems(str(i)
                                    for i in waves[start_wave_index + 1::])
        self.ui.comboBox_2.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)

        def update_end_waves():
            self.ui.comboBox_2.clear()
            start_wave_index = self.ui.comboBox.findText(
                self.ui.comboBox.currentText())
            for i in range(start_wave_index + 1, self.ui.comboBox.count()):
                self.ui.comboBox_2.addItem(self.ui.comboBox.itemText(i))

        self.ui.comboBox.currentTextChanged.connect(update_end_waves)

    def calc(self):
        # Получение исходных данных: список длин волн и список соответствующих им спектральных коэффициентов
        waves = spectr.get_waves(AppWin.current_file)
        data = spectr.get_data(AppWin.current_file)
        min_wave = float(self.ui.comboBox.currentText())
        max_wave = float(self.ui.comboBox_2.currentText())
        # Вычисление интегрального коэффициента
        result = spectr.calc_integral_coeff(data, waves, min_wave, max_wave)
        # Вывод результата в зависимости от режима измерения: отражение (R) или пропускание (T)
        mode = spectr.get_info(AppWin.current_file)[2]
        if mode == 'Mode: R':
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_3.setText('R = ' + str('%.3f' % result) + ' %')
        elif mode == 'Mode: T':
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_3.setText('T = ' + str('%.3f' % result) + ' %')
        # Рисуем график в области widget
        # Создаем переменную, хранящую рисунок графика
        self.fig = spectr.draw_plot(waves, data, mode, min_wave, max_wave)
        self.place_for_plot = QtWidgets.QVBoxLayout(self.ui.PlotWidget)
        self.canvas = MyCanvas(self.fig)
        self.place_for_plot.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.place_for_plot.addWidget(self.toolbar)
        self.place_for_plot.deleteLater()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AppWin()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
