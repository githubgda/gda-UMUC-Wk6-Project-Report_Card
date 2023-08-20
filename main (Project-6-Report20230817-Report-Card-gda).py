################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

# This function will involve you adding a student and a collection for their grades to a dictionary!
def getStudentName():

  val = None

  while(val == None):
    try:
      test = input("Enter student name: ")
      val = test
    except:
      val = None
  
  return val


# This function will return the Letter Grade for a student based upon numerical grade provided
# Source: W6D1 - Modules | Objects
def getLetterGrade(grade):
    if(grade >= 90):
      return "A"
    elif(grade >= 80):
      return "B"
    elif(grade >= 70):
      return "C"
    elif(grade >= 60):
      return "D"
    elif(grade >= 50):
      return "E"
    else:
      return "F"

################ Main Program ################
# Define variables and Students' Dictionary
import math
selectedOption = ""
studentDictionary = {}

# Application Loop
while(selectedOption != "6"):

  # Prompt the user to select an Menu Option
  print()
  displayMenu()
  selectedOption = input("Select an Option: ")

  # Add student name to Dictionary when Menu Option 1 is selected
  if selectedOption == "1":
    gotStudentName = getStudentName()
    
    # Defind and initialize list to hold students grades
    studentGrade = []

    # Add Student Name and initialize list that will hold the grades for student    
    studentDictionary[gotStudentName] = studentGrade

    # Print Details of Action that was Completed for this option
    print(f"{gotStudentName} was added")
     
  # Remove student name and associated grades pair from the Dictionary when Menu Option 2 is selected
  if selectedOption == "2":

    # Get Student Name
    gotStudentName = getStudentName()

    # If Student Name is not in Dictionary print appropriate message
    if gotStudentName not in studentDictionary:
      print(f"{gotStudentName} is not in the dictionary!")
    else:
      # If Student Name is in Dictionary Remove it
      studentDictionary.pop(gotStudentName)

      # Print Details of Action that was Completed for this option
      print(f"{gotStudentName} was removed")
    
  # Add student quiz grade to it's corresponding collection of grades to Dictionary when Menu Option 3 is selected
  # Using a pre-written function (i.e., getNumberGradeFromUser) that ensures the user is entering a valid grade (a decimal number)
  if selectedOption == "3":
    
    # Get Student Name
    gotStudentName = getStudentName()

    # If Student Name is not in Dictionary print appropriate message
    if gotStudentName not in studentDictionary:
      print(f"{gotStudentName} is not in the dictionary!")
    else:
      # Add Student's Quiz Grade to Dictionary
      gotStudentGrade = getNumberGradeFromUser()
      gradeList = gotStudentGrade
      studentDictionary[gotStudentName].append(gradeList)

      # Print Details of Action that was Completed for this option
      print(f"Added {gotStudentGrade} to {gotStudentName}'s Quiz Grades")
      
  # List all of the grades for an INDIVIDUAL student when Option 4 is selected
  if selectedOption == "4":
    
    # Get Student Name
    gotStudentName = getStudentName()
            
    # If Student Name is not in Dictionary print appropriate message
    if gotStudentName not in studentDictionary:
      print(f"{gotStudentName} is not in the dictionary!")
    
    else:
      # Confirm Student's and process the all grades for an INDIVIDUAL student  
      for key, value in studentDictionary.items():
        if key == gotStudentName:
          
          # Print all of the grades for an INDIVIDUAL student
          print(f"{gotStudentName}'s Quizzes: ")
          for item in value:
            print(item)

  # Calculate and Print a Student's Average Grade and Print the Equivalent Letter Grade
  if selectedOption == "5":
      
    # Get Student Name
    gotStudentName = getStudentName()
              
    # If Student Name is not in Dictionary print appropriate message
    if gotStudentName not in studentDictionary:
      print(f"{gotStudentName} is not in the dictionary!")
      
    else:
      # Calculates a Student's Average Grade and Determine Equivalent Letter Grade
      sumOfGrades = 0  
      for key, value in studentDictionary.items():

        # Calculate number of Grades a Student have in Dictionary
        numberOfGrades = len(value)

        # Verify that correct Student Name/Key is being processed
        if key == gotStudentName:

          # Acquire Student's Grades and Calculate Sum of all Grades
          for item in value:
            sumOfGrades = sumOfGrades + item
            
          # Divide the Sum of total number of Grades by number of Grades
          # "import math" and "math.floor()" reference W6D1 -Modules-Lecture
          averageOfGrades = math.floor(sumOfGrades/numberOfGrades)

          # Call function to get Letter Grade
          letterGrade = getLetterGrade(averageOfGrades)

          # Print Letter Grade Result
          print(f"{gotStudentName}'s Quizzes Average is {averageOfGrades}.")
          print(f"Therefore, {gotStudentName}'s Letter Grade is a {letterGrade}.")
          

  # This code will execute when Option 6 is selected to Quit the program
  if selectedOption == "6":
    print("You selected Option 6 to Quit the program.")
    print("See you later")
   