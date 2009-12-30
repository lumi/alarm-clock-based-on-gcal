from datetime import timedelta, datetime
from time import strftime

for i in range (2400):
	nimi = 'Lorem'+str(i)+"Ipsaani"
	email = 'Ipsun'+str(i)+"@gmail.com"
	puh = 4407489960+i
	print "INSERT INTO kuskit (name, email, phone) VALUES ('%s', '%s', %s);" % (nimi, email, puh)



	alku = i
	loppu = (960 +i) % 2400 
	kuvaus =  nimi+str(i)
	print "INSERT INTO vuorot (starting_time, ending_time, description) VALUES (%d, %d, '%s');" % (alku, loppu, kuvaus)

	kuski_id = i
	vuoro_id = i
	date = datetime.today() + timedelta(days=i)
	date = date.strftime("%Y-%m-%d")
	print "INSERT INTO kuskin_vuorot (kuski_id, vuoro_id, date) VALUES (%d, %d, '%s');" % (kuski_id, vuoro_id, date)
