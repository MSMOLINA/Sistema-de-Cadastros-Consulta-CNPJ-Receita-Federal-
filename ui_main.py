# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(767, 480)
        font = QFont()
        font.setFamilies([u"Agency FB"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255,255,255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(0, 16777215))
        self.left_menu.setCursor(QCursor(Qt.SplitVCursor))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, 0, -1)
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 9)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(65,65,65);\n"
"}\n"
"\n"
"QToolBox{\n"
"	text-align: left;\n"
"	background-color: rgb(228,254,255);\n"
"}\n"
"\n"
"QToolBox::Tab{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(194,232,255);\n"
"	text-align: left;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(65,65,65);\n"
"	border-top-left-radius: 15px\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 63, 342))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.btn_contatos = QPushButton(self.page)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(0, 30))
        self.btn_contatos.setFont(font1)
        self.btn_contatos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setFont(font1)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 16, 342))
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 161, 321))
        self.label_4.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.toolBox.addItem(self.page_2, u"Informa\u00e7\u00f5es")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icones/ico_menu_suspenso.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background-color: rgb(62,62,62);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_7 = QVBoxLayout(self.pg_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")

        self.verticalLayout_7.addWidget(self.logo)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_8 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(231,231,231);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_origem_api = QLabel(self.frame_4)
        self.lbl_origem_api.setObjectName(u"lbl_origem_api")
        self.lbl_origem_api.setStyleSheet(u"color: rgb(0,99,148);\n"
"background-color: rgb(249,249,249);")

        self.gridLayout.addWidget(self.lbl_origem_api, 1, 0, 1, 4)

        self.txt_sistema = QLineEdit(self.frame_4)
        self.txt_sistema.setObjectName(u"txt_sistema")
        self.txt_sistema.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_sistema, 8, 1, 1, 1)

        self.txt_resp_cargo = QLineEdit(self.frame_4)
        self.txt_resp_cargo.setObjectName(u"txt_resp_cargo")
        self.txt_resp_cargo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_resp_cargo, 11, 3, 1, 1)

        self.txt_uf = QLineEdit(self.frame_4)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_uf, 5, 1, 1, 1)

        self.txt_Num_Cont = QLineEdit(self.frame_4)
        self.txt_Num_Cont.setObjectName(u"txt_Num_Cont")
        self.txt_Num_Cont.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_Num_Cont, 8, 0, 1, 1)

        self.txt_cnpj = QLineEdit(self.frame_4)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        self.txt_cnpj.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cnpj, 2, 0, 1, 1)

        self.txt_email = QLineEdit(self.frame_4)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_email, 6, 0, 1, 4)

        self.txt_telefone = QLineEdit(self.frame_4)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone, 5, 3, 1, 1)

        self.lbl_preencher_dados = QLabel(self.frame_4)
        self.lbl_preencher_dados.setObjectName(u"lbl_preencher_dados")
        self.lbl_preencher_dados.setStyleSheet(u"color: rgb(0,99,148);\n"
"background-color: rgb(249,249,249);")

        self.gridLayout.addWidget(self.lbl_preencher_dados, 7, 0, 1, 4)

        self.txt_logradouro = QLineEdit(self.frame_4)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_logradouro, 3, 0, 1, 4)

        self.txt_tel_resp_cons = QLineEdit(self.frame_4)
        self.txt_tel_resp_cons.setObjectName(u"txt_tel_resp_cons")
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dig 2"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.txt_tel_resp_cons.setFont(font2)
        self.txt_tel_resp_cons.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_tel_resp_cons, 11, 2, 1, 1)

        self.txt_nome = QLineEdit(self.frame_4)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 2, 1, 1, 3)

        self.txt_complemento = QLineEdit(self.frame_4)
        self.txt_complemento.setObjectName(u"txt_complemento")

        self.gridLayout.addWidget(self.txt_complemento, 4, 1, 1, 2)

        self.txt_numero = QLineEdit(self.frame_4)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_numero, 4, 0, 1, 1)

        self.txt_municipio = QLineEdit(self.frame_4)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio, 5, 0, 1, 1)

        self.txt_hs_contrato = QLineEdit(self.frame_4)
        self.txt_hs_contrato.setObjectName(u"txt_hs_contrato")

        self.gridLayout.addWidget(self.txt_hs_contrato, 8, 2, 1, 1)

        self.txt_tp_assistencia = QLineEdit(self.frame_4)
        self.txt_tp_assistencia.setObjectName(u"txt_tp_assistencia")
        self.txt_tp_assistencia.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_tp_assistencia, 8, 3, 1, 1)

        self.txt_bairro = QLineEdit(self.frame_4)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro, 4, 3, 1, 1)

        self.lbl_empresas = QLabel(self.frame_4)
        self.lbl_empresas.setObjectName(u"lbl_empresas")
        self.lbl_empresas.setStyleSheet(u"color: rgb(0,99,148);\n"
"background-color: rgb(249,249,249);")
        self.lbl_empresas.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.lbl_empresas, 0, 0, 1, 4)

        self.txt_cep = QLineEdit(self.frame_4)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep, 5, 2, 1, 1)

        self.txt_inicio_contrato = QLineEdit(self.frame_4)
        self.txt_inicio_contrato.setObjectName(u"txt_inicio_contrato")
        self.txt_inicio_contrato.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_inicio_contrato, 9, 0, 1, 1)

        self.txt_fim_contrato_2 = QLineEdit(self.frame_4)
        self.txt_fim_contrato_2.setObjectName(u"txt_fim_contrato_2")
        self.txt_fim_contrato_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_fim_contrato_2, 9, 1, 1, 1)

        self.txt_resp_cons = QLineEdit(self.frame_4)
        self.txt_resp_cons.setObjectName(u"txt_resp_cons")
        self.txt_resp_cons.setFont(font2)
        self.txt_resp_cons.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_resp_cons, 9, 2, 1, 2)

        self.txt_resp_email_cons = QLineEdit(self.frame_4)
        self.txt_resp_email_cons.setObjectName(u"txt_resp_email_cons")
        self.txt_resp_email_cons.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_resp_email_cons, 11, 0, 1, 2)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(160, 30))
        font3 = QFont()
        font3.setPointSize(12)
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0,170,255);\n"
"	border-radius: 15px;\n"
"	color: afff\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243,243,243);\n"
"}")

        self.verticalLayout_11.addWidget(self.pushButton_5, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.title_empresa = QLabel(self.tab_2)
        self.title_empresa.setObjectName(u"title_empresa")
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(24)
        font4.setBold(True)
        self.title_empresa.setFont(font4)
        self.title_empresa.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.title_empresa.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.title_empresa)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tb_company = QTableWidget(self.tab_2)
        if (self.tb_company.columnCount() < 21):
            self.tb_company.setColumnCount(21)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        self.tb_company.setObjectName(u"tb_company")
        self.tb_company.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148,148,148);\n"
