from rcu import *
import _thread
import os, subprocess, hashlib
#Poodle-anotaciones :
'''

mejora el descaergador
Arregla el esquivar
Mover objeto
'''

class argon:
     def __init__(self):
          pass
     def beep(self, time: int = 1):
          SetInBeep(1)
          SetWaitForTime(time)
          SetInBeep(0)
     def setMotors(self, motors: str | list, speed: int | list, time: int = 0, ) -> None:
          if type(motors) == list:
               for motor, key in motors:
                    SetMotor(motor, speed[key])
          if type(motors) == str:    
               SetMotor(motors, speed) 
          SetWaitForTime(time)

     def getLigthSensors(self, *ports:int):
          """
          Returns the values of the two light sensors.

          :return: A tuple containing the values of the two light sensors.
          """
          ls = []
          for sensor in ports:
               ls.append(GetLightSensor(sensor))
          return ls

     def detectObstacle(self, distance:int = 10, port: int = 1):
          return GetUltrasound(port) < distance

class Sephir:
     def __init__(self) -> None:
          pass
     
     class Motor(object):
          '''
          Return all of the motor property and information, speed encoder etc.
          '''
          def __init__(self):
               pass
     class Rcu:
          def __init__(self):
               self.id = self.getID()[0]
               self.uuid = self.getID()[1]
               
          # Left RCU button
          class leftButton(): 
               def __init__(self): 
                    pass
               # Defining __call__ method 
               def __call__(self): 
                    return GetLeftButton() 
               def onPressed(self, callback):
                    def whatsdas(callback):
                         while True:
                              if GetLeftButton() == True:
                                   callback()
                              SetWaitForTime(0.5)
                    _thread.start_new_thread(whatsdas, (callback))
          # Rigth RCU button
          class rightButton(): 
               def __init__(self): 
                    pass
               # Defining __call__ method 
               def __call__(self): 
                    return GetRightButton()
               def onPressed(self, callback):
                    def whatsdas(callback):
                         while True:
                              if GetRightButton() == True:
                                   callback()
                    _thread.start_new_thread(whatsdas, (callback))

          def getID():
               """
               Returns a unique identifier for the device.
               """
               # Get the system hostname
               hostname = os.uname().nodename

               # Get the machine ID
               try:
                    with open("/etc/machine-id", "r") as f:
                         machine_id = f.read().strip()
               except (IOError, OSError):
                    machine_id = ""

                    # Get the boot ID
                    try:
                         with open("/proc/sys/kernel/random/boot_id", "r") as f:
                              boot_id = f.read().strip()
                    except (IOError, OSError):
                         boot_id = ""

               # Combine the system information to generate a unique identifier
               unique_identifier = f"{hostname}-{machine_id}-{boot_id}"
               device_uuid = hashlib.sha256(unique_identifier.encode()).hexdigest()

               return [unique_identifier, device_uuid]
               