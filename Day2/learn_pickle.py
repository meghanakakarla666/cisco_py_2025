import pickle
flight={'flight_number':'1700','airline':'Indigo','capacity':180,'price':5000}
file_name='flight.dat'
with open(file_name,'wb') as writer:
    pickle.dump(flight,writer)
    print("saved the flight to file")

with open(file_name,'rb') as reader:
    flight_from_file=pickle.load(reader)
    print(flight_from_file)