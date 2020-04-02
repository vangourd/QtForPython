import sys
from PySide2.QtWidgets import QDialog, QApplication
from reserveHotel import *

class MyForm(QDialog):

    def __init__(self,roomData):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.roomData = roomData
        self.addRoomTypes(list(roomData))
        self.ui.pushButton.clicked.connect(self.computeRoomRent)
        self.show()
    
    def addRoomTypes(self, listRoomTypes=[]):
        for i in listRoomTypes:
            self.ui.comboBox.addItem(i)

    def computeRoomRent(self):
        dateselected = self.ui.calendarWidget.selectedDate()
        dateinstring = str(dateselected.toPython())
        noOfDays=self.ui.spinBox.value()
        chosenRoomType=self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        self.ui.Enteredinfo.setText(f"Date of reservation: {dateinstring}, Number of days: {noOfDays}, Room type selected {chosenRoomType} ")
        roomRent = self.roomData[chosenRoomType]
        total = roomRent*noOfDays
        self.ui.RoomRentInfo.setText(f"Room rent for single day for {chosenRoomType} is ${str(roomRent)} per night. Total ${str(total)}")



if __name__ == "__main__":
    roomData = {
        "Suite": 40,
        "Super Luxury": 30,
        "Super Deluxe": 20,
        "Ordinary": 10
    }
    app = QApplication(sys.argv)
    w = MyForm(roomData)
    w.show()
    sys.exit(app.exec_())