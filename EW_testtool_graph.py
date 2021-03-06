#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from matplotlib.dates import datestr2num

import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc, candlestick2_ohlc
from matplotlib import style

import numpy as np
import urllib2
import datetime as dt
import csv

import fibonacci
from EW_testtool_V01 import *
import EW_finder_V01

def create_list_for_drawing(data_input, data_output):
    for item in data_input:
        if item == 1:
            data_output[0].append(data_input[item][2][0])
            data_output[1].append(data_input[item][3][0])
            data_output[0].append(data_input[item][2][1])
            data_output[1].append(data_input[item][3][1])
        else:
            data_output[0].append(data_input[item][2][1])
            data_output[1].append(data_input[item][3][1])

################################       
################################
################################
data = Database()
test = Test(data.stock_data)
ew_finder = EW_finder_V01.TEST(test.detail_view_lines)



#       plots
################################       
################################
################################    test.raw_values
style.use('dark_background')

fig = plt.figure()
ax1 = fig.add_subplot(111)
#plot1 = candlestick_ohlc(ax1, data.ohlc, width=1.0, colorup='#77d879', colordown='#db3f3f', alpha=1.0)


########>>>>>>>>>  plots der Innenstaebe 
##for item in test.aussenstaebe_up_lim:
##    ax1.plot(test.aussenstaebe_up_lim[item][0],test.aussenstaebe_up_lim[item][1],color='blue')
##for item in test.aussenstaebe_low_lim:
##    ax1.plot(test.aussenstaebe_low_lim[item][0],test.aussenstaebe_low_lim[item][1],color='blue')


########>>>>>>>>>  plots der detail_lines
##detail_lines = [[],[]]
##create_list_for_drawing(test.detail_lines,detail_lines)
##ax1.plot(detail_lines[0],detail_lines[1],label='detail_lines',color='white', linewidth=0.5)
#>>>>>>>>>  plots der detail_simple_lines
##detail_view_lines = [[],[]]
##create_list_for_drawing(test.detail_view_lines,detail_view_lines)
##ax1.plot(detail_view_lines[0],detail_view_lines[1],label='detail_view_lines',color='#7cfc00', linewidth=1.0)


######>>>>>>>>>  plots der EW_finder_V01 basis_waves
for item in ew_finder.basis_waves:
    if not item %2:
        ax1.plot(ew_finder.basis_waves[item][2],ew_finder.basis_waves[item][3],color='white', linewidth=1.0)
    else:
        ax1.plot(ew_finder.basis_waves[item][2],ew_finder.basis_waves[item][3],color='orange', linewidth=1.0)

######>>>>>>>>>  plots der EW_finder_V01 comb_lvl_1
for item in ew_finder.comb_lvl_1:
    if len(ew_finder.comb_lvl_1[item][2]) == 4:
        ax1.plot(ew_finder.comb_lvl_1[item][2],ew_finder.comb_lvl_1[item][3],color='blue', linewidth=1.5)
    if len(ew_finder.comb_lvl_1[item][2]) == 6:
        ax1.plot(ew_finder.comb_lvl_1[item][2],ew_finder.comb_lvl_1[item][3],color='red', linewidth=1.5)    


########>>>>>>>>>  plots der simple_l1
##simple_line_l1 = [[],[]]
##create_list_for_drawing(test.simple_line_l1,simple_line_l1)
##ax1.plot(simple_line_l1[0],simple_line_l1[1],label='level_1',color='white')
########>>>>>>>>>  plots der simple_l2
##simple_line_l2 = [[],[]]
##create_list_for_drawing(test.simple_line_l2,simple_line_l2)
##ax1.plot(simple_line_l2[0],simple_line_l2[1],label='level_2',color='#ffd700', linewidth=1.0)
######>>>>>>>>>  plots der simple_l3
##simple_line_l3 = [[],[]]
##create_list_for_drawing(test.simple_line_l3,simple_line_l3)
##ax1.plot(simple_line_l3[0],simple_line_l3[1],label='level_3',color='#ff0000', linewidth=1.0)
####>>>>>>>>>  plots der simple_l4
##simple_line_l4 = [[],[]]
##create_list_for_drawing(test.simple_line_l4,simple_line_l4)
##ax1.plot(simple_line_l4[0],simple_line_l4[1],label='level_4',color='#4169e1', linewidth=3.0)
######>>>>>>>>>  plots der simple_l5
##simple_line_l5 = [[],[]]
##create_list_for_drawing(test.simple_line_l5,simple_line_l5)
##ax1.plot(simple_line_l5[0],simple_line_l5[1],label='level_5',color='#ff1493', linewidth=4.0)
####>>>>>>>>>  plots der simple_l6
##simple_line_l6 = [[],[]]
##create_list_for_drawing(test.simple_line_l6,simple_line_l6)
##ax1.plot(simple_line_l6[0],simple_line_l6[1],label='level_6',color='green', linewidth=2.0)
####>>>>>>>>>  plots der simple_l7
##simple_line_l7 = [[],[]]
##create_list_for_drawing(test.simple_line_l7,simple_line_l7)
##ax1.plot(simple_line_l7[0],simple_line_l7[1],label='level_7',color='white', linewidth=2.0)



for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(90)

#ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y %m %d'))
ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))


#ax1.grid(True)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title("TEST_IMPORT_CSV")
plt.legend()
plt.subplots_adjust(left=0.11, bottom=0.12, right=0.99, top=0.95, wspace=0.2, hspace=0)
plt.show()
################################       
################################
################################





