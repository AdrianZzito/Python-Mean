#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import statistics

name = input("What's your name? ")
filename = "notas" + name + "-" + subject + ".csv"
file = open(filename, "w")

marks = []
user_marks = 0.0
## subject_range = int(input("How many subjects you have? "))

def mean_calc():
    
    global user_marks
    
    while user_marks != 666:
        user_marks = float(input("What is your mark? Type 666 if you have already typed all your notes\n \t"))
        marks.append(user_marks)

    # Deletes the exit number (666) which per default, gets appended into the array 'marks'
    marks.pop()

    ## Ask the user for the subject where that mark came from
    subject = input("In what subject? ")
    
    ## Calculate the mean
    mean = statistics.mean(marks)
    
    ## Create the DataFrame
    notes_df = pd.DataFrame([ [marks], [mean] ], columns = [subject], index = ["Marks", "Mean"])
    
    ## Prints the DataFrame and the global mean
    print(notes_df)
    print("The global mean is", round(mean, 2))
    
    file.write(str(notes_df))
    file.close()
    
## Calls the function
mean_calc()  

