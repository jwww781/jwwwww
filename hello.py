import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QHBoxLayout

class AddressBook(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("주소록")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        # 테이블 설정
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(3)  # 3개의 열 (이름, 전화번호, 이메일)
        self.tableWidget.setHorizontalHeaderLabels(['이름', '전화번호', '이메일'])
        self.layout.addWidget(self.tableWidget)

        # 입력 필드와 레이아웃
        self.formLayout = QHBoxLayout()

        self.nameInput = QLineEdit(self)
        self.nameInput.setPlaceholderText("이름")
        self.formLayout.addWidget(self.nameInput)

        self.phoneInput = QLineEdit(self)
        self.phoneInput.setPlaceholderText("전화번호")
        self.formLayout.addWidget(self.phoneInput) 

        self.emailInput = QLineEdit(self)
        self.emailInput.setPlaceholderText("이메일")
        self.formLayout.addWidget(self.emailInput)

        self.layout.addLayout(self.formLayout)

        # 추가 버튼
        self.addButton = QPushButton("추가", self)
        self.addButton.clicked.connect(self.add_entry)
        self.layout.addWidget(self.addButton)

        self.setLayout(self.layout)

    def add_entry(self):
        # 입력된 값들을 가져오기
        name = self.nameInput.text()
        phone = self.phoneInput.text()
        email = self.emailInput.text()

        # 테이블에 새 항목 추가
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(name))
        self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(phone))
        self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(email))

        # 입력 필드 초기화
        self.nameInput.clear()
        self.phoneInput.clear()
        self.emailInput.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddressBook()
    window.show()
    sys.exit(app.exec_())
