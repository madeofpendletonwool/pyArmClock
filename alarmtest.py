#!/bin/python3

import time
import datetime
import PySimpleGUI as sg
import yaml
import pyglet
import tkinter.font

Time_Period = ("AM", "PM")
Hour = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
Min = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60)

def now():
    ntime=datetime.datetime.now()
    nt=ntime.strftime('%H:%M:%S')
    return nt

def play():
    player.play()

def pause():
    player.pause()

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            Wake_Up()
            break

def time_conversion():
    # Conversions to make time work - 12 to 24
    if time_section == "PM":
        hour_conv = hour_time + 12
    else: hour_conv = hour_time

    if min_time < 10:
        min_strconv = str(min_time)
        min_conv = "0" + min_strconv
    else: min_conv = str(min_time)

    if hour_conv < 10:
        hour_strconv = str(hour_conv)
        hour_convfin = "0" + hour_strconv
    else: hour_convfin = str(hour_conv)

def Wake_Up():
    while True:
        play()

        sg.theme('DarkAmber')   # Add a touch of color
        # All the stuff inside your window.
        layout = [  [sg.Text('Wake up!')],
                    [sg.Button('Ok'), sg.Button('Snooze')]             
                ]
            
        window = sg.Window('pyArmClock', layout)

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Snooze': # if user closes window or clicks cancel
            window.close()
            pause()
            time.sleep(5)
        else: break

def reverse_time_conversion(alarm_convert):

    # Conversions to make time work in reverse order - 24 to 12

    rev_hour = alarm_convert[:2]
    rev_min = alarm_convert[3:5]

    if rev_hour[:1] == '0':
        rev_hour1 = rev_hour[:2]
    else: rev_hour1 = rev_hour

    if rev_min[:1] == '0':
        rev_min1 = rev_min[:2]
    else: rev_min1 = rev_min

    num_rev_hour = int(rev_hour1)
    num_rev_min = int(rev_min1)

    if num_rev_hour > 12:
        num_rev_hourconv = num_rev_hour - 12
        rev_time_period = 'PM'
    else: 
        rev_time_period = 'AM'
        num_rev_hourconv = num_rev_hour


    num_rev_hourconv1 = str(num_rev_hourconv)

    if num_rev_min < 10:
        num_rev_minconv = '0' + str(num_rev_min)
    else: num_rev_minconv = str(num_rev_min)

    rev_time_convert = f'{num_rev_hourconv1}:{num_rev_minconv} {rev_time_period}'
    return rev_time_convert




def alarm_select(theme):
        while True:
            sg.theme(theme)   # Add a touch of color
            # Call in alarms file
            with open('/home/collinp/Documents/GitHub/pyArmClock/alarms_sample.yaml') as f:
                alarms = yaml.load(f, Loader=yaml.FullLoader)

            # Time Conversion
                rtc1 = reverse_time_conversion(alarms['Alarm1'][1]['Time'])
                rtc2 = reverse_time_conversion(alarms['Alarm2'][1]['Time'])
                rtc3 = reverse_time_conversion(alarms['Alarm3'][1]['Time'])
            # All the stuff inside your window.
                layout = [  [sg.Text('Alarm 1:')],
                            [sg.Text(alarms['Alarm1'][0]['Alarm_Name']), sg.Text('|'), sg.Text(rtc1)],
                            [sg.Button(f'Wake up to {alarms["Alarm1"][0]["Alarm_Name"]}?'), sg.Button(f'Edit {alarms["Alarm1"][0]["Alarm_Name"]}?'), sg.Button(f'Delete {alarms["Alarm1"][0]["Alarm_Name"]}?')],
                            [sg.Text('Alarm 2:')],
                            [sg.Text(alarms['Alarm2'][0]['Alarm_Name']), sg.Text('|'), sg.Text(rtc2)],
                            [sg.Button(f'Wake up to {alarms["Alarm2"][0]["Alarm_Name"]}?'), sg.Button(f'Edit {alarms["Alarm1"][0]["Alarm_Name"]}?'), sg.Button(f'Delete {alarms["Alarm2"][0]["Alarm_Name"]}?')],
                            [sg.Text('Alarm 3:')],
                            [sg.Text(alarms['Alarm3'][0]['Alarm_Name']), sg.Text('|'), sg.Text(rtc3)],
                            [sg.Button(f'Wake up to {alarms["Alarm3"][0]["Alarm_Name"]}?'), sg.Button(f'Edit {alarms["Alarm1"][0]["Alarm_Name"]}?'), sg.Button(f'Delete {alarms["Alarm3"][0]["Alarm_Name"]}?')],
                            [sg.Button('Ok')]               
                        ]
                    
                window = sg.Window('pyArmClock', layout)

                event, values = window.read()

                if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks cancel
                    window.close()
                    break

                if event == f'Wake up to {alarms["Alarm1"][0]["Alarm_Name"]}?':
                    window.close()
                    alarm(alarms['Alarm1'][1]['Time'])
                    break
                elif event == f'Wake up to {alarms["Alarm2"][0]["Alarm_Name"]}?':
                    window.close()
                    alarm(alarms['Alarm2'][1]['Time'])
                    break
                elif event == f'Wake up to {alarms["Alarm3"][0]["Alarm_Name"]}?':
                    window.close()
                    alarm(alarms['Alarm3'][1]['Time'])
                    break


