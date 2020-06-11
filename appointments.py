#-------------------------------------------------------
# Name:        appointments.py
# Purpose:     Education only, copying will be subject to plagiarism
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

class Application(MySort):

  '''
  An object that holds the information of the main window of the user interface and extends base-class name MySort to implement sorting 

  Attributes
  ----------
  heading : str
      The heading of the application
  name : str
      The name of the patient
  age : str
      The age of the patient
  gender : str
      The gender of the patient
  phone : str
      The contact number of the patient
  residence : str
      The home address of the patient
  reason : str
      The reason of the patient's visit
  time : str
      The time of the patient's appointment

  Methods
  -------
  schedule_appointment
      A function to set an appointment for a patient successfully

  ''' 
  def __init__(self, master):

    '''
    A constructor to build Application

    Parameters
    ----------
    master : frame

    '''
    self.master = master

    # Design for main window
    self.left = Frame(master, width=700, height=720, bg='lightBlue1')
    self.left.pack(side=LEFT)

    self.right = Frame(master, width=500, height=720, bg='lightgrey')
    self.right.pack(side=RIGHT)

    # Creates a label for the heading of the user interface
    self.heading = Label(self.left, text= "Fraser Clinic Appointments", font=("Times", 20, "bold"), fg='black', bg= 'lightblue1')
    self.heading.place(x=177, y=30)
    # Creates a label and entry box for the patient's name
    self.name = Label(self.left, text="Patient's Name:", font=("Times", 16, "bold"), fg='black',bg='lightblue1')
    self.name.place(x=38, y=130)
    self.name_entry = Entry(self.left, width=30)
    self.name_entry.place(x=25, y=180)
    # Creates a label and entry box for the patient's age
    self.age = Label(self.left, text="Age:", font=("Times", 16, "bold"), fg='black',bg='lightblue1')
    self.age.place(x=315, y=130)
    self.age_entry = Entry(self.left, width=30)
    self.age_entry.place(x=250, y=180)
    # Creates a label and entry box for the patient's gender
    self.gender = Label(self.left, text="Gender:", font=("Times", 16, "bold"), fg='black',bg='lightblue1')
    self.gender.place(x=520, y=130)
    self.gender_entry = Entry(self.left, width=30)
    self.gender_entry.place(x=475, y=180)
    # Creates a label and entry box for the patient's contact number
    self.phone = Label(self.left, text="Phone:", font=("Times", 16, "bold"), fg='black',bg='lightblue1')
    self.phone.place(x=85, y=280)
    self.phone_entry = Entry(self.left, width=30)
    self.phone_entry.place(x=25, y=330)
    # Creates a label and entry box for the patient's residence
    self.residence = Label(self.left, text="Residence:", font=("Times", 16, "bold"), fg='black',bg='lightblue1')
    self.residence.place(x=290, y=280)
    self.residence_entry = Entry(self.left, width=30)
    self.residence_entry.place(x=250, y=330)
    # Creates a label and entry box for the patient's reason of visit
    self.reason = Label(self.left, text="Reason:", font=("Times", 16, "bold"), fg='black',bg='lightblue1')
    self.reason.place(x=520, y=280)
    self.reason_entry = Entry(self.left, width=30)
    self.reason_entry.place(x=475, y=330)
    # Creates a label and entry box for the patient's appointment time
    self.time = Label(self.left, text="Time:", font=("Times", 16, "bold"), fg='black',bg='lightblue1')
    self.time.place(x=310, y=400)
    self.time_entry = Entry(self.left, width=30)
    self.time_entry.place(x=250, y=450)        
    # A button that will set the appointment and add it in the database
    self.enter = Button(self.left, text="Set Appointment", width=35, height=3, bg="mintcream", command=self.schedule_appointment)
    self.enter.place(x=215, y=525)

    super().__init__() # Calling the base class constructor

    # A log that shows all the appointments and patients in queue
    self.queue = Label(self.right, text="Queue", font=("Times", 20, "bold"), fg="black",bg="lightgrey")
    self.queue.place(x=210, y=30)
    self.box = Text(self.right, width=50, height=33)
    self.box.place(x=50, y=80)
    self.box.insert(END, "Total number of appointments: " + str(self.final_id))

    # Complexity Analaysis

    '''
    # BUBBLE SORT CODE
    arr = [] 
    then = datetime.now()
    print(then,"printing then for bubble sort")
    for i in range (len(ids)):
      if i > 0:
        arr.append(int(ids[i]))

    n=len(arr)
    sorted = True
    for k in range(n): 
      for i in range(0,n-k-1):
        if arr[i] < arr[i+1]:
          sorted = False
          temp = arr[i+1]
          arr[i+1] = arr[i]
          arr[i] = temp
        if sorted == True:
          break
    now = datetime.now()
    print(now,"printing now for bubble sort")
    print(now-then,"printing diff for bubble sort")
    for l in range(n):             
      print("Bubble Sorted", arr[l]) 

    # Best Case : Algorithm will have to be run n times
    # Average Case Scenario: Algorithm will have to be run n^2 times
    # Worst Case: Algorithm will have to be run n^2 times
    # Why? Even if we used sorted function then the program will still not recognize that the data in the array was already sorted.
    # Algorithm in its original form will take O(n^2) and now when we tweak it it becomes O(n)

    # SELECTION SORT CODE
    n=len(arr)
    then = datetime.now()
    print(then,"printing then for selection sort")
    for k in range(n): 
      for i in range(k+1,n):
        if arr[k] > arr[i]:
          temp = arr[k]
          arr[k] = arr[i]
          arr[i] = temp
    now = datetime.now()
    print(now,"printing now for selection sort")
    print(now-then,"printing diff for selection sort")
    for l in range(n):             
      print("Selection Sorted", arr[l]) 

    # Best Case Scenario: Algorithm will have to be run n^2 times
    # Average Case Scenario: Algorithm will have to be run n^2 times
    # Worst Case Scenario: Algorithm will have to be run n^2 times

    # LINEAR SEARCH CODE (Searches the whole array)

    x = 4 # change x value to search id 
    found = False

    # Since x value is 4, you are searching 4
    for l in range(n):
      if x == arr[l]:
        found = True
        print("Element found",x)
        break 

    if found == False:
      print("Linear Search element not found")

    # Best Case scenario: Element is found immediately, result is 1
    # Average Case scenario: Result is n/2
    # Worst Case scenario: Element takes time to be found, big O notation is used and result is n, which is the number of input/length of the array
    # Worst Case scenario Cnt'd: T(n) = 6n + 3 is the equation of the run time, 6 comes from the total number of operations needed and 3 is the number of operations needed to be performed irrespective of the size of the array
    # Worst Case scenario Cnt'd: It is evident that T(n) is solely dependent upon size of array because others are constants like 6 and 3 are constant and can be eliminated as per axioms of big O notation
    # Worst Case scenario Cnt'd: O of T(n) is going to be n 

    # BINARY SEARCH CODE (Searches from midpoint of array, input has to be sorted to run this)

    def binarySearch(arr, l, r, x): 

      while l <= r: 
        mid = l + (r - l) // 2

    # Check if x is present at midpoint 
        if arr[mid] == x: 
          return mid 

    # If x is greater, ignore left half 
        elif arr[mid] < x: 
          l = mid + 1

    # If x is smaller, ignore right half 
        else: 
          r = mid - 1

    # If we reach here, then the element was not present 
        return -1

    # Function call 
    result = binarySearch(arr, 0, len(arr)-1, x) 

    if result != -1: 
      print ("Index of element found % d" % result) # finds index
    else: 
      print ("Binary Search element not found") 

    # Best Case Scenario: Element is found at midpoint immediately
    # Average Case Scenario: Log base 2 (n), we need to slice the number of input by half
    # Worst Case Scenario: Log base 2 (n), we need to slice the number of input by half
    # Let say the iteration in Binary Search terminates after k iterations. In the above example, it terminates after 3 iterations, so here k = 3
    # At each iteration, the array is divided by half. So let’s say the length of array at any iteration is n
    # Iteration 1 is that Length of array = n
    # Iteration 2 is that the Length of array = n/2
    # Iteration 3 is that the Length of array = (n/2)^2
    # Hence in this pattern, Iteration k, Length of array = (n/2)^k
    # So due to this after k divisions, the length of the array will become 1: Length of array = n/2k = 1 -> n = 2k 
    # Use log on both sides and it becomes k = log2(n), this is why we use log base 2 (n)

    '''

  def schedule_appointment(self):

    '''
    A function to get input from patient to successfully set an appointment

    Parameters
    ----------
    None

    '''
    p1 = Patient(self.reason_entry.get(),self.name_entry.get(),self.age_entry.get(),self.gender_entry.get(),self.phone_entry.get(),self.residence_entry.get(),self.time_entry.get())
    self.patient_detail = p1

    if p1.name == "" or p1.age == "" or p1.gender == "" or p1.phone == "" or p1.residence == "" or p1.reason == "" or p1.time == "": 
      messagebox.showwarning("Warning!", "Patient information is incomplete")

    else:
      sql = "INSERT INTO 'Appointments' (Name, Age, Gender, Phone, Residence, Reason, Time) VALUES(?, ?, ?, ?, ?, ?, ?)"
      c.execute(sql, (p1.name, p1.age, p1.gender, p1.phone, p1.residence, p1.reason, p1.time,))
      conn.commit()
      messagebox.showinfo("Success", "Appointment has been created for " + str(p1.name))
      self.box.insert(END, '\nAppointment set for ' + str(p1.name) + " at " + str(p1.time))

# Creates the object
root = Tk()
b = Application(root)

# This is the resolution for the window of the application 
root.geometry('1200x650+0+0')

# This stops the application from resizing itself
root.resizable(False, False)

# Finishing the loop
root.mainloop()
