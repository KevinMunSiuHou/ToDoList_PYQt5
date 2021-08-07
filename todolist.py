from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json

app = QApplication([])
my_win = QWidget()

with open("notes.json", "r") as file:
    data = file.read()
obj = json.loads(data)
Users = {}

#General
H_line = {}
V_line = {}

def check_user():
    if (name_fill.text() in obj) and (obj[name_fill.text()]['Password'] == pw_fill.text()):
        text = name_fill.text() + ', Welcome Back!'
        to_do_text.setText(text)
        Intro_Group.hide()
        to_do_list_Group.show()
        display_task()
    elif (name_fill.text() in obj) and (obj[name_fill.text()]['Password'] != pw_fill.text()):
        text_label.setText('Wrong Password!')
        pw_fill.clear()
    else:
        text_label.setText('User Not Found! Please click the new user button!')

def create_user():
    pw_label_con.show()
    pw_fill_con.show()
    text_label.setText('New User Details:')
    new_user_text.hide()
    new_button.hide()
    sub_button.clicked.connect(new_user_data)

def display_task():
    to_do_list.clear()
    if obj[name_fill.text()]['note'] != []:
        for note in obj[name_fill.text()]['note']:
            to_do_list.addItem(QListWidgetItem(note))
    with open("notes.json", "w") as file:
        json.dump(obj, file, ensure_ascii=False)

def add_new():
    if new_task.text() != '':
        obj[name_fill.text()]['note'].append(new_task.text())
        new_task.clear()
        display_task()
    else:
        to_do_text.setText('Please insert new task!')

def delete_old():
    obj[name_fill.text()]['note'].remove(to_do_list.currentItem().text())
    display_task()

def new_user_data():
    if pw_fill_con.text() == '' or pw_fill_con.text() != pw_fill.text():
        text_label.setText('Please insert the same password as confirmation password!')
    else:
        obj[name_fill.text()] = {'Password':pw_fill_con.text(),'note':[]}
        text = name_fill.text() + ', Welcome Back!'
        to_do_text.setText(text)
        Intro_Group.hide()
        to_do_list_Group.show()
        display_task()

#Login Page
text_label = QLabel('User Login Page:')
name_label = QLabel('Name :')
name_fill = QLineEdit('')
name_fill.setPlaceholderText('Enter Name...')
pw_label = QLabel('Password :')
pw_fill = QLineEdit('')
pw_fill.setPlaceholderText('Enter Password...')
pw_label_con = QLabel('Confirm Password :')
pw_fill_con = QLineEdit('')
pw_fill_con.setPlaceholderText('Confirm Password...')
sub_button = QPushButton('Submit')
new_user_text = QLabel('For new user, please click this button!')
new_button = QPushButton('New User')
Intro_Group = QGroupBox()

#Login Position
H_line[0] = QHBoxLayout()
H_line[1] = QHBoxLayout()
H_line[2] = QHBoxLayout()
H_line[3] = QHBoxLayout()
H_line[4] = QHBoxLayout()
H_line[5] = QHBoxLayout()
V_line[0] = QVBoxLayout()
H_line[0].addWidget(text_label)
H_line[1].addWidget(name_label)
H_line[1].addWidget(name_fill)
H_line[2].addWidget(pw_label)
H_line[2].addWidget(pw_fill)
H_line[3].addWidget(pw_label_con)
H_line[3].addWidget(pw_fill_con)
H_line[4].addWidget(sub_button,alignment=Qt.AlignCenter)
H_line[5].addWidget(new_user_text)
H_line[5].addWidget(new_button)
V_line[0].addLayout(H_line[0])
V_line[0].addLayout(H_line[1])
V_line[0].addLayout(H_line[2])
V_line[0].addLayout(H_line[3])
V_line[0].addLayout(H_line[4])
V_line[0].addLayout(H_line[5])
Intro_Group.setLayout(V_line[0])

#To Do list Page
to_do_text = QLabel('')
to_do_list = QListWidget()
to_do_list_Group = QGroupBox()
new_task = QLineEdit('')
new_task.setPlaceholderText('Enter task here...')
new_task_submit = QPushButton('Add New Task')
delete_task_submit = QPushButton('Delete Task')

#To Do list Position
V_line[1] = QVBoxLayout()
H_line[6] = QHBoxLayout()
V_line[1].addWidget(to_do_text)
V_line[1].addWidget(to_do_list)
H_line[6].addWidget(new_task)
H_line[6].addWidget(new_task_submit)
H_line[6].addWidget(delete_task_submit)
V_line[1].addLayout(H_line[6])
to_do_list_Group.setLayout(V_line[1])

#Button link
sub_button.clicked.connect(check_user)
new_button.clicked.connect(create_user)
new_task_submit.clicked.connect(add_new)
delete_task_submit.clicked.connect(delete_old)

#Final Position
V_line_final = QVBoxLayout()
V_line_final.addWidget(Intro_Group)
V_line_final.addWidget(to_do_list_Group)

#Hidden
pw_label_con.hide()
pw_fill_con.hide()
to_do_list_Group.hide()

my_win.setLayout(V_line_final)
my_win.show()
app.exec_()