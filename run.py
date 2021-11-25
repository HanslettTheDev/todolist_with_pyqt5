import sys, json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize

from gui import Ui_MainWindow

tick = QtGui.QImage('tick.png').scaled(15, 15, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, *args, todos=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure
            status, text = self.todos[index.row()]
            # return the todo text only
            return text

        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick
    
    def rowCount(self, index):
        return len(self.todos)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(QSize(394,392))
        # create the model to add text into the QlistView
        self.model = TodoModel()
        self.load()
        # setModel sends the response from the TodoModel to add the item to the view
        self.todoView.setModel(self.model)
        # Connect the add function to the add button
        self.addButton.pressed.connect(self.add)
        # Connect the delete function to the delete button
        self.deleteButton.pressed.connect(self.delete)
        # Connect the completed Button
        self.completeButton.pressed.connect(self.complete)

    def add(self):
        """
        Add an item to our todo list getting the text from the
         QlineEdit.todoEddit and then clearing its
        """
        text = self.todoEdit.text()
        text = text.strip() # Remove whitespaces from the ends of the strings
        if text: # don't add empty text
            # Access the list via the model
            self.model.todos.append((False, text))
            # trigger refresh
            self.model.layoutChanged.emit()
            # Empty the input
            self.todoEdit.setText("")
            self.save()
    
    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            # Indexes is a list of a single item in a single select  
            index = indexes[0]
            # Remove the item and refresh
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit() # refresh the layout 
            # Clear the selection (As it no longer exist)
            self.todoView.clearSelection()
            self.save()

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            # .dataChanged takes top-left and bottom right which are equal for a single selection
            self.model.dataChanged.emit(index, index)
            # Clear the selection
            self.todoView.clearSelection()
            self.save()
    
    def load(self):
        try:
            with open('data.json', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            print("not found")
            pass
    
    def save(self):
        with open('data.json', 'w') as f:
            data = json.dump(self.model.todos, f)

app = QtWidgets.QApplication(sys.argv)
window= MainWindow()
window.show()
app.exec_()