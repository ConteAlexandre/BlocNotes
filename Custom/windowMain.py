# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'blocnotes.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_BlocNotes(object):
    def setupUi(self, BlocNotes):
        if BlocNotes.objectName():
            BlocNotes.setObjectName(u"BlocNotes")
        BlocNotes.resize(932, 699)
        self.gridLayout = QGridLayout(BlocNotes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_deleteNote = QPushButton(BlocNotes)
        self.btn_deleteNote.setObjectName(u"btn_deleteNote")

        self.gridLayout.addWidget(self.btn_deleteNote, 4, 0, 1, 1)

        self.btn_updateNote = QPushButton(BlocNotes)
        self.btn_updateNote.setObjectName(u"btn_updateNote")

        self.gridLayout.addWidget(self.btn_updateNote, 4, 1, 1, 1)

        self.te_contentNote = QTextEdit(BlocNotes)
        self.te_contentNote.setObjectName(u"te_contentNote")

        self.gridLayout.addWidget(self.te_contentNote, 0, 1, 4, 1)

        self.btn_createdNote = QPushButton(BlocNotes)
        self.btn_createdNote.setObjectName(u"btn_createdNote")

        self.gridLayout.addWidget(self.btn_createdNote, 0, 0, 1, 1)

        self.lw_listNote = QListWidget(BlocNotes)
        self.lw_listNote.setObjectName(u"lw_listNote")

        self.gridLayout.addWidget(self.lw_listNote, 1, 0, 3, 1)


        self.retranslateUi(BlocNotes)

        QMetaObject.connectSlotsByName(BlocNotes)
    # setupUi

    def retranslateUi(self, BlocNotes):
        BlocNotes.setWindowTitle(QCoreApplication.translate("BlocNotes", u"BlocNotes", None))
        self.btn_deleteNote.setText(QCoreApplication.translate("BlocNotes", u"Delete", None))
        self.btn_updateNote.setText(QCoreApplication.translate("BlocNotes", u"Update", None))
        self.btn_createdNote.setText(QCoreApplication.translate("BlocNotes", u"Create", None))
    # retranslateUi

