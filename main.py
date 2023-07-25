def car_pooling():
    trip_data = input("Enter trip data (comma-separated for each trip's data): ")
    trip_data = trip_data.split(',')
    row = len(trip_data) // 3
    car = []
    passenger = 0
    for i in range(row):
        start_index = i * 3
        num_passengers = int(trip_data[start_index])
        from_location = int(trip_data[start_index + 1])
        to_location = int(trip_data[start_index + 2])
        car.append([num_passengers, from_location, to_location])
        passenger += num_passengers
    capacity = int(input("Enter the car's capacity: "))
    count = 0
    if passenger == capacity:
        for i in range(row):
            if car[i][1] < car[i][2]:
                count += 1
        if count == row:
            return True
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    result = car_pooling()
    print(result)
