import sys
from calculate import calculate
from math import pi
from math import sqrt

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *




import TrnglCalcApp_ui
import Preferences_ui

class Main(QMainWindow, TrnglCalcApp_ui.Ui_TrnglCalculatorApp):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.precision = 2
        self.degrees = 1
        self.setWindowIcon(QIcon('icons\\trngl.png'))
        self.CalcBtn.clicked.connect(self.calc_btn)
        self.actionPreferences.triggered.connect(self.openPref)
        self.calculated = False



    def resizeEvent(self, a0: QResizeEvent):
        if self.calculated:
            self.draw()

    def openPref(self):
        window = prefWindow(self)
        window.show()
        window.exec_()

    def calc_btn(self):
        self.calculated = True
        try:
            cb1 = self.comboBox_1.currentText()
            cb2 = self.comboBox_2.currentText()
            cb3 = self.comboBox_3.currentText()
            a = 0
            b = 0
            c = 0
            alpha = 0
            beta = 0
            gamma = 0

            if cb1 == "a":
                a = float(self.sideA.text())
            elif cb1 == "b":
                b = float(self.sideA.text())
            elif cb1 == "c":
                c = float(self.sideA.text())
            elif cb1 == "α":
                alpha = float(self.sideA.text())
            elif cb1 == "β":
                beta = float(self.sideA.text())
            elif cb1 == "ɣ":
                gamma = float(self.sideA.text())


            if cb2 == "a":
                a = float(self.sideB.text())
            elif cb2 == "b":
                b = float(self.sideB.text())
            elif cb2 == "c":
                c = float(self.sideB.text())
            elif cb2 == "α":
                alpha = float(self.sideB.text())
            elif cb2 == "β":
                beta = float(self.sideB.text())
            elif cb2 == "ɣ":
                gamma = float(self.sideB.text())


            if cb3 == "a":
                a = float(self.sideC.text())
            elif cb3 == "b":
                b = float(self.sideC.text())
            elif cb3 == "c":
                c = float(self.sideC.text())
            elif cb3 == "α":
                alpha = float(self.sideC.text())
            elif cb3 == "β":
                beta = float(self.sideC.text())
            elif cb3 == "ɣ":
                gamma = float(self.sideC.text())

            results = calculate(a, b, c, alpha, beta, gamma)

            self.Perimeter.setText("%.*f" % (self.precision, results[6]))
            self.Area.setText("%.*f" % (self.precision, results[7]))
            self.Radius.setText("%.*f" % (self.precision, results[8]))
            self.alpha.setText("%.*f" % (self.precision, results[3] * self.degrees))
            self.beta.setText("%.*f" % (self.precision, results[4] * self.degrees))
            self.gamma.setText("%.*f" % (self.precision, results[5] * self.degrees))
            self.lineEdit_a.setText("%.*f" % (self.precision, results[0]))
            self.lineEdit_b.setText("%.*f" % (self.precision, results[1]))
            self.lineEdit_c.setText("%.*f" % (self.precision, results[2]))

            self.a = results[0]
            self.b = results[1]
            self.c = results[2]
            self.R = results[8]
            print(self.a)
            print(self.b)
            print(self.c)
            print(self.R)
            self.draw()


        except:
            self.ErrorPopUp('Enter numbers')

    def ErrorPopUp(self, errorMsg = 'Error'):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(errorMsg)
        msg.setWindowTitle("Error")
        msg.exec_()

    def draw(self):
        self.coeff = 0.80 * self.graphicsView.height() / 2 / self.R
        self.canvas = QGraphicsScene(self)

        self.graphicsView.setScene(self.canvas)

        self.drawCircle(0, 0, 2 * self.R * self.coeff, 2 * self.R * self.coeff)

        x1 = (self.b ** 2 - 2 * self.R**2) / 2 / self.R * self.coeff
        y1 = 0

        if self.R ** 2 * self.coeff ** 2 - x1 ** 2 > 0:
            y1 = sqrt(self.R ** 2 * self.coeff ** 2 - x1 ** 2)
        self.drawLineB(0, self.R * self.coeff, x1 + self.R * self.coeff, -y1 + self.R * self.coeff)

        x2 = (self.c ** 2 - 2 * self.R ** 2) / 2 / self.R * self.coeff
        y2 = 0

        if self.R ** 2 * self.coeff ** 2 - x2 ** 2 > 0:
            y2 = sqrt(self.R ** 2 * self.coeff ** 2 - x2 ** 2)

        if self.b == self.c:
            y2 = -y2

        self.drawLineC(0, self.R * self.coeff, x2 + self.R * self.coeff, -y2 + self.R * self.coeff)
        self.drawLineA(x1 + self.R * self.coeff, -y1 + self.R * self.coeff, x2 + self.R * self.coeff, -y2 + self.R * self.coeff)

        self.graphicsView.show()

    def drawCircle(self, x, y, lx, ly):
        self.circle = QGraphicsEllipseItem(x, y, lx, ly)
        pen = QPen(QColor(50, 50, 50), 2, Qt.SolidLine)
        self.circle.setPen(pen)
        self.canvas.addItem(self.circle)

    def drawLineB(self, x1, y1, x2, y2):
        self.line_b = QGraphicsLineItem(x1, y1, x2, y2)
        pen = QPen(QColor(50, 50, 50), 2, Qt.SolidLine)
        self.line_b.setPen(pen)
        self.canvas.addItem(self.line_b)

    def drawLineA(self, x1, y1, x2, y2):
        self.line_a = QGraphicsLineItem(x1, y1, x2, y2)
        pen = QPen(QColor(50, 50, 50), 2, Qt.SolidLine)
        self.line_a.setPen(pen)
        self.canvas.addItem(self.line_a)

    def drawLineC(self, x1, y1, x2, y2):
        self.line_c = QGraphicsLineItem(x1, y1, x2, y2)
        pen = QPen(QColor(50, 50, 50), 2, Qt.SolidLine)
        self.line_c.setPen(pen)
        self.canvas.addItem(self.line_c)


class prefWindow(QDialog, Preferences_ui.Ui_Form):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setModal(True)
        self.pushButton.clicked.connect(self.onCancel)
        self.pushButton_2.clicked.connect(self.onSaveClose)
        self.parentDialog = parent
        self.spinBox.setValue(self.parentDialog.precision)
        if self.parentDialog.degrees == 1:
            self.radioButton.setChecked(True)
        else:
            self.radioButton_2.setChecked(True)

    def onCancel(self):
        self.close()

    def onSaveClose(self):
        value = int(self.spinBox.text())
        self.parentDialog.precision = value
        if self.radioButton_2.isChecked():
            self.parentDialog.degrees = 180 / pi
        else:
            self.parentDialog.degrees = 1
        self.close()



MainApp = QApplication(sys.argv)
TrnglCalcApp = Main()
TrnglCalcApp.show()
MainApp.exec_()
