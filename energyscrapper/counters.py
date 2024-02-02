# The script gets energy counters info
import re
from connections import cursor


def get_counters_info():
    """ Gets counters' info (number of a counter, what it counts)
        from the database, filters the extra data and makes a list
        of the data. """
    request = ("""
            SELECT 
            NAME, 
            SERIALNUM, 
            NUM_DEVICE, 
            NUM_CH 
            FROM CHANNEL
            """)
    cursor.execute(request)
    all_counters_info = []
    for i in cursor.fetchall():
        counters_info = []
        for j in i:
            counters_info.append((j))
        reg = r"R\-|R\+|A\-|А\-"
        if not re.findall(reg, str(counters_info[0])):
            all_counters_info.append(counters_info)
    return all_counters_info


if __name__ == "__main__":
    counters = get_counters_info()
    for num, char in enumerate(counters, 1):
        print(num, char)