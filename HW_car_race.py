# ДЗ 2. Перегони автомобілів

from random import randrange


class Car:
    
    def __init__(self, trip_distance, model, color):
        self.fuel = randrange(0, 9)
        self.trip_distance = trip_distance
        self.model = model
        self.color = color


    def move(self, distance):

        if isinstance(self, Car):

            if self.fuel < distance:
                self.trip_distance += self.fuel
                self.fuel = 0
            else:
                self.trip_distance += distance
                self.fuel -= distance

            return self.trip_distance
        
        else:
            raise AttributeError("Wrong instance!")

    

    def __str__(self):
        return f"{self.model} with distance: {self.trip_distance}"


 
race_dist = 0
desired_dist = randrange(1,9)

car_1 = Car(trip_distance=race_dist, model="Honda", color="gray")
car_2 = Car(race_dist, "Toyota", "white")
car_3 = Car(race_dist, "Subaru", "blue")

cars = [car_2, car_1, car_3]


while race_dist < desired_dist:

    for car in cars:
        race_dist = car.move(desired_dist)

        if race_dist >= desired_dist:
            winner = cars.index(car)
            print(cars.index(car))
            print(f"{car} - finished first!")
            break
    
    if race_dist < desired_dist:
        winner = 0
        print("There is no winner")
        break


for i in cars[winner + 1:]:
    i.move(desired_dist)

# print(f"dist is {desired_dist}")
print()

for car in cars:
    print(f"- {car}; fuel left - {car.fuel}")
