
def file_reader():

    try:

        file_name = input("\nEnter a file name to be read: ")

        with open(f"{file_name}", "r") as file1:
            file_contents = file1.read()

        print(f"\nFile Contents: \n {file_contents}")

    except FileNotFoundError as error:
        print("\nOops the file you are accessing does not exists")
        print(f"{error=} \n")

    except ValueError as error:
        print(f"YOU SHOULD HAVE KNOWN BETTER! \n {error=} \n ")

    except OSError as error:
        print(f"What??")

    except Exception as error:
        print("Shrugs")
        print(f"{error=} \n")



file_reader()

















