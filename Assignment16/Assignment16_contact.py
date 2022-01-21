import sqlite3
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('H:\Project\PYTHON\Assignment16\contac_database.db')
        self.cursor = self.conn.cursor()
        loader = QUiLoader()
        self.ui = loader.load('H:\Project\PYTHON\Assignment16\untitled.ui')
        self.ui.show()
        self.id = 0
        #func
        self.ui.darkmode.clicked.connect(self.darkmode)
        self.ui.showbtn.clicked.connect(self.show_contac)
        self.ui.addbtn.clicked.connect(self.add_new_contact)
        self.ui.deletebtn.clicked.connect(self.delete_contact)
        self.ui.deleteAllbtn.clicked.connect(self.delete_contacts)

    def darkmode(self):
        self.ui.setStyleSheet("background-color: rgb(100, 100, 100);")

    def show_contac(self):
        self.cursor.execute('SELECT * FROM contac_database')
        result = self.cursor.fetchall()
        for item in result:
            self.id += 1
            label = QLabel()
            label.setText(str(item[0]) + '\t' + item[1] + '\t' + item[2] + '\t' + item[3] + '\t' + item[4] + '\t' + item[5])
            self.ui.verticalLayout.addWidget(label)
    def add_new_contact(self):
        self.id += 1
        name = self.ui.Name.text()
        surename = self.ui.Surname.text()
        cellphone = self.ui.phone.text()
        phone = self.ui.Cellphone.text()
        email = self.ui.email.text()
        self.cursor.execute(f"INSERT INTO contacts VALUES({self.id},'{name}','{surename}','{cellphone}','{phone}','{email}');")
        self.conn.commit()
        label = QLabel()
        label.setText(str(self.id) + '\t' + name + '\t' + surename + '\t' + cellphone + '\t' + phone + '\t' + email)
        self.ui.verticalLayout.addWidget(label)
    
    def delete_contact(self):
        id = int(self.ui.deletingIDEdit.text())
        self.cursor.execute(f"DELETE FROM contacts WHERE id = {id};")
        self.conn.commit()
        for i in range(self.ui.verticalLayout.count()):
            self.ui.verticalLayout.itemAt(i).widget().deleteLater()
        self.show_data()

    def delete_contacts(self):
        self.cursor.execute("DELETE FROM contac_database;")
        self.conn.commit()
        for i in range(self.ui.verticalLayout.count()):
            self.ui.verticalLayout.itemAt(i).widget().deleteLater()
        self.id = 0

app = QApplication()
main_window = MainWindow()
app.exec()