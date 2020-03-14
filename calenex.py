from datetime import datetime, timedelta

import PySimpleGUI as sg
import stk

layout = [[sg.Text('Calendar Test')],
          [sg.Input('', size=(20, 1), key='input1')],

          [sg.CalendarButton('Choose Date', target='input1', key='date', format='%Y-%m-%d')],
[sg.Output(size=(50, 20),  key='_OUTPUT_', )],
          [sg.Ok(key=1)]]

window = sg.Window('Calendar', layout, grab_anywhere=False)
while True:
    k=0
    k1=0
    k2=0
    k3=0
    rdp=0
    ema15=0
    pema15=0
    event, values = window.read()
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
    
    #window['_OUTPUT_'].update(values['input1'])

    s1=values['input1']
    today = datetime.strptime(s1,'%Y-%m-%d')
    yesterday = today - timedelta(days=1)
    d=datetime.strftime(yesterday,'%Y-%m-%d');
    day2=yesterday - timedelta(days=5);
    d2=datetime.strftime(day2,'%Y-%m-%d');
    day3=day2 - timedelta(days=5);
    d3=datetime.strftime(day3,'%Y-%m-%d');
    day4 = day3 - timedelta(days=5);
    d4 = datetime.strftime(day4, '%Y-%m-%d');

    mycursor = stk.mydb.cursor()
    mycursor.execute("Select Close from  fbtab where Date='%s'" % (d,))

    for x in mycursor:
       k=x[0]
    print("1",k)

    mycursor.execute("Select Close from  fbtab where Date='%s'" % (d2,))
    for x in mycursor:
       k1=x[0]
    print("2",k1)
    mycursor.execute("Select Close from  fbtab where Date='%s'" % (d3,))
    for x in mycursor:
        k2 = x[0]
    print("3",k2)
    mycursor.execute("Select Close from  fbtab where Date='%s'" % (d4,))
    for x in mycursor:
        k3 = x[0]
    print("4",k3)
    rdp=k+k1+k2+k3
    print("rdp:",rdp,"ema15:",ema15)
    ema15=rdp-k2
    pe=k3+k2+k1
    pema15=ema15-pe
    print("e15",pema15,"cl: ",pe)


window.close()
