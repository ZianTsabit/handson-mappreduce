#!/home/bigdata/anaconda3/bin/python
import sys

current_product = None
current_price = 0
product = None

for line in sys.stdin:
     line = line.strip()
     product, price = line.split('\t')
     try:
          price = float(price)
     except ValueError:
          continue
     if current_product == product:
          current_price += price
     else:
          if current_product:
               print('%s\t%s' % (current_product, current_price))
          current_price = price
          current_product = product
print('%s\t%s' % (current_product, current_price))