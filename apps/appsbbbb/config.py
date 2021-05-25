# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:30:29 2021

@author: pati
"""
def config():
    connection = mysql.connector.connect(host='sql10.freemysqlhosting.net',
                                         user='sql10411482',
                                         password='VmhMnlwmuN',db='sql10411482')
    return connection