def generate_csv():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')
    yield ('2020-11-01', 'Toyota', 'Corolla', 2016, 24000)
    yield ('2020-11-02', 'Ford', 'Fusion', 2018, 33000)
    yield ('2020-11-03', 'Chevrolet', 'Volt', 2014, 14000)

all_csv_rows = list(generate_csv())
header, *rows = all_csv_rows[0], all_csv_rows[1:]
print(all_csv_rows)
#print('CSV Header:', header)
#print('CSV Row:', rows) 