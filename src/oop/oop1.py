# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#This is the base vehicle
class Vehicle:
    pass

class FlightVehicle(Vehicle): #Inheriting from Vehicle
    pass

class Starship(FlightVehicle): #Inheriting from FlightVehicle
    pass

class GroundVehicle(Vehicle): #Inheriting from Vehicle
    pass

class Car(GroundVehicle): #Inheriting from GroundVehicle
    pass

class Motorcycle(GroundVehicle): #Inheriting from GroundVehicle
    pass

class Airplane(FlightVehicle): #Inheriting from FlightVehicle
    pass

