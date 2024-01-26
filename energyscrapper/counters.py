# The script gets energy counters info
from connections import cursor


request = ("SELECT NAME, SERIALNUM, NUM_DEVICE, NUM_CH FROM CHANNEL")
cursor.execute(request)


def get_counters_info():
    """ Gets counters' info (number of a counter, what it counts) 
        from the database, filters the extra data and makes a list
        of the data. """
    all_counters_info=[]
    for i in  cursor.fetchall():
        counters_info=[]
        for j in i:
            counters_info.append((j)) 
        if not 'R-' in str(counters_info[0]):
            if not 'R+' in str(counters_info[0]):
                if not 'А-' in str(counters_info[0]):
                    if not 'A-' in str(counters_info[0]):
                        all_counters_info.append(counters_info)
    return all_counters_info


if __name__ == "__main__":
    counters = get_counters_info()
    for num, char  in enumerate (counters, 1):
        print(num, char)