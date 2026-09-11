1. Agent Product for youtube & gmail :
2. app -> __init__.py
2.1. functions:
   def create_app()
   def home()
   def html()
   def health()
   def agent()
   Flask(__name__)
   CORS(app)
   app.register_blueprint()
   app.route()
   render_template()
   request.get_json()
   jsonify()
   str.strip()	
   dict.get()	
   str()
   Exception
3. app -> requirements.txt
3.1. packages:
   Flask 3.1.1	
   Gunicorn 21.0.0	
   Flask-CORS
4. app -> wsgi.py
4.1. functions:
   create_app()
5. app -> templates
6. app -> templates -> index.html
6.1. functions:
   $(id)	
   isGmail(command)	
   isYouTube(command)	
   processCommand(command)	
   showEmail(data)	
   playYouTube(data)
   document.getElementById()	
   new SR()	
   recognition.start()	
   classList.add()	
   classList.remove()	
   fetch()	
   response.json()	
   JSON.stringify()	
   Error()	
   console.error()
7. app -> youtube
8. app -> youtube -> __init__.py
8.1. functions:
   create_youtube_url(command)
   play()
   Blueprint()
   route()
   request.get_json()
   data.get()
   strip()
   jsonify()
9. app -> youtube -> player.py
9.1. functions:
   get_vid(query)
   create_youtube_url(command)
   urllib.parse.quote()	
   urllib.request.Request()	
   urllib.request.urlopen()	
   .read()	
   .decode()	
   re.findall()	
   re.search()	
   .lower()	
   .strip()	
   .group()	
   Exception	
   print
10. app -> gmail
11. app -> gmail -> __init__.py
11.1. functions imported:
   is_email_command()
   extract_email()
   generate_email_with_gemini()
   create_gmail_url()
12. app -> gmail -> gmail_gen.py
12.1. functions:
   generate_email_with_gemini(command)
   os.getenv()	
   urllib.request.Request()	
   json.dumps()	
   .encode()
   urllib.request.urlopen()	
   .read()	
   .decode()	
   json.loads()	
   re.sub()	
   re.search()	
   .group()	
   .strip()
   range()	
   time.sleep()	
   random.random()	
   RuntimeError()	
   Exception
13. app -> gmail -> gmail_write.py
13.1. functions:
   is_email_command(text)	
   extract_email(text)	
   create_gmail_url(subject, body, recipient)
