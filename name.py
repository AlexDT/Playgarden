'''
Created on Jul 23, 2012

@author: Alex
'''
name = raw_input('Hoe heet je? \n')
maxChar = 10

if len(name) == maxChar:
    print ('Hoi %s, hoe gaat het? \nJe naam is %i characters lang (inclusief spaties).\n' % (name, maxChar))
elif len(name) > maxChar:
    print ('Hoi %s, hoe is het? \nJe naam is (inclusief spaties) meer dan %i characters.\n' % (name, maxChar))
else:
    print ('Hoi %s, hoe is het? \nJe naam is (inclusief spaties) minder dan %i characters.\n' % (name, maxChar))
print ('Klaar!\n\n')
