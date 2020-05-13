class Item:
    def __init__(self, carrier, carrier_name, airport, airport_name, arr_flights, arr_del15, arr_delay):
        self.cCode = carrier
        self.cName = carrier_name
        self.aCode = airport
        self.aName = airport_name
        self.flights = arr_flights
        self.delayed = arr_del15
        self.delayMinutes = arr_delay

class Carrier:
    delayedPercent = 0
    avgLate = 0

    def __init__(self, cCode, cName, flights, delayed, delayMinutes, aCode):
        self.cCode = cCode
        self.cName = cName
        self.flights = flights
        self.delayed = delayed
        self.delayedMinutes = delayMinutes
        self.visited = set()
        self.visited.add(aCode)

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

carriers = []
carrierDatas = []
for item in items:
    try:
        index = carriers.index(item.cName)
    except Exception:
        carriers.append(item.cName)
        carrierDatas.append(Carrier(item.cCode, item.cName, item.flights,
                                    item.delayed, item.delayMinutes, item.aCode))
    else:
        carrierDatas[index].flights += item.flights
        carrierDatas[index].delayed += item.delayed
        carrierDatas[index].delayedMinutes += item.delayMinutes
        carrierDatas[index].delayedPercent = carrierDatas[index].delayed / carrierDatas[index].flights * 100
        carrierDatas[index].avgLate = carrierDatas[index].delayedMinutes / carrierDatas[index].flights
        carrierDatas[index].visited.add(item.aCode)


file = open('carriers.txt','w')
print('{0:4s} {1:*^30s}{2:>8}{3:>8}{4:>8} {5} {6:8} {7}'.format(
    'Code','Name of the Airline','Flights','Delayed','Minutes','Delayed %','Avg Minutes','Visited Airports'
))
file.write('{0:4s} {1:*^30s}{2:>8}{3:>8}{4:>8} {5} {6:8} {7}'.format(
    'Code','Name of the Airline','Flights','Delayed','Minutes','Delayed %','Avg Minutes','Visited Airports'
)+'\n')

for carrier in carrierDatas:
    print('{0:>4s} {1:>30s}{2:8}{3:8}{4:8} {5:8.2f}% {6:>11.2f} {7:>16}'.format(
        carrier.cCode, carrier.cName, carrier.flights, carrier.delayed,
        carrier.delayedMinutes, carrier.delayedPercent,
        carrier.avgLate, len(carrier.visited)
    ))
    file.write('{0:>4s} {1:>30s}{2:8}{3:8}{4:8} {5:8.2f}% {6:>11.2f} {7:>16}'.format(
        carrier.cCode, carrier.cName, carrier.flights, carrier.delayed,
        carrier.delayedMinutes, carrier.delayedPercent,
        carrier.avgLate, len(carrier.visited)
    )+'\n')
file.close()