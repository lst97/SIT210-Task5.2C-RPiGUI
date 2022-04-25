import RPi.GPIO as GPIO
import time
from tkinter import *

class LED:
	def __init__(self, pin, selected=False):
		self.pin = pin
		self._selected = selected
		self._set_pin_mode()
		
		if self._selected:
			self._led_on()
		else: self._led_off()
		
	def _set_pin_mode(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin, GPIO.OUT)
		
	def _led_on(self):
		GPIO.output(self.pin, GPIO.HIGH)

	def _led_off(self):
		GPIO.output(self.pin, GPIO.LOW)
	
	def click(self):
		self._led_on()
		self._selected = True
		
	def unclick(self):
		self._led_off()
		self._selected = False
			
class GUI:
	def __init__(self):
		self.root = Tk()
		self.root.title('SIT210 - Task5.2C')
		# pin15,     16,    18
		# 0=red; 1=green; 2=blue
		self.led_objs = []
		self.var = IntVar()
	
	def _led_controller(self):
		selection = self.var.get()
		self.led_objs[selection].click()
		for led in self.led_objs:
			if led is not self.led_objs[selection]:
				led.unclick()
				
	def _quit(self):
		GPIO.cleanup()
		self.root.quit()
		
	def start(self):
		label_title = Label(self.root, text="SIO TOU LAI - 220619375")
		label_title.grid(row=0, column=1)

		self.led_objs.append(LED(15, selected=True))
		self.led_objs.append(LED(16))
		self.led_objs.append(LED(18))
		
		radio_red = Radiobutton(self.root, text="RED", variable=self.var, value=0, command=self._led_controller)
		radio_green = Radiobutton(self.root, text="GREEN", variable=self.var, value=1, command=self._led_controller)
		radio_blue = Radiobutton(self.root, text="BLUE", variable=self.var, value=2, command=self._led_controller)
		
		radio_red.grid(row=1, column=0)
		radio_green.grid(row=1, column=1)
		radio_blue.grid(row=1, column=2)

		button_exit = Button(self.root, text="Exit", command=self._quit)
		button_exit.grid(row=2, column=1)

		self.root.mainloop()

GUI().start()
