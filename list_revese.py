from datetime import datetime, timedelta


def get_date_range(from_Date, to_Date):
    date_list = []
    temp_date = from_Date
    while temp_date <= to_Date:
        date_list.append(temp_date.strftime('%d-%b-%Y'))  #('%Y-%m-%d'))
        temp_date += timedelta(days=1)
    date_list.reverse()
    return date_list # example: ['2024-03-10','2024-03-09','....','2024-02-28']


fromDate = datetime(2024, 2, 27, 0, 0, 0).date() #date.today()
toDate = datetime(2024, 3, 8, 0, 0, 0).date() #date.today()

date_range = get_date_range(from_Date=fromDate, to_Date=toDate)
print(date_range)
print()
master_data = {'08-Mar-2024': 0, '07-Mar-2024': 1, '06-Mar-2024': 2, '04-Mar-2024': 4, '03-Mar-2024': 5, '02-Mar-2024': 6, '29-Feb-2024': 8, '28-Feb-2024': 9, '27-Feb-2024': 10}
print(master_data)


obtained_records = []
for each_date in date_range:
    if not master_data.get(each_date,False):
        pass
    else:
        obtained_records.append(master_data[each_date])
print(obtained_records)