from login import login
from profile import display_profile
from dashboard import display_dashboard


def main():
    print("Welcome to Student Learning Portal")

    result = login("student", "1234")
    print(result)

    if result == "Login Successful":
        print("\nStudent Profile:")
        display_profile()

        print("\nStudent Dashboard:")
        display_dashboard()


if __name__ == "__main__":
    main()