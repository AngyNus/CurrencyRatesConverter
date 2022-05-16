import PySimpleGUI as sg
import Rates


converter = Rates.Rates()

sg.theme('BlueMono')


layout = [[sg.Text('Insert Currency', size=(22, 1), font='Lucida', justification='left')],
          [sg.Combo([x for x in converter.rates], default_value='USD', key='curr1', size=(10, 1))],
          [sg.Text('Amount', size=(10, 1), font='Lucida', justification='left')],
          [sg.In(1, key='amount', size=(20, 1))],
          [sg.Text('Insert Currency', size=(22, 1), font='Lucida', justification='left')],
          [sg.Combo([x for x in converter.rates], default_value='USD', key='curr2', size=(10, 1))],
          [sg.Button('Calculate', font=('Times New Roman', 12)), sg.Button('Cancel', font=('Times New Roman', 12))]]


window = sg.Window("Exchange rates calculator", layout, resizable=True)

# read user valus
while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    if event == "Calculate":
        amount = int(values['amount'])
        print(values)
        f_cur = values['curr1']
        s_cur = values['curr2']
        print(amount, f_cur, s_cur)
        print(converter.exchange(amount, f_cur, s_cur))
        sg.Print(size=(10, 2), end=str(converter.exchange(amount, f_cur, s_cur)), resizable=True)

    if event == "Cancel":
        break

window.close()
