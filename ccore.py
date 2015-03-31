from PyQt4 import QtCore, QtGui
import sys,subprocess,os,configparser,signal

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

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, form):
        global status
        status = "Stopped"
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
        self.startbtn = QtGui.QPushButton(form)
        self.startbtn.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.startbtn.setObjectName(_fromUtf8("startbtn"))
        self.stopbtn = QtGui.QPushButton(form)
        self.stopbtn.setGeometry(QtCore.QRect(90, 170, 75, 23))
        self.stopbtn.setObjectName(_fromUtf8("stopbtn"))
        self.label_5 = QtGui.QLabel(form)
        self.label_5.setGeometry(QtCore.QRect(110, 130, 71, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line = QtGui.QFrame(form)
        self.line.setGeometry(QtCore.QRect(0, 150, 251, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.debugbtn = QtGui.QPushButton(form)
        self.debugbtn.setGeometry(QtCore.QRect(170, 170, 75, 23))
        self.debugbtn.setObjectName(_fromUtf8("debugbtn"))
        self.startbtn.clicked.connect(self.colorstart)
        self.stopbtn.clicked.connect(self.colorstop)
        #self.debugbtn.clicked.connect(self.parseconfig)


        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def colorstart(form):
        parseconfig(form)
        cmd = ""
        #runz(cmd)
        global p
        p = subprocess.Popen(['python', 'colorcore.py', 'server'], shell=False)
        global pid
        pid = p.pid
        form.label_5.setText(_translate("form", "Running", None))

    def colorstop(form):
        form.label_5.setText(_translate("form", "Stopped", None))
        p.terminate()
        print("killed %s"%pid)


    def retranslateUi(self, form):
        form.setWindowTitle(_translate("form", "CC RPC Server", None))
        self.label.setText(_translate("form", "ColorCore", None))
        self.port.setText(_translate("form", "51990", None))
        self.label_2.setText(_translate("form", "RPC User:", None))
        self.label_3.setText(_translate("form", "RPC Pass:", None))
        self.label_4.setText(_translate("form", "RPC Port:", None))
        self.startbtn.setText(_translate("form", "Start", None))
        self.stopbtn.setText(_translate("form", "Stop", None))
        self.label_5.setText(_translate("form", "Stopped", None))
        self.debugbtn.setText(_translate("form", "Debug", None))

#def runz(cmd):
    #p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #stdout = []
    #while True:
        #line = p.stdout.readline()
        #stdout.append(line)
        #print(line),
        #if line == '' and p.poll() != None:
            #break
    #return ''.join(stdout)

def parseconfig(form):
    config = configparser.ConfigParser()
    url = "http://%s:%s@dev.opal-coin.com:%s"%(form.user.text(),form.passw.text(),form.port.text())
    config.read('config.ini')
    config.set('opalcoind','rpcurl', url)
    configfile = open('config.ini', 'w')
    config.write(configfile)
    configfile.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    global ex
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())