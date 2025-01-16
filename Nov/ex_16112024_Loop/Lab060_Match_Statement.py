# Match Statement -> It's like switch statement in Java

# WAP to ask the user which browser he wants to run automation.

browser_name = input("Enter the browser name :")

match browser_name:
    case "firefox":
        print("Starting Firefox!!!!")
    case "chrome":
        print("Execute the Chrome Code")
    case "edge":
        print("Execute the Edge Code")
    case "safari":
        print("Execute the Safari Code")
    case _:
        print("Browser not Found")