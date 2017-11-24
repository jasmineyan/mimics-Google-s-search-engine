import bottle, httplib2, beaker.middleware

from collections import Counter
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from beaker.middleware import SessionMiddleware

from bottle import run, static_file, get, request, template, route

#global valiable for recording the history
search_history={}
user_recent_history={}
user_email = ""
login = False;

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': False,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)

@get('/')
def user_input():
	global user_email
	global login
	global search_history
	global user_recent_history
	#get the user input
	keywords = request.query_string

	#show the home page first
	if (not keywords.replace(" ","")):
		#return static_file('home.html',root='')
		return template('home', login=login, user_email=user_email)
	else:		
		#convert the input into results
		results = keywords.lower().split("=")[1].split("+")
		keywords = ' '.join(results)


		#see if user has signed in before
		if login:
			#store the recent search history
			if user_email in user_recent_history.keys():	
				user_recent_history[user_email] = results + user_recent_history[user_email]
			else:
				user_recent_history[user_email] = results 
			while '' in user_recent_history[user_email]:
				user_recent_history[user_email].remove('')
			if len(user_recent_history[user_email])>10:
				user_recent_history[user_email]=user_recent_history[user_email][:10]
			print (user_recent_history[user_email])
	
			#store the history word count			
			results = Counter(results)
			
			if user_email in search_history.keys():
				#store the user input into history
				search_history[user_email]=search_history[user_email]+results
			else:
				search_history[user_email]=results
			results = results.most_common()
			temp = search_history[user_email].most_common()
			if len(temp)>20:
				theRange = 20
			else:
				theRange = len(temp)
			return template('results_history', keywords=keywords, results=results,length=len(results),theRange=theRange, temp=temp, login=login, user_email=user_email, recent_history=user_recent_history[user_email], wordcount=len(user_recent_history[user_email]))
		else:
			results = Counter(results)
			results = results.most_common()
			return template('results_history', keywords=keywords, results=results,length=len(results),theRange=-1, temp=Counter(), login=login, user_email='', recent_history="", wordcount=-1)


@route('/login')
def log_in():
	s = bottle.request.environ.get('beaker.session')
	s.save()
	flow = flow_from_clientsecrets('client_secrets.json', scope='https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/userinfo.email', redirect_uri='http://ec2-34-237-28-99.compute-1.amazonaws.com:80/redirect')
	uri = flow.step1_get_authorize_url()
	bottle.redirect(str(uri))

@route('/logout')
def log_out():
	global user_email
	global login
	user_email = ""
	login=False
	s = bottle.request.environ.get('beaker.session')
	s.delete()
	bottle.redirect('https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=http://ec2-34-237-28-99.compute-1.amazonaws.com:80')

@route('/redirect')
def redirect_page():
	global user_email
	global login
	code = request.query.get('code','')
	flow = OAuth2WebServerFlow(client_id="671072941053-a8e1u2istl2pgdm1ah2l3q6j97q3vvdt.apps.googleusercontent.com",
							client_secret='mml2jXHYW_TNAQNdStlvP4wW',
							scope='https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/userinfo.email',
							redirect_uri="http://ec2-34-237-28-99.compute-1.amazonaws.com:80/redirect")
	credentials = flow.step2_exchange(code)
	token = credentials.id_token['sub']

	http = httplib2.Http()
	http = credentials.authorize(http)
	# Get user email
	users_service = build('oauth2', 'v2', http=http)
	user_document = users_service.userinfo().get().execute()
	user_email = user_document['email']
	login = True
	return template('home', login=login, user_email=user_email)

run(host='0.0.0.0', port=80, app=app, debug=True)
