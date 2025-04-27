
'''
    The brains behind a simple vending machine to be run by a Raspberry Pi Zero or other python microcontroller
    Allows user to push a button once per day to dispense a drink. Users get one drink per day, and a spare per week.
    Any unused drinks become spare drinks at the end of the day.
'''
import RPi.GPIO as GPIO
import time
from datetime import datetime


# Simulate button press (To be done later with R.Pi)
# Check if today's drink has been used
# If so, check if a spare is available
# At the end of the day, roll today's unused drink over to the spares
# needs simple storage to track amounts

def CheckDrinkTotals(drink_type):
    # return number of available drinks of the given type
    check_file = 'sparedrinks.txt'
    remaining = 0
    if drink_type.lower() == 'daily':
        check_file = 'dailydrink.txt'
    try:
        with open(check_file,'r') as file:
            remaining = int(file.read)
    except Exception as e:
        print(e)
    return remaining

def UseTodaysDrink():
    with open('dailydrink.txt','w') as file:
        file.write('0')

def UseSpareDrink():
    with open('sparedrinks.txt','wr') as file:
        current_total = int(file.readline())
        file.write(current_total-1)

def RollDrinksOver():
    today_amount = CheckDrinkTotals('daily')
    add_amount = 0
    if today_amount:
        add_amount += 1
    if datetime.today().weekday() == 0:
        add_amount += 1
    with open('sparedrinks.txt','wr') as file:
        current_total = int(file.readline())
        file.write(current_total + add_amount)
    with open('dailydrinks.txt','w') as file:
        file.write('1')

def MakeMachineVend():
    failsafe_count = 30
    # Send signal to machine
    while True and failsafe_count > 0:
        time.sleep(1)
        #Check if GPIO sensor tripped
        failsafe_count -= 1
    return failsafe_count > 0

def ButtonPressed():
    if CheckDrinkTotals('daily'):
        if MakeMachineVend():
            UseTodaysDrink()
    elif CheckDrinkTotals('spare'):
        if MakeMachineVend():
            UseSpareDrink()


if __name__ == '__main__':
    last_day = datetime.now().day
    while True:
        #wait for button press
        # Check if time is after midnight
        if datetime.now().day != last_day:
            RollDrinksOver()
            last_day = datetime.now().day
        time.sleep(1)
        pass