"""
COMP 1110 Fall 2026 Group Project
Group Members: Jacob Feser, Tadiwanashe Dondo, Munashe Isaac Chapoka
Everyday Useful Calculator
"""

from rich import print

# Global Variables Checked / called by the Log Function
times_called = 0


def main():
    """ Function # 1: The Main Function
    The Main method doubles as the Menu Function
    Author: Jacob Feser
    """
    print("COMP 1110 Project Fall 2026\nJacob Feser, Tadiwanashe Dondo, Munashe Isaac Chapoka")
    print("Select an Option (Type the Option Number to use that function):\n 1. [underline]L[/underline]oan Interest Calculator\n 2. [underline]U[/underline]nit Converter\n 3. u[underline]S[/underline]eful Car Details Calculator\n 4. [underline]C[/underline]urrency Converter\n 5. [underline]P[/underline]aint Area Calculator\n 6. [underline]D[/underline]iscount Calcuator\n 7. [underline]E[/underline]lectricity Cost Calcuator\n 0. e[underline]X[/underline]it")
    inputcode = "1"
    while True:
        inputcode = input("Code: ")
        match inputcode:
            case 'X':
                print("Exiting Program, Thank you for using [bold]The Everyday Calculator[/bold]")
                Log(1,"Menu","{inputcode}, Exit")
                break
            case '0':
                print("Exiting Program, Thank you for using [bold]The Everyday Calculator[/bold]")
                Log(1,"Menu","{inputcode}, Exit")
                break
            case 'L':
                print("Loan Interest Calculator Selected")
                Log(1,"Menu","{inputcode}, LIC")
                LoanInterest
            case '1':
                print("Loan Interest Calculator Selected")
                Log(1,"Menu","{inputcode}, LIC")
                LoanInterest
            case 'U':
                print("Unit Converter Selected")
                Log(1,"Menu","{inputcode}, UC")
                UnitConverter
            case '2':
                print("Unit Converter Selected")
                Log(1,"Menu","{inputcode}, UC")
                UnitConverter
            case 'S':
                print("Useful Car Details Calculator Selected")
                Log(1,"Menu","{inputcode}, CDC")
                CarDetails
            case '3':
                print("Useful Car Details Calculator Selected")
                Log(1,"Menu","{inputcode}, CDC")
                CarDetails
            case 'C':
                print("Currency Converter Selected")
                Log(1,"Menu","{inputcode}, CC")
                CurrencyConverter
            case '4':
                print("Currency Converter Selected")
                Log(1,"Menu","{inputcode}, CC")
                CurrencyConverter
            case 'P':
                print("Paint Area Calculator Selected")
                Log(1,"Menu","{inputcode}, PAC")
                Paint
            case '5':
                print("Paint Area Calculator Selected")
                Log(1,"Menu","{inputcode}, PAC")
                Paint
            case 'D':
                print("Discount Calculator Selected")
                Log(1,"Menu","{inputcode}, DC")
                Discount
            case '6':
                print("Discount Calculator Selected")
                Log(1,"Menu","{inputcode}, DC")
                Discount
            case 'E':
                print("Electricity Cost Calculator Selected")
                Log(1,"Menu","{inputcode}, ECC")
                ElectricityCost
            case '7':
                print("Electricity Cost Calculator Selected")
                Log(1,"Menu","{inputcode}, ECC")
                ElectricityCost
            


def LoanInterest():
    """Function # 2: The Loan Interest Calculator
    Author: Tadiwanashe Dondo
    """

def UnitConverter():
    """Function # 3: The Unit Converter
    Author: Tadiwanashe Dondo
    """

def CarDetails():
    """Function # 4: The Useful Car Details Calculator
    Author: Munashe
    """ 
    fuel_cost = liters*price 

def CurrencyConverter():
    """Function # 5: The Currency Converter
    Author: Jacob Feser
    """

def Paint():
    """Function # 6: The Paint (Area) Calculator
    Author: Munashe
    """

def Discount():
    """Function # 7: The Discount Calculator
    Author: Munashe
    """

def ElectricityCost():
    """Function # 8: The Electricity Cost Calculator
    Author: Tadiwanashe Dondo
    """

def Log(fxnnum, fxnname, calldetails):
    """Function # 9: The Data Log Function
    Author: Jacob Feser
    """
    

main()
