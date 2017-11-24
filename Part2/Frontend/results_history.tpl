<html>
	<style>
	h1{
		color: #FCFCFC;
		margin-top: 100px;
		text-align: center;
		font-family: "Georgia";
		font-style: oblique;
	}
	p{
		color: #FCFCFC;
		text-align: center;
		font-family: "Georgia";
		font-style: oblique;
	}
	table, th, td{
		color: #FCFCFC;
		border: 1px solid white;
		position: absolute
		left: 50%;
		margin-left: 400px;
	}
	</style>
	<title>Result page</title>
	<link rel="shortcut icon" type='image/png' href='https://cdn.education.com/worksheet-image/124952/letter-coloring-page-the-alphabet.png'/>
	<body  background='http://www.planwallpaper.com/static/images/cool-background.jpg'>
		% if (login):
			<p><img src='https://cdn.education.com/worksheet-image/124952/letter-coloring-page-the-alphabet.png' width=20 height=20/> Welcome to AlphaSearch {{user_email}}! You can sign out by clicking <a href='http://ec2-34-237-28-99.compute-1.amazonaws.com:80/logout'>here</a></p>
		% else:
			<p><img src='https://cdn.education.com/worksheet-image/124952/letter-coloring-page-the-alphabet.png' width=20 height=20/> Welcome to AlphaSearch! Please click here to <a href="http://ec2-34-237-28-99.compute-1.amazonaws.com:80/login">sign in</a></p>
		% end
		<p>Back to the <a href="http://ec2-34-237-28-99.compute-1.amazonaws.com:80">home page</a> and search again!!!</p>
		<h1>Search for "{{keywords}}"</h1>
		<table id='results' style="width:25%">
			<caption>Result for this search:</caption>
			<tr>
				<th>Word</th>
				<th>Count</th>
			</tr>
			% for n in range(length):
				<tr><td>{{results[n][0]}}</td><td>{{results[n][1]}}</td></tr>
			% end
		</table>
		% if (login):
			<table id='history' style="width:25%">
			<caption>User history word count:</caption>
			<tr>
				<th>Word</th>
				<th>Count</th>
			</tr>
			% for n in range(theRange):
				<tr><td>{{temp[n][0]}}</td><td>{{temp[n][1]}}</td></tr>
			% end
			</table>
			<table>
			<table id='history' style="width:25%">
			<caption>User recently search:</caption>
			<tr>
				<th>Word</th>
			</tr>
			% for n in range(wordcount):
				<tr><td>{{recent_history[n]}}</td></tr>
			% end
			</table>
		% end
	</body>
</html>
