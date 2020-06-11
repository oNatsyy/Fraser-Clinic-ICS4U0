#-------------------------------------------------------
# Name:        mysort.py
# Purpose:     Education purposes only, copying will be subject to plagiarism
# Author:      Syed Abidi
# Created:     2-February-2020
# Updated:     10-June-2020
#-------------------------------------------------------
from tkinter import *
import sqlite3
from tkinter import messagebox 
from datetime import datetime
from patient import Patient

conn = sqlite3.connect('database.db')
c = conn.cursor()

# An empty to list to append the id's from our database
ids = [""]

class MySort:

  '''
  This is a base-class used for sorting

  Attributes
  ----------
  None

  Methods
  ----------
  None

  '''

  def __init__(self):

    '''
    A constructor to implement sorting

    Parameters
    ----------
    None

    '''

    # Used to get the number of set appointments and show them in the queue

    sqlTwo = "SELECT ID FROM Appointments"
    self.result = c.execute(sqlTwo)
    for self.row in self.result:
      self.id = self.row[0]
      ids.append(self.id)

    # This is used to order the ids
    ids[0] = 0
    # then = datetime.now()
    # print(then,"printing then for .sort")
    ids.sort()
    # now = datetime.now()
    # print(now,"printing now for .sort")
    # print(now-then,"printing diff for .sort")
    self.new = list(ids)
    self.final_id = self.new[len(ids)-1]
