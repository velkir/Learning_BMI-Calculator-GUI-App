import PySimpleGUI as sg

def calculate_bmi(weight, height):
  bmi = round(weight / ((height/100)**2), 2)
  return bmi

layout = [  [sg.Text('Weight (kg):')],
            [sg.InputText(key='Weight')],
            [sg.Text('Height (cm):')], 
            [sg.InputText(key='Height')],
            [sg.Button('Calculate BMI')],
            [sg.Text('Your BMI:'), sg.Text(key='-BMI-')]]
# Create the Window
window = sg.Window('BMI Calculator', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    weight = float(values["Weight"])
    height = float(values["Height"])

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Calculate BMI':
      bmi = calculate_bmi(weight, height)
      window['-BMI-'].update(bmi)

window.close()