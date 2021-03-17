import mysql.connector as mysqlcon

connection = mysqlcon.connect(host='johnny.heliohost.org',user='aarav_admin',password='Xx.GulagROOT123')

def sendBugReport(name,email,title,bugReport):

	try:	
		cursor = connection.cursor()
		cursor.execute('USE aarav_admin')
		cursor.execute('SELECT ReportID FROM reports')

		reportID = str(int(cursor.fetchall()[-1][0]) + 1)
	except:
		reportID = str(1)

	cursor.execute('INSERT INTO reports VALUES('+reportID+','+'\''+name+'\''+','+'\''+email+'\''+','+'\''+title+'\''+','+'\''+bugReport+'\''+')')
	cursor.execute('commit')
	cursor.close()

def sendFeedback(name,rate,note):
	try:
		cursor = connection.cursor()
		cursor.execute('USE aarav_admin')
		cursor.execute('SELECT FeedbackID FROM feedback')

		feedbackID = str(int(cursor.fetchall()[-1][0]) + 1)
	except:
		feedbackID = str(1)

	cursor.execute('INSERT INTO feedback VALUES('+feedbackID+','+'\''+name+'\''+','+str(rate)+','+'\''+note+'\''+')')
	cursor.execute('commit')
	cursor.close()

def sendRootRequest(name,email,reason):
	try:
		cursor = connection.cursor()
		cursor.execute('USE aarav_admin')
		cursor.execute('SELECT RequestID FROM requests')

		requestID = str(int(cursor.fetchall()[-1][0]) + 1)
	except:
		requestID = str(1)

	try:
		cursor.execute('INSERT INTO requests VALUES('+requestID+','+'\''+name+'\''+','+'\''+email+'\''+','+'\''+reason+'\')')
	except mysqlcon.Error as e:
		print(e)
	cursor.execute('COMMIT')
	cursor.close()
