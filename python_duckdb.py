import duckdb

if __name__ == '__main__':
    res = duckdb.sql('''
    SELECT city, MIN(temp) as 'min', MAX(temp) as 'max', ROUND(AVG(temp), 1) as 'avg'
    from read_csv('measurements.txt',
        delim = ';',
        header = false,
        columns = {
            'city': 'VARCHAR',
            'temp': 'DECIMAL(8,1)'
        })
    GROUP BY city
    ORDER BY city ASC;
    ''')

    out = [f'{i[0]}={i[1]}/{i[3]}/{i[2]}' for i in res.fetchall()]
    print(f'{{{", ".join(out)}}}')