"	color: rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252,252,252);\n"
"}")

        self.horizontalLayout_5.addWidget(self.tb_company)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,255,255);\n"
"	font: 11pt \"MS Shell Dig 2\";\n"
"	color: rgb(0,24,74);\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(230,230,230);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_excel = QPushButton(self.frame_3)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(120, 30))
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(49,147,0);\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(120, 30))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(255,170,0);\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(120, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(199,66,0);\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_12 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_5 = QLabel(self.pg_contatos)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_12.addWidget(self.label_5)

        self.lbl_whatsapp = QLabel(self.pg_contatos)
        self.lbl_whatsapp.setObjectName(u"lbl_whatsapp")

        self.verticalLayout_12.addWidget(self.lbl_whatsapp)

        self.lbl_fazebook = QLabel(self.pg_contatos)
        self.lbl_fazebook.setObjectName(u"lbl_fazebook")

        self.verticalLayout_12.addWidget(self.lbl_fazebook)

        self.lbl_instagram = QLabel(self.pg_contatos)
        self.lbl_instagram.setObjectName(u"lbl_instagram")

        self.verticalLayout_12.addWidget(self.lbl_instagram)

        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_6 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_sobre = QLabel(self.pg_sobre)
        self.lbl_sobre.setObjectName(u"lbl_sobre")
        font5 = QFont()
        font5.setBold(True)
        self.lbl_sobre.setFont(font5)
        self.lbl_sobre.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lbl_sobre)

        self.lbl_objetivo = QLabel(self.pg_sobre)
        self.lbl_objetivo.setObjectName(u"lbl_objetivo")
        self.lbl_objetivo.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.lbl_objetivo)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.foote_frame = QFrame(self.main_container)
        self.foote_frame.setObjectName(u"foote_frame")
        self.foote_frame.setFrameShape(QFrame.StyledPanel)
        self.foote_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.foote_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, -1, 0)
        self.label_2 = QLabel(self.foote_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.foote_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MMDESENVOLVIMENTO", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Usu\u00e1rio:</span> MMDESENVOLVIMENTO</p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Sistema:</span> Cadastro</p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Status</span>: Ativo</p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Venc:</span> 12/12/9999</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Sistema de Cadastro </span></p></body></html>", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icones/python.png\"/></p></body></html>", None))
        self.lbl_origem_api.setText(QCoreApplication.translate("MainWindow", u"Campos Origem API:", None))
        self.txt_sistema.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sistema", None))
        self.txt_resp_cargo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_Num_Cont.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero do Contrato", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.lbl_preencher_dados.setText(QCoreApplication.translate("MainWindow", u"Preencher Dados:", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_tel_resp_cons.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone Respons\u00e1vel Consultoria", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Empresarial", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.txt_hs_contrato.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Horas Contratada", None))
        self.txt_tp_assistencia.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo Assist\u00eancia", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.lbl_empresas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">EMPRESAS</span></p></body></html>", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_inicio_contrato.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data In\u00edcio Contrato", None))
        self.txt_fim_contrato_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Fim Contrato", None))
        self.txt_resp_cons.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Respons\u00e1vel Consultoria", None))
        self.txt_resp_email_cons.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail Respons\u00e1vel Consultoria", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.title_empresa.setText(QCoreApplication.translate("MainWindow", u"Empresas", None))
        ___qtablewidgetitem = self.tb_company.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tb_company.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tb_company.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tb_company.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None));
        ___qtablewidgetitem4 = self.tb_company.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.tb_company.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tb_company.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None));
        ___qtablewidgetitem7 = self.tb_company.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.tb_company.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.tb_company.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.tb_company.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem11 = self.tb_company.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"CONTRATO", None));
        ___qtablewidgetitem12 = self.tb_company.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"SISTEMA", None));
        ___qtablewidgetitem13 = self.tb_company.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"HS CONTRATADA", None));
        ___qtablewidgetitem14 = self.tb_company.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"TP ASSIST\u00caNCIA", None));
        ___qtablewidgetitem15 = self.tb_company.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"IN\u00cdCIO CONTRATO", None));
        ___qtablewidgetitem16 = self.tb_company.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"FIM CONTRATO", None));
        ___qtablewidgetitem17 = self.tb_company.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"RESP. CONSULTORIA", None));
        ___qtablewidgetitem18 = self.tb_company.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"EMAIL RESPONS\u00c1VEL CONS", None));
        ___qtablewidgetitem19 = self.tb_company.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"TEL RESP CONSULTORIA", None));
        ___qtablewidgetitem20 = self.tb_company.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"CARGO RESP CONSULTORIA", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">CONTATOS</span></p></body></html>", None))
        self.lbl_whatsapp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icones/ico_whatspp.png\"/><span style=\" font-size:18pt; vertical-align:super;\"/></p></body></html>", None))
        self.lbl_fazebook.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icones/ico_facebook.png\"/></p></body></html>", None))
        self.lbl_instagram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icones/ico_instagram.png\"/></p></body></html>", None))
        self.lbl_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Sobre</span></p></body></html>", None))
        self.lbl_objetivo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Este sistema faz consulta na base da Receita Federal atrav\u00e9s do CNPJ utilizando a API da Receita e possibilita cadastrar consultoria e registrar tempo de contrato via presta\u00e7\u00e3o de Servi\u00e7o.</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MMDESENVOLVIMENTO", None))
    # retranslateUi
    

