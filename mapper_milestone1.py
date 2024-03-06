#!/home/bigdata/anaconda3/bin/python
import sys

for line in sys.stdin:
     line = line.strip()
     datas = line.split('\t')
     if len(datas) == 6:
          date, time, location, product, price, payment = datas
          if 'Toys' in product or 'Consumer Electronics' in product:
               print("%s\t%s" % (product, price))
     else:
          continue