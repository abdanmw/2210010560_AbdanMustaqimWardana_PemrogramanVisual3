#Abdan Mustaqim Wardana
import PySimpleGUI as sg
sg.theme("BlueMono")
sg.theme_text_color("blue")
layout = [
    [sg.Text('NPM       :'), sg.Text('2210010560')],
    [sg.Text('Nama      :'), sg.Text('Abdan Mustaqim Wardana')],
    [sg.Text('Kelas     :'), sg.Text('5N Reguler Banjarmasin')],
    [sg.Text('Matkul    :'), sg.Text('Pemrograman Visual 3')]
],

font=("times",40)
window = sg.Window('Profile', layout, size=(400, 200), element_justification='left')


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  
        break
window()
window.close()
