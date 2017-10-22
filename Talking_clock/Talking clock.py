# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:51:57 2017

@author: Oliver
"""

import time as time

time_strings={'1':'one',
              '2':'two',
              '3':'three',
              '4':'four',
              '5':'five',
              '6':'six',
              '7':'seven',
              '8':'eight',
              '9':'nine',
              '10':'ten',
              '11':'eleven',
              '12':'twelve',
              '13':'thirteen',
              '15':'fifteen',
              '20':'twenty',
              '30':'thirty',
              '40':'forty',
              '50':'fifty',
              '0':'twelve',
              '00':''}

print('Enter time in HH:MM format:')
hours,minutes=input().split(':')

hours=int(hours)
ampm=' AM'

if hours>12:
    hours = hours-12
    ampm=' PM'

try:
    minutes_string=time_strings[minutes]
except KeyError:
    try:
        minutes=str(int(minutes))
        
        if minutes[0]=='1':
            minutes_string=time_strings[minutes[1]]+'teen'
        else:
            minutes_string=time_strings[minutes[0]+'0']+' '+time_strings[minutes[1]]
            
    except KeyError:
        minutes_string='oh '+time_strings[minutes[0]]

print('The time is '+time_strings[str(hours)]+ ' '+ minutes_string+ampm)
