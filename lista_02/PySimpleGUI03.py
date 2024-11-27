#https://www.dionysus.biz/PySimpleGUI-Examples.html
#site de referencia
#!/usr/bin/python
# Multi Widget Window with PySimpleGUI27
# Example below presents Slider in horizontal orientation
# The GUI panel presents three radio buttons, slaved together
# finally, a button that triggers python to read the window & produce return values to the main program
# values are printed by the i loop near the end

import PySimpleGUI as sg
form=sg.FlexForm('colors',auto_size_text=True,font=('Helvetica',14))
layout=[[sg.Text('Colors',text_color='black')],
	[sg.Slider(range=(1,80), orientation='h', size=(15,20),background_color='#7BEA0C')],
	[sg.Radio('coffee',group_id=1,background_color='red')],
	[sg.Radio('tea',group_id=1, background_color='blue')],
	[sg.Radio('milk', group_id=1, background_color='cyan')],
	[sg.Radio('OJ', group_id=1, background_color='green')],
	[sg.SimpleButton('Do It!',size=(8,1))],
	]
window=sg.Window('Cat Barn', layout)

button,values=window.Read()

print ('value of button is:')
print (button)
print ('values of various controls are:')

for i in range(0,5):
	print (values[i])

quit()
    