def make_window(theme,cfont):
    sg.theme(theme)   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('',key='clocktime',font=(cfont,40),justification='center')],
                [sg.Text('When Would you like to wake up?')],
                [sg.Text('Select Time:')],
                [sg.Combo(Hour), sg.Combo(Min), sg.Combo(Time_Period)],
                [sg.Button('Ok')],
                [sg.Button('Choose Alarm'), sg.FileBrowse('Choose Song', file_types=(("MP3 files", "*.mp3"),))],
                [sg.Button('Change Theme',key='Choose Theme'), [sg.Button('Clock Font',key='-font-')]]
                
            ]
        # Create the Window
    window = sg.Window('pyArmClock', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    print(window)
    while True:
        event, values = window.read(timeout=10,timeout_key='timeout')
        if event == 'timeout':
            window['clocktime'].update(now())

        if event == 'Choose Theme':
            theme_choose(theme)

        if event == 'Choose Alarm':
            alarm_select(theme)

        # Check if alarm values were populated
        if values == {}:
            sg.theme('DarkAmber')   # Add a touch of color
            # All the stuff inside your window.
            layout = [  [sg.Text('ALARM TIME REQUIRED!!')],
                        [sg.Button('Ok')]
                        
                    ]

            # Create the Window
            window = sg.Window('pyArmClock', layout)
            if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks cancel
                break
                window.close()
        #End Alarm Values check
        if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks cancel
            window.close()
            break
        
    #Pyglet Music Setup
    player = pyglet.media.Player()
    song = values['Choose Song']
    src = pyglet.media.load(song)
    player.queue(src)

    hour_temp = values[0]
    hour_time = values[0]
    min_time = values[1]
    time_section = values[2]
    print(values)

    # Conversions to make time work 
    if time_section == "PM":
        hour_conv = hour_time + 12
    else: hour_conv = hour_time

    if min_time < 10:
        min_strconv = str(min_time)
        min_conv = "0" + min_strconv
    else: min_conv = str(min_time)

    if hour_conv < 10:
        hour_strconv = str(hour_conv)
        hour_convfin = "0" + hour_strconv
    else: hour_convfin = str(hour_conv)

    print(f"Got it! I'll wake you up at {hour_temp}:{min_conv} {time_section}")

    current_time = time.localtime()
    if current_time.tm_sec < 10:
        sec_strconv = str(current_time.tm_sec)
        sec_conv = "0" + sec_strconv
    else: sec_conv = str(current_time.tm_sec)

    print("before returning")


    set_alarm_timer = f"{hour_convfin}:{min_conv}:{sec_conv}"
    print('Next line Timer')
    print(set_alarm_timer)
    Time_Period
    alarm(set_alarm_timer)


def main():
    #preset font and theme
    cfont='Times New Roman'
    theme='DarkBrown'
    window=make_window(theme,cfont)

def theme_choose(theme):
    #layout and window create
    sg.theme(theme)
    event,values = sg.Window('Theme Browser',
    [[sg.Text('theme browsing')],
    [sg.Text('click theme color')],
    [sg.Combo(values=sg.theme_list(),size=(20,12),key='-LIST-',readonly=True)],
    [sg.OK(),sg.Cancel()]]).read(close=True)

            #select and click 'OK', change theme value 
    #and pass over  make_window function it
    if event == 'OK':
        theme=values['-LIST-']
        window.close()
        make_window(theme,cfont) 

    while True:
#if you set timeout, you can operate GUI by spend time
        event,values=wnd.read(timeout=10,timeout_key='-timeout-')
        #getting current time per 10ms
        if event == '-timeout-':
            wnd['-time-'].update(now())

        if event in (sg.WIN_CLOSED,'-close-'):
            break

            #select and click 'OK', change theme value 
            #and pass over  make_window function it
            if event == 'OK':
                theme=values['-LIST-']
                wnd.close()
                wnd= make_window(theme,cfont) 
        #when click font change button, open the window its looks like theme window
        if event == '-font-':
            #layout and window create
            event,values = sg.Window('Font Browser',
            [[sg.Text('Font browsing')],
            [sg.Text('click font')],
            [sg.Combo(values=tkinter.font.families(),size=(20,12),key='-FONT-',readonly=True)],
            # or
            # [sg.Combo(values=sg.Text.fonts_installed_list(),size=(20,12),key='-FONT-',readonly=True)],
            [sg.OK(),sg.Cancel()]]).read(close=True)

            #change font value and pass over make_window function it
            if event == 'OK':
                cfont=values['-FONT-']
                wnd.close()
                wnd= make_window(theme,cfont)
            
        
    wnd.close()

main()
