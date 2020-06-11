#-------------------------------------------------------
# Name:        patient.py
# Purpose:     Education purposes only, copying will be subject to plagiarism
# Author:      Syed Abidi
# Created:     2-February-2020
# Updated:     10-June-2020
#-------------------------------------------------------
from Person import Person

class Patient(Person):

  '''
  A derived class for person

  Attributes
  ----------
  reason : str
      reason of the patient's appointment
  time : str
      time given for patient's appointment
  '''
  
  def __init__(self,reason,name,age,gender,phone,residence,time):
  
    '''
    A constructor for the Patient class

    Parameters
    ----------
    name : str
        name of patient
    age : str
        age of patient
    gender : str
        gender of patient
    phone : str
        phone number of patient
    residence : str
        residence of patient
    reason : str
        reason of the patient's appointment
    time : str
        time given for patient's appointment
    '''

    self.reason = reason
    self.time = time
    super().__init__(name,age,gender,phone,residence)
