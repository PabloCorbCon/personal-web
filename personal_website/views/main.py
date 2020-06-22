from django.http import HttpResponse

def index(repquest)
	
	html_code = '''
	<!DOCTYPE html>
	<html>
	<head>
		<title>Pablo Corbalán</title>
		<link rel='stylesheet" type="text/css" href="style/indexStyle.css'>
	</head>
	<body>
		<header>
			<div id = "pablo-corbalan-div">
				<h1 align="center" id="pablo-corbalan">Pablo Corbalán</h1>
			</div>
			<h3 id = "description-of-myself">Programmer, Software dev, freelancer, student</h3>
		</header>
		<!--Navigation-->
		<nav>
			<ul>
				<li>
					<a href="https://github.com/PabloCorbCon">GitHub</a>
				</li>
				<li>
					<a href="#">Contact</a>
				</li>
			</ul>
		</nav>
		<!--About me paragraph-->
		<p>
			Hi. I'm Pablo.
			I enjoy technology. I enjoy programming and I enjoy the economy.
			I have been programming since I was 10 years old, I started with C # and currently I mostly write Python.
			I hope I can continue learning
		</p>
		<!-- Habilities-->
		<h4 class = "intro-title">Programming as pasion</h4>
		<p>
			My main skill, hobby and hobby is programming, the feeling of solving an error or solving a problem that you have been going around for a long time is really good and I love it.
		</p>
		<h4 class = "intro-title">Economy for the future</h4>
		<p>
			The economy is also a sector that I particularly like. I preffer the economy focused on a practical and functional field, more than the economy focused on the historical field.
		</p>
		<h4 class = "intro-title">Debate to think</h4>
		<p>
			I like to debate and talk to people, explain things or argue. If we can talk about an interesting topic, better!
		</p>
		<h4 class= "intro-title">Digital marketing to explore</h4>
		<p>
			Since I liked retail business, economics, and programming, I became interested in digital marketing. I like the promotion on social networks and decided, thanks to this ability to start with web programming.
		</p>
		<!--Git Hub-->
		<h3 class = "intro-title">Lazy GitHub</h3>
		<a href="https://github.com/PabloCorbCon">GitHub</a>
		<p>
			As many programmers know nowadays I use github, and I am not the exception. Virtually all the code I write is open source and unlicensed. You can see everything from the link to my github: "PabloCorbCon"
		</p>
	</body>
	</html>
	'''

	return(HttpResponse(html_code))