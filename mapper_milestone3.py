#!/home/bigdata/anaconda3/bin/python
from datetime import datetime, time
import sys

for line in sys.stdin:
     line = line.strip()
     datas = line.split('\t')
     if len(datas) == 6:
          date, time_str, location, product, price, payment = datas
          time_obj = datetime.strptime(time_str, '%H:%M').time()
          if time(9,1) <= time_obj <= time(10,0):
               print("%s\t%s" % ('09:01-10:00',1))
          elif time(10, 1) <= time_obj <= time(11,0):
               print("%s\t%s" % ('10:01-11:00',1)) 
     else:
          continue