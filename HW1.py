#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = 'sample_input.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.

C0A880 = [v for v in data if v['station_id'] == 'C0A880']
C0F9A0 = [v for v in data if v['station_id'] == 'C0F9A0']
C0G640 = [v for v in data if v['station_id'] == 'C0G640']
C0R190 = [v for v in data if v['station_id'] == 'C0R190']
C0X260 = [v for v in data if v['station_id'] == 'C0X260']

Max=max(C0A880, key=lambda x: x['WDSD'] )
Min=min(C0A880, key=lambda x: x['WDSD'])
if Max['WDSD']!='-99.000' and Max['WDSD']!='-999.000'and Min['WDSD']!='-99.000' and Min['WDSD']!='-999.000':
    C0A880=['C0A880',abs(float(Max['WDSD'])-float(Min['WDSD']))]
else:
    C0A880=['C0A880','None']

Max=max(C0F9A0, key=lambda x: x['WDSD'] )
Min=min(C0F9A0, key=lambda x: x['WDSD'])
if Max['WDSD']!='-99.000' and Max['WDSD']!='-999.000'and Min['WDSD']!='-99.000' and Min['WDSD']!='-999.000':
    C0F9A0=['C0F9A0',abs(float(Max['WDSD'])-float(Min['WDSD']))]
else:
    C0F9A0=['C0F9A0','None']
    
Max=max(C0G640, key=lambda x: x['WDSD'] )
Min=min(C0G640, key=lambda x: x['WDSD'])
if Max['WDSD']!='-99.000' and Max['WDSD']!='-999.000'and Min['WDSD']!='-99.000' and Min['WDSD']!='-999.000':
    C0G640=['C0G640',abs(float(Max['WDSD'])-float(Min['WDSD']))]
else:
    C0G640=['C0G640','None']
    
Max=max(C0R190, key=lambda x: x['WDSD'] )
Min=min(C0R190, key=lambda x: x['WDSD'])
if Max['WDSD']!='-99.000' and Max['WDSD']!='-999.000'and Min['WDSD']!='-99.000' and Min['WDSD']!='-999.000':
    C0R190=['C0R190',abs(float(Max['WDSD'])-float(Min['WDSD']))]
else:
    C0R190=['C0R190','None']
    
Max=max(C0X260, key=lambda x: x['WDSD'] )
Min=min(C0X260, key=lambda x: x['WDSD'])
if Max['WDSD']!='-99.000' and Max['WDSD']!='-999.000'and Min['WDSD']!='-99.000' and Min['WDSD']!='-999.000':
    C0X260=['C0X260',abs(float(Max['WDSD'])-float(Min['WDSD']))]
else:
    C0X260=['C0X260','None']
# Retrive ten data points from the beginning.
target_data = [C0A880]
target_data.append(C0G640)
target_data.append(C0F9A0)
target_data.append(C0R190)
target_data.append(C0X260)
#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================


# In[ ]:




