import csv
from datetime import *
from dateutil.relativedelta import *
import calendar
import dateutil.parser
import matplotlib.pyplot as plt
from pprint import pprint


# CHALLENGE ONE
def format_data():
  with open("turnstile_150404.txt", "r") as turn_data:
    reader=csv.reader(turn_data)
    my_hash={}
    for row in reader:
        key = tuple(row[0:4])
        val = row[4:-1]
        # check if the key, val exists
        if key in my_hash:
            my_hash[key].append( val )
        else:
            my_hash[key] = [ val ]
  return my_hash


# CHALLENGE TWO AND THREE
def fetch_data():
  my_list=[]
  with open("turnstile_150404.txt", "r") as turn_data:
    reader=csv.reader(turn_data)
    reader.next()
    for row in reader:
      my_list.append(row)

  return my_list


# CHALLENGE TWO
def format_data_hour():
  my_hash={}
  the_list = fetch_data()
  for index, row in enumerate(the_list):
    key = tuple(row[0:4])
    time_str = row[6] + " " + row[7]
    time = dateutil.parser.parse( time_str )
    if index == len(the_list)-1:
      count = "Fuck This Value Of The Day"
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


def split_date_and_time():
  my_hash = format_data_day()
  vals = my_hash.values()
  return vals



pprint(format_data_day())
# print count_by_day()
# print format_data_day()
# print split_date_and_time()


