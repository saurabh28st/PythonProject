def add_security(func):

    def wrapper():
        print("1.Before the function is called")
        print("2.Add Helmet,Dashcam,gloves,knee guard,License")
        func()      # driving scooty()

        print("3.After the function is called.")
        print("4.Secure Driving, Leave all the items")
    return wrapper()

@add_security
def drive_ola_scooter():
    print("ola")

@add_security
def drive_scooty():
    print("Normal Function!!")
    print("I am driving a scooty")