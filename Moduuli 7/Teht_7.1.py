seasons = ("Winter", "Spring", "Summer", "Fall")
month_number = int(input("Give a months number: "))



while month_number !=0:
    if month_number == 12 or month_number == 1 or month_number == 2:
        print(f"{month_number}. is in {seasons[0]}")
    elif month_number == 3 or month_number == 4 or month_number == 5:
        print(f"{month_number}. is in {seasons[1]}")
    elif month_number == 6 or month_number ==  7 or month_number == 8:
        print(f"{month_number}. is in {seasons[2]}")
    elif month_number == 9 or month_number == 10 or month_number == 11:
        print(f"{month_number}. is in {seasons[3]}")

    break

