# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 16:50:58 2019

@author: user
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import sqlite3
import numpy as np
import matplotlib.pyplot as plt



class Ui_MainWindow(object):
    
    def Main_Window(self, MainWindow):
        ##### 主視窗 #####
        MainWindow.resize(200, 213)
        self.flag = ''
        self.font_size()
        self.home_page_object()
        
##############主頁#############################################################
    def home_page_object(self):
        self.homepage = QtWidgets.QWidget(MainWindow)
        self.homepage.resize(200, 200)
        self.title = QtWidgets.QLabel('採收賣出管理',self.homepage)
        self.title.setFont(QtGui.QFont("微軟正黑體",48))
        
        ###主頁按鈕區###    
        self.enterdata_button = QtWidgets.QPushButton('輸入',self.homepage)
        self.enterdata_button.setMinimumSize(QtCore.QSize(250, 250))
        self.enterdata_button.setFont(self.font_32)
        self.enterdata_button.setObjectName('enterdata_button')
        
        self.revisedata_button = QtWidgets.QPushButton('修改',self.homepage)
        self.revisedata_button.setMinimumSize(QtCore.QSize(250, 250))
        self.revisedata_button.setFont(self.font_32)
        self.revisedata_button.setObjectName('revisedata_button')

        
        self.checkdata_button = QtWidgets.QPushButton('查看',self.homepage)
        self.checkdata_button.setMinimumSize(QtCore.QSize(250, 250))
        self.checkdata_button.setFont(self.font_32)
        self.checkdata_button.setObjectName('checkdata_button')

        
        self.statistics_button = QtWidgets.QPushButton('統計\n資料',self.homepage)
        self.statistics_button.setMinimumSize(QtCore.QSize(250, 250))
        self.statistics_button.setFont(self.font_32)
        self.statistics_button.setObjectName('statistics_button')


        
        ###主頁排版###
        self.homepage_horizontalLayout = QtWidgets.QHBoxLayout(self.homepage)
        self.homepage_gridLayout = QtWidgets.QGridLayout(self.homepage)
        self.homepage_gridLayout.addWidget(self.title, 0, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.homepage_gridLayout.addWidget(self.enterdata_button, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.homepage_gridLayout.addWidget(self.revisedata_button, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.homepage_gridLayout.addWidget(self.checkdata_button, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.homepage_gridLayout.addWidget(self.statistics_button, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.homepage_horizontalLayout.addLayout(self.homepage_gridLayout)
        MainWindow.setCentralWidget(self.homepage)

        ###按鈕連接###
        self.enterdata_button.clicked.connect(self.home_connection_page)
        self.revisedata_button.clicked.connect(self.home_connection_page)
        self.checkdata_button.clicked.connect(self.home_connection_page)
        self.statistics_button.clicked.connect(self.home_connection_page)
    
    
############輸入頁面###########################################################
    def enter_page_object(self):
        self.flag = 'enter'
        self.enterpage = QtWidgets.QWidget(MainWindow)
        self.enterpage.resize(200, 200)

        
        ###品項###
        self.enter_item = QtWidgets.QLabel('品項',self.enterpage)
        self.enter_item.setMinimumSize(QtCore.QSize(140, 200))
        self.enter_item.setMaximumSize(QtCore.QSize(140, 200))
        self.enter_item.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_item.setFont(self.font_24)
        self.item_edit = QtWidgets.QLineEdit(self.enterpage)
        self.item_edit.setMinimumSize(QtCore.QSize(300, 110))
        self.item_edit.setMaximumSize(QtCore.QSize(300, 110))
        self.item_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.item_edit.setFont(self.font_22)

        
        ###日期###
        self.enter_date = QtWidgets.QLabel('日期',self.enterpage)
        self.enter_date.setMinimumSize(QtCore.QSize(140, 200))
        self.enter_date.setMaximumSize(QtCore.QSize(140, 200))        
        self.enter_date.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_date.setFont(self.font_24)
        self.enter_date_text = QtWidgets.QLineEdit(self.enterpage)
        self.enter_date_text.setText(time.strftime("%Y/%m/%d", time.localtime()))
        self.enter_date_text.setReadOnly(True)
        self.enter_date_text.setMinimumSize(QtCore.QSize(400, 110))
        self.enter_date_text.setMaximumSize(QtCore.QSize(400, 110))
        self.enter_date_text.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_date_text.setFont(self.font_22)
        self.enter_date_select = QtWidgets.QPushButton(self.enterpage)
        self.enter_date_select.setStyleSheet('QPushButton{border-image:url(calendar.png)}')
        self.enter_date_select.setMinimumSize(QtCore.QSize(50, 50))
        self.enter_date_select.setMaximumSize(QtCore.QSize(50, 50))
        
        
        
        
        
        
        ###採收###
        self.enter_harvest = QtWidgets.QLabel('採收',self.enterpage)
        self.enter_harvest.setMinimumSize(QtCore.QSize(140, 200))
        self.enter_harvest.setMaximumSize(QtCore.QSize(140, 200))        
        self.enter_harvest.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_harvest.setFont(self.font_24)
        self.harvest_edit = QtWidgets.QLineEdit(self.enterpage)
        self.harvest_edit.setMinimumSize(QtCore.QSize(180, 110))
        self.harvest_edit.setMaximumSize(QtCore.QSize(180, 110))
        self.harvest_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.harvest_edit.setFont(self.font_22)
        self.harvest_tkg = QtWidgets.QLabel('斤',self.enterpage)
        self.harvest_tkg.setMinimumSize(QtCore.QSize(50, 100))
        self.harvest_tkg.setFont(self.font_22)

        
        ###網路銷售###
        self.enter_online_sales = QtWidgets.QLabel('網路\n銷售',self.enterpage)
        self.enter_online_sales.setMinimumSize(QtCore.QSize(140, 200))        
        self.enter_online_sales.setMaximumSize(QtCore.QSize(140, 200))
        self.enter_online_sales.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_online_sales.setFont(self.font_24)
        self.online_sales_edit = QtWidgets.QLineEdit(self.enterpage)
        self.online_sales_edit.setMinimumSize(QtCore.QSize(180, 110))        
        self.online_sales_edit.setMaximumSize(QtCore.QSize(180,110))
        self.online_sales_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.online_sales_edit.setFont(self.font_22)
        self.online_sales_tkg = QtWidgets.QLabel('斤',self.enterpage)
        self.online_sales_tkg.setMinimumSize(QtCore.QSize(50, 100))
        self.online_sales_tkg.setFont(self.font_22)
        self.online_sales_price = QtWidgets.QLabel('網路\n單價',self.enterpage)
        self.online_sales_price.setMinimumSize(QtCore.QSize(140, 200))
        self.online_sales_price.setMaximumSize(QtCore.QSize(140, 200))
        self.online_sales_price.setAlignment(QtCore.Qt.AlignCenter)
        self.online_sales_price.setFont(self.font_24)
        self.online_sales_price_edit = QtWidgets.QLineEdit(self.enterpage)
        self.online_sales_price_edit.setMinimumSize(QtCore.QSize(180, 110))
        self.online_sales_price_edit.setMaximumSize(QtCore.QSize(180, 110))
        self.online_sales_price_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.online_sales_price_edit.setFont(self.font_22)

        
        ###市場銷售###
        self.enter_market_sales = QtWidgets.QLabel('市場\n銷售',self.enterpage)
        self.enter_market_sales.setMinimumSize(QtCore.QSize(140, 200))
        self.enter_market_sales.setMaximumSize(QtCore.QSize(140, 200))
        self.enter_market_sales.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_market_sales.setFont(self.font_24)
        self.market_sales_edit = QtWidgets.QLineEdit(self.enterpage)
        self.market_sales_edit.setMinimumSize(QtCore.QSize(180, 110))
        self.market_sales_edit.setMaximumSize(QtCore.QSize(180, 110))
        self.market_sales_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.market_sales_edit.setFont(self.font_22)
        self.market_sales_tkg = QtWidgets.QLabel('斤',self.enterpage)
        self.market_sales_tkg.setMinimumSize(QtCore.QSize(50, 100))
        self.market_sales_tkg.setFont(self.font_22)
        self.market_sales_price = QtWidgets.QLabel('市場\n單價',self.enterpage)
        self.market_sales_price.setMinimumSize(QtCore.QSize(140, 200))
        self.market_sales_price.setMaximumSize(QtCore.QSize(140, 200))
        self.market_sales_price.setAlignment(QtCore.Qt.AlignCenter)
        self.market_sales_price.setFont(self.font_24)
        self.market_sales_price_edit = QtWidgets.QLineEdit(self.enterpage)
        self.market_sales_price_edit.setMinimumSize(QtCore.QSize(180, 110))
        self.market_sales_price_edit.setMaximumSize(QtCore.QSize(180, 110))
        self.market_sales_price_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.market_sales_price_edit.setFont(self.font_22)

        
        ###收入###
        self.enter_income = QtWidgets.QLabel('收入',self.enterpage)
        self.enter_income.setMinimumSize(QtCore.QSize(140, 150))
        self.enter_income.setMaximumSize(QtCore.QSize(140, 150))
        self.enter_income.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_income.setFont(self.font_24)
        self.income_edit = QtWidgets.QLineEdit(self.enterpage)
        self.income_edit.setReadOnly(True)
        self.income_edit.setMinimumSize(QtCore.QSize(250, 110))
        self.income_edit.setMaximumSize(QtCore.QSize(250,110))
        self.income_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.income_edit.setFont(self.font_22)

        

        ###返回###
        self.backhome_enter_button = QtWidgets.QPushButton('返回',self.enterpage)
        self.backhome_enter_button.setMaximumSize(QtCore.QSize(180,130))
        self.backhome_enter_button.setFont(self.font_24)


        ###儲存###
        self.savedata_button = QtWidgets.QPushButton('儲存',self.enterpage)
        self.savedata_button.setMaximumSize(QtCore.QSize(180,130))
        self.savedata_button.setFont(self.font_24)

       
        ###輸入區排版###
        self.enterpage_horizontalLayout = QtWidgets.QHBoxLayout(self.enterpage)
        self.enterpage_gridLayout = QtWidgets.QGridLayout()

        self.enterpage_gridLayout.addWidget(self.enter_item, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.item_edit, 0, 1, 1, 2)
        
        self.enterpage_gridLayout.addWidget(self.enter_date, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.enter_date_text, 1, 1, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.enter_date_select, 1, 3, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        
        self.enterpage_gridLayout.addWidget(self.enter_harvest, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.harvest_edit, 2, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.harvest_tkg, 2, 2, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        
        self.enterpage_gridLayout.addWidget(self.enter_online_sales, 3, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.online_sales_edit, 3, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.online_sales_tkg, 3, 2, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.online_sales_price, 3, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.online_sales_price_edit, 3, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.enterpage_gridLayout.addWidget(self.enter_market_sales, 4, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.market_sales_edit, 4, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.market_sales_tkg, 4, 2, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.market_sales_price, 4, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.market_sales_price_edit, 4, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.enterpage_gridLayout.addWidget(self.enter_income, 5, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.income_edit, 5, 1, 1, 2)
        
        self.enterpage_gridLayout.addWidget(self.backhome_enter_button, 6, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.savedata_button, 6, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.enterpage_horizontalLayout.addLayout(self.enterpage_gridLayout)
        MainWindow.setCentralWidget(self.enterpage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.sales_calculation()
        ###按鈕連結###
        self.enter_date_select.clicked.connect(self.show_calendar)
        self.backhome_enter_button.clicked.connect(self.back_home_page)
        self.savedata_button.clicked.connect(self.sqlite_add_change)
        
        
############修改頁面############################################################
    def revise_page_object(self):
        self.flag = 'revise'
        self.revisepage = QtWidgets.QWidget(MainWindow)
        self.revisepage.resize(200, 200)
        conn = sqlite3.connect('salesdata.sqlite')
        
        ###品項###
        self.revise_item = QtWidgets.QLabel('品項',self.revisepage)
        self.revise_item.setMinimumSize(QtCore.QSize(140, 200))
        self.revise_item.setMaximumSize(QtCore.QSize(140, 200))
        self.revise_item.setAlignment(QtCore.Qt.AlignCenter)
        self.revise_item.setFont(self.font_24)
        self.revise_item_comboBox = QtWidgets.QComboBox(self.revisepage)
        self.revise_item_comboBox.addItems([item[0] for item in conn.execute("select name from sqlite_master where type = 'table';")])
        self.revise_item_comboBox.resize(300, 100)
        self.revise_item_comboBox.setMaximumSize(QtCore.QSize(300, 100))
        self.revise_item_comboBox.setFont(self.font_22)
            
        ###日期###
        self.revise_date = QtWidgets.QLabel('日期',self.revisepage)
        self.revise_date.setMinimumSize(QtCore.QSize(140, 200))
        self.revise_date.setMaximumSize(QtCore.QSize(140, 200))        
        self.revise_date.setAlignment(QtCore.Qt.AlignCenter)
        self.revise_date.setFont(self.font_24)
        self.revise_date_text = QtWidgets.QLineEdit(self.revisepage)
        self.revise_date_text.setText(time.strftime("%Y/%m/%d", time.localtime()))
        self.revise_date_text.setMinimumSize(QtCore.QSize(400, 110))
        self.revise_date_text.setMaximumSize(QtCore.QSize(400, 110))
        self.revise_date_text.setAlignment(QtCore.Qt.AlignCenter)
        self.revise_date_text.setFont(self.font_22)
        self.revise_date_text.setReadOnly(True)
        self.revise_date_select = QtWidgets.QPushButton(self.revisepage)
        self.revise_date_select.setStyleSheet('QPushButton{border-image:url(calendar.png)}')
        self.revise_date_select.setMinimumSize(QtCore.QSize(50, 50))
        self.revise_date_select.setMaximumSize(QtCore.QSize(50, 50))

        
        ###採收###
        self.revise_harvest = QtWidgets.QLabel('採收',self.revisepage)
        self.revise_harvest.setMinimumSize(QtCore.QSize(140, 200))
        self.revise_harvest.setMaximumSize(QtCore.QSize(140, 200))        
        self.revise_harvest.setAlignment(QtCore.Qt.AlignCenter)
        self.revise_harvest.setFont(self.font_24)
        self.harvest_revise = QtWidgets.QLineEdit(self.revisepage)
        self.harvest_revise.setMinimumSize(QtCore.QSize(180, 110))
        self.harvest_revise.setMaximumSize(QtCore.QSize(180, 110))
        self.harvest_revise.setAlignment(QtCore.Qt.AlignCenter)
        self.harvest_revise.setFont(self.font_22)
        self.harvest_tkg = QtWidgets.QLabel('斤',self.revisepage)
        self.harvest_tkg.setMinimumSize(QtCore.QSize(50, 100))
        self.harvest_tkg.setFont(self.font_24)

        
        ###網路銷售###
        self.revise_online_sales = QtWidgets.QLabel('網路\n銷售',self.revisepage)
        self.revise_online_sales.setMinimumSize(QtCore.QSize(140, 200))        
        self.revise_online_sales.setMaximumSize(QtCore.QSize(140, 200))
        self.revise_online_sales.setAlignment(QtCore.Qt.AlignCenter)
        self.revise_online_sales.setFont(self.font_24)
        self.online_sales_revise = QtWidgets.QLineEdit(self.revisepage)
        self.online_sales_revise.setMinimumSize(QtCore.QSize(180, 110))     
        self.online_sales_revise.setMaximumSize(QtCore.QSize(180, 110))
        self.online_sales_revise.setAlignment(QtCore.Qt.AlignCenter)
        self.online_sales_revise.setFont(self.font_22)
        self.online_sales_tkg = QtWidgets.QLabel('斤',self.revisepage)
        self.online_sales_tkg.setMinimumSize(QtCore.QSize(50, 100))
        self.online_sales_tkg.setFont(self.font_22)
        self.revise_online_sales_price = QtWidgets.QLabel('網路\n單價',self.revisepage)
        self.revise_online_sales_price.setMinimumSize(QtCore.QSize(140, 200))
        self.revise_online_sales_price.setMaximumSize(QtCore.QSize(140, 200))
        self.revise_online_sales_price.setAlignment(QtCore.Qt.AlignCenter)
        self.revise_online_sales_price.setFont(self.font_24)
        self.online_sales_price_revise = QtWidgets.QLineEdit(self.revisepage)
        self.online_sales_price_revise.setMinimumSize(QtCore.QSize(180, 110))
        self.online_sales_price_revise.setMaximumSize(QtCore.QSize(180, 110))
        self.online_sales_price_revise.setAlignment(QtCore.Qt.AlignCenter)
        self.online_sales_price_revise.setFont(self.font_22)

        
        ###市場銷售###
        self.revise_market_sales = QtWidgets.QLabel('市場\n銷售',self.revisepage)
        self.revise_market_sales.setMinimumSize(QtCore.QSize(140, 200))
        self.revise_market_sales.setMaximumSize(QtCore.QSize(140, 200))
        self.revise_market_sales.setAlignment(QtCore.Qt.AlignCenter)
        self.revise_market_sales.setFont(self.font_24)
        self.market_sales_revise = QtWidgets.QLineEdit(self.revisepage)
        self.market_sales_revise.setMinimumSize(QtCore.QSize(180, 110))
        self.market_sales_revise.setMaximumSize(QtCore.QSize(180, 110))
        self.market_sales_revise.setAlignment(QtCore.Qt.AlignCenter)
        self.market_sales_revise.setFont(self.font_22)
        self.market_sales_tkg = QtWidgets.QLabel('斤',self.revisepage)
        self.market_sales_tkg.setMinimumSize(QtCore.QSize(50, 100))
        self.market_sales_tkg.setFont(self.font_22)
        self.revise_market_sales_price = QtWidgets.QLabel('市場\n單價',self.revisepage)
        self.revise_market_sales_price.setMinimumSize(QtCore.QSize(140, 200))
        self.revise_market_sales_price.setMaximumSize(QtCore.QSize(140, 200))
        self.revise_market_sales_price.setAlignment(QtCore.Qt.AlignCenter)
        self.revise_market_sales_price.setFont(self.font_24)
        self.market_sales_price_revise = QtWidgets.QLineEdit(self.revisepage)
        self.market_sales_price_revise.setMinimumSize(QtCore.QSize(180, 110))
        self.market_sales_price_revise.setMaximumSize(QtCore.QSize(180, 110))
        self.market_sales_price_revise.setAlignment(QtCore.Qt.AlignCenter)
        self.market_sales_price_revise.setFont(self.font_22)

        
        ###收入###
        self.revise_income = QtWidgets.QLabel('收入',self.revisepage)
        self.revise_income.setMinimumSize(QtCore.QSize(140, 150))
        self.revise_income.setMaximumSize(QtCore.QSize(140, 150))
        self.revise_income.setAlignment(QtCore.Qt.AlignCenter)
        self.revise_income.setFont(self.font_24)
        self.income_revise = QtWidgets.QLineEdit('',self.revisepage)
        self.income_revise.setMinimumSize(QtCore.QSize(250, 110))
        self.income_revise.setMaximumSize(QtCore.QSize(250, 110))
        self.income_revise.setReadOnly(True)
        self.income_revise.setAlignment(QtCore.Qt.AlignCenter)
        self.income_revise.setFont(self.font_22)

        ###返回###
        self.backhome_revise_button = QtWidgets.QPushButton('返回',self.revisepage)
        self.backhome_revise_button.setMaximumSize(QtCore.QSize(180,130))
        self.backhome_revise_button.setFont(self.font_24)

        ###刪除###
        self.delete_revise_button = QtWidgets.QPushButton('刪除',self.revisepage)
        self.delete_revise_button.setMaximumSize(QtCore.QSize(180,130))
        self.delete_revise_button.setFont(self.font_24)
        
        ###修改###
        self.revisedata_button = QtWidgets.QPushButton('修改',self.revisepage)
        self.revisedata_button.setMaximumSize(QtCore.QSize(180,130))
        self.revisedata_button.setFont(self.font_24)

       
        ###修改區排版###
        self.enterpage_horizontalLayout = QtWidgets.QHBoxLayout(self.revisepage)
        self.enterpage_gridLayout = QtWidgets.QGridLayout()

        self.enterpage_gridLayout.addWidget(self.revise_item, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.revise_item_comboBox, 0, 1, 1, 2)
        
        self.enterpage_gridLayout.addWidget(self.revise_date, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.revise_date_text, 1, 1, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.revise_date_select, 1, 3, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)


        
        self.enterpage_gridLayout.addWidget(self.revise_harvest, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.harvest_revise, 2, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.harvest_tkg, 2, 2, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        
        self.enterpage_gridLayout.addWidget(self.revise_online_sales, 3, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.online_sales_revise, 3, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.online_sales_tkg, 3, 2, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.revise_online_sales_price, 3, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.online_sales_price_revise, 3, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.enterpage_gridLayout.addWidget(self.revise_market_sales, 4, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.market_sales_revise, 4, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.market_sales_tkg, 4, 2, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.revise_market_sales_price, 4, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.market_sales_price_revise, 4, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)


        self.enterpage_gridLayout.addWidget(self.revise_income, 5, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.income_revise, 5, 1, 1, 2)
        
        self.enterpage_gridLayout.addWidget(self.backhome_revise_button, 6, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.delete_revise_button, 6, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.enterpage_gridLayout.addWidget(self.revisedata_button, 6, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.enterpage_horizontalLayout.addLayout(self.enterpage_gridLayout)
        MainWindow.setCentralWidget(self.revisepage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.sales_calculation()
        ###按鈕連結###
        self.revise_date_select.clicked.connect(self.show_calendar)
        self.backhome_revise_button.clicked.connect(self.back_home_page)
        self.revisedata_button.clicked.connect(self.sqlite_add_change)
        self.sqlite_take()
        self.revise_date_text.textChanged['QString'].connect(self.sqlite_take)
        self.delete_revise_button.clicked.connect(self.sqlite_delete)

        


############查看頁面############################################################        
    def check_page_object(self):
        self.flag = 'chick'
        self.checkpage = QtWidgets.QWidget(MainWindow)
        self.checkpage.resize(200, 200)
        conn = sqlite3.connect('salesdata.sqlite')
        
        ###品項###
        self.check_item = QtWidgets.QLabel('品項',self.checkpage)
        self.check_item.setMinimumSize(QtCore.QSize(300, 200))
        self.check_item.setMaximumSize(QtCore.QSize(300, 200))
        self.check_item.setAlignment(QtCore.Qt.AlignCenter)
        self.check_item.setFont(self.font_28)
        self.check_item_comboBox = QtWidgets.QComboBox(self.checkpage)
        self.check_item_comboBox.resize(300, 100)
        self.check_item_comboBox.setMaximumSize(QtCore.QSize(300, 100))
        self.check_item_comboBox.addItems([item[0] for item in conn.execute("select name from sqlite_master where type = 'table';")])
        self.check_item_comboBox.setFont(self.font_24)

        
        ###年###
        self.check_year = QtWidgets.QLabel('年',self.checkpage)
        self.check_year.setMinimumSize(QtCore.QSize(300, 200))
        self.check_year.setMaximumSize(QtCore.QSize(300, 200))
        self.check_year.setAlignment(QtCore.Qt.AlignCenter)
        self.check_year.setFont(self.font_28)
        self.check_year_comboBox = QtWidgets.QComboBox(self.checkpage)
        self.check_year_comboBox.setMinimumSize(QtCore.QSize(250, 100))
        self.check_year_comboBox.setMaximumSize(QtCore.QSize(250, 100))
        self.check_year_comboBox.addItems(set([year[0].split('/')[0] for year in conn.execute("select time from %s " %(self.check_item_comboBox.currentText()))]))
        self.check_year_comboBox.setFont(self.font_24)
        
        
        ###月###
        self.check_month = QtWidgets.QLabel('月',self.checkpage)
        self.check_month.setMinimumSize(QtCore.QSize(300, 200))
        self.check_month.setMaximumSize(QtCore.QSize(300, 200))
        self.check_month.setAlignment(QtCore.Qt.AlignCenter)
        self.check_month.setFont(self.font_28)
        self.check_month_comboBox = QtWidgets.QComboBox(self.checkpage)
        self.check_month_comboBox.setMinimumSize(QtCore.QSize(150, 100))
        self.check_month_comboBox.setMaximumSize(QtCore.QSize(150, 100))
        self.check_month_comboBox.addItems([str(month) for month in range (1,13)])
        self.check_month_comboBox.setFont(self.font_24)
        
        ###確定###
        self.determine_chick_button = QtWidgets.QPushButton('確定',self.checkpage)
        self.determine_chick_button.setMaximumSize(QtCore.QSize(200,150))
        self.determine_chick_button.setFont(self.font_28)   
        
        ###返回###
        self.backhome_chick_button = QtWidgets.QPushButton('返回',self.checkpage)
        self.backhome_chick_button.setMaximumSize(QtCore.QSize(200,150))
        self.backhome_chick_button.setFont(self.font_28)        


        
        ###列表### 
        headItem = ["日","採收","網路銷售","市場銷售","收入"]
        self.check_table = QtWidgets.QTableWidget(self.checkpage)
        self.check_table.setMinimumSize(QtCore.QSize(1000, 900))
        self.check_table.setMaximumSize(QtCore.QSize(1000, 900))
        self.check_table.setColumnCount(5)
        self.check_table.setHorizontalHeaderLabels(headItem)
        self.check_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
        for index in range(self.check_table.columnCount()):
            headItem = self.check_table.horizontalHeaderItem(index)
            headItem.setFont(QtGui.QFont("微軟正黑體", 12))
            headItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)




        
        
        
        
        
        ###檢查區排版####
        self.checkpage_horizontalLayout = QtWidgets.QHBoxLayout(self.checkpage)
        self.checkpage_gridLayout = QtWidgets.QGridLayout()
        
        self.checkpage_gridLayout.addWidget(self.check_item, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.checkpage_gridLayout.addWidget(self.check_item_comboBox, 0, 1, 1, 1)

        self.checkpage_gridLayout.addWidget(self.check_year, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.checkpage_gridLayout.addWidget(self.check_year_comboBox, 1, 1, 1, 1)

        self.checkpage_gridLayout.addWidget(self.check_month, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.checkpage_gridLayout.addWidget(self.check_month_comboBox, 2, 1, 1, 1)

        self.checkpage_gridLayout.addWidget(self.determine_chick_button, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.checkpage_gridLayout.addWidget(self.backhome_chick_button, 2, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.checkpage_gridLayout.addWidget(self.check_table, 3, 0, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        
        self.checkpage_horizontalLayout.addLayout(self.checkpage_gridLayout)
        MainWindow.setCentralWidget(self.checkpage)
        
        ###按鈕連結###
        self.backhome_chick_button.clicked.connect(self.back_home_page)
        self.determine_chick_button.clicked.connect(self.sqlite_chick)


############統計資料頁面############################################################        
    def statistics_page_object(self):
        self.flag = 'statistics'
        self.statisticspage = QtWidgets.QWidget(MainWindow)
        self.statisticspage.resize(200, 200)
        conn = sqlite3.connect('salesdata.sqlite')

        ###品項###
        self.statistics_item = QtWidgets.QLabel('品項',self.statisticspage)
        self.statistics_item.setMinimumSize(QtCore.QSize(300, 200))
        self.statistics_item.setMaximumSize(QtCore.QSize(300, 200))
        self.statistics_item.setAlignment(QtCore.Qt.AlignCenter)
        self.statistics_item.setFont(self.font_28)
        self.statistics_item_comboBox = QtWidgets.QComboBox(self.statisticspage)
        self.statistics_item_comboBox.resize(300, 100)
        self.statistics_item_comboBox.setMaximumSize(QtCore.QSize(300, 100))
        self.statistics_item_comboBox.addItems([item[0] for item in conn.execute("select name from sqlite_master where type = 'table';")])
        self.statistics_item_comboBox.setFont(self.font_24)
        
        ###開始日期####
        self.statistics_start_date = QtWidgets.QLabel('開始',self.statisticspage)
        self.statistics_start_date.setMinimumSize(QtCore.QSize(300, 200))
        self.statistics_start_date.setMaximumSize(QtCore.QSize(300, 200))
        self.statistics_start_date.setAlignment(QtCore.Qt.AlignCenter)
        self.statistics_start_date.setFont(self.font_28)
        self.statistics_start_date_text = QtWidgets.QTextBrowser(self.statisticspage)
        self.statistics_start_date_text.setMinimumSize(QtCore.QSize(460, 100))
        self.statistics_start_date_text.setMaximumSize(QtCore.QSize(460, 100))
        self.statistics_start_date_text.setAlignment(QtCore.Qt.AlignCenter)
        self.statistics_start_date_text.setFont(self.font_24)
        self.statistics_start_date_select = QtWidgets.QPushButton(self.statisticspage)
        self.statistics_start_date_select.setStyleSheet('QPushButton{border-image:url(calendar.png)}')
        self.statistics_start_date_select.setMinimumSize(QtCore.QSize(50, 50))
        self.statistics_start_date_select.setMaximumSize(QtCore.QSize(50, 50))
        self.statistics_start_date_select.setObjectName('start_date')

        
        ###結束日期####
        self.statistics_end_date = QtWidgets.QLabel('結束',self.statisticspage)
        self.statistics_end_date.setMinimumSize(QtCore.QSize(300, 200))
        self.statistics_end_date.setMaximumSize(QtCore.QSize(300, 200))
        self.statistics_end_date.setAlignment(QtCore.Qt.AlignCenter)
        self.statistics_end_date.setFont(self.font_28)
        self.statistics_end_date_text = QtWidgets.QTextBrowser(self.statisticspage)
        self.statistics_end_date_text.setMinimumSize(QtCore.QSize(460, 100))
        self.statistics_end_date_text.setMaximumSize(QtCore.QSize(460, 100))
        self.statistics_end_date_text.setAlignment(QtCore.Qt.AlignCenter)
        self.statistics_end_date_text.setFont(self.font_24)
        self.statistics_end_date_select = QtWidgets.QPushButton(self.statisticspage)
        self.statistics_end_date_select.setStyleSheet('QPushButton{border-image:url(calendar.png)}')
        self.statistics_end_date_select.setMinimumSize(QtCore.QSize(50, 50))
        self.statistics_end_date_select.setMaximumSize(QtCore.QSize(50, 50))
        self.statistics_end_date_select.setObjectName('end_date')

        
        ###返回###
        self.backhome_statistics_button = QtWidgets.QPushButton('返回',self.statisticspage)
        self.backhome_statistics_button.setMaximumSize(QtCore.QSize(200,150))
        self.backhome_statistics_button.setFont(self.font_28)

        
        ###畫圖###
        self.statistics_drawing_button = QtWidgets.QPushButton('畫圖',self.statisticspage)
        self.statistics_drawing_button.setMaximumSize(QtCore.QSize(200,150))
        self.statistics_drawing_button.setFont(self.font_28)        

        ###圖表顯示###
        self.statistics_drawing_show = QtWidgets.QTextBrowser(self.statisticspage)
        self.statistics_drawing_show.setMinimumSize(QtCore.QSize(1040, 850))
        
        
        ###統計資料區排版####
        self.statistics_horizontalLayout = QtWidgets.QHBoxLayout(self.statisticspage)
        self.statisticspage_gridLayout = QtWidgets.QGridLayout()
        
        self.statisticspage_gridLayout.addWidget(self.statistics_item, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.statisticspage_gridLayout.addWidget(self.statistics_item_comboBox, 0, 1, 1, 1,QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.statisticspage_gridLayout.addWidget(self.statistics_start_date, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.statisticspage_gridLayout.addWidget(self.statistics_start_date_text, 1, 1, 1, 1,QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statisticspage_gridLayout.addWidget(self.statistics_start_date_select, 1, 1, 1, 1,QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.statisticspage_gridLayout.addWidget(self.statistics_end_date, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.statisticspage_gridLayout.addWidget(self.statistics_end_date_text, 2, 1, 1, 1,QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statisticspage_gridLayout.addWidget(self.statistics_end_date_select, 2, 1, 1, 1,QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.statisticspage_gridLayout.addWidget(self.backhome_statistics_button, 4, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.statisticspage_gridLayout.addWidget(self.statistics_drawing_button, 4, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        
        self.statisticspage_gridLayout.addWidget(self.statistics_drawing_show, 5, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.statistics_horizontalLayout.addLayout(self.statisticspage_gridLayout)
        MainWindow.setCentralWidget(self.statisticspage)

        
        ###按鈕連結###
        self.backhome_statistics_button.clicked.connect(self.back_home_page)
        self.statistics_start_date_select.clicked.connect(self.show_calendar)
        self.statistics_start_date_select.clicked.connect(self.statistics_choose)
        self.statistics_end_date_select.clicked.connect(self.show_calendar)
        self.statistics_end_date_select.clicked.connect(self.statistics_choose)
        self.statistics_drawing_button.clicked.connect(self.plot_)
        

################################小日曆##########################################
    def Calendar(self):
        self.Calendar_page = QtWidgets.QWidget(MainWindow)
        self.Calendar_page.resize(1000, 1000)
        self.cal = QtWidgets.QCalendarWidget(self.Calendar_page)
        self.cal.resize(1000, 1000)
        self.cal.setGridVisible(True)
        self.cal.selectionChanged.connect(self.showDate)
        
    def showDate(self):
        date = self.cal.selectedDate()
        self.date_text = str(date.toPyDate())
        if self.flag == 'enter':
            self.enter_date_text.setText(str(date.toPyDate()).replace('-','/'))
            self.enter_date_select.show()

        elif self.flag == 'revise':
            self.revise_date_text.setText(str(date.toPyDate()).replace('-','/'))
            self.revise_date_select.show()
            
        elif self.flag == 'statistics':
            self.statistics_choose()
            if self.statistics_flag == 1:
                 self.statistics_start_date_text.setText(str(date.toPyDate()).replace('-','/'))
            elif self.statistics_flag == 2:
                self.statistics_end_date_text.setText(str(date.toPyDate()).replace('-','/'))
            self.statistics_start_date_select.show()
            self.statistics_end_date_select.show()
        self.Calendar_page.close()
        

#########################連接其他頁面###########################################
    def home_connection_page (self):
        home_button = self.homepage.sender()
        if home_button.objectName() == 'enterdata_button':
            self.enter_page_object()
            self.homepage.close()
            self.enterpage.show()
            
        elif home_button.objectName() == 'revisedata_button':
            self.revise_page_object()
            self.homepage.close()
            self.revisepage.show()
            
        elif home_button.objectName() == 'checkdata_button':
            self.check_page_object()
            self.homepage.close()
            self.checkpage.show()
            
        elif home_button.objectName() == 'statistics_button':
            self.statistics_page_object()
            self.homepage.close()
            self.statisticspage.show()
            
    def back_home_page(self):
        if self.flag == 'enter':
            self.home_page_object()
            self.enterpage.close()
            self.homepage.show()
        elif self.flag == 'revise':
            self.home_page_object()
            self.revisepage.close()
            self.homepage.show()
        elif self.flag == 'chick':
            self.home_page_object()
            self.checkpage.close()
            self.homepage.show()
        elif self.flag == 'statistics':
            self.home_page_object()
            self.statisticspage.close()
            self.homepage.show()
            
    def show_calendar(self):
        self.Calendar()
        self.Calendar_page.show()
        if self.flag == 'enter':
            self.enter_date_select.hide()
        elif self.flag == 'revise':
            self.revise_date_select.hide()
        elif self.flag == 'statistics':
            self.statistics_start_date_select.hide()
            self.statistics_end_date_select.hide()

    def statistics_choose(self):
        statistics_date = self.statisticspage.sender()
        if statistics_date.objectName() == 'start_date':
            self.statistics_flag = 1
        elif statistics_date.objectName() == 'end_date':
            self.statistics_flag = 2
            
#############################收入計算##########################################
    def sales_calculation(self):
        if self.flag == 'enter':
            self.online_sales_edit.textChanged['QString'].connect(self.judgment)
            self.online_sales_price_edit.textChanged['QString'].connect(self.judgment)
            self.market_sales_edit.textChanged['QString'].connect(self.judgment)
            self.market_sales_price_edit.textChanged['QString'].connect(self.judgment)
        elif self.flag == 'revise':
            self.online_sales_revise.textChanged['QString'].connect(self.judgment)
            self.online_sales_price_revise.textChanged['QString'].connect(self.judgment)
            self.market_sales_revise.textChanged['QString'].connect(self.judgment)
            self.market_sales_price_revise.textChanged['QString'].connect(self.judgment)
            

    def judgment(self):
        if self.flag == 'enter':
            self.online_sales_edit_text = self.online_sales_edit.text()
            self.online_sales_price_edit_text = self.online_sales_price_edit.text()
            self.market_sales_edit_text = self.market_sales_edit.text()
            self.market_sales_price_edit_text = self.market_sales_price_edit.text()
            try:
                self.income_edit.setText('%s' %eval('%s*%s+%s*%s' %(self.online_sales_edit_text,self.online_sales_price_edit_text,self.market_sales_edit_text,self.market_sales_price_edit_text)))
            except:
                self.income_edit.setText('')
                pass
            
        elif self.flag == 'revise':
            self.online_sales_revise_text = self.online_sales_revise.text()
            self.online_sales_price_revise_text = self.online_sales_price_revise.text()
            self.market_sales_revise_text = self.market_sales_revise.text()
            self.market_sales_price_revise_text = self.market_sales_price_revise.text()
            try:
                self.income_revise.setText('%s' %eval('%s*%s+%s*%s' %(self.online_sales_revise_text,self.online_sales_price_revise_text,self.market_sales_revise_text,self.market_sales_price_revise_text)))
            except:
                self.income_revise.setText('')
                pass

##############################資料庫########################################
    def sqlite_add_change(self):
        conn = sqlite3.connect('salesdata.sqlite')
        cur = conn.cursor()
        if self.flag == 'enter':
            try:
                if (type(eval(self.income_edit.text())) == type(float()) or type(eval(self.income_edit.text())) == type(int())) and self.item_edit.text() != '':
                    cur.execute('create table if not exists %s (time TEXT, harvest TEXT, online_sales TEXT, online_sales_price TEXT, market_sales TEXT, market_sales_price TEXT, income TEXT)' %self.item_edit.text())
                    time_list = [time[0] for time in cur.execute("select * from %s" %self.item_edit.text())]
                    if self.enter_date_text.text() in time_list:
                        pass
                        QtWidgets.QMessageBox.information(self.enterpage, "Message", "已有資料")
                    else:
                        cur.execute('insert into %s (time, harvest, online_sales, online_sales_price, market_sales, market_sales_price, income) values(?, ?, ?, ?, ?, ?, ?) ' %self.item_edit.text(),(self.enter_date_text.text(), self.harvest_edit.text(), self.online_sales_edit.text(), self.online_sales_price_edit.text(), self.market_sales_edit.text(), self.market_sales_price_edit.text(), self.income_edit.text()))
                        QtWidgets.QMessageBox.information(self.enterpage, "Message", "儲存完成")
                        self.back_home_page()
                else:
                    QtWidgets.QMessageBox.information(self.enterpage, "Message", "輸入錯誤")
            except:
                QtWidgets.QMessageBox.information(self.enterpage, "Message", "輸入錯誤")
        elif self.flag =='revise':
            try:
                if type(eval(self.income_revise.text())) == type(float()) or type(eval(self.income_revise.text())) == type(int()):
                    cur.execute("update %s set harvest = ? ,online_sales = ?, online_sales_price = ?, market_sales = ?, market_sales_price = ?, income = ? where time = ?" %(self.revise_item_comboBox.currentText()), (self.harvest_revise.text(),self.online_sales_revise.text(),self.online_sales_price_revise.text(),self.market_sales_revise.text(),self.market_sales_price_revise.text(),self.income_revise.text(),self.revise_date_text.text())) #修改
                    QtWidgets.QMessageBox.information(self.revisepage, "Message", "修改完成")
                    self.back_home_page()
                else:
                    QtWidgets.QMessageBox.information(self.enterpage, "Message", "輸入錯誤")
            except:
                QtWidgets.QMessageBox.information(self.enterpage, "Message", "輸入錯誤")
        conn.commit()
        conn.close()
        
    def sqlite_delete(self):
        conn = sqlite3.connect('salesdata.sqlite')
        cur = conn.cursor()
        cur.execute("delete from %s where time = ? and harvest = ? and online_sales = ? and online_sales_price = ? and market_sales = ? and market_sales_price = ? and income = ?" %(self.revise_item_comboBox.currentText()),(self.revise_date_text.text(),self.harvest_revise.text(),self.online_sales_revise.text(),self.online_sales_price_revise.text(),self.market_sales_revise.text(),self.market_sales_price_revise.text(),self.income_revise.text())) #刪除
        QtWidgets.QMessageBox.information(self.revisepage, "Message", "刪除完成")
        conn.commit()
        cur = conn.cursor()
        cur.execute("select * from %s" %self.revise_item_comboBox.currentText())
        if len(cur.fetchall())==0:
            cur.execute("DROP TABLE %s" %self.revise_item_comboBox.currentText())
        conn.commit()
        conn.close()
        self.back_home_page()
        
    def sqlite_take(self):
        conn = sqlite3.connect('salesdata.sqlite')
        cur = conn.cursor()
        try:
            data_dict = {data[0]:[data[1], data[2], data[3], data[4], data[5], data[6]] for data in cur.execute("select * from %s" %self.revise_item_comboBox.currentText())}
            self.harvest_revise.setText(data_dict[self.revise_date_text.text()][0])
            self.online_sales_revise.setText(data_dict[self.revise_date_text.text()][1])
            self.online_sales_price_revise.setText(data_dict[self.revise_date_text.text()][2])
            self.market_sales_revise.setText(data_dict[self.revise_date_text.text()][3])
            self.market_sales_price_revise.setText(data_dict[self.revise_date_text.text()][4])
            self.income_revise.setText(data_dict[self.revise_date_text.text()][5])
        except:
            pass
        
    def sqlite_chick(self):
        conn = sqlite3.connect('salesdata.sqlite')
        row_count = 0
        for row in conn.execute("select * from %s order by time" %(self.check_item_comboBox.currentText())):
            if row[0].split('/')[0] == self.check_year_comboBox.currentText() and int(row[0].split('/')[1]) == int(self.check_month_comboBox.currentText()):
                self.check_table.setRowCount(row_count+1)
                day = QtWidgets.QTableWidgetItem(row[0].split('/')[2])
                day.setTextAlignment((QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)) 
                day.setFont(self.font_14)
                self.check_table.setItem(row_count,0, day)
                harvest = QtWidgets.QTableWidgetItem(row[1])
                harvest.setTextAlignment((QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter))
                harvest.setFont(self.font_14)
                self.check_table.setItem(row_count,1, harvest)
                online_sales = QtWidgets.QTableWidgetItem(row[2])
                online_sales.setTextAlignment((QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter))
                online_sales.setFont(self.font_14)
                self.check_table.setItem(row_count,2, online_sales)
                market_sales = QtWidgets.QTableWidgetItem(row[4])
                market_sales.setTextAlignment((QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter))
                market_sales.setFont(self.font_14)
                self.check_table.setItem(row_count,3, market_sales)
                income = QtWidgets.QTableWidgetItem(row[6])
                income.setTextAlignment((QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter))
                income.setFont(self.font_14)
                income.setForeground(QtGui.QColor(255, 0, 0))
                self.check_table.setItem(row_count,4, income)
                row_count += 1
            else:
                self.check_table.setRowCount(0)

##############################畫圖設定##########################################
    def plot_(self):
        fig = plt.figure()
        labels = ["day1","day2","day3","day3","day5","day6"]
        word_size = [2000, 3250, 4600 , 2300, 3600, 5600]
        explode = [0 , 0, .05, 0, 0, 0]  #0則不突凸出，值越大 則凸出越大
        plt.pie(word_size, explode= explode, labels = labels, autopct= "%3.1f%%")
        plt.savefig("pic.png")
        self.statistics_drawing_show.clear()
        self.statistics_drawing_show.setStyleSheet('QTextBrowser{border-image:url(pic.png)}')

##############################字型設定##########################################
    def font_size (self):
        self.font_14 = QtGui.QFont("微軟正黑體",14)
        
        self.font_22 = QtGui.QFont("微軟正黑體",22)
                
        self.font_24 = QtGui.QFont("微軟正黑體",24)
        
        self.font_28 = QtGui.QFont("微軟正黑體",28)
        
        self.font_32 = QtGui.QFont("微軟正黑體",32)
        





        



        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.Main_Window(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    