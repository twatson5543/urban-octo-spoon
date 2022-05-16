# /////////////////////////////// Main Imports ///////////////////////////////
# Libraries
from smtplib import SMTP
import time
from datetime import datetime
# Python Files
import cfg

# ///////////////////////////////// Functions /////////////////////////////////


# Get Date and Time
def GetTimeDate():
    DateTime = datetime.now()
    CurrentTime = DateTime.strftime("%H%M%S")
    #print(CurrentTime)
    return CurrentTime


# Splice Time to just minutes and seconds
def TimeSplice(Time):
    TimeStr = str(Time)
    TimeMinSec = TimeStr[5:]
    #print(TimeMinSec)
    return TimeMinSec


# If Time = '0000' Return True
def TimeSpliceChk(TimeSplced):
    if TimeSplced == "0":
        print("True!")
        print(GetTimeDate())
        time.sleep(2)


# Send Email MSG
def EmailSend():
    print()


# ======================== Sequences ========================


def Sequence1():
    TimeDateNum = GetTimeDate()
    SecondsFinal = TimeSplice(TimeDateNum)
    TimeSpliceChk(SecondsFinal)


def SequenceLoop1():
    while True:
        Sequence1()
        time.sleep(0.2)


# ///////////////////////////// Main Sequence /////////////////////////////
SequenceLoop1()
