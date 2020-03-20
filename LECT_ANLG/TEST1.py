import sys,time, machine
from machine import Pin, ADC
def lecture(pin):
	value=ADC(Pin(pin))
	value.atten(ADC.ATTN_11DB)
	try:
		valor=value.read()
		return(valor)
	except:
		valor=0
		print('Error o Valor 0')
		return(valor)

#-------------------------------
if __name__=='__main__':
	while 1:
		ADC_pin=36
		lecture(ADC_pin)
	
