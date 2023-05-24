# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.Widgets import (QCustomSlideMenu, QCustomStackedWidget)

class Ui_centralWidget(object):
    def setupUi(self, centralWidget):
        if not centralWidget.objectName():
            centralWidget.setObjectName(u"centralWidget")
        centralWidget.resize(1221, 745)
        centralWidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color:  #fff;\n"
"}\n"
"#centralWidget, #homeBtn, #mainBodyContent, QLineEdit{\n"
"	background-color: #1b1b27;\n"
"}\n"
"\n"
"#header, #mainBody, #footer{\n"
"	background-color: #27263c;\n"
"}\n"
"\n"
"#user{\n"
"	border: 1px sold #cc5bce;\n"
"	border-radius: 19px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"#adicionarBtn{\n"
"	background-color: #cc5bce;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#homeBtn{\n"
"	border-left: 3px solid #cc5bce;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	padding: 5px 10px;\n"
"	border-radus: 5px; \n"
"}")
        self.verticalLayout = QVBoxLayout(centralWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(centralWidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuBtn = QPushButton(self.frame_2)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn, 0, Qt.AlignLeft)

        self.lupalupaBtn = QLabel(self.frame_2)
        self.lupalupaBtn.setObjectName(u"lupalupaBtn")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lupalupaBtn.setFont(font)

        self.horizontalLayout_3.addWidget(self.lupalupaBtn)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"../icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.user = QPushButton(self.frame)
        self.user.setObjectName(u"user")
        self.user.setMinimumSize(QSize(38, 38))
        self.user.setMaximumSize(QSize(38, 38))
        self.user.setCursor(QCursor(Qt.PointingHandCursor))
        self.user.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"../icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.user.setIcon(icon4)
        self.user.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.user)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.mainBody = QWidget(centralWidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(1221, 615))
        self.horizontalLayout_2 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.mainBody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(200, 0))
        self.leftMenu.setMaximumSize(QSize(0, 16777215))
        self.leftMenu.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 595))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.frame_3)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn.setStyleSheet(u"background-color: #1b1b27;")
        icon5 = QIcon()
        icon5.addFile(u"../icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.homeBtn)

        self.relatorioBtn = QPushButton(self.frame_3)
        self.relatorioBtn.setObjectName(u"relatorioBtn")
        self.relatorioBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"../icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.relatorioBtn.setIcon(icon6)

        self.verticalLayout_5.addWidget(self.relatorioBtn)

        self.minhaContaBtn = QPushButton(self.frame_3)
        self.minhaContaBtn.setObjectName(u"minhaContaBtn")
        self.minhaContaBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minhaContaBtn.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.minhaContaBtn)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.configuracoesBtn = QPushButton(self.frame_4)
        self.configuracoesBtn.setObjectName(u"configuracoesBtn")
        self.configuracoesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"../icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.configuracoesBtn.setIcon(icon7)

        self.verticalLayout_6.addWidget(self.configuracoesBtn)

        self.ajudaBtn = QPushButton(self.frame_4)
        self.ajudaBtn.setObjectName(u"ajudaBtn")
        self.ajudaBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"../icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ajudaBtn.setIcon(icon8)

        self.verticalLayout_6.addWidget(self.ajudaBtn)

        self.sobreBtn = QPushButton(self.frame_4)
        self.sobreBtn.setObjectName(u"sobreBtn")
        self.sobreBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u"../icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sobreBtn.setIcon(icon9)

        self.verticalLayout_6.addWidget(self.sobreBtn)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_10 = QVBoxLayout(self.homePage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.homePage)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.widget_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamilies([u"Tibetan Machine Uni"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.label_5.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_5, 0, Qt.AlignLeft)

        self.showUserFormBtn = QPushButton(self.frame_6)
        self.showUserFormBtn.setObjectName(u"showUserFormBtn")
        font2 = QFont()
        font2.setBold(True)
        self.showUserFormBtn.setFont(font2)
        self.showUserFormBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u"../icons/plus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.showUserFormBtn.setIcon(icon10)
        self.showUserFormBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.showUserFormBtn, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.tableWidget = QTableWidget(self.widget_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_11.addWidget(self.tableWidget)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.mainPages.addWidget(self.homePage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.label_3 = QLabel(self.reportsPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(440, 230, 71, 111))
        self.label_3.setFont(font1)
        self.mainPages.addWidget(self.reportsPage)
        self.accountsPage = QWidget()
        self.accountsPage.setObjectName(u"accountsPage")
        self.label_7 = QLabel(self.accountsPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(430, 230, 91, 111))
        self.label_7.setFont(font1)
        self.mainPages.addWidget(self.accountsPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_4 = QLabel(self.settingsPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(430, 250, 81, 111))
        self.label_4.setFont(font1)
        self.mainPages.addWidget(self.settingsPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.label_6 = QLabel(self.helpPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(400, 200, 71, 111))
        self.label_6.setFont(font1)
        self.mainPages.addWidget(self.helpPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.label_8 = QLabel(self.aboutPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(440, 230, 71, 111))
        self.label_8.setFont(font1)
        self.mainPages.addWidget(self.aboutPage)

        self.verticalLayout_2.addWidget(self.mainPages)


        self.horizontalLayout_2.addWidget(self.mainBodyContent)

        self.rightMenu = QCustomSlideMenu(self.mainBody)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_7 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_2 = QWidget(self.rightMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(196, 191))
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 0))
        self.label_2.setMaximumSize(QSize(70, 70))
        self.label_2.setPixmap(QPixmap(u"../icons/edit.svg"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.autor = QLineEdit(self.frame_5)
        self.autor.setObjectName(u"autor")

        self.verticalLayout_9.addWidget(self.autor)

        self.destinatario = QLineEdit(self.frame_5)
        self.destinatario.setObjectName(u"destinatario")

        self.verticalLayout_9.addWidget(self.destinatario)

        self.local = QLineEdit(self.frame_5)
        self.local.setObjectName(u"local")

        self.verticalLayout_9.addWidget(self.local)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.adicionarBtn = QPushButton(self.widget_2)
        self.adicionarBtn.setObjectName(u"adicionarBtn")
        self.adicionarBtn.setFont(font2)
        self.adicionarBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u"../icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.adicionarBtn.setIcon(icon11)
        self.adicionarBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.adicionarBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.rightMenu)


        self.verticalLayout.addWidget(self.mainBody)

        self.footer = QWidget(centralWidget)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.footer)
        self.label_9.setObjectName(u"label_9")
        font3 = QFont()
        font3.setFamilies([u"Sans"])
        font3.setBold(True)
        self.label_9.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_9, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.footer)


        self.retranslateUi(centralWidget)

        QMetaObject.connectSlotsByName(centralWidget)
    # setupUi

    def retranslateUi(self, centralWidget):
        centralWidget.setWindowTitle(QCoreApplication.translate("centralWidget", u"Widget", None))
        self.menuBtn.setText("")
        self.lupalupaBtn.setText(QCoreApplication.translate("centralWidget", u"Lupa Lupa App", None))
        self.pushButton_4.setText("")
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.user.setText("")
        self.homeBtn.setText(QCoreApplication.translate("centralWidget", u"Home", None))
        self.relatorioBtn.setText(QCoreApplication.translate("centralWidget", u"Relat\u00f3rios", None))
        self.minhaContaBtn.setText(QCoreApplication.translate("centralWidget", u"Minha conta", None))
        self.configuracoesBtn.setText(QCoreApplication.translate("centralWidget", u"Configura\u00e7\u00f5es", None))
        self.ajudaBtn.setText(QCoreApplication.translate("centralWidget", u"Ajuda", None))
        self.sobreBtn.setText(QCoreApplication.translate("centralWidget", u"Sobre", None))
        self.label_5.setText(QCoreApplication.translate("centralWidget", u"Home", None))
        self.showUserFormBtn.setText(QCoreApplication.translate("centralWidget", u"Add novos Dados", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("centralWidget", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("centralWidget", u"Autor", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("centralWidget", u"Destinat\u00e1rio", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("centralWidget", u"Local", None));
        self.label_3.setText(QCoreApplication.translate("centralWidget", u"Reports", None))
        self.label_7.setText(QCoreApplication.translate("centralWidget", u"Accounts", None))
        self.label_4.setText(QCoreApplication.translate("centralWidget", u"Settings", None))
        self.label_6.setText(QCoreApplication.translate("centralWidget", u"Help", None))
        self.label_8.setText(QCoreApplication.translate("centralWidget", u"About", None))
        self.label_2.setText("")
        self.autor.setText(QCoreApplication.translate("centralWidget", u"Autor", None))
        self.autor.setPlaceholderText(QCoreApplication.translate("centralWidget", u"Username", None))
        self.destinatario.setText(QCoreApplication.translate("centralWidget", u"Destinat\u00e1rio", None))
        self.destinatario.setPlaceholderText(QCoreApplication.translate("centralWidget", u"Email", None))
        self.local.setText(QCoreApplication.translate("centralWidget", u"Local", None))
        self.local.setPlaceholderText(QCoreApplication.translate("centralWidget", u"Phone Number", None))
        self.adicionarBtn.setText(QCoreApplication.translate("centralWidget", u"Adicionar", None))
        self.label_9.setText(QCoreApplication.translate("centralWidget", u"Lupa Lupa App Tm - Copyright 2023", None))
    # retranslateUi

