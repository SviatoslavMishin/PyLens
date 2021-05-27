# -*- coding: utf-8 -*-
'''

'''
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyCanvas(FigureCanvas): #Класс, представляющий собой холст для рисования графика
	def __init__(self, fig, parent = None):
		#Подаем на вход рисунок (экземпляр класса Figure)
		self.fig = fig
		#Инициализация холста (вызов суперкласса)
		FigureCanvas.__init__(self, self.fig)
		#Устанавливаем поведение размеров холста
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		FigureCanvas.setSizePolicy(self, sizePolicy)
		#Сообщаем системе, что политика геометрии для объекта изменилась
		FigureCanvas.updateGeometry(self)
	