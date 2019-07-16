from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def index():
   return """
<!doctype html>
<html>
   <head>
   	<title>Nerd's work and space</title>
   	<meta charset="utf-8"/>
   	<style>
   	  img{
   	  	 height: 309px;
         width: -webkit-fill-available;
   	  }
   	  .abt{
   	  	    font-size: 42px;
            font-family: cursive;
   	  }
   	  .lr{
   	  	    font-size: 25px;
            text-align: center;
            word-spacing: 32px;
            margin-top: 20px;
   	  }
   	  #link:hover{
             text-decoration: underline;
             background-color: blue;
      }
      #link{
             border: 2px solid black;
             padding: 5px 5px;
             text-align: center;
             text-decoration: none;
             display: inline-block;
             font-size: 20px;
             font-style: bold;
             cursor: pointer;
             margin:auto;
             text-decoration: none;
             background-color: gold;
             color: unset;
       }
   	</style>
   </head>
   <body>
   	 <img src="logo.jpeg">
   	 <div class="abt">
   	 	Hey there Nerd! Are you looking for python courses,then you are at right place to start with.
        We provide best learning courses for the programmers who are beginers in python language and we have
        questions that to be solved.As you learn python the questions level will also increase so that you can be a pro in python.
   	 </div>
   	 <div class="lr">
   	 	<a id="link" href="login.html" target="_self">Login</a>
   	 	<a id="link" href="registration.html" target="_self">Register</a>
   	 </div>	
   </body>
</html>"""

if __name__=='__main__':
   app.run(host="0.0.0.0",port=5000,debug=True)
