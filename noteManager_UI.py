# Import Package for UI
from PySide2 import QtWidgets, QtGui, QtCore
import os
# Import UI make with QT4Designer
from Custom.windowMain import Ui_BlocNotes
# Import the functions define before in the file noteManager.py
import noteManager
import utils as utl


# Created class for the application
class CreatedNote(QtWidgets.QWidget, Ui_BlocNotes):
    def __init__(self):
        super().__init__()
        # Recover the setupUi from UI_BlocNotes
        self.setupUi(self)
        # Define the method who well be initialize at start application
        self.recoverAllNote()
        self.setup_connection()

    # Define the connection when interacted with
    def setup_connection(self):
        self.btn_createdNote.clicked.connect(self.createNote)
        self.btn_updateNote.clicked.connect(self.updateNote)
        self.btn_deleteNote.clicked.connect(self.deleteNote)

        self.lw_listNote.itemClicked.connect(self.displayNote)

    def recoverNoteSlected(self):
        # Here, we recover all notes but as an object
        notes = self.lw_listNote.selectedItems()
        # Check if object exist
        if not notes:
            return
        # About, recover the last note selected and recover only text who is equal at the name of the note
        nameNote = notes[-1].text()
        # Recover the path, of the file
        pathNote = os.path.join(utl.DATA_DIR, nameNote +'.txt')

        return nameNote, pathNote

    # Method for created the note
    def createNote(self):
        # Here, we define a new widget for display a pop-up when push the button Create
        nameNote, ok = QtWidgets.QInputDialog.getText(self, "Created Note", "Enter the title of the note :")
        # If we don't push the button ok then nothing happens
        if not ok:
            return
        # Else, we call method in the file noteManager and parameter is a name of the note
        noteManager.createdNote(nameNote)
        # Then, this method permit to display all notes int the List Widget
        self.recoverAllNote()

    # This method displays the content of the note in the widget Text Edit
    def displayNote(self):
        # Here, i recover the name and path of the item selected in the List Widget
        nameNote, pathNote = self.recoverNoteSlected()
        # Here, i use the method in the file noteManager for recover the content
        content = noteManager.recoverContent(nameNote)
        # We fill up the Text Edit with the content
        self.te_contentNote.setText(content)

    # Method for delete the note with the name
    def deleteNote(self):
        # Call this method for recover only one note
        nameNote, pathNote = self.recoverNoteSlected()
        # Then, we call the function delete in the file noteManager
        noteManager.deleteNote(nameNote)
        # And refresh the List Widget
        self.recoverAllNote()
        # Update the Text Edit for delete the content
        self.te_contentNote.setText("")

    # This method, update the content in the application and the file
    def updateNote(self):
        # Call this method for recover only one note
        nameNote, pathNote = self.recoverNoteSlected()
        # Recover the content of the note but which is in the Text Edit
        content = self.te_contentNote.toPlainText()
        # After, we crush the content before and update with the Text Edit
        noteManager.createdNote(nameNote, content)

    # Method for display all notes in the file
    def recoverAllNote(self):
        # Here, clear the List Widget
        self.lw_listNote.clear()
        # Here, we call method for recover the notes in the file
        notes = noteManager.recoverNote()
        # Add the widget of the notes
        self.lw_listNote.addItems(notes)

app = QtWidgets.QApplication()
win = CreatedNote()
win.show()
app.exec_()