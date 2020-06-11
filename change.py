#-------------------------------------------------------
# Name:        change.py
# Purpose:     Education purposes only, copying will be subject to plagiarism
# Author:      Syed Abidi
# Created:     2-February-2020
# Updated:     10-June-2020
#-------------------------------------------------------
from tkinter import *
import sqlite3
from tkinter import messagebox
from patient import Patient

conn = sqlite3.connect('database.db')
c = conn.cursor()

class ApplicationTwo:

  '''
  An object that holds the information of the update appointments window of the user interface

  Attributes
  ----------
  heading : str
      The heading of the update appointments window
  updname : str
      The updated name of the patient
  updage : str
      The updated age of the patient
  updgender : str
      The updated gender of the patient
  updphone : str
      The updated contact number of the patient
  updresidence : str
      The updated home address of the patient
  updreason : str
      The updated reason of the patient's visit
  updtime : str
      The updated time of the patient's appointment

  Methods
  -------
  search_database
      A function to search the patient's appointment in the database
  update_database
      A function to update the patient's appointment in the database
  delete_appointment
      A function to delete the patient's appointment from the database

  ''' 

  def __init__(self, master):

    '''
    A constructor to build ApplicationTwo

    Parameters
    ----------
    master : frame

    '''

    self.master = master

    self.main = Frame(master, width=1200, height=720, bg='navajowhite')
    self.main.pack(side=LEFT)
    # Creates a label for the heading of the user interface
    self.heading = Label(master, text="Update Appointments", bg='navajowhite', fg='black', font=('Times', 20,'bold'))
    self.heading.place(x=470, y=30)
    # Creates a label and entry box for the patient's name
    self.name = Label(master, text="Enter Patient's Name", bg='navajowhite', font=('Times', 16, 'bold'))
    self.name.place(x=500, y=120)
    self.nameupd = Entry(master, width=30)
    self.nameupd.place(x=506, y=175)
    # Creates a search button for the patient's name
    self.search = Button(master, text="Search", width=12, height=1, bg='skyblue1', command=self.search_database)
    self.search.place(x=547, y=215)

  def search_database(self):

    '''
    A function to allow the user to search the patient's appointment

    Parameters
    ----------
    None

    '''
    patients = [] # empty list 

    self.input = self.nameupd.get()

    # Used to choose appointment information from database
    sql = "Select * FROM Appointments WHERE name LIKE ?"
    self.result = c.execute(sql, (self.input,))
    for self.row in self.result:
      patients.append(Patient(self.row[6],self.row[1],self.row[2],self.row[3],self.row[4],self.row[5],self.row[7]))
      self.name = self.row[1]
      self.age = self.row[2]
      self.gender = self.row[3]
      self.phone = self.row[4]
      self.residence = self.row[5]
      self.reason = self.row[6]
      self.time = self.row[7]

    if len(patients) == 0:
      messagebox.showerror("Error", "Information is missing")
      return

    self.updname = Label(self.master, text="Patient's Name", bg='navajowhite', font=('Times', 16, 'bold'))
    self.updname.place(x=150, y=275)
    self.entname = Entry(self.master, width=30)
    self.entname.place(x=130, y=325)
    self.entname.insert(END, str(patients[0].name))

    self.updage = Label(self.master, text="Age", bg='navajowhite', font=('Times', 16, 'bold'))
    self.updage.place(x=570, y=275)
    self.entage = Entry(self.master, width=30)
    self.entage.place(x=506, y=325)
    self.entage.insert(END, str(patients[0].age))

    self.updgender = Label(self.master, text="Gender", bg='navajowhite', font=('Times', 16, 'bold'))
    self.updgender.place(x=940, y=275)
    self.entgender = Entry(self.master, width=30)
    self.entgender.place(x=882, y=325)
    self.entgender.insert(END, str(patients[0].gender))

    self.updphone = Label(self.master, text="Phone", bg='navajowhite', font=('Times', 16, 'bold'))
    self.updphone.place(x=184, y=375)
    self.entphone = Entry(self.master, width=30)
    self.entphone.place(x=130, y=425)
    self.entphone.insert(END, str(patients[0].phone))

    self.updresidence = Label(self.master, text="Residence", bg='navajowhite', font=('Times', 16, 'bold'))
    self.updresidence.place(x=550, y=375)
    self.entresidence = Entry(self.master, width=30)
    self.entresidence.place(x=506, y=425)
    self.entresidence.insert(END, str(patients[0].residence))

    self.updreason = Label(self.master, text="Reason", bg='navajowhite', font=('Times', 16, 'bold'))
    self.updreason.place(x=940, y=375)
    self.entreason = Entry(self.master, width=30)
    self.entreason.place(x=882, y=425)
    self.entreason.insert(END, str(patients[0].reason))

    self.updtime = Label(self.master, text="Time", bg='navajowhite', font=('Times', 16, 'bold'))
    self.updtime.place(x=570, y=475)
    self.enttime = Entry(self.master, width=30)
    self.enttime.place(x=506, y=525)
    self.enttime.insert(END, str(patients[0].time))

    # This button is used to update the appointment
    self.update = Button(self.master, text="Update", width=15, height=2, bg='yellowgreen', command=self.update_database)
    self.update.place(x=630, y=575)
    # This button is used to update the appointment 
    self.delete = Button(self.master, text="Delete", width=15, height=2, bg='orangered', command=self.delete_appointment)
    self.delete.place(x=450, y=575)

  def update_database(self):

    '''
    A function to allow the user to update the patient's appointment

    Parameters
    ----------
    None

    '''

    self.finalname = self.entname.get()
    self.finalage = self.entage.get()
    self.finalgender = self.entgender.get()
    self.finalphone = self.entphone.get()
    self.finalresidence = self.entresidence.get()
    self.finalreason = self.entreason.get()
    self.finaltime = self.enttime.get()

    update = "UPDATE Appointments SET name=?, age=?, gender=?, phone=?, residence=?, reason=?, time=? WHERE name LIKE ?"
    c.execute(update, (self.finalname, self.finalage, self.finalgender, self.finalphone, self.finalresidence, self.finalreason, self.finaltime, self.nameupd.get(),))
    conn.commit()
    messagebox.showinfo("Updated", "Appointment has been updated successfully")

  def delete_appointment(self):

    '''
    A function to allow the user to delete the patient's appointment

    Parameters
    ----------
    None

    '''

    sqlTwo = "DELETE FROM Appointments WHERE name LIKE ?"
    c.execute(sqlTwo, (self.nameupd.get(),))
    conn.commit()
    messagebox.showinfo("Success", "Appointment has been deleted successfully")

# Creates the object
root = Tk()
b = ApplicationTwo(root)

# This is the resolution for the window of the application 
root.geometry('1200x650+0+0')

# This stops the application from resizing itself
root.resizable(False, False)

# Finishing the loop
root.mainloop()
