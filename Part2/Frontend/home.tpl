<!DOCTYPE html>
<html>
	<style>
	h1{
		color: #FCFCFC;
		margin-top: 250px;
		text-align: center;
		font-family: "Georgia";
		font-style: oblique;
	}
	form{
		color: #FCFCFC;
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
	</style>
	<link rel="shortcut icon" type='image/png' href='https://cdn.education.com/worksheet-image/124952/letter-coloring-page-the-alphabet.png'/>
	<body background='http://www.planwallpaper.com/static/images/cool-background.jpg'>
		% if (login):
			<p>Welcome {{user_email}}! You can sign out by clicking <a href='http://ec2-34-237-28-99.compute-1.amazonaws.com:80/logout'>here</a></p>
		% else:
			<p>Welcome! Please click here to <a href="http://ec2-34-237-28-99.compute-1.amazonaws.com:80/login">sign in</a></p>
		% end
		<h1><img src='https://cdn.education.com/worksheet-image/124952/letter-coloring-page-the-alphabet.png' width=30 height=30/> AlphaSearch</h1>
		<p>Please type in your keywords:</p>
		<form action='/' method='GET'>
			Keywords:
			<input type='text' name='keywords'>
			Submit:
			<input type='submit' value='Submit'>
		</form>
	</body>
</html>
