# GOALS
# Compare rush hour to non for consistency

from pprint import pprint
import csv
from datetime import *
from dateutil.relativedelta import *
import calendar
import dateutil.parser
import matplotlib.pyplot as plt
import operator

# Collect and Store Data in Memory
def fetch_data():
  my_list=[]
  with open("turnstile_150404.txt", "r") as turn_data:
    reader=csv.reader(turn_data)
    reader.next()
    for row in reader:
      my_list.append(row)

  return my_list


# CHALLENGE ONE
def format_data():
  my_hash={}
  the_list=fetch_data()
  for row in the_list:
      key = tuple(row[0:4])
      val = row[4:-1]
      # check if the key, val exists
      if key in my_hash:
          my_hash[key].append( val )
      else:
          my_hash[key] = [ val ]
  return my_hash



# CHALLENGE TWO
def format_data_hour():
  my_hash={}
  the_list = fetch_data()
  for index, row in enumerate(the_list):
    key = tuple(row[0:4])
    time_str = row[6] + " " + row[7]
    time = dateutil.parser.parse( time_str )
    if index == len(the_list)-1:
      count = "Last Value Of The Day"
    else:
      count = int(float(the_list[index+1][-2])) - int(float(row[-2]))
    val = [time,  count]
    if key in my_hash:
        my_hash[key].append( val )
    else:
        my_hash[key] = [ val ]

  return my_hash


def rush_hour_entries():
  mta_hour_list = format_data_hour().items()
  my_hash = {}

  for index, row in enumerate(mta_hour_list):

    station_info = row[0]
    time_info = row[1]

    key = tuple([station_info[0], station_info[1], station_info[3]])
    first_hour = time_info[0][0].hour

    if first_hour == 1 or first_hour == 2 or first_hour == 3:
      morning_val = time_info[1][1]
    elif first_hour == 0:
      morning_val = time_info[2][1]

    if first_hour == 0 or first_hour == 1 or first_hour == 2:
      evening_val = time_info[4][1]
    elif first_hour == 3:
      evening_val = time_info[3][1]

    val = evening_val + morning_val

    if key in my_hash:
      my_hash[key] += val
    else:
      my_hash[key] = val

  sorted_hash = sorted( my_hash.items(), key=operator.itemgetter(1) )

  return sorted_hash




def density_by_turnstile():
  mta_hour_list = format_data_hour().items()
  my_hash = {}

  for index, row in enumerate(mta_hour_list):

    if index == 10:
      break


    key = tuple([station_info[0], station_info[1], station_info[3]])

    if key in my_hash:
      my_hash[key].append(val)
    else:
      my_hash[key] = [ val ]

  return my_hash




# ====================================
#           DRIVER CODE
# ====================================

rush_entries= rush_hour_entries()

