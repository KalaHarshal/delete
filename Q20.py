import re

class InvalidVehicleNumberException(Exception):
    pass

def validate_vehicle_registration(vehicle_number):
    pattern = r'^[A-Za-z]{2}[0]{1}[0-9]{1}[A-Za-z]{1,2}[0-9]{4}$'
    
    if not re.match(pattern, vehicle_number):
        raise InvalidVehicleNumberException("Invalid Vehicle Registration Number")
    return "Valid Vehicle Registration Number"

def main():
    vehicle_number = input("Enter the Vehicle Registration Number: ")
    
    try:
        result = validate_vehicle_registration(vehicle_number)
        print(result)
    
    except InvalidVehicleNumberException as e:
        print(e)
    
    finally:
        print("Ride/Drive vehicles only if you have licence riding/driving the vehicle")

if __name__ == "__main__":
    main()
