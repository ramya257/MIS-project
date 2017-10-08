from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import connection
from models import *
import json
from django.db.models import Q


import MySQLdb

# Create your views here.

def home(request):
	'''
		render home.html
	'''
	return HttpResponse(render(request, "home.html"))

@login_required
def traininfo(request):
    if request.method == "POST": 
    #commit      
    	print ("true")                                
    	trainno = str(request.POST.get('trainno'))
    	print(trainno)
    	if trainno == "" or 'e' in trainno:
            HttpResponse("invalid train number")	
        response_json={}	
        train=Train.objects.filter(Train_No=trainno)
    
        #stoppage_data=Stoppage.objects.filter(Train_No=trainno)
        stoppage_data=Stoppage.objects.filter(Train_No=trainno)
        # print(trainno)
        # print(stoppage_data.Train_No)
        # print(stoppage_data.Station_Code)
        print(stoppage_data)
        response_json["stoppages"]=[]
        response_json["station_details"] = []
        response_json["train_details"]=[]
        response_json["train_running_days"]=[]
        
        #station_data=Station.objects.get(Station_Code=stoppage_data.Station_Code)
        for stops in stoppage_data:
        	temp_stoppage={}
        	temp_stoppage["station_code"]=str(stops.Station_Code)
        	temp_stoppage["arrival_time"]=str(stops.Arrival_Time)
        	temp_stoppage["departure_time"]=str(stops.Departure_Time)
        
        response_json["stoppages"].append(temp_stoppage)
        response_json["show"]=True

        for trains in train:
        	temp_trains={}
        	temp_train_running_days={}
        	temp_trains["train_number"]=str(trains.Train_No)
        	temp_trains["train_name"]=str(trains.Name)
        	temp_trains["sleepeer_seats"]=str(trains.Seat_Sleeper)
        	temp_trains["ac_first_class_seats"]=str(trains.Seat_First_Class_AC)
        	temp_trains["ac_third_class_seats"]=str(trains.Seat_Third_Class_AC)
        	temp_trains["wifi"]=str(trains.Wifi)
        	temp_trains["fare"]=str(trains.Fare)
        	temp_trains["food"]=str(trains.Food)
        	temp_train_running_days["Sunday"]=str(trains.Run_On_Sunday)
        	temp_train_running_days["Monday"]=str(trains.Run_On_Monday)
        	temp_train_running_days["Tuesday"]=str(trains.Run_On_Tuesday)
        	temp_train_running_days["Wednesday"]=str(trains.Run_On_Wednesday)
        	temp_train_running_days["Thursday"]=str(trains.Run_On_Thursday)
        	temp_train_running_days["Friday"]=str(trains.Run_On_Friday)
        	temp_train_running_days["Saturday"]=str(trains.Run_On_Saturday)
        response_json["train_details"].append(temp_trains)
        response_json["train_running_days"].append(temp_train_running_days)

       # stoppage=Stoppage.objects.select_related().filter(train_Train_No=trainno)
        # all_rows=Station.objects.all()
        # print(all_rows)
        # scode={}
        # for row in all_rows:
        #     scode[str(row[0])] = str(row[1])
        # station={}
      
        for row in stoppage_data:
        	print(1)
        	print (row.Station_Code) 
        	station_data=Station.objects.get(Station_Code=row.Station_Code)
        	temp_json = {}
        	temp_json["station_code"] = str(station_data.Station_Code)
        	temp_json["station_name"] = str(station_data.Station_Name)
        	response_json["station_details"].append(temp_json)
              
        print(response_json)
        # context = {"info":train, "stop":stoppage_data, "station":station, "show":True}
        # print(context)
        if train == None:
        	return HttpResponse("invalid train number")
        else:
        	#return HttpResponse(render(request, "traininfo.html",{"obj_as_json": json.dumps(context)}))
        	return JsonResponse(response_json)
    else:
    	return HttpResponse(render(request, "traininfo.html", {"show":False,}))

