import sys
import os
from Interface import *
from GlassCatAnalysis import *
from DispEquations import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
	SelectedCatalog = [] #Здесь будет храниться выбранный каталог, который загружается функцией loadCatalog
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.comboBox_2.addItems(['0.365 (i)', '0.40466 (h)', '0.43583 (g)', '0.47999 (F\')', '0.48613 (F)', '0.54607 (e)', '0.58756 (d)', '0.58929 (D)', '0.6328 (He-Ne)', '0.64385 (C\')', '0.65627 (C)', '0.70652 (r)']) 
		self.ui.pushButton.clicked.connect(self.loadCatalog)
		self.ui.pushButton_2.clicked.connect(self.calculate)

	def loadCatalog(self): #Изменяет выбранный каталог с каждым нажатием кнопки pushButton
		self.ui.comboBox.clear() #Очистка списка марок стекол
		catalog_path = QtWidgets.QFileDialog.getOpenFileName()[0] #Получаем имя каталога
		MyWin.SelectedCatalog = get_GlassCatalog(catalog_path) #Принимаем данный каталог для использования
		self.ui.lineEdit_3.setText(os.path.basename(catalog_path)) #Отображаем имя выбранного каталога
		self.ui.lineEdit_3.setReadOnly(True) 
		self.ui.comboBox.addItems(get_Glasses(MyWin.SelectedCatalog)) #Заполняем список доступных по каталогу марок стекол 
		self.ui.comboBox.setEnabled(True)
		self.ui.groupBox_3.setEnabled(True)
		self.ui.pushButton_2.setEnabled(True)
			
	def calculate(self):
		#Получение введенных пользователем значений диаметра детали и алгебраической суммы колец
		Diameter = float(self.ui.lineEdit.text())
		Fringes = float(self.ui.lineEdit_2.text())
		#Запись выбранной пользователем марки стекла
		SelectedGlass = 'NM '+str(self.ui.comboBox.currentText())
		#Поиск местонахождения этой марки стекла в выбранном каталоге
		GlassPosition = get_GlassPosition(SelectedGlass, MyWin.SelectedCatalog)
		#Извлечение типа дисперсионной формулы и её коэффициентов
		DispCode = get_DispersionCode(GlassPosition, MyWin.SelectedCatalog)
		DispCoeffs = get_DispCoeffs(GlassPosition, MyWin.SelectedCatalog)
		#Запись выбранного пользователем значения длины волны
		Wave = (self.ui.comboBox_2.currentText()).split(' ')
		Wave = float(Wave[0])
		#Вычисление показателя преломления в зависимости от типа дисперсионной формулы стекла по каталогу
		if DispCode == 1:
			refIndex = schott(Wave, DispCoeffs[0], DispCoeffs[1], DispCoeffs[2], DispCoeffs[3], DispCoeffs[4], DispCoeffs[5])
		elif DispCode == 2:
			refIndex = sellmeier1(Wave, DispCoeffs[0], DispCoeffs[1], DispCoeffs[2], DispCoeffs[3], DispCoeffs[4], DispCoeffs[5])
		elif DispCode == 3:
			refIndex = herzberger(Wave, DispCoeffs[0], DispCoeffs[1], DispCoeffs[2], DispCoeffs[3], DispCoeffs[4], DispCoeffs[5])
		elif DispCode == 4:
			refIndex = sellmeier2(Wave, DispCoeffs[0], DispCoeffs[1], DispCoeffs[2], DispCoeffs[3], DispCoeffs[4])
		elif DispCode == 5:
			refIndex = conrady(Wave, DispCoeffs[0], DispCoeffs[1], DispCoeffs[2])
		elif DispCode == 6:
			refIndex = sellmeier3(Wave, DispCoeffs[0], DispCoeffs[1], DispCoeffs[2], DispCoeffs[3], DispCoeffs[4], DispCoeffs[5], DispCoeffs[6], DispCoeffs[7])
		elif DispCode == 7:
			refIndex = handbook1(Wave, DispCoeffs[0], DispCoeffs[1], DispCoeffs[2], DispCoeffs[3])		
		elif DispCode == 8:
			refIndex = handbook2(Wave, DispCoeffs[0], DispCoeffs[1], DispCoeffs[2], DispCoeffs[3])	
		elif DispCode == 9:
			refIndex = sellmeier4(Wave, DispCoeffs[0], DispCoeffs[1], DispCoeffs[2], DispCoeffs[3], DispCoeffs[4])	
		elif DispCode == 10:
			refIndex = extended(Wave, DispCoeffs[0], DispCoeffs[1], DispCoeffs[2], DispCoeffs[3], DispCoeffs[4], DispCoeffs[5], DispCoeffs[6], DispCoeffs[7])
		elif DispCode == 11:
			refIndex = sellmeier5(Wave, DispCoeffs[0], DispCoeffs[1], DispCoeffs[2], DispCoeffs[3], DispCoeffs[4], DispCoeffs[5], DispCoeffs[6], DispCoeffs[7], DispCoeffs[8], DispCoeffs[9])
		elif DispCode == 12:
			refIndex = extended2(Wave, DispCoeffs[0], DispCoeffs[1], DispCoeffs[2], DispCoeffs[3], DispCoeffs[4], DispCoeffs[5], DispCoeffs[6], DispCoeffs[7])				
		FocalLength = (1000*Diameter*Diameter)/(4*Wave*(refIndex-1)*Fringes)	
		#Вывод результата в поле Focal Length
		self.ui.lineEdit_4.setText(str("%.3f"%(FocalLength/1000)) + " m")

def main():
		app = QtWidgets.QApplication(sys.argv)
		window = MyWin()
		window.show()
		app.exec_()

if __name__=="__main__":
	main()