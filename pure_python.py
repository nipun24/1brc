if __name__ == '__main__':
    res = {}
    with open('measurements.txt', 'r') as f:
        for i in f:
            city, temp = i.strip().split(";")
            if res.get(city):
                res[city][0] = min(res[city][0], float(temp))  # min
                res[city][1] = max(res[city][1], float(temp))  # max
                res[city][2] = res[city][2] + float(temp)  # sum
                res[city][3] = res[city][3] + 1  # count
            else:
                d = [None, None, None, None]
                temp_float = float(temp)
                d[0] = temp_float
                d[1] = temp_float
                d[2] = temp_float
                d[3] = 1
                res[city] = d

    out = [f'{i}={res[i][0]}/{round(res[i][2] / res[i][3], 1)}/{res[i][1]}' for i in sorted(res.keys())]
    print(f'{{{", ".join(out)}}}')
