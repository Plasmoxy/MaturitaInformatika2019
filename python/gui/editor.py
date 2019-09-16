#!/usr/bin/env python
# a minimal text editor to demo PyQt5

# GNU All-Permissive License
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.

import sys
import os
import pickle
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class TextEdit(QMainWindow):
    def __init__(self):
        super(TextEdit, self).__init__()
        #font = QFont("Courier", 11)
        #self.setFont(font)
        self.filename = False
        self.Ui()

    def Ui(self):
        quitApp = QAction(QIcon('/usr/share/icons/breeze-dark/actions/32/application-exit.svg'), 'Quit', self)
        saveFile = QAction(QIcon('/usr/share/icons/breeze-dark/actions/32/document-save.svg'), 'Save', self)
        newFile = QAction('New', self)
        openFile = QAction('Open', self)
        copyText = QAction('Copy', self)
        pasteText = QAction('Yank', self)
        newFile.setShortcut('Ctrl+N')
        newFile.triggered.connect(self.newFile)
        openFile.setShortcut('Ctrl+O')
        openFile.triggered.connect(self.openFile)
        saveFile.setShortcut('Ctrl+S')
        saveFile.triggered.connect(self.saveFile)
        quitApp.setShortcut('Ctrl+Q')
        quitApp.triggered.connect(self.close)
        copyText.setShortcut('Ctrl+K')
        copyText.triggered.connect(self.copyFunc)
        pasteText.setShortcut('Ctrl+Y')
        pasteText.triggered.connect(self.pasteFunc)
        menubar = self.menuBar()
        menubar.setNativeMenuBar(True)
        menuFile = menubar.addMenu('&File')
        menuFile.addAction(newFile)
        menuFile.addAction(openFile)
        menuFile.addAction(saveFile)
        menuFile.addAction(quitApp)
        menuEdit = menubar.addMenu('&Edit')
        menuEdit.addAction(copyText)
        menuEdit.addAction(pasteText)
        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(quitApp)
        toolbar.addAction(saveFile)
        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)
        self.setMenuWidget(menubar)
        self.setMenuBar(menubar)
        self.setGeometry(200,200,480,320)
        self.setWindowTitle('TextEdit')
        self.show()

    def copyFunc(self):
        self.text.copy()

    def pasteFunc(self):
        self.text.paste()

    def unSaved(self):
        destroy = self.text.document().isModified()
        print(destroy)

        if destroy == False:
            return False
        else:
            detour = QMessageBox.question(self,
                            "Hold your horses.",
                            "File has unsaved changes. Save now?",
                            QMessageBox.Yes|QMessageBox.No|
                            QMessageBox.Cancel)
            if detour == QMessageBox.Cancel:
                return True
            elif detour == QMessageBox.No:
                return False
            elif detour == QMessageBox.Yes:
                return self.saveFile()

        return True

    def saveFile(self):
        self.filename = QFileDialog.getSaveFileName(self, 'Save File', os.path.expanduser('~'))
        f = self.filename[0]
        with open(f, "w") as CurrentFile:
            CurrentFile.write(self.text.toPlainText() )
        CurrentFile.close()

    def newFile(self):
        if not self.unSaved():
            self.text.clear()

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", '', "All Files (*)")
        try:
            self.text.setText(open(filename).read())
        except:
            True

    def closeEvent(self, event):
        if self.unSaved():
            event.ignore()
        else:
            exit

def main():
    app = QApplication(sys.argv)
    editor = TextEdit()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()