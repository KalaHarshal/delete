#a
from datetime import datetime

current_datetime = datetime.now()

extract_year = lambda dt: dt.year
extract_month = lambda dt: dt.month
extract_day = lambda dt: dt.day
extract_time = lambda dt: dt.strftime("%H:%M:%S")

print("Year:", extract_year(current_datetime))
print("Month:", extract_month(current_datetime))
print("Day:", extract_day(current_datetime))
print("Time:", extract_time(current_datetime))


#b
cars = [
    {"make": "Toyota", "model": "Corolla", "color": "Blue"},
    {"make": "Honda", "model": "Civic", "color": "Black"},
    {"make": "Ford", "model": "Mustang", "color": "Red"},
    {"make": "Toyota", "model": "Camry", "color": "White"},
    {"make": "Honda", "model": "Accord", "color": "Grey"}
]

def sort_cars(cars_list, sort_key):
    return sorted(cars_list, key=lambda car: car[sort_key])

print("Sort by Make:")
sorted_by_make = sort_cars(cars, "make")
for car in sorted_by_make:
    print(car)

print("\nSort by Model:")
sorted_by_model = sort_cars(cars, "model")
for car in sorted_by_model:
    print(car)

print("\nSort by Color:")
sorted_by_color = sort_cars(cars, "color")
for car in sorted_by_color:
    print(car)


#c
subjects = [
    ("Math", 85),
    ("English", 78),
    ("Science", 92),
    ("History", 74),
    ("Art", 88)
]

def sort_subjects(subjects_list, sort_by="name"):
    if sort_by == "name":
        return sorted(subjects_list, key=lambda subject: subject[0])
    elif sort_by == "marks":
        return sorted(subjects_list, key=lambda subject: subject[1])
    else:
        raise ValueError("sort_by must be 'name' or 'marks'")

print("Sort by Subject Name:")
sorted_by_name = sort_subjects(subjects, "name")
for subject in sorted_by_name:
    print(subject)

print("\nSort by Marks:")
sorted_by_marks = sort_subjects(subjects, "marks")
for subject in sorted_by_marks:
    print(subject)
