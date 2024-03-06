#!/home/bigdata/anaconda3/bin/python
import sys

current_location = None
max_product = None
max_price = 0
location = None
product = None

for line in sys.stdin:
     line = line.strip()
     location, price, product = line.split('\t')
     try:
          price = float(price)
     except ValueError:
          continue
     
     if current_location == location:
          if price > max_price: 
               max_price = price
               max_product = product 
     else:
          if current_location:
               print('%s\t%s\t%s' % (current_location, max_price, max_product))
          current_location = location
          max_price = price
          max_product = product
print('%s\t%s\t%s' % (current_location, max_price, max_product))