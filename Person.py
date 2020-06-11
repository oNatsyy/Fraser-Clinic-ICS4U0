#-------------------------------------------------------
# Name:        Person.py
# Purpose:     Education purposes only, copying will be subject to plagiarism
# Author:      Syed Abidi
# Created:     2-February-2020
# Updated:     10-June-2020
#-------------------------------------------------------
class Person:

  '''
  A base class for the person

  Attributes
  ----------
  name : str
      name of person
  age : str
      age of person
  gender : str
      gender of person
  phone : str
      phone number of person
  residence : str
      residence of person
  '''
  
  def __init__(self,name,age,gender,phone,residence):

    '''
    A constructor for the base class

    Parameters
    -----------
    name : str
        name of person
    age : str
        age of person
    gender : str
        gender of person
    phone : str
        phone number of person
    residence : str
        residence of person
    '''
    
    self.name = name
    self.age = age
    self.gender = gender
    self.phone = phone
    self.residence = residence
