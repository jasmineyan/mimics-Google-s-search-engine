from bottle import run, static_file, get, request, template
from collections import Counter

#global valiable for recording the history
search_history=Counter()

#clear the history of previous search	
text_file = open('history.txt','w')
text_file.write("")
text_file.close

@get('/')
def user_input():
	global search_history
	#get the user input
	keywords = request.query_string

	#show the home page first
	if (not keywords.replace(" ","")):
		return static_file('home.html',root='')
	else:		
		#convert the input into results
		results = keywords.lower().split("=")[1].split("+")
		keywords = ' '.join(results)
		results = Counter(results)
		#store the user input into history
		search_history=search_history+results
		results = results.most_common()
		
		#store the history
		history = "<table id='history'>\n\t<tr>\n\t\t<th>Word</th>\n\t\t<th>Count</th>\n"
		temp = search_history.most_common()
		if len(temp)>20:
			theRange = 20
		else:
			theRange = len(temp)
		for n in range(theRange):	
			history = history + "\t</tr>\n\t<tr>\n\t\t<td>"+str(temp[n][0])+"</td>\n\t\t<td>"+str(temp[n][1])+"</td>\n\t</tr>\n"
		history = history + "</table>"
		
		#write the history in a text file called history.txt
		text_file = open('history.txt','w')
		text_file.write(history)
		text_file.close()

		#show the result
		return template('results', keywords=keywords, results=results,length=len(results))

run(host='localhost', port=8080, debug=True)
