import csv
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
print my_hash[my_hash.keys()[0]]