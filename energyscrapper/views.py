# Here willbe the main logic

# def get_counters_consumption():
#     """ Gets energy consumption data from the database,
#             looks for which the data belongs to which counter,
#             makes a list of the summed up data. """
#     counters = get_counters_info()
#     request = (f"SELECT NUM_DEVICE, NUM_CH , DT_DAY,TARIF1, TARIF2, TARIF3 FROM IMPULS4 WHERE DT_DAY='{sql_date}'")
#     cursor.execute(request)
#     all_counters_consumption = []
#     for consumption in cursor.fetchall():
#         for counter in counters:
#             one_counter_consumption = []
#             if counter[3] == consumption[1]:
#                 if counter[2] == consumption[0]:
#                     one_counter_consumption.append(counter[1])
#                     total_consumption = round(consumption[3]+consumption[4]+consumption[5], 2)
#                     one_counter_consumption.append(total_consumption)
#                     break
#             all_counters_consumption.append(one_counter_consumption)
#     return all_counters_consumption
