#!/usr/bin/env python

import mysql.connector

mydb = mysql.connector.connect("localhost","root","admin") 
print("données trouvées" ) 
mydb.close()
