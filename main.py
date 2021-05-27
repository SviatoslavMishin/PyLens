import sys
import os
import interface
import logic
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport

class AppWin(QtWidgets.QMainWindow):
    
    lens_kits = []

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = interface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit.setReadOnly(True)
        self.ui.pushButton_10.setEnabled(False)
        self.ui.pushButton_11.setEnabled(False)

        #Подключаем действия к кнопкам редактирования таблиц
        self.ui.pushButton.clicked.connect(self.add_row)
        self.ui.pushButton_2.clicked.connect(self.del_row)
        self.ui.pushButton_3.clicked.connect(self.clear_table)
        self.ui.pushButton_4.clicked.connect(self.add_row)
        self.ui.pushButton_5.clicked.connect(self.del_row)
        self.ui.pushButton_6.clicked.connect(self.clear_table)
        self.ui.pushButton_7.clicked.connect(self.add_row)
        self.ui.pushButton_8.clicked.connect(self.del_row)
        self.ui.pushButton_9.clicked.connect(self.clear_table)

        #Подключаем действие к кнопке "Скомплектовать"
        self.ui.pushButton_12.clicked.connect(self.make_kits)

        #Подключаем действие к кнопке "Сохранить"
        self.ui.pushButton_10.clicked.connect(self.save_result)

        #Подключаем действие к кнопке "Печать"
        self.ui.pushButton_11.clicked.connect(self.print_result)
       
    def add_row(self):
        row_count = 0
        sender = self.sender()
        sender_name = sender.objectName()
        if sender_name == 'pushButton':
            row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_count)
        elif sender_name == 'pushButton_4':
            row_count = self.ui.tableWidget_2.rowCount()
            self.ui.tableWidget_2.insertRow(row_count)
        elif sender_name == 'pushButton_7':
            row_count = self.ui.tableWidget_3.rowCount()
            self.ui.tableWidget_3.insertRow(row_count)
    
    def del_row(self):
        row_count = 0
        sender = self.sender()
        sender_name = sender.objectName()
        if sender_name == 'pushButton_2':
            row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(row_count-1)
        elif sender_name == 'pushButton_5':
            row_count = self.ui.tableWidget_2.rowCount()
            self.ui.tableWidget_2.setRowCount(row_count-1)
        elif sender_name == 'pushButton_8':
            row_count = self.ui.tableWidget_3.rowCount()
            self.ui.tableWidget_3.setRowCount(row_count-1)

    def clear_table(self):
        sender = self.sender()
        sender_name = sender.objectName()
        if sender_name == 'pushButton_3':
            self.ui.tableWidget.clearContents()
        elif sender_name == 'pushButton_6':
            self.ui.tableWidget_2.clearContents()
        elif sender_name == 'pushButton_9':
            self.ui.tableWidget_3.clearContents()

    def make_kits(self):
        #Берем данные о толщинах линз из таблиц
        parts_001 = []
        parts_103 = []
        parts_104 = []
        
        parts_001_count = self.ui.tableWidget.rowCount()
        parts_103_count = self.ui.tableWidget_2.rowCount()
        parts_104_count = self.ui.tableWidget_3.rowCount()
        for row in range(parts_001_count):
            
            if self.ui.tableWidget.item(row, 0) is None or self.ui.tableWidget.item(row, 0).text() == '': #Когда инициализировалась таблица - в ячейках None, а если просто туда не впечатали, то уже будет пустая строка
                error_msg = QtWidgets.QErrorMessage()
                error_msg.showMessage(
                    'Ошибка! Заполните все ячейки в таблице ' + self.ui.label.text())
                error_msg.exec_()
                return
            else:
                parts_001.append(float(self.ui.tableWidget.item(row, 0).text()))

        for row in range(parts_103_count):

            # Когда инициализировалась таблица - в ячейках None, а если просто туда не впечатали, то уже будет пустая строка
            if self.ui.tableWidget_2.item(row, 0) is None or self.ui.tableWidget_2.item(row, 0).text() == '':
                error_msg = QtWidgets.QErrorMessage()
                error_msg.showMessage(
                    'Ошибка! Заполните все ячейки в таблице ' + self.ui.label_2.text())
                error_msg.exec_()
                return
            else:
                parts_103.append(
                    float(self.ui.tableWidget_2.item(row, 0).text()))
        
        for row in range(parts_104_count):

            # Когда инициализировалась таблица - в ячейках None, а если просто туда не впечатали, то уже будет пустая строка
            if self.ui.tableWidget_3.item(row, 0) is None or self.ui.tableWidget_3.item(row, 0).text() == '':
                error_msg = QtWidgets.QErrorMessage()
                error_msg.showMessage(
                    'Ошибка! Заполните все ячейки в таблице ' + self.ui.label_3.text())
                error_msg.exec_()
                return
            else:
                parts_104.append(
                    float(self.ui.tableWidget_3.item(row, 0).text()))
       
        #Применяем к полученным спискам линз функцию kitmaker из файла logic.py
        #На выходе получим список комплектов линз - lens_kits
        AppWin.lens_kits = logic.kitmaker(parts_001, parts_103, parts_104)

        #Выведем результат
        for lens_kit in AppWin.lens_kits:
            self.ui.textEdit.append(str(lens_kit))

        #Делаем активными кнопки Сохранить и Печать
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_11.setEnabled(True)

    def print_result(self):
        print_dialog = QtPrintSupport.QPrintDialog()
        if print_dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.ui.textEdit.document().print_(print_dialog.printer())
         

    def save_result(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(filter='*.txt')[0]
        with open(file_name, 'w') as f:
            for lens_kit in AppWin.lens_kits:
                f.write("%s\n" % lens_kit)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AppWin()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()


        
