import math
import tanksheet


def main():

    print()
    print("Available Tanks to choose:")
    for key in tanksheet.availtanks:
        print("Tank: ", key)
    print()

    credbg = '\33[41m'
    cend = '\33[0m'
    cgreenbg = '\33[42m'
    cyellowbg = '\33[43m'
    cgreen = '\33[32m'

    again = "Y"

    while again == "Y":

        while True:

            fromtank = input("From Tank: ")  # Tank transfering from
            print()
            fromtank2 = fromtank
            if fromtank in tanksheet.availtanks.keys():  # if the tank exists, move to next step
                break
            else:
                print("Tank not available.")
                print()

        fromtank = tanksheet.availtanks.get(str(fromtank))
        print("Would you like to see the tank specs before continuing?")
        print()
        print("Enter 'Y' for yes or 'N' for no:")

        while True:

            specs = input()
            specs = specs.upper()
            if specs == "Y":
                print()
                print(tanksheet.tank_info.get(str(fromtank2)))
                print()
                break
            if specs == "N":
                break
            else:
                print("Please enter 'Y' for Yes or 'N' for No.")

        while True:
            try:

                print()
                lev1 = float(input("Enter current tank level in feet: "))
                if lev1 <= tanksheet.tank_max_fill.get(fromtank2):
                    print()
                    break
                else:
                    print()
                    print(credbg + "Warning: Level Too High." + cend)
                    print()
            except:
                pass
            print("Invalid Entry")

        tanksheet.current_tank_levs.get(str(fromtank)) == lev1

        while True:
            try:
                print()
                gal_tranfered = int(
                    input("Enter amount of gallons you are transfering: "))
                break
            except:
                pass
            print("Invalid Entry")

        lev2 = (gal_tranfered / int(fromtank))
        lev3 = (lev1 - lev2)

        while True:
            print()
            totank = input("To Tank: ")  # Tank transfering from
            totank2 = totank
            if totank in tanksheet.availtanks.keys():  # if the tank exists, move to next step
                break
            else:
                print("Tank not available.")

        print()
        totank = tanksheet.availtanks.get(str(totank))
        print("Would you like to see the tank specs before continuing?")
        print()
        print("Enter 'Y' for yes or 'N' for no:")
        print()

        while True:

            specs = input()
            specs = specs.upper()
            print()
            if specs == "Y":
                print(tanksheet.tank_info.get(str(totank2)))
                print()
                break
            if specs == "N":
                break
            else:
                print("Please enter 'Y' for Yes or 'N' for No.")

        totankmax = tanksheet.tank_max_fill.get(str(totank2))

        while True:
            try:
                print()
                lev4 = float(input("Enter current tank level in feet: "))
                if lev4 <= tanksheet.tank_max_fill.get(totank2):
                    print()
                    break

                else:
                    print()
                    print(credbg + "Warning: Level Too High." + cend)
                    print()
            except:
                pass
            print("Invalid Entry")
            print()

        print()
        enter = input("Press Enter to activate transfer..")

        tanksheet.current_tank_levs.get(str(totank)) == lev4
        lev5 = (gal_tranfered / int(totank))
        lev6 = (lev4 + lev5)

        if lev6 > int(totankmax):
            print()
            print(credbg + "WARNING OVERFILL" + cend)
            print()
            print(totank2, "Estimated Stop: ", credbg, "%.2f" % lev6, cend)
            print()
            print("Must not exceed", totank2, "Max Fill: ", totankmax)
        else:
            print()
            print(fromtank2, "Estimated Stop: ",
                  cgreenbg, "%.2f" % lev3, cend)
            print()
            print(totank2, "Estimated Stop: ",
                  cgreenbg, "%.2f" % lev6, cend)

        print()
        again = input("Do you want to make another transfer? Y/N: ")
        again = again.upper()

   # xgpf = 200
   # xmax = 30
   # xlev = 0
   # print()
   # y = float(input("Enter Gallons: "))
   # print()
   # xlev = xlev + (y / xgpf)
   # print(xlev)
   # print()
   # print()
   # print(tk416.info())
   # print()
   # print(tk403.info())
   # print()
   # print(tk408.info())
   # print()
   # print("The max capacity of 316 is: ", tk416.tkmax * tk416.tkgpf)
   # print()


main()
