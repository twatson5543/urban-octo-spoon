# /////////////////////////////// Main Imports ///////////////////////////////
# Libraries
from smtplib import SMTP
import time
from datetime import datetime
# Python Files
import cfg

# ///////////////////////////////// Functions /////////////////////////////////


# /// Sequence1
# Get Date and Time
def GetTimeDate():
    DateTime = datetime.now()
    CurrentTime = DateTime.strftime("%H%M%S")
    #print(CurrentTime)
    return CurrentTime


# Splice Time to just minutes and seconds
def TimeSplice(Time):
    TimeStr = str(Time)
    TimeMinSec = TimeStr[4:]
    #print(TimeMinSec)
    return TimeMinSec


# If Time = '0000' Return True
def TimeSpliceChk(TimeSplced):
    if TimeSplced == "00":
        print("True!")
        print(GetTimeDate())
        time.sleep(2)
        return True
    else:
        return False


# /// Sequence3
# Send Email MSG
def EmailSend():
    print()


# ======================== Sequences ========================


# Getting Time, splicing it, and verifying it to be at certain time(s)
def Sequence1():
    # Getting Time as a number
    Time_AsNum = GetTimeDate()
    # Splicing number to just minutes and seconds
    SplicedTime = TimeSplice(Time_AsNum)
    # Checks if Spliced time == '0000' so that returns True hourly
    ChckVerify = TimeSpliceChk(SplicedTime)
    return ChckVerify


def Sequence2(RunPrgm):
    if RunPrgm == True:
        print("Sequence2 Running...")


def Sequence3():
    print()


# ========================== Loops ==========================


# Main Loop
def SequenceLoop1():
    while True:
        # Run Sequence1
        Seq1 = Sequence1()
        # Run Sequence2
        Sequence2(Seq1)
        # End of Loop Delay
        time.sleep(0.25)


# ///////////////////////////// Main Sequence /////////////////////////////
# Main Program
SequenceLoop1()
# // End of Program
