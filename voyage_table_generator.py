""" Voyage Table Generator """

class Port:
    def __init__(self, port, lat, long):
        self.port = int(port)
        self.lat = float(lat)
        self.long = float(long)

class Location:
    def __init__(self, vessel, date, lat, long, heading, speed, draft):
        self.vessel = int(vessel)
        self.date = date
        self.lat = float(lat)
        self.long = float(long)
        self.heading = heading
        self.speed = speed
        self.draft = draft

    def __str__(self):
        return "Vessel: " + self.vessel + "\nDate: " + self.date + "\nLatitude: " + self.lat + "\nLongitude: " + self.long + "\nHeading: " + self.heading + "\nSpeed: " + self.speed + "\nDraft: " + self.draft

    def __lt__(self, other):
        return self.vessel < other.vessel

# munge the location data
        
with open("tracking.csv") as file:
    d = file.readlines()
tracking_data = []
for line in d:
    tracking_data.append(line.strip())

del(tracking_data[0])

tracking_data.sort()

with open("ports.csv") as file2:
    e = file2.readlines()
raw_port_data = []
for line in e:
    raw_port_data.append(line.strip())

del(raw_port_data[0])

long_array = []

for line in tracking_data:
    temp_array = line.split(",")
    long_array.append(Location(temp_array[0],temp_array[1],temp_array[2],temp_array[3],temp_array[4],temp_array[5],temp_array[6]))

# munge the port data

raw_port_data.sort()

port_data = []

for line in raw_port_data:
    temp_array = line.split(",")
    port_data.append(Port(temp_array[0],temp_array[1],temp_array[2]))

# identify a port for every line that we can

i = 0

locs_with_ports = []

prev_port = port_data[0]
prev_loc = long_array[0]
voyages = []

for loc in long_array:
    for port in port_data:
        if abs(port.long - loc.long) < 0.01 and abs(port.lat - loc.lat) < 0.01:
            if prev_port != port and loc.vessel != prev_loc.vessel:
                prev_port = port
                prev_loc = loc
            elif prev_port != port:
                voyages.append(str(loc.vessel) + "," + str(prev_loc.date) + "," + str(loc.date) + "," + str(prev_port.port) + "," + str(port.port))
                prev_port = port
                prev_loc = loc

    i += 1

file3 = open("voyages.csv","w")
file3.write("vessel,begin_date,end_date,begin_port_id,end_port_id\n")
for line in voyages:
    file3.write(line + "\n")
file3.close()
