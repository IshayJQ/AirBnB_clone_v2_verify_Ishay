 ![Project badge](https://intranet.hbtn.io/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png) 
41.54%100%# AirBnB clone - Web framework
## Details
Novice By: Guillaume, CTO at Holberton School Weight: 2Your score will be updated once you launch the project review.Manual QA review was done byJuan Avila onFeb 9, 2024 11:30 AM### Concepts
For this project, we expect you to look at this concept:
* [AirBnB clone](https://intranet.hbtn.io/concepts/865) 

## Resources
Read or watch :
* [What is a Web Framework?](https://intranet.hbtn.io/rltoken/qk3bO45DSY-P4qmdnEX93w) 

* [A Minimal Application](https://intranet.hbtn.io/rltoken/DCF-0NHTuXLykc1ijX5HVg) 

* [Routing](https://intranet.hbtn.io/rltoken/mfdHqOmCsS7veXQ3nK6PcQ) 
 (except “HTTP Methods”)
* [Rendering Templates](https://intranet.hbtn.io/rltoken/_dU2691FhIZB3lBtSF5nMg) 

* [Synopsis](https://intranet.hbtn.io/rltoken/V24BEPWuJb3yPZpOvA3-Zw) 

* [Variables](https://intranet.hbtn.io/rltoken/GKvdWdthYkstOwnDs9LJWg) 

* [Comments](https://intranet.hbtn.io/rltoken/qum7hVpPWLaqMZBQCpcRyA) 

* [Whitespace Control](https://intranet.hbtn.io/rltoken/LxOb-5Fe9bHvx0TguTDY9g) 

* [List of Control Structures](https://intranet.hbtn.io/rltoken/8D9OoDX5cYQOFXUqwAiCNw) 
 (read up to “Call”)
* [Flask](https://intranet.hbtn.io/rltoken/OMqE9vlalgkWcT_3fu4Hvg) 

* [Jinja](https://intranet.hbtn.io/rltoken/L3kYnmfrbc86Asb4JZq0rg) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/lVg3jl6IEzhNeQiHwhC-Fg) 
 ,  without the help of Google :
### General
* What is a Web Framework
* How to build a web framework with Flask
* How to define routes in Flask
* What is a route
* How to handle variables in a route
* What is a template
* How to create a HTML response in Flask by using a template
* How to create a dynamic template (loops, conditions…)
* How to display in HTML data from a MySQL database
## Requirements
### Python Scripts
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/python3 ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using  ` wc ` 
* All your modules should have documentation ( ` python3 -c 'print(__import__("my_module").__doc__)' ` )
* All your classes should have documentation ( ` python3 -c 'print(__import__("my_module").MyClass.__doc__)' ` )
* All your functions (inside and outside a class) should have documentation ( ` python3 -c 'print(__import__("my_module").my_function.__doc__)' `  and  ` python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' ` )
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
### HTML/CSS Files
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files should end with a new line
* A  ` README.md `  file at the root of the folder of the project is mandatory
* Your code should be W3C compliant and validate with [W3C-Validator](https://intranet.hbtn.io/rltoken/BABHSFrobycuS0xRtRtXVQ) 
 (except for jinja template)
* All your CSS files should be in the  ` styles `  folder
* All your images should be in the  ` images `  folder
* You are not allowed to use  ` !important `  or  ` id `  ( ` #... `  in the CSS file)
* All tags must be in uppercase
* Current screenshots have been done on  ` Chrome 56.0.2924.87 ` . 
* No cross browsers 
## More Info
### MySQL Default charset issues
* If you get Flask errors after executing the   ` curl ... `  commands, it might be because of the  ` DEFAULT CHARSET ` . If it’s  ` DEFAULT CHARSET=latam1 ` , you might want to change it to  ` DEFAULT CHARSET=utf8mb4 ` , either on the server’s config file (/etc/mysql/my.cnf commonly) orm on the CREATE DATABASE statement.
### Install Flask
 ` $ pip3 install Flask
 `  ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/concepts/74/hbnb_step3.png) 

### NOTE:
* Try setting FLASK configuration  ` debug `  to  ` False `   iIf you get the following error when running the checker:
```bash
 - [Got]
rpc error: code = 2 desc = oci runtime error: exec failed: container_linux.go:290: starting container process caused "process_linux.go:111: decoding init error from pipe caused \"read parent: connection reset by peer\""


(222 chars long)

```
### Manual QA Review
It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.
## Tasks
### 0. Hello Flask!
          mandatory         Progress vs Score  Task Body Write a script that starts a Flask web application:
* Your web application must be listening on  ` 0.0.0.0 ` , port  ` 5000 ` 
* Routes:*  ` / ` : display “Hello HBNB!”

* You must use the option  ` strict_slashes=False `  in your route definition
```bash
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```
In another tab:
 ` guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 
 `  Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* Directory:  ` web_flask ` 
* File:  ` 0-hello_route.py, __init__.py ` 
 Self-paced manual review  Panel footer - Controls 
### 1. HBNB
          mandatory         Progress vs Score  Task Body Write a script that starts a Flask web application:
* Your web application must be listening on  ` 0.0.0.0 ` , port  ` 5000 ` 
* Routes:*  ` / ` : display “Hello HBNB!”
*  ` /hbnb ` : display “HBNB”

* You must use the option  ` strict_slashes=False `  in your route definition
```bash
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```
In another tab:
 ` guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$ 
 `  Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* Directory:  ` web_flask ` 
* File:  ` 1-hbnb_route.py ` 
 Self-paced manual review  Panel footer - Controls 
### 2. C is fun!
          mandatory         Progress vs Score  Task Body Write a script that starts a Flask web application:
* Your web application must be listening on  ` 0.0.0.0 ` , port  ` 5000 ` 
* Routes:*  ` / ` : display “Hello HBNB!”
*  ` /hbnb ` : display “HBNB”
*  ` /c/<text> ` : display “C ” followed by the value of the  ` text `  variable (replace underscore  ` _ `  symbols with a space  `  ` )

* You must use the option  ` strict_slashes=False `  in your route definition
```bash
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```
In another tab:
```bash
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 

```
 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* Directory:  ` web_flask ` 
* File:  ` 2-c_route.py ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Python is cool!
          mandatory         Progress vs Score  Task Body Write a script that starts a Flask web application:
* Your web application must be listening on  ` 0.0.0.0 ` , port  ` 5000 ` 
* Routes:*  ` / ` : display “Hello HBNB!”
*  ` /hbnb ` : display “HBNB”
*  ` /c/<text> ` : display “C ”, followed by the value of the  ` text `  variable (replace underscore  ` _ `  symbols with a space  `  ` )
*  ` /python/<text> ` : display “Python ”, followed by the value of the  ` text `  variable (replace underscore  ` _ `  symbols with a space  `  ` )* The default value of  ` text `  is “is cool”


* You must use the option  ` strict_slashes=False `  in your route definition
```bash
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```
In another tab:
```bash
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ 

```
 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* Directory:  ` web_flask ` 
* File:  ` 3-python_route.py ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Is it a number?
          mandatory         Progress vs Score  Task Body Write a script that starts a Flask web application:
* Your web application must be listening on  ` 0.0.0.0 ` , port  ` 5000 ` 
* Routes:*  ` / ` : display “Hello HBNB!”
*  ` /hbnb ` : display “HBNB”
*  ` /c/<text> ` : display “C ”, followed by the value of the  ` text `  variable (replace underscore  ` _ `  symbols with a space  `  ` )
*  ` /python/<text> ` : display “Python ”, followed by the value of the  ` text `  variable (replace underscore  ` _ `  symbols with a space  `  ` )* The default value of  ` text `  is “is cool”

*  ` /number/<n> ` : display “ ` n `  is a number” only if  ` n `  is an integer

* You must use the option  ` strict_slashes=False `  in your route definition
```bash
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```
In another tab:
```bash
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 

```
 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* Directory:  ` web_flask ` 
* File:  ` 4-number_route.py ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Number template
          mandatory         Progress vs Score  Task Body Write a script that starts a Flask web application:
* Your web application must be listening on  ` 0.0.0.0 ` , port  ` 5000 ` 
* Routes:*  ` / ` : display “Hello HBNB!”
*  ` /hbnb ` : display “HBNB”
*  ` /c/<text> ` : display “C ”, followed by the value of the  ` text `  variable (replace underscore  ` _ `  symbols with a space  `  ` )
*  ` /python/<text> ` : display “Python ”, followed by the value of the  ` text `  variable (replace underscore  ` _ `  symbols with a space  `  ` )* The default value of  ` text `  is “is cool”

*  ` /number/<n> ` : display “ ` n `  is a number” only if  ` n `  is an integer
*  ` /number_template/<n> ` : display a HTML page only if  ` n `  is an integer: *  ` H1 `  tag: “Number:  ` n ` ” inside the tag  ` BODY ` 


* You must use the option  ` strict_slashes=False `  in your route definition
```bash
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```
In another tab:
```bash
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 

```
 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* Directory:  ` web_flask ` 
* File:  ` 5-number_template.py, templates/5-number.html ` 
 Self-paced manual review  Panel footer - Controls 
### 6. Odd or even?
          mandatory         Progress vs Score  Task Body Write a script that starts a Flask web application:
* Your web application must be listening on  ` 0.0.0.0 ` , port  ` 5000 ` 
* Routes:*  ` / ` : display “Hello HBNB!”
*  ` /hbnb ` : display “HBNB”
*  ` /c/<text> ` : display “C ”, followed by the value of the  ` text `  variable (replace underscore  ` _ `  symbols with a space  `  ` )
*  ` /python/<text> ` : display “Python ”, followed by the value of the  ` text `  variable (replace underscore  ` _ `  symbols with a space  `  ` )* The default value of  ` text `  is “is cool”

*  ` /number/<n> ` : display “ ` n `  is a number” only if  ` n `  is an integer
*  ` /number_template/<n> ` : display a HTML page only if  ` n `  is an integer: *  ` H1 `  tag: “Number:  ` n ` ” inside the tag  ` BODY ` 

*  ` /number_odd_or_even/<n> ` : display a HTML page only if  ` n `  is an integer: *  ` H1 `  tag: “Number:  ` n `  is  ` even|odd ` ” inside the tag  ` BODY ` 


* You must use the option  ` strict_slashes=False `  in your route definition
```bash
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```
In another tab:
```bash
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 

```
 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* Directory:  ` web_flask ` 
* File:  ` 6-number_odd_or_even.py, templates/6-number_odd_or_even.html ` 
 Self-paced manual review  Panel footer - Controls 
### 7. Improve engines
          mandatory         Progress vs Score  Task Body Before using Flask to display our HBNB data, you will need to update some part of our engine:
Update   ` FileStorage `  : (  ` models/engine/file_storage.py `  )
* Add a public method  ` def close(self): ` : call  ` reload() `  method for deserializing the JSON file to objects
Update   ` DBStorage `  : (  ` models/engine/db_storage.py `  )
* Add a public method  ` def close(self): ` : call  ` remove() `  method on the private session attribute ( ` self.__session ` ) [tips](https://intranet.hbtn.io/rltoken/Ev0jeeBWNlaFqPAFe-rZKA) 
 or  ` close() `  on the class  ` Session ` [tips](https://intranet.hbtn.io/rltoken/d7XXqTOZnNCO47YVh5ZziQ) 

Update   ` State `  : (  ` models/state.py `  ) - If it’s not already present
* If your storage engine is not  ` DBStorage ` , add a public getter method  ` cities `  to return the list of  ` City `  objects from  ` storage `  linked to the current  ` State ` 
```bash
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 
>>> from models import storage
>>> from models.state import State
>>> len(storage.all(State))
5
>>> len(storage.all(State))
5
>>> # Time to insert new data!

```
At this moment, in another tab:
```bash
guillaume@ubuntu:~/AirBnB_v2$ echo 'INSERT INTO `states` VALUES ("421a55f1-7d82-45d9-b54c-a76916479545", "Alabama", "2017-03-25 19:42:40","2017-03-25 19:42:40");' | mysql -uroot -p hbnb_dev_db
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ 

```
And let’s go back the Python console:
```bash
>>> # Time to insert new data!
>>> len(storage.all(State))
5
>>> # normal: the SQLAlchemy didn't reload his `Session`
>>> # to force it, you must remove the current session to create a new one:
>>> storage.close()
>>> len(storage.all(State))
6
>>> # perfect!

```
And for the getter   ` cities `   in the   ` State `   model:
```bash
guillaume@ubuntu:~/AirBnB_v2$ cat main.py
#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

"""
 Objects creations
"""
state_1 = State(name="California")
print("New state: {}".format(state_1))
state_1.save()
state_2 = State(name="Arizona")
print("New state: {}".format(state_2))
state_2.save()

city_1_1 = City(state_id=state_1.id, name="Napa")
print("New city: {} in the state: {}".format(city_1_1, state_1))
city_1_1.save()
city_1_2 = City(state_id=state_1.id, name="Sonoma")
print("New city: {} in the state: {}".format(city_1_2, state_1))
city_1_2.save()
city_2_1 = City(state_id=state_2.id, name="Page")
print("New city: {} in the state: {}".format(city_2_1, state_2))
city_2_1.save()


"""
 Verification
"""
print("")
all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in state.cities:
        print("Find the city {} in the state {}".format(city, state))

guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ rm file.json ; HBNB_TYPE_STORAGE=fs ./main.py 
New state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509954), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510256), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
New city: [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510797), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511437), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511873), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}

Find the city [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510953), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511513), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 512073), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
guillaume@ubuntu:~/AirBnB_v2$ 

```
 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* File:  ` models/engine/file_storage.py, models/engine/db_storage.py, models/state.py ` 
 Self-paced manual review  Panel footer - Controls 
### 8. List of states
          mandatory         Progress vs Score  Task Body Write a script that starts a Flask web application:
* Your web application must be listening on  ` 0.0.0.0 ` , port  ` 5000 ` 
* You must use  ` storage `  for fetching data from the storage engine ( ` FileStorage `  or  ` DBStorage ` ) =>  ` from models import storage `  and  ` storage.all(...) ` 
* After each request you must remove the current SQLAlchemy Session:* Declare a method to handle  ` @app.teardown_appcontext ` 
* Call in this method  ` storage.close() ` 

* Routes:*  ` /states_list ` : display a HTML page: (inside the tag  ` BODY ` )*  ` H1 `  tag: “States”
*  ` UL `  tag: with the list of all  ` State `  objects present in  ` DBStorage ` sorted by  ` name `  (A->Z) [tip](https://intranet.hbtn.io/rltoken/UVC1Bw_-nfa_0T2gv1MuQg) 
*  ` LI `  tag: description of one  ` State ` :  ` <state.id>: <B><state.name></B> ` 



* NOTE: Students have reported that this one does not work - use the next on instead. Import this [7-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql) 
 to have some data
* Import this [100-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql) 
 to have some data
* You must use the option  ` strict_slashes=False `  in your route definition
IMPORTANT
* Make sure you have a running and valid  ` setup_mysql_dev.sql `  in your  ` AirBnB_clone_v2 `  repository ([Task](https://intranet.hbtn.io/rltoken/-Sz0UGvAe4_SLfTbSXSbzg) 
)
* Make sure all tables are created when you run ```bash
echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

```bash
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```
In another tab:
```bash
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states_list ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

        </UL>
    </BODY>
</HTML>
guillaume@ubuntu:~$ 

```
 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* File:  ` web_flask/7-states_list.py, web_flask/templates/7-states_list.html ` 
 Self-paced manual review  Panel footer - Controls 
### 9. Cities by states
          mandatory         Progress vs Score  Task Body Write a script that starts a Flask web application:
* Your web application must be listening on  ` 0.0.0.0 ` , port  ` 5000 ` 
* You must use  ` storage `  for fetching data from the storage engine ( ` FileStorage `  or  ` DBStorage ` ) =>  ` from models import storage `  and  ` storage.all(...) ` 
* To load all cities of a  ` State ` :* If your storage engine is  ` DBStorage ` , you must use  ` cities `  relationship
* Otherwise, use the public getter method  ` cities ` 

* After each request you must remove the current SQLAlchemy Session:* Declare a method to handle  ` @app.teardown_appcontext ` 
* Call in this method  ` storage.close() ` 

* Routes:*  ` /cities_by_states ` : display a HTML page: (inside the tag  ` BODY ` )*  ` H1 `  tag: “States”
*  ` UL `  tag: with the list of all  ` State `  objects present in  ` DBStorage ` sorted by  ` name `  (A->Z) [tip](https://intranet.hbtn.io/rltoken/UVC1Bw_-nfa_0T2gv1MuQg) 
*  ` LI `  tag: description of one  ` State ` :  ` <state.id>: <B><state.name></B> `  +  ` UL `  tag: with the list of  ` City `  objects linked to the  ` State ` sorted by  ` name `  (A->Z)*  ` LI `  tag: description of one  ` City ` :  ` <city.id>: <B><city.name></B> ` 




* NOTE: Students have reported that this one does not work - use the next on instead. Import this [7-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql) 
 to have some data
* Import this [100-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql) 
 to have some data
* You must use the option  ` strict_slashes=False `  in your route definition
IMPORTANT
* Make sure you have a running and valid  ` setup_mysql_dev.sql `  in your  ` AirBnB_clone_v2 `  repository ([Task](https://intranet.hbtn.io/rltoken/gIfF4l2eWBO13bfNduSG4w) 
)
* Make sure all tables are created when you run ```bash
echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

```bash
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```
In another tab:
```bash
guillaume@ubuntu:~$ curl 0.0.0.0:5000/cities_by_states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479545: <B>Akron</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479545: <B>Babbie</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479545: <B>Calera</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479545: <B>Fairfield</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479546: <B>Douglas</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479546: <B>Kearny</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479546: <B>Tempe</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B>
                <UL>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479547: <B>Fremont</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479547: <B>Napa</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479547: <B>San Francisco</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479547: <B>San Jose</B></LI>

                        <LI>561a55f4-7d82-47d9-b54c-a76916479547: <B>Sonoma</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479548: <B>Denver</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479549: <B>Miami</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479549: <B>Orlando</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B>
                <UL>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479551: <B>Honolulu</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479551: <B>Kailua</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479551: <B>Pearl city</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

                        <LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B>
                <UL>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B>
                <UL>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479554: <B>Baton rouge</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479554: <B>Lafayette</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479554: <B>New Orleans</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479555: <B>Saint Paul</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479556: <B>Jackson</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479556: <B>Meridian</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479556: <B>Tupelo</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B>
                <UL>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479557: <B>Eugene</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479557: <B>Portland</B></LI>

                </UL>
            </LI>

        </UL>
    </BODY>
</HTML>
guillaume@ubuntu:~$ 

```
 ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/9a7ae8155274b17881442200437e8793cf08de48.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240214%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240214T160236Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b2e35e99ae0624766b096c0ddbb880b5979393e18f24e718c13e265f00bb1fc7) 

 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* File:  ` web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html ` 
 Self-paced manual review  Panel footer - Controls 
### 10. States and State
          mandatory         Progress vs Score  Task Body Write a script that starts a Flask web application:
* Your web application must be listening on  ` 0.0.0.0 ` , port  ` 5000 ` 
* You must use  ` storage `  for fetching data from the storage engine ( ` FileStorage `  or  ` DBStorage ` ) =>  ` from models import storage `  and  ` storage.all(...) ` 
* To load all cities of a  ` State ` :* If your storage engine is  ` DBStorage ` , you must use  ` cities `  relationship
* Otherwise, use the public getter method  ` cities ` 

* After each request you must remove the current SQLAlchemy Session:* Declare a method to handle  ` @app.teardown_appcontext ` 
* Call in this method  ` storage.close() ` 

* Routes:*  ` /states ` : display a HTML page: (inside the tag  ` BODY ` )*  ` H1 `  tag: “States”
*  ` UL `  tag: with the list of all  ` State `  objects present in  ` DBStorage ` sorted by  ` name `  (A->Z) [tip](https://intranet.hbtn.io/rltoken/UVC1Bw_-nfa_0T2gv1MuQg) 
*  ` LI `  tag: description of one  ` State ` :  ` <state.id>: <B><state.name></B> ` 


*  ` /states/<id> ` : display a HTML page: (inside the tag  ` BODY ` )* If a  ` State `  object is found with this  ` id ` :*  ` H1 `  tag: “State: ”
*  ` H3 `  tag: “Cities:”
*  ` UL `  tag: with the list of  ` City `  objects linked to the  ` State ` sorted by  ` name `  (A->Z)*  ` LI `  tag: description of one  ` City ` :  ` <city.id>: <B><city.name></B> ` 


* Otherwise: *  ` H1 `  tag: “Not found!”



* You must use the option  ` strict_slashes=False `  in your route definition
* NOTE: Students have reported that this one does not work - use the next on instead. Import this [7-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql) 
 to have some data
* Import this [100-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql) 
 to have some data
IMPORTANT
* Make sure you have a running and valid  ` setup_mysql_dev.sql `  in your  ` AirBnB_clone_v2 `  repository ([Task](https://intranet.hbtn.io/rltoken/gIfF4l2eWBO13bfNduSG4w) 
)
* Make sure all tables are created when you run ```bash
echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

```bash
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```
In another tab:
```bash
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

        </UL>

    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>State: Illinois</H1>
        <H3>Cities:</H3>
        <UL>
                <LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

                <LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

                <LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

                <LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

                <LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>
        </UL>

    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/holberton ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>Not found!</H1>

    </BODY>
</HTML>
guillaume@ubuntu:~$ 

```
 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* File:  ` web_flask/9-states.py, web_flask/templates/9-states.html ` 
 Self-paced manual review  Panel footer - Controls 
### 11. HBNB filters
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a script that starts a Flask web application:
* Your web application must be listening on  ` 0.0.0.0 ` , port  ` 5000 ` 
* You must use  ` storage `  for fetching data from the storage engine ( ` FileStorage `  or  ` DBStorage ` ) =>  ` from models import storage `  and  ` storage.all(...) ` 
* To load all cities of a  ` State ` :* If your storage engine is  ` DBStorage ` , you must use  ` cities `  relationship
* Otherwise, use the public getter method  ` cities ` 

* After each request you must remove the current SQLAlchemy Session:* Declare a method to handle  ` @app.teardown_appcontext ` 
* Call in this method  ` storage.close() ` 

* Routes:*  ` /hbnb_filters ` : display a HTML page like  ` 6-index.html ` , which was done during the project [0x01. AirBnB clone - Web static](https://intranet.hbtn.io/rltoken/LSsy0WYsMdxl-zlZqbAthg) 
* Copy files  ` 3-footer.css ` ,  ` 3-header.css ` ,  ` 4-common.css `  and  ` 6-filters.css `  from  ` web_static/styles/ `  to the folder  ` web_flask/static/styles ` 
* Copy files  ` icon.png `  and  ` logo.png `  from  ` web_static/images/ `  to the folder  ` web_flask/static/images ` 
* Update  ` .popover `  class in  ` 6-filters.css `  to allow scrolling in the popover and a max height of 300 pixels.
* Use  ` 6-index.html `  content as source code for the template  ` 10-hbnb_filters.html ` :* Replace the content of the  ` H4 `  tag under each filter title ( ` H3 `  States and  ` H3 `  Amenities) by  ` &nbsp; ` 

*  ` State ` ,  ` City `  and  ` Amenity `  objects must be loaded from  ` DBStorage `  and sorted by name (A->Z)


* You must use the option  ` strict_slashes=False `  in your route definition
* Import this [10-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql) 
 to have some data
IMPORTANT
* Make sure you have a running and valid  ` setup_mysql_dev.sql `  in your  ` AirBnB_clone_v2 `  repository ([Task](https://intranet.hbtn.io/rltoken/gIfF4l2eWBO13bfNduSG4w) 
)
* Make sure all tables are created when you run ```bash
echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

```bash
guillaume@ubuntu:~/AirBnB_v2$ curl -o 10-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 10-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```
In the browser:
 ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/4f993ec8ca2a2f639a80887667106ac63a0a3701.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240214%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240214T160236Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7952a8aba971cbfd0eb050a676bb1a373fff2ff9e5103a6587ed412ba32af06a) 
  ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/1549b553d726cc37f64440be910cb6b858aa32ae.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240214%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240214T160236Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9f4d3852976a20fd4150045993fe7c294960095082d93f5af3b90ff15c4fcbfa) 
  ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/94b3a416ba1551c59701eb6672ac0a36fbebba14.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240214%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240214T160236Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=919914101dc0d7b37cacf22a71f2ee4090a8c08d4ef8e5b44441eda38615ddcc) 
  ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/1e559707dd34a37564dc10e54b707815a516d363.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240214%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240214T160236Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ed741add84506f22413ac11827ebad1119db6be7c62c4b891e864c04ff45741b) 

 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* File:  ` web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/ ` 
 Self-paced manual review  Panel footer - Controls 
### 12. HBNB is alive!
          #advanced         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a script that starts a Flask web application:
* Your web application must be listening on  ` 0.0.0.0 ` , port  ` 5000 ` 
* You must use  ` storage `  for fetching data from the storage engine ( ` FileStorage `  or  ` DBStorage ` ) =>  ` from models import storage `  and  ` storage.all(...) ` 
* To load all cities of a  ` State ` :* If your storage engine is  ` DBStorage ` , you must use  ` cities `  relationship
* Otherwise, use the public getter method  ` cities ` 

* After each request you must remove the current SQLAlchemy Session:* Declare a method to handle  ` @app.teardown_appcontext ` 
* Call in this method  ` storage.close() ` 

* Routes:*  ` /hbnb ` : display a HTML page like  ` 8-index.html ` , done during the [0x01. AirBnB clone - Web static](https://intranet.hbtn.io/rltoken/LSsy0WYsMdxl-zlZqbAthg) 
 project* Copy files  ` 3-footer.css ` ,  ` 3-header.css ` ,  ` 4-common.css ` ,  ` 6-filters.css `  and  ` 8-places.css `  from  ` web_static/styles/ `  to the folder  ` web_flask/static/styles ` 
* Copy all files from  ` web_static/images/ `  to the folder  ` web_flask/static/images ` 
* Update  ` .popover `  class in  ` 6-filters.css `  to enable scrolling in the popover and set max height to 300 pixels.
* Update  ` 8-places.css `  to always have the price by night on the top right of each place element, and the name correctly aligned and visible (i.e. screenshots below)
* Use  ` 8-index.html `  content as source code for the template  ` 100-hbnb.html ` :* Replace the content of the  ` H4 `  tag under each filter title ( ` H3 `  States and  ` H3 `  Amenities) by  ` &nbsp; ` 
* Make sure all HTML tags from objects are correctly used (example:  ` <BR /> `  must generate a new line)

*  ` State ` ,  ` City ` ,  ` Amenity `  and  ` Place `  objects must be loaded from  ` DBStorage `  and sorted by name (A->Z)


* You must use the option  ` strict_slashes=False `  in your route definition
* Import this [100-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql) 
 to have some data
IMPORTANT
* Make sure you have a running and valid  ` setup_mysql_dev.sql `  in your  ` AirBnB_clone_v2 `  repository ([Task](https://intranet.hbtn.io/rltoken/gIfF4l2eWBO13bfNduSG4w) 
)
* Make sure all tables are created when you run ```bash
echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

```bash
guillaume@ubuntu:~/AirBnB_v2$ curl -o 100-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 100-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.100-hbnb
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```
In the browser:
 ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/396ae10c9f85a6128ae40e1b63f4bce95adf411c.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240214%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240214T160236Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e44fc226e8a4e7288a8e9255f698c9f0ce9f54b8c10589624965107124054b67) 
  ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/9eb21499b5f3b59751fdbf561174e2f259d97482.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240214%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240214T160236Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=343e1fb68ddbf741aba7e2208e122fe0893bc84709de95c1585e5ac14b7538b3) 
  ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/bf248a63c15a746ad694acffdd56d80281782c71.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240214%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240214T160236Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=25df3b81fb7b93d53a076b7bdf3f6862d1cdb80e775aa4a752517122a42ea452) 
  ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/494317aad058a649a51f416eceee1a609f07c6c0.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240214%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240214T160236Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2d4edd984cdef8c5e18753e9a737f6acfa7c05f294c49130bf4fc5b9bb5bd89d) 
  ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/016911388aa92532e06c4d5361188a2622425517.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240214%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240214T160236Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=330d356ac940d302f5a65bad5760aa1af9a1f4fd522bbb21dca7a127d2dd557e) 

 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-AirBnB_clone_v2 ` 
* File:  ` web_flask/100-hbnb.py, web_flask/templates/100-hbnb.html, web_flask/static/ ` 
 Self-paced manual review  Panel footer - Controls 
### Score
 ![Project badge](https://intranet.hbtn.io/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png) 
41.54%100%Still some tasks to work on!
Now that you are ready to be reviewed, share your link to your peers. You can find some [here](https://intranet.hbtn.io/projects/2130#available-reviewers-modal) 
 .
×#### Contact one of your peers
https://intranet.hbtn.io/corrections/692712/correct[]() 
Don't forget to[review one of them](https://intranet.hbtn.io/corrections/to_review) 
.
Next project: API
[Open the next project](https://intranet.hbtn.io/projects/2076) 
×#### Recommended Sandboxes
[Running only]() 
### 3 images(1/5 Sandboxes spawned)
### Ubuntu 14.04 - Python 3.4
Ubuntu 14.04 with all tools needed and Python 3.4
[Run]() 
### Ubuntu 20.04
Basic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Holberton Foundations
SSHSFTP[Webterm](https://intranet.hbtn.io/user_containers/33540/webterm) 
[Restart]() 
[Destroy]() 
#### Credentials
Host8b068769613a.a5fea2b8.hbtn-cod.ioUsername8b068769613aPassword437336e20583fceb9e66#### Web access
[HTTPS](https://8b068769613a.a5fea2b8.hbtn-cod.io/) 
[HTTP](http://8b068769613a.a5fea2b8.hbtn-cod.io/) 
[3000](http://8b068769613a.a5fea2b8.hbtn-cod.io:3000/) 
[4000](http://8b068769613a.a5fea2b8.hbtn-cod.io:4000/) 
[5000](http://8b068769613a.a5fea2b8.hbtn-cod.io:5000/) 
[5001](http://8b068769613a.a5fea2b8.hbtn-cod.io:5001/) 
[8000](http://8b068769613a.a5fea2b8.hbtn-cod.io:8000/) 
[8080](http://8b068769613a.a5fea2b8.hbtn-cod.io:8080/) 
#### Port mapping
SSH35303HTTP35302HTTPS35301300035300MySQL35299400035298500035297500135296800035295808035294### Ubuntu 20.04 - Flask
Ubuntu 20.04 with Flask
[Run]() 
×#### Recommended Sandboxes
[View User Containers (deprecated)](https://intranet.hbtn.io/user_containers/current) 
New sandbox * [US East (N. Virginia)	 - Ubuntu 22.04 LTS]() 

* [South America (São Paulo) - Ubuntu 22.04 LTS]() 

* [Europe (Paris) - Cyber - NetSec 0x01]() 

* [Europe (Paris) - Cyber - NetSec 0x02]() 

* [Europe (Paris) - Cyber - NetSec 0x04]() 

* [Europe (Paris) - Cyber - WebSec 0x00]() 

* [Europe (Paris) - Machine Learning - Ubuntu 22.04]() 

* [Europe (Paris) - Ubuntu 22.04 LTS]() 

* [Asia Pacific (Sydney) - Ubuntu 22.04 LTS]() 

No sandboxes yet!              Next project            
