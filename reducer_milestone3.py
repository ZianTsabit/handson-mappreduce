#!/home/bigdata/anaconda3/bin/python
import sys

current_time = None
current_count = 0
time = None

for line in sys.stdin:
     line = line.strip()
     time, count = line.split('\t')
     try:
          count = int(count)
     except ValueError:
          continue
     if current_time == time:
          current_count += count
     else:
          if current_time:
               print('%s\t%s' % (current_time, current_count))
          current_count = count
          current_time = time
print('%s\t%s' % (current_time, current_count))