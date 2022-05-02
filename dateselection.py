from datetime import date, datetime, timedelta
import time
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from calenderUtility import find_holidays, is_holiday
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
import sys

def qdate_to_pydate(dt:qtc.QDate):
    return datetime.strptime(dt.toString("dd-MM-yyyy"), "%d-%m-%Y").date()

def print_date(dt:qtc.QDate):
    selected_date = qdate_to_pydate(dt)
    if not is_holiday(selected_date):
        print(f'selected date {selected_date.strftime("%d-%m-%Y")} is working day')
    else:
        print(f'selected date {selected_date.strftime("%d-%m-%Y")} is holiday')

def get_max_date()->date:
    localtime = time.localtime(time.time())
    hour = localtime.tm_hour
    cur_date = date.today()
    if hour < 19 :
        return cur_date - timedelta(days=1)
    else:
        return cur_date



class MainWindow(qtw.QWidget):
    events = {}

    def __init__(self):
        super().__init__()

        # UI CODE START

        # fetch report button
        self.get_eq_eod_btn = qtw.QPushButton("EQ EOD Report")
        self.get_fo_eod_btn = qtw.QPushButton("FO EOD Report")

        # calendar
        self.calendar = qtw.QCalendarWidget()
        self.calendar.setGridVisible(False)
        self.calendar.setVerticalHeaderFormat(qtw.QCalendarWidget.NoVerticalHeader)
        self.calendar.setSelectionMode(qtw.QCalendarWidget.SingleSelection)
        self.calendar.setMaximumDate(get_max_date())

        # set holidays in calendar
        self.holiday_list = find_holidays()
        holiday_text_format = self.calendar.weekdayTextFormat(qtc.Qt.Saturday)
        for holiday in self.holiday_list:
            self.calendar.setDateTextFormat(holiday, holiday_text_format)

        self.calendar.clicked.connect(print_date)
        # GUI Layout
        main_layout = qtw.QHBoxLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(self.calendar)

        right_layout = qtw.QVBoxLayout()
        main_layout.addLayout(right_layout)

        right_layout.addWidget(self.get_eq_eod_btn)
        right_layout.addWidget(self.get_fo_eod_btn)

        #signal handling
        self.get_eq_eod_btn.clicked.connect(self.get_eq_eod)
        self.get_fo_eod_btn.clicked.connect(self.get_fo_eod)

        # UI CODE END
        self.show()
        
    #event handling
    def get_eq_eod(self):
        selected_date = qdate_to_pydate(self.calendar.selectedDate())
        bhavcopy_save(selected_date,".")

    def get_fo_eod(self):
        selected_date = qdate_to_pydate(self.calendar.selectedDate())
        bhavcopy_fo_save(selected_date,"./fo_eod/")
            

        


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    mw = MainWindow()

    sys.exit(app.exec())
