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
  with open("turnstile_150404.txt", "r") as turn_data:
    reader=csv.reader(turn_data)
    reader.next()
    my_list = [ [ cell.strip() for cell in row ] for row in reader]

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
def format_data_hour_tohei():
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





# CHALLENGE THREE
def create_data_for_day_list():
  my_hash={}
  the_list=fetch_data()
  for index, row in enumerate(the_list):
    key = tuple(row[0:4])
    time =  row[6]
    cumalitive_count= int(float(row[-2]))

    val = [time,  cumalitive_count]
    if key in my_hash:
        my_hash[key].append( val )
    else:
        my_hash[key] = [ val ]
  return my_hash


def format_data_day():
  my_hash={}
  data_hash= create_data_for_day_list()
  for k, v in data_hash.items():
    i=0
    while i < len(v) - 1:
      date = v[i][0]
      initial_count=v[i][1]
      next_count=v[i][1]
      while date == v[i][0] and i < len(v)-1:
         i += 1
         next_count = v[i][1]
      new_val = [date, next_count - initial_count ]

      if k in my_hash:
        my_hash[k].append(new_val)
      else:
        my_hash[k]= [new_val]

  return my_hash

def density_by_turnstile_hash():
  mta_day_list = format_data_day().items()
  my_hash = {}

  for index, row in enumerate(mta_day_list):
    station_info = row[0]
    # key = tuple([station_info[0], station_info[1], station_info[3]])
    key = station_info[3]
    vals = []

    for val in row[1]:
      vals.append(val[1])
    # pprint(vals)

    if key in my_hash:
      my_hash[key] + vals
    else:
      my_hash[key] = vals

  return my_hash


def density_for_station():
  turnstile_hash = density_by_turnstile_hash()
  my_hash = {}

  for index, row in enumerate(turnstile_hash.items()):
    number_of_turnstiles = len(row[1])
    average= float(sum(row[1])) / number_of_turnstiles
    avg = float("{0:.2f}".format(average))
    my_hash[row[0]]=avg

  sorted_hash = sorted( my_hash.items(), key=operator.itemgetter(1) )
  return sorted_hash



def commuter_index():
  mta_hour_list = format_data_hour().items()
  my_hash = {}

  for index, row in enumerate(mta_hour_list):

    station_info = row[0]
    time_info = row[1]

    key = tuple([station_info[0], station_info[1], station_info[3]])
    first_hour = time_info[0][0].hour

    if first_hour == 1 or first_hour == 2 or first_hour == 3:
      morning_val_rush = time_info[1][1]
      morning_val_non_rush = time_info[2][1]
    elif first_hour == 0:
      morning_val_rush = time_info[2][1]
      morning_val_non_rush = time_info[3][1]

    if first_hour == 0 or first_hour == 1 or first_hour == 2:
      evening_val_rush = time_info[4][1]
      evening_val_non_rush = time_info[5][1]
    elif first_hour == 3:
      evening_val_rush = time_info[3][1]
      evening_val_non_rush = time_info[4][1]

    val_rush = evening_val_rush + morning_val_rush
    val_non_rush = evening_val_non_rush + morning_val_non_rush

    commuter_index = val_rush - val_non_rush

    if key in my_hash:
      my_hash[key] += commuter_index
    else:
      my_hash[key] = commuter_index

  sorted_hash = sorted( my_hash.items(), key=operator.itemgetter(1) )

  return sorted_hash

# ====================================
#           DRIVER CODE
# ====================================

pprint(commuter_index())

# pprint(density_for_station())

# pprint(rush_entries)
# pprint(non_rush_entries)
# density_by_turnstile_hash()
# pprint( density_by_turnstile_hash() )

