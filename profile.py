def display_profile():
    student = {
        "name": "Arjun",
        "course": "Python Programming",
        "progress": "75%"
    }

    for key, value in student.items():
        print(f"{key.title()}: {value}")