'''
Created on Jul 23, 2012

@author: Alex Dias Teixeira
'''
def namegame():
	DoWhat = raw_input("Wil je je naam doorgeven? (Y/N)\n")

	if DoWhat == 'Y':
	    print 'Ok, lets go!\n'
	    import name
	elif DoWhat == 'N':
	    print 'Ok, dan niet... :S\n'
	else:
	    print 'Je had met Y of N moeten antwoorden. Y staat voor Yes(ja) en N staat voor No(nee).\n'
    	namegame()
namegame()
