"""
Created in May 2022

@author: KhadijaHammawa Aug 2022
"""

import win32com.client
import os
import photoshop as ps

psApp = win32com.client.Dispatch('Photoshop.Application')
psApp.Open('C:/Users/feusn/Desktop/VMphotos/scripts/remove-bg.jsx')
psApp.Quit()

