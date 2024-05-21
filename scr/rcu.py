from time import sleep
from random import randint
def SetMotor(motor, speed):
     print(f'Motor {motor} Set To {speed}')
def SetInBeep(onoff):
     print(f"> Beep {onoff}")
def SetWaitForTime(time):
     print(f"> Waiting {time}")
     sleep(time)
def GetLightSensor(sensor_id):
     return randint(100, 3000)
def GetUltrasound(sensor_id):
     return randint(0, 100)
def GetColorSensor(nolose, sensor_id):
     return randint(0, 100)
def GetLeftButton():
     if randint(0, 5) == 4 :
          return True
     return False
def GetRightButton():
     if randint(0, 5) == 4 :
          return True
     return False