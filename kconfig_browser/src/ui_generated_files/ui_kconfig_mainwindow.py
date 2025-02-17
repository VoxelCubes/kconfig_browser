# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kconfig_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow_kconf(object):
    def setupUi(self, MainWindow_kconf):
        if not MainWindow_kconf.objectName():
            MainWindow_kconf.setObjectName(u"MainWindow_kconf")
        MainWindow_kconf.resize(800, 600)
        icon = QIcon()
        iconThemeName = u"settings-configure"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        MainWindow_kconf.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow_kconf)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(6)
        self.splitter.setChildrenCollapsible(False)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.left_panel = QVBoxLayout(self.verticalLayoutWidget)
        self.left_panel.setObjectName(u"left_panel")
        self.left_panel.setContentsMargins(0, 0, 0, 0)
        self.comboBox_config_files = QComboBox(self.verticalLayoutWidget)
        self.comboBox_config_files.setObjectName(u"comboBox_config_files")

        self.left_panel.addWidget(self.comboBox_config_files)

        self.listWidget_groups = QListWidget(self.verticalLayoutWidget)
        self.listWidget_groups.setObjectName(u"listWidget_groups")

        self.left_panel.addWidget(self.listWidget_groups)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_reload = QPushButton(self.verticalLayoutWidget)
        self.pushButton_reload.setObjectName(u"pushButton_reload")
        self.pushButton_reload.setEnabled(False)
        icon1 = QIcon()
        iconThemeName = u"view-refresh"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.pushButton_reload.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButton_reload)

        self.pushButton_save = QPushButton(self.verticalLayoutWidget)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setEnabled(False)
        icon2 = QIcon()
        iconThemeName = u"document-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.pushButton_save.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pushButton_save)


        self.left_panel.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.right_panel = QVBoxLayout(self.verticalLayoutWidget_2)
        self.right_panel.setObjectName(u"right_panel")
        self.right_panel.setContentsMargins(0, 0, 0, 0)
        self.listWidget_keys = QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_keys.setObjectName(u"listWidget_keys")

        self.right_panel.addWidget(self.listWidget_keys)

        self.lineEdit_value = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_value.setObjectName(u"lineEdit_value")
        self.lineEdit_value.setEnabled(False)

        self.right_panel.addWidget(self.lineEdit_value)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.verticalLayout_3.addWidget(self.splitter)

        MainWindow_kconf.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow_kconf)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow_kconf.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_kconf)

        QMetaObject.connectSlotsByName(MainWindow_kconf)
    # setupUi

    def retranslateUi(self, MainWindow_kconf):
        MainWindow_kconf.setWindowTitle(QCoreApplication.translate("MainWindow_kconf", u"KConfig Browser", None))
        self.pushButton_reload.setText(QCoreApplication.translate("MainWindow_kconf", u"Reload", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow_kconf", u"Save", None))
        self.lineEdit_value.setPlaceholderText(QCoreApplication.translate("MainWindow_kconf", u"Key value...", None))
    # retranslateUi

