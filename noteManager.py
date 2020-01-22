# Packages imported in the file
# Packages os for the path and folder
import os
# Package logging to display different message with their specificity
import logging
# Package use for recover the global content to folder
from glob import glob
# Import a file for most clarity
import utils as utl

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')

# Method for created note in the folder data
def createdNote(name, content = ""):
    # define the name of the file and extension
    pathNote = os.path.join(utl.DATA_DIR, name + ".txt")
    # function for open and close automatically a file
    with open(pathNote, "w") as f:
        # Method for write in the file
        f.write(content)
    # Condition if file exist
    if os.path.isfile(pathNote):
        print(f"The note {name} has been created !")

# Method for delete note with us name
def deleteNote(name):
    # define the name of the file and extension
    pathNote = os.path.join(utl.DATA_DIR, name + ".txt")
    # If file exist about
    if os.path.isfile(pathNote):
        # Delete the file
        os.remove(pathNote)
        print(f"The note {name} has been removed")
    # Else to display a error message
    else:
        logging.error(f"The note {name} not exist")

# Method for recover note
def recoverNote():
    # Variable for recover all file in the folder data
    notes = glob(utl.DATA_DIR + "/*.txt")
    # Redefine the variable for recover only the name of the file
    # the first path.split with [-1] recover the name and extension of the file everytime.
    # And the second recover only the name
    notes = [os.path.splitext(os.path.split(n)[-1])[0] for n in notes]
    # Return the name for to display in the list Widget
    return notes

# Method for recover the content in the file
def recoverContent(name):
    # Open file with the method read
    with open(utl.DATA_DIR + "/" + name + ".txt", "r") as f:
        # Return the content
        return f.read()
