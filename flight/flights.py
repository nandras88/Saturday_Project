class Item:
    def __init__(self, carrier, carrier_name, airport, airport_name, arr_flights, arr_del15, arr_delay):
        self.cCode = carrier
        self.cName = carrier_name
        self.aCode = airport
        self.aName = airport_name
        self.flights = arr_flights
        self.delayed = arr_del15
        self.delayMinutes = arr_delay

def Zero( value ):
    if value == '':
        return '0.0'
    else:
        return value

file = open('flight_new.csv', 'r')

line = file.readline()
line = file.readline().strip()


items = []
szum = 0
while line:
    datas = line.split(';')
    datas[6] = Zero(datas[6])
    datas[7] = Zero(datas[7])
    datas[15] = Zero(datas[15])
    items.append(Item(datas[2], datas[3], datas[4], datas[5],
                      round(float(datas[6])),
                      round(float(datas[7])),
                      round(float(datas[15]))))
    line = file.readline().strip()

file.close()
