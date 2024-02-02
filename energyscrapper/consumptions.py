# The script gets the energy consumption info
from datetime import datetime, timedelta
from connections import cursor


def get_counters_consumption(data_date):
    """ Gets all the energy consumption data from the database. """
    request = (f"""
        SELECT 
        NUM_DEVICE,
        NUM_CH, 
        DT_DAY,
        TARIF1, 
        TARIF2, 
        TARIF3 
        FROM IMPULS4 
        WHERE 
        DT_DAY='{data_date}'
        """)
    cursor.execute(request)
    return cursor.fetchall()


if __name__ == "__main__":
    yesterday = datetime.today()-timedelta(days=16)
    sql_date = yesterday.strftime("%Y-%m-%d") 
    all_consumptions = get_counters_consumption(sql_date)
    for num, char in enumerate(all_consumptions, 1):
        print(num, char)


