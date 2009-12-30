import psycopg2
from datetime import timedelta, datetime, strptime

db = psycopg2.connect(user='aal', db='posgresql', passwd='123', host='localhost')
cursor = db.cursor()
kuski_id = postparams['kuski_id']

def get_vuorot(request):
	cursor.executemany("""
	SELECT v.date, kv.start_time, v.end_time, v.description
	FROM kuskin_vuorot kv
	LEFT JOIN vuorot v
	WHERE kuski_id = %(kuski_id)i
	ORDER BY v.start_time DESC""",
	kuski_id)

	vuorot = cursor.fetchall()
	return vuorot


def get_end_date(start_date, start_time):
	

# kuski_id from POST
def get_reminder_time(kuski_id):
	cursor.execute("""
	SELECT reminder_minutes FROM kuskit
	WHERE kuski_id = %(kuski_id)i""",
	kuski_id)

	reminder_time = cursor.fetch()
	return reminder_time


def get_reminder_date(reminder_time, start_date, start_time):
	reminder_minutes = timedelta(minutes=reminder_time)
	start_time = strptime(start_time, "%Y-%m-%d")
	reminder_date = start_date - reminder_minutes 
	return reminder_date


def get_google_csv(request):
	vuorot = get_vuorot()

	subject = vuoro_id
		
	start_date = vuorot[0]
	start_time = vuorot[1]
	end_date = get_end_date(start_time, end_time)
	end_time = vuorot[2]

	all_day_event_status = "off"
	reminder_status = "on"
	reminder_date = get_reminder_date(reminder_time, start_date, start_time)
	reminder_time = get_reminder_time(kuski_id)
	description = vuorot[3]

	reminder_date = get_reminder_date(reminder_time(kuski_id), start_time, end_time)
	organizer = "Paunu"
	description = "Tampere Helsinki ja Ikaalinen"
	location = "Tampere"
	private_status = "on"


	# Take a vuoro
	# Subject,Start Date,Start Time,End Date,End Time,All Day Event,Reminder On/Off,Reminder Date,Reminder Time,Meeting Organizer,Description,Location,Private
	return [subject, start_date, start_time, end_date, end_time, 
		all_day_event_status, reminder_status, reminder_date, reminder_time, 
		organizer, description, location, private_status] 



# Let's fire!
get_google_csv()
