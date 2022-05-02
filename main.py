from datetime import date
from enum import Flag
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import sys
class MainWindow(qtw.QWidget):
    events = {}
    def __init__(self):
        super().__init__()

        #UI CODE START
        self.setWindowTitle("Calendar App")
        self.resize(800,800)

        #Create Widgets
        self.calendar = qtw.QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setVerticalHeaderFormat(qtw.QCalendarWidget.NoVerticalHeader)
        self.calendar.setSelectionMode(qtw.QCalendarWidget.SingleSelection)
        self.event_list = qtw.QListWidget()
        self.event_title = qtw.QLineEdit()
        self.event_time = qtw.QTimeEdit(qtc.QTime(12,0))
        self.event_category = qtw.QComboBox()
        self.allday_check = qtw.QCheckBox("All day")
        self.event_deatil = qtw.QTextEdit()
        self.add_button = qtw.QPushButton("Add/Update")
        self.delete_button = qtw.QPushButton("Delete")

        #populate event category
        self.event_category.addItems(["Select Category...","New...","Work","Meeting","Home","Travel","Shopping"])
        self.event_category.model().item(0).setEnabled(False)

        #Calendar size policy
        self.calendar.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding)

        #Event List size policy
        self.event_list.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding)

        #GUI Layout
        main_layout = qtw.QHBoxLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(self.calendar)

        right_layout = qtw.QVBoxLayout()
        main_layout.addLayout(right_layout)
        right_layout.addWidget(qtw.QLabel("Events on Date"))
        right_layout.addWidget(self.event_list)

        event_form = qtw.QGroupBox("Event")
        event_form_layout = qtw.QGridLayout()
        event_form.setLayout(event_form_layout)
        right_layout.addWidget(event_form)

        event_form_layout.addWidget(self.event_title,1,1,1,3)
        event_form_layout.addWidget(self.event_category,2,1)
        event_form_layout.addWidget(self.event_time,2,2)
        event_form_layout.addWidget(self.allday_check,2,3)
        event_form_layout.addWidget(self.event_deatil,3,1,1,3)
        event_form_layout.addWidget(self.add_button,4,1)
        event_form_layout.addWidget(self.delete_button,4,3)

        #Event Handling
        self.allday_check.toggled.connect(self.event_time.setDisabled)
        self.calendar.selectionChanged.connect(self.populate_list)
        self.event_list.itemSelectionChanged.connect(self.populate_form)
        self.event_list.itemSelectionChanged.connect(self.check_del_button)
        self.add_button.clicked.connect(self.save_event)
        self.delete_button.clicked.connect(self.delete_event)

        self.check_del_button()
        #UI CODE END
        self.show()
    
    def clear_form(self):
        print("clear_form func")
        self.event_time.setTime(qtc.QTime(8,0)) 
        self.event_title.clear()
        self.event_category.setCurrentIndex(0)
        self.event_deatil.setPlainText("")
        self.allday_check.setChecked(False)

    def populate_list(self):
        print("populate_list func")
        self.event_list.clear()
        self.clear_form()
        date = self.calendar.selectedDate()
        for event in self.events.get(date,[]):
            if event['time']:
                time = event['time'].toString('hh:mm')
            else:
                time = 'All Day'
            
            self.event_list.addItem(f"{time}:{event['title']}")

    def populate_form(self):
        print("populate_form func")
        self.clear_form()
        date = self.calendar.selectedDate()
        event_number = self.event_list.currentRow()
        print(event_number)
        if event_number == -1:
            return
        if not self.events.get(date,[]):
            return
        event_data = self.events.get(date)[event_number]
        self.event_category.setCurrentText(event_data['category'])
        self.event_deatil.setPlainText(event_data['detail'])
        if event_data['time']:
            self.event_time.setTime(event_data['time'])
        else:
            self.allday_check.setChecked(True)
        self.event_title.setText(event_data['title'])
    
    def save_event(self):
        print("save event func")
        event_data = {}
        date = self.calendar.selectedDate()
        event_data['category'] = self.event_category.currentText()
        event_data['detail'] = self.event_deatil.toPlainText()
        if self.allday_check.isChecked():
            event_data['time'] = None
        else:
            event_data['time'] = self.event_time.time()
        event_data['title'] = self.event_title.text()

        event_list = self.events.get(date,[])
        event_number = self.event_list.currentRow()
        if event_number == -1:
            event_list.append(event_data)
        else:
            event_list[event_number] = event_data
        
        event_list.sort(key=lambda e: e['time'] or qtc.QTime(0,0))
        self.events[date] = event_list
        self.populate_list()

    def delete_event(self):
        print("delete event func")
        date = self.calendar.selectedDate()        
        row = self.event_list.currentRow()        
        del(self.events[date][row])        
        self.event_list.setCurrentRow(-1)        
        self.clear_form()
        self.populate_list()

    def check_del_button(self):
        self.delete_button.setEnabled(
            self.event_list.currentRow() == -1
        )
        
if __name__ == '__main__':
    
    app = qtw.QApplication(sys.argv)

    mw = MainWindow()

    sys.exit(app.exec())