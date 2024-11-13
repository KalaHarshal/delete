class Classroom:
    # Static dictionary with all keys in lowercase for case-insensitive search
    classroom_list = {
        "a101": "left",
        "b102": "right",
        "c103": "left",
        "d104": "right",
        "e105": "left"
        # Add more classrooms as needed, all in lowercase
    }

    @staticmethod
    def search_classroom(class_room):
        # Convert input to lowercase to ensure case-insensitive comparison
        class_room = class_room.lower()

        # Search for the classroom in the classroom_list
        if class_room in Classroom.classroom_list:
            wing = Classroom.classroom_list[class_room]
            if wing == "left":
                return "Room in LEFT WING"
            else:
                return "Room in RIGHT WING"
        else:
            return "Not Found"

# Testing the implementation
class_room = input("Enter the classroom name to search: ")
result = Classroom.search_classroom(class_room)
print(result)