@login_required
def findtrains(request):
	'''
		This method can be called iff user is signed in
		Case 1: GET request
			render 	findtrains.html
		Case 2: POST request
			check for validation of inputs
			if valid render modified findtrains.html
	'''
	response_json={}
	if request.method == "POST":
		fstation = request.POST.get('fstation')
		sstation = request.POST.get('sstation')
		print(fstation)
		print(sstation)

		if len(fstation) == 0 or len(sstation) == 0:
			return HttpResponse("station code can't be empty")

		for c in fstation:
			if c == " ":
				return HttpResponse("space is not allowed")

		for c in sstation:
			if c == " ":
				return HttpResponse("space is not allowed")

		if fstation == sstation:
			return HttpResponse("station code must be different")

		# c = connection.cursor()
		# c.execute('''select a.Train_No from Stoppage as a join Stoppage as b on a.Train_No = b.Train_No 
		# 	         where a.Station_Code = "%s" and b.Station_Code = "%s" ''' %(fstation, sstation))
		response_json["train_details"]=[]
		# trains = c.fetchall()
		try:
			filterargs = { 'Station_Code': fstation, 'Station_Code': sstation}
			trains=Stoppage.objects.filter(**filterargs)
			for t in trains:
				temp_trains={}
				temp_trains["train_no"]=str(t.Train_No)
				train_name=Train.objects.get(Train_No=str(t.Train_No))
				temp_trains["train_name"]=str(train_name.Name)
				response_json["train_details"].append(temp_trains)	
				print(response_json)
			return JsonResponse(response_json)
		except Exception as e:
			print(e)
			return HttpResponse("Something went wrong!!")
		finally:
			print("success")
			pass
			
		#trains=train1.filter(Q(Station_Code=fstation) | Q(Station_Code=sstation)).values('Train_No').distinct()
	else:
		return HttpResponse(render(request, "findtrains.html", {"show":False}))	

@login_required
def ticket(request):
	'''
		This method can be called iff user is signed in
		Case 1: GET request
			render 	ticket.html
		Case 2: POST request
			check for validation of inputs
			if valid render modified ticket.html
	'''
	if request.method == "POST":
		tnumber = request.POST.get('tnumber')
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		gender = request.POST.get('gender')
		age = request.POST.get('age')
		tclass = request.POST.get('tclass')
		number = request.POST.get('number')

		c = connection.cursor()
		c.execute("SELECT * FROM Train where Train_No = '%s' " %(tnumber))

		train = c.fetchall()

		if len(train) == 0:
			return HttpResponse("Incorrect Train Number")

		train = train[0]

		alpha = map(chr, range(97, 123))

		invalid = False
		
		if len(fname) == 0:
			invalid = True

		for c in fname:
			if c not in alpha:
				invalid = True
				break	

		if invalid:
			return HttpResponse("invalid fname, characters allowed [a-z]")

		invalid = False
		
		if len(lname) == 0:
			invalid = True

		for c in lname:
			if c not in alpha:
				invalid = True
				break

		if invalid:
			return HttpResponse("invalid lname, characters allowed [a-z]")

		if age == "" or 'e' in age or int(age) > 100:
			return HttpResponse("invalid age")

		num = map(chr, range(48, 58))
		invalid = False

		if len(number) != 10:
			invalid = True
		for c in number:
			if c not in num:
				invalid = True
				break

		if invalid:
			return HttpResponse("invalid phone number")

		gender = gender[0]
		if str(tclass) == "sleeper" and int(train[2]) <= 0:
			return HttpResponse("seat not available in sleeper class")
		if str(tclass) == "first class ac" and int(train[3]) <= 0:
			return HttpResponse("seat not available in first class ac")
		if str(tclass) == "second class ac" and int(train[4]) <= 0:
			return HttpResponse("seat not available in second class ac")
		if str(tclass) == "third class ac" and int(train[5]) <= 0:
			return HttpResponse("seat not available in third class ac")

		c = connection.cursor()		
		c.execute("SELECT * FROM Ticket")
		maximum = 0
		for row in c.fetchall():
			maximum = max(maximum, int(row[0]))

		ticketno = maximum + 1
		import datetime
		now = datetime.datetime.now()
		now = str(now)
		jdate = (now.split())[0]
		
		c.execute('''INSERT INTO Ticket VALUES("%s", "%s", "%s", "%s")
					 ''' %(ticketno, tnumber, jdate, request.user))

		c.execute('''INSERT INTO Passenger(First_name, Last_name, Gender, Phone_No,
			         Ticket_No, Age, Class) VALUES
			         ("%s", "%s", "%s", "%s", "%s", "%s", "%s")
			         ''' %(fname, lname, gender, number, ticketno, age, tclass))
        
		if str(tclass) == "sleeper":
			c.execute('''UPDATE Train set Seat_Sleeper = "%s" WHERE Train_No = "%s"
				         ''' %(int(train[2])-1, tnumber))
		if str(tclass) == "first class ac":
			c.execute('''UPDATE Train set Seat_First_Class_AC = "%s" WHERE Train_No = "%s"
				         ''' %(int(train[3])-1, tnumber))
		if str(tclass) == "second class ac":
			c.execute('''UPDATE Train set Seat_Second_Class_AC = "%s" WHERE Train_No = "%s"
				         ''' %(int(train[4])-1, tnumber))
		if str(tclass) == "third class ac":
			c.execute('''UPDATE Train set Seat_Third_Class_AC = "%s" WHERE Train_No = "%s"
				         ''' %(int(train[5])-1, tnumber))			

		return HttpResponse(render(request, "ticket.html", {"show":True}))
	else:
		return HttpResponse(render(request, "ticket.html", {"show":False}))	

