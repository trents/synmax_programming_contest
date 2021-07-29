""" Voyage Predictor """

def most_common(lst):
    return max(set(lst), key=lst.count)

class Voyage:
    def __init__(self, vessel, start_port, end_port):
        self.vessel = int(vessel)
        self.start_port = int(start_port)
        self.end_port = int(end_port)

    def __str__(self):
        return "Vessel: " + str(self.vessel) + ", Start Port: " + str(self.start_port) + ", End Port: " + str(self.end_port)

# munge the voyage data
        
with open("voyages.csv") as file:
    d = file.readlines()
raw_voyage_data = []
for line in d:
    raw_voyage_data.append(line.strip())

del(raw_voyage_data[0])

voyages_list = []

for voyage in raw_voyage_data:
    temp_array = voyage.split(",")
    voyages_list.append(Voyage(temp_array[0],temp_array[3],temp_array[4]))

# get a list of distinct vessels

vessel_list = []

for voyage in voyages_list:
    if voyage.vessel not in vessel_list:
        vessel_list.append(voyage.vessel)

# make predictions for each vessel

final_predictions = []

for vessel in vessel_list:
    voyage_vessel_list = []
    for voyage in voyages_list:
        if(voyage.vessel == vessel):
            voyage_vessel_list.append(voyage) # just creates an array of voyages for this vessel

    voyage1_start = voyage_vessel_list[len(voyage_vessel_list)-1].end_port # start for first voyage
    voyage1_end = 0
    voyage2_start = 0
    voyage2_end = 0
    voyage3_start = 0
    voyage3_end = 0

    voyage_end_possible = []
    for voyage in voyage_vessel_list:
        if voyage.start_port == voyage1_start and voyage.end_port != voyage1_start:
            voyage_end_possible.append(voyage.end_port)

    if len(voyage_end_possible) == 1:
        voyage1_end = voyage_end_possible[0]
    elif len(voyage_end_possible) > 1:
        temp_v_e_p = []
        for voyage_end_number in voyage_end_possible:
            if voyage_end_number != voyage1_start:
                temp_v_e_p.append(voyage_end_number)
        voyage1_end = most_common(temp_v_e_p)
    elif len(voyage_vessel_list) == 1:
        voyage1_end = voyage_vessel_list[0].start_port
    else:
        for voyage in voyage_vessel_list:
            if voyage != voyage1_start:
                voyage_end_possible.append(voyage.end_port)
        if(len(voyage_end_possible) > 0):
            voyage1_end = most_common(voyage_end_possible)
        else:
            voyage1_end = voyage_vessel_list[0].end_port
#    print("Vessel: " + str(vessel) + ", Voyage 1 Start: " + str(voyage1_start) + ", Voyage 1 End: " + str(voyage1_end))   
    final_predictions.append(str(vessel) + "," + str(voyage1_start) + "," + str(voyage1_end) + ",1")

    voyage2_start = voyage1_end

    voyage_end_possible = []
    for voyage in voyage_vessel_list:
        if voyage.start_port == voyage2_start and voyage.end_port != voyage2_start:
            voyage_end_possible.append(voyage.end_port)

    if len(voyage_end_possible) == 1:
        voyage2_end = voyage_end_possible[0]
    elif len(voyage_end_possible) > 1:
        temp_v_e_p = []
        for voyage_end_number in voyage_end_possible:
            if voyage_end_number != voyage2_start:
                temp_v_e_p.append(voyage_end_number)
        voyage2_end = most_common(temp_v_e_p)
    elif len(voyage_vessel_list) == 1:
        voyage2_end = voyage_vessel_list[0].start_port
    else:
        for voyage in voyage_vessel_list:
            if voyage != voyage2_start:
                voyage_end_possible.append(voyage.end_port)
        if(len(voyage_end_possible) > 0):
            voyage2_end = most_common(voyage_end_possible)
        else:
            voyage2_end = voyage_vessel_list[0].end_port
#    print("Vessel: " + str(vessel) + ", Voyage 2 Start: " + str(voyage2_start) + ", Voyage 2 End: " + str(voyage2_end))
    final_predictions.append(str(vessel) + "," + str(voyage2_start) + "," + str(voyage2_end) + ",2")

    voyage3_start = voyage2_end

    voyage_end_possible = []
    for voyage in voyage_vessel_list:
        if voyage.start_port == voyage3_start and voyage.end_port != voyage3_start:
            voyage_end_possible.append(voyage.end_port)

    if len(voyage_end_possible) == 1:
        voyage3_end = voyage_end_possible[0]
    elif len(voyage_end_possible) > 1:
        temp_v_e_p = []
        for voyage_end_number in voyage_end_possible:
            if voyage_end_number != voyage2_start:
                temp_v_e_p.append(voyage_end_number)
        if(len(temp_v_e_p) > 0):
            voyage3_end = most_common(temp_v_e_p)
        elif voyage3_start != voyage_vessel_list[0].end_port:
            voyage3_end = voyage_vessel_list[0].end_port
        else:
            voyage3_end = voyage_vessel_list[0].start_port
    elif len(voyage_vessel_list) == 1:
        voyage3_end = voyage_vessel_list[0].start_port
    else:
        for voyage in voyage_vessel_list:
            if voyage != voyage3_start:
                voyage_end_possible.append(voyage.end_port)
        if(len(voyage_end_possible) > 0):
            voyage3_end = most_common(voyage_end_possible)
        else:
            voyage3_end = voyage_vessel_list[0].end_port
#    print("Vessel: " + str(vessel) + ", Voyage 3 Start: " + str(voyage3_start) + ", Voyage 3 End: " + str(voyage3_end))
    final_predictions.append(str(vessel) + "," + str(voyage3_start) + "," + str(voyage3_end) + ",3")

file3 = open("predict.csv","w")
file3.write("vessel,begin_port_id,end_port_id,voyage\n")
for line in final_predictions:
    file3.write(line + "\n")
file3.close()
