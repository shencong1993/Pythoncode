months=['January','February','March','April','May','June',
        'July','August','September','October','November','December']

endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']

year = raw_input('Please input year: ')
month = raw_input('Please input month(1-12): ')
day = raw_input('Please input day(1-31): ')

month_number=int(month)
day_number= int(day)

ordinal = day+endings[day_number-1]+'.'+months[month_number-1]

print ordinal+'.'+year