def signup(request):
	if request.method == "POST":
		username = str(request.POST.get('username'))
		password = str(request.POST.get('password'))
		email = str(request.POST.get('email'))
		address = str(request.POST.get('address'))
		fnumber = str(request.POST.get('fnumber'))
		snumber = str(request.POST.get('snumber'))

		alphanum = map(chr, range(97, 123)) + map(chr, range(48, 58))
		num = map(chr, range(48, 58))

		invalid = False
		
		if len(username) == 0:
			invalid = True

		for c in username:
			if c not in alphanum:
				invalid = True
				break

		if invalid:
			return HttpResponse("invalid username, characters allowed [a-z] and [0-9]")


		invalid = False

		if len(password) == 0:
			invalid = True

		for c in password:
			if c == " ":
				invalid = True
				break

		if invalid:
			return HttpResponse("space not allowed in the password")
		
		if len(address) == address.count(' '):
			return HttpResponse("invalid address")

		
		invalidf, invalids = False, False	

		if len(fnumber) != 10:
			invalidf = True
		for c in fnumber:
			if c not in num:
				invalidf = True
				break

		if len(snumber) != 10:
			invalids = True
		for c in snumber:
			if c not in num:
				invalids = True
				break

		if invalidf and invalids:
			return HttpResponse("atleast one contact must be valid")

		try:
			#user = User.objects.create_user(username, None, password)
			# c = connection.cursor()
			# c.execute('INSERT INTO Account VALUES("%s", "%s", "%s", "%s")' %(username, password, email, address))
			# if not invalidf:	
			# 	c.execute('INSERT INTO Contact VALUES("%s", "%s")' %(username, fnumber))
			# if not invalids:	
			# 	c.execute('INSERT INTO Contact VALUES("%s", "%s")' %(username, snumber))
			account_data, created=Account.objects.get_or_create(Username=username,Password=password,Email_Id=email,Address=address)
			account_data.save()
			return HttpResponse(render(request, "login_success.html"))

		except Exception as e:
			print e
			return HttpResponse("Something went wrong")
	else:
		return HttpResponse(render(request, "form_signup.html"))

def login_user(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		#user = authenticate(username = username, password = password)	
		user=Account.objects.get(Username=username,Password=password)	

		try :
			if (user):
				#login(request, user)
				print("true")
				return HttpResponse(render(request, "login_success.html",{"user_name": username}))
			
			else:
				return HttpResponse("invalid credentials")
		except Exception as e:
			print e
			return HttpResponse("User Not Found !")

		'''
		try:
			c = connection.cursor()
			c.execute('SELECT * FROM Account WHERE Username = "%s" and Password = "%s"' %(username, password))
			table = c.fetchall()
			if len(table) != 1:
				return HttpResponse("invalid credentials")
			return HttpResponse("login successful! cheers")

		except Exception as e:
			print e
		finally:
			c.close()
		'''	

	return HttpResponse(render(request, "form_login.html"))


def logout_user(request):	
	logout(request)	
	return HttpResponseRedirect("/home/")
	#return HttpResponse(render(request, "home.html"))