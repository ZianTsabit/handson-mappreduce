#!/home/bigdata/anaconda3/bin/python
import sys

for line in sys.stdin:
     line = line.strip()
     datas = line.split('\t')
     if len(datas) == 6:
          date, time, location, product, price, payment = datas
          if location == 'Miami' or location == 'San Francisco' or location == 'Atlanta':
               print("%s\t%s\t%s" % (location, price, product))
     else:
          continue