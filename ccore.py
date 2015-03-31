from PyQt4 import QtCore, QtGui
import sys,subprocess,os,configparser

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class RPC_UI(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupRPC_UI(self)

    def setupRPC_UI(self, form):
        global status,stp
        status = "Stopped"
        stp = 1
        form.setObjectName(_fromUtf8("form"))
        form.resize(252, 198)
        self.label = QtGui.QLabel(form)
        self.label.setGeometry(QtCore.QRect(70, -20, 121, 71))
        self.label.setStyleSheet(_fromUtf8("font: 20pt \"MS Shell Dlg 2\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.user = QtGui.QLineEdit(form)
        self.user.setGeometry(QtCore.QRect(70, 50, 131, 20))
        self.user.setObjectName(_fromUtf8("user"))
        self.passw = QtGui.QLineEdit(form)
        self.passw.setGeometry(QtCore.QRect(70, 80, 131, 20))
        self.passw.setObjectName(_fromUtf8("pass"))
        self.port = QtGui.QLineEdit(form)
        self.port.setGeometry(QtCore.QRect(70, 110, 131, 20))
        self.port.setObjectName(_fromUtf8("port"))
        self.label_2 = QtGui.QLabel(form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(form)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(form)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.start_btn = QtGui.QPushButton(form)
        self.start_btn.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.start_btn.setObjectName(_fromUtf8("startbtn"))
        self.stop_btn = QtGui.QPushButton(form)
        self.stop_btn.setGeometry(QtCore.QRect(90, 170, 75, 23))
        self.stop_btn.setObjectName(_fromUtf8("stopbtn"))
        self.label_5 = QtGui.QLabel(form)
        self.label_5.setGeometry(QtCore.QRect(110, 130, 71, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line = QtGui.QFrame(form)
        self.line.setGeometry(QtCore.QRect(0, 150, 251, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.debug_btn = QtGui.QPushButton(form)
        self.debug_btn.setGeometry(QtCore.QRect(170, 170, 75, 23))
        self.debug_btn.setObjectName(_fromUtf8("debugbtn"))
        self.start_btn.clicked.connect(self.colorStart)
        self.stop_btn.clicked.connect(self.colorStop)
        self.debug_btn.clicked.connect(self.showConsole)


        self.rtUI(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def colorStart(form):
        global stp
        if stp == 1:
            parseConfig(form)
            global p
            p = subprocess.Popen(['python', 'colorcore.py', 'server'], shell=False)
            global pid
            pid = p.pid
            form.label_5.setText(_translate("form", "Running", None))
            li = QtGui.QListWidgetItem()
            li.setText("Starting RPC server on port %s..."%(lPort))
            ex2.listWidget.addItem(li)
            stp = 0
        else:
            print("Server Already Running on Port %s"%lPort)
            li = QtGui.QListWidgetItem()
            li.setText("Server Already Running on Port %s"%lPort)
            ex2.listWidget.addItem(li)

    def colorStop(form):
        global stp
        if stp != 1:
            form.label_5.setText(_translate("form", "Stopped", None))
            p.terminate()
            li = QtGui.QListWidgetItem()
            li.setText("killed Server Running on Port %s PID: %s"%(lPort,pid))
            ex2.listWidget.addItem(li)
            print("killed Server Running on Port %s PID: %s"%(lPort,pid))
            stp = 1
        else:
            print("No Process to Stop")
            li = QtGui.QListWidgetItem()
            li.setText("No Process to Stop")
            ex2.listWidget.addItem(li)

    def showConsole(form):
        ex2.show()

    def rtUI(self, form):
        form.setWindowTitle(_translate("form", "CC RPC Server", None))
        self.label.setText(_translate("form", "ColorCore", None))
        self.port.setText(_translate("form", "51990", None))
        self.label_2.setText(_translate("form", "RPC User:", None))
        self.label_3.setText(_translate("form", "RPC Pass:", None))
        self.label_4.setText(_translate("form", "RPC Port:", None))
        self.start_btn.setText(_translate("form", "Start", None))
        self.stop_btn.setText(_translate("form", "Stop", None))
        self.label_5.setText(_translate("form", "Stopped", None))
        self.debug_btn.setText(_translate("form", "Debug", None))


def parseConfig(form):
    config = configparser.ConfigParser()
    url = "http://%s:%s@dev.opal-coin.com:%s"%(form.user.text(),form.passw.text(),form.port.text())
    config.read('config.ini')
    config.set('opalcoind','rpcurl', url)
    configfile = open('config.ini', 'w')
    config.write(configfile)
    configfile.close()
    global lPort
    lPort = config.get("rpc","port")

class opForm(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupOP(self)

    def setupOP(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(280, 93)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.rtOPF(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def rtOPF(self, Form):
        Form.setWindowTitle(_translate("Form", "Output", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    global ex
    ex = RPC_UI()
    ex.show()
    global ex2
    ex2 = opForm()
    sys.exit(app.exec_())