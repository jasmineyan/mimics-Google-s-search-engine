<html>
	<title>Result page</title>
	<img src='https://cdn.education.com/worksheet-image/124952/letter-coloring-page-the-alphabet.png' width=50 height=50/>
	<link rel="shortcut icon" type='image/png' href='https://cdn.education.com/worksheet-image/124952/letter-coloring-page-the-alphabet.png'/>
	<style>
		th{
			text-align: left;
		}
	</style>
	<body>
		<h1>Search for "{{keywords}}"</h1>
		<table id='results' style="width:25%">
			<tr>
				<th>Word</th>
				<th>Count</th>
			</tr>
			% for n in range(length):
				<tr><td>{{results[n][0]}}</td><td>{{results[n][1]}}</td></tr>
			% end
		</table>
	<p>Back to the <a href="http://localhost:8080/">home page</a></p>
	</body>
</html>
