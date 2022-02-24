usernameInput = input("Username : ")
passwordInput = input("Password : ")
guava = 20
potato = 10
durian = 120
vat = 7/100

if usernameInput == "Take" and passwordInput == "1234" :
    print("Welcome to AllTake Shop")
    print("----------------------------")
    print("           MENU           ")
    print("1. Guava               : ",guava,"THB")
    print("2. Sweet potato        : ",potato,"THB")
    print("3. Durian              : ",durian,"THB")
    print("----------------------------")
    product = (input("add to cart : "))
    a = int(input("How many do you want? >> "))

    if product == "guava":
        print("Price :",guava*a,"THB")
        print("vat 7% :",(guava*a)*vat,"THB")
        print("Total :  ",(guava*a)+((guava*a)*vat),"THB")
        print("Thank you")

    elif product == "sweet potato":
        print("Price :",potato*a,"THB")
        print("vat 7% :", (potato*a)*vat, "THB")
        print("Total :  ", (potato*a)+((potato*a)*vat), "THB")
        print("Thank you")

    else:
        print("Price :",durian*a,"THB")
        print("vat 7% :", (durian*a) *vat, "THB")
        print("Total :  ", (durian * a) + ((durian * a) * vat), "THB")
        print("Thank you")

else:
    print("Wrong password,please try again.")
