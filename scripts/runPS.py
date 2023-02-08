"""
Created in May 2022

@author: KhadijaHammawa Aug 2022
"""

import win32com.client
import os

psApp = win32com.client.Dispatch('Photoshop.Application')
psApp.Open("C:/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/scripts/remove-bg.jsx".encode('utf-8'))
psApp.Quit()


