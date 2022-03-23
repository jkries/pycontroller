"""Simple example showing how to get gamepad events."""

from __future__ import print_function

from inputs import get_gamepad

import requests, time, subprocess, serial
from datetime import datetime
import os.path
import os
from os import path

#D-Pad Left - ABS_HAT0X -1
#D-Pad Right - ABS_HAT0X 1
#D-Pad Up - ABS_HAT0Y -1
#D-Pad Down - ABS_HAT0Y 1

#Left Stick - ABS_X .. ABS_Y
#Right Stick - ABS_RX .. ABS_RY

print("~(o_o)~")

print("You may need to run this command to get your Com port or just ask Mr. Kries!")
print("python -m serial.tools.list_ports -v")
print("================================================================================================")

if path.exists("comport.txt"):
    #Load channel from text file
    f = open("comport.txt", "r")
    whatPort = f.read()
else:
    whatPort = input("\nWhat Com port are you using? ")
    f = open("comport.txt", "w")
    f.write(str(whatPort))
    f.close()
print("Using Com Port #" + str(whatPort))
#whatPort = 4
#whatPort = input("Enter the com port # from above: ")
print("================================================================================================")


if path.exists("channel.txt"):
    #Load channel from text file
    f = open("channel.txt", "r")
    botChannel = f.read()
else:
    botChannel = input("\nWhat channel are the controller & robot using? ")
    f = open("channel.txt", "w")
    f.write(str(botChannel))
    f.close()
print("Using channel " + str(botChannel) + " for transmissions to robot.")
print("================================================================================================")

#Configure the serial stuff
ser = serial.Serial()
ser.baudrate = 115200
ser.port = str('COM' + str(whatPort))

def sendCommandSerial(commandCheck):
    ser.open()
    # Using bytes(str, enc)
    # convert string to byte
    serialSend = bytes(commandCheck + '#', 'utf-8')
    ser.write(serialSend)
    ser.close()

def main():
    """Just print out some event infomation when the gamepad is used."""
    going = True

    stickOffset = 15000

    while going:
        events = get_gamepad()
        for event in events:
            if (event.code == "BTN_EAST"):
                if (event.state == 1):
                    print("B pressed")
                    toSend = "9"
                    sendCommandSerial(toSend)
                elif (event.state == 0):
                    print("B released")
            elif (event.code == "BTN_WEST"):
                if (event.state == 1):
                    print("X pressed")
                    toSend = "10"
                    sendCommandSerial(toSend)
                elif (event.state == 0):
                    print("X released")
            elif (event.code == "BTN_SOUTH"):
                if (event.state == 1):
                    print("A pressed")
                    toSend = "8"
                    sendCommandSerial(toSend)
                elif (event.state == 0):
                    print("A released")
            elif (event.code == "BTN_NORTH"):
                if (event.state == 1):
                    print("Y pressed")
                    toSend = "11"
                    sendCommandSerial(toSend)
                elif (event.state == 0):
                    print("Y released")

            #D-Pad
            elif (event.code == "ABS_HAT0X"):
                if (event.state == -1):
                    print("D Pad Left")
                    toSend = "1"
                    sendCommandSerial(toSend)
                elif (event.state == 1):
                    print("D Pad Right")
                    toSend = "2"
                    sendCommandSerial(toSend)
                elif(event.state == 0):
                    print("D Pad Released")
                    toSend = "5"
                    sendCommandSerial(toSend)
            elif (event.code == "ABS_HAT0Y"):
                if (event.state == -1):
                    print("D Pad Up")
                    toSend = "4"
                    sendCommandSerial(toSend)
                elif (event.state == 1):
                    print("D Pad Down")
                    toSend = "3"
                    sendCommandSerial(toSend)
                elif(event.state == 0):
                    print("D Pad Released")
                    toSend = "5"
                    sendCommandSerial(toSend)

            #Shoulder buttons
            elif (event.code == "ABS_RZ"):
                print("Right Trigger: " + str(event.state))
                toSend = "5"
                sendCommandSerial(toSend)
            elif (event.code == "ABS_Z"):
                print("Left Trigger: " + str(event.state))
                toSend = "5"
                sendCommandSerial(toSend)
            elif (event.code == "BTN_TR"):
                #print("Right Bumper: " + str(event.state))
                if (event.state == 1):
                    print("Right Bumper pressed")
                elif (event.state == 0):
                    print("Right Bumper released")
            elif (event.code == "BTN_TL"):
                #print("Left Bumper: " + str(event.state))
                if (event.state == 1):
                    print("Left Bumper pressed")
                elif (event.state == 0):
                    print("Left Bumper released")

            #Left Stick Forward/Back:
            elif (event.code == "ABS_Y"):
                #print("Left Stick: Y" + str(event.state))
                if (event.state >= stickOffset):
                    print("Left Stick Forward")
                    toSend = "7"
                    sendCommandSerial(toSend)
                elif (event.state <= -stickOffset):
                    print("Left Stick Reverse")
                    toSend = "6"
                    sendCommandSerial(toSend)
                elif (event.state == 0):
                    print("Left Stick released")
                else:
                    print("Left Stick released")
            #Left Stick Left/Right:
            elif (event.code == "ABS_X"):
                #print("Left Bumper: X" + str(event.state))
                if (event.state >= stickOffset):
                    print("Left Stick Right")
                elif (event.state <= -stickOffset):
                    print("Left Stick Left")
                elif (event.state == 0):
                    print("Left Stick released")
                else:
                    print("Left Stick released")

            #Right Stick Forward/Back:
            elif (event.code == "ABS_RY"):
                    #print("Left Stick: Y" + str(event.state))
                    if (event.state >= stickOffset):
                        print("Right Stick Forward")
                    elif (event.state <= -stickOffset):
                        print("Right Stick Reverse")
                    elif (event.state == 0):
                        print("Right Stick released")
                    else:
                        print("Right Stick released")
                #Left Stick Left/Right:
            elif (event.code == "ABS_RX"):
                    #print("Left Bumper: X" + str(event.state))
                    if (event.state >= stickOffset):
                        print("Right Stick Right")
                        toSend = "2"
                        sendCommandSerial(toSend)
                    elif (event.state <= -stickOffset):
                        print("Right Stick Left")
                        toSend = "1"
                        sendCommandSerial(toSend)
                    elif (event.state == 0):
                        print("Right Stick released")
                    else:
                        print("Right Stick released")

#print(event.ev_type, event.code, event.state)

if __name__ == "__main__":
    main()
