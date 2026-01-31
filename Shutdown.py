def shut_down(choice):
    if choice == "yes":
        print("Shutting down")
    else:
        print("abort shotdown")
User = input("Do you want to shutdown?")
shut_down(User)