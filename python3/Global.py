#!/usr/bin/env python

#SELECTED_CONFIG_ENVIRONMENT = 'GARRETT2'
SELECTED_CONFIG_ENVIRONMENT = 'GARRETT3'

if SELECTED_CONFIG_ENVIRONMENT == 'development':
    #development
    CONFIG = {
        'SystemAutomationHostname': 'GARRETT2',
        'CurrentSystemHostnamePort': 'GARRETT2:9001',

        'LogFileName': '_HttpServer.log'
    }
elif SELECTED_CONFIG_ENVIRONMENT == 'GARRETT3':
    CONFIG = {
        'SystemAutomationHostname': 'localhost',
        'CurrentSystemHostnamePort': 'GARRETT3:9001',

        'LogFileName': '_HttpServer.log'
    }
else:
    CONFIG = {
        '': ''
    }