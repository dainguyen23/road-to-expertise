Network Programming
===================

|

For this section, I'll be going over exercises 12.1 to 12.5, plus the 3 autograder assignments.

.. contents:: Contents
    :local:

.. note::

    **Somethings to be familiar with:**

    We need to ``import`` the ``socket`` library for network programming.

    There are many documents that describe different network protocols. We'll be working with the Hypertext Transfer Protocol so refer to this document for detailed descriptions: https://www.w3.org/Protocols/rfc2616/rfc2616.txt

    To request a document from a web server, we make a connection, for example, to a server called ``www.pr4e.org server`` on port ``80``, and then send a line of the form
    ::

        GET http://data.pr4e.org/romeo.txt HTTP/1.0

    where the *second parameter* is the **web page** we are requesting, and then we also send a blank line. The *web server* will respond with some **header** information about the document and a **blank line** followed by the document **content**.
    
    .. code-block:: text

        HTTP/1.1 200 OK
        Date: Wed, 11 Apr 2018 18:52:55 GMT
        Server: Apache/2.4.7 (Ubuntu)
        Last-Modified: Sat, 13 May 2017 11:22:22 GMT
        ETag: "a7-54f6609245537"
        Accept-Ranges: bytes
        Content-Length: 167
        Cache-Control: max-age=0, no-cache, no-store, must-revalidate
        Pragma: no-cache
        Expires: Wed, 11 Jan 1984 05:00:00 GMT
        Connection: close
        Content-Type: text/plain

        But soft what light through yonder window breaks
        It is the east and Juliet is the sun
        Arise fair sun and kill the envious moon
        Who is already sick and pale with grief

    One of the requirements for using the HTTP protocol is the need to send and receive data as **bytes** objects, instead of strings. The ``encode()`` and ``decode()`` methods convert strings into bytes objects and back again.

    To a similar effect, you can use ``b''`` notation to specify that a variable should be stored as a bytes object. ``encode()`` and ``b''`` are equivalent.
    
    .. code-block:: text

        >>> b'Hello world'
        b'Hello world'
        >>> 'Hello world'.encode()
        b'Hello world'

    Another approach to network programming is to use the ``urllib`` library designed by folks that work on the Python language. One benefit of using this library is that it handles the connection protocol in it's code, making writing the code more efficient.

    One of the common uses of the ``urllib`` capability in Python is to *scrape* the web. **Web scraping** is when we write a program that pretends to be a web browser and retrieves pages, then examines the data in those pages looking for patterns.

|

----

Exercise 12.1
-------------

**Prompt:** Change the socket program ``socket1.py`` to prompt the user for the URL so it can read any web page. You can use ``split('/')`` to break the URL into its component parts so you can extract the host name for the socket ``connect`` call. Add error checking using ``try`` and ``except`` to handle the condition where the user enters an improperly formatted or non-existent URL.

Link to ``socket1.py``: https://www.py4e.com/code3/socket1.py

Content of ``socket1.py``:
::

    import socket

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

**Expected output:** None available.

**My outputs:**
::

    $ python temporaryFile.py 
    Enter URL in the format of "http://<host-name>/<page-name>": google.com 
    Please enter the URL in proper format!

::

    $ python temporaryFile.py 
    Enter URL in the format of "http://<host-name>/<page-name>": htttpp://datt.pre4.org/romeon.txx
    Please enter an existing URL!

::

    $ python temporaryFile.py 
    Enter URL in the format of "http://<host-name>/<page-name>": http://data.pr4e.org/romeo.txt
    HTTP/1.1 200 OK
    Date: Mon, 03 Jul 2023 03:42:36 GMT
    Server: Apache/2.4.18 (Ubuntu)
    Last-Modified: Sat, 13 May 2017 11:22:22 GMT
    ETag: "a7-54f6609245537"
    Accept-Ranges: bytes
    Content-Length: 167
    Cache-Control: max-age=0, no-cache, no-store, must-revalidate
    Pragma: no-cache
    Expires: Wed, 11 Jan 1984 05:00:00 GMT
    Connection: close
    Content-Type: text/plain

    But soft what light through yonder window breaks
    It is the east and Juliet is the sun
    Arise fair sun and kill the envious moon
    Who is already sick and pale with grief

**My code:**
::

    import socket

    url = input("Enter URL in the format of \"http://<host-name>/<page-name>\": ")

    if len(url) < 1:
        url = "http://data.pr4e.org/romeo.txt"

    token = url.split('/')

    try:
        hostname = token[2]

    except:
        print("Please enter the URL in proper format!")
        exit()

    portnum = 80
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        mysock.connect((hostname, portnum))

    except:
        print("Please enter an existing URL!")
        exit()

    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

**Reasoning behind my code:**

- The ``socket`` library needs to be imported for network programming.
- ``url`` asks and stores user input.
- ``if`` no input is entered, ``url`` is automatically initialized with a default input.
- The first ``try``/``except`` block tests to see if the input is in the proper format.
- The second ``try``/``except`` block tests to see if the URL is a valid link.
- ``cmd`` is edited to incorporate the user input.
- Once the input passes the checks, successfully, the socket is established and connected to the server side. The ``while`` loop runs for as long as the program receives packets from the server. Each packet is the size of 512 bytes. Notice the ``encode()`` and ``decode()`` methods. These are for switching *string type* to *byte type*. They're necessary for network programming.

|

----

Exercise 12.2
-------------

**Prompt:** Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

**Expected output:** None available.

**My output:**
::

    $ python temporaryFile.py 
    Enter URL in the format of "http://<host-name>/<page-name>": http://data.pr4e.org/romeo-full.txt
    HTTP/1.1 200 OK
    Date: Mon, 03 Jul 2023 21:53:38 GMT
    Server: Apache/2.4.18 (Ubuntu)
    Last-Modified: Sat, 13 May 2017 11:22:22 GMT
    ETag: "22a0-54f6609245537"
    Accept-Ranges: bytes
    Content-Length: 8864
    Cache-Control: max-age=0, no-cache, no-store, must-revalidate
    Pragma: no-cache
    Expires: Wed, 11 Jan 1984 05:00:00 GMT
    Connection: close
    Content-Type: text/plain

    Romeo and Juliet
    Act 2, Scene 2

    SCENE II. Capulet's orchard.

    Enter ROMEO

    ROMEO

    He jests at scars that never felt a wound.
    JULIET appears above at a window

    But, soft! what light through yonder window breaks?
    It is the east, and Juliet is the sun.
    Arise, fair sun, and kill the envious moon,
    Who is already sick and pale with grief,
    That thou her maid art far more fair than she:
    Be not her maid, since she is envious;
    Her vestal livery is but sick and green
    And none but fools do wear it; cast it off.
    It is my lady, O, it is my love!
    O, that she knew she were!
    She speaks yet she says nothing: what of that?
    Her eye discourses; I will answer it.
    I am too bold, 'tis not to me she speaks:
    Two of the fairest stars in all the heaven,
    Having some business, do entreat her eyes
    To twinkle in their spheres till they return.
    What if her eyes were there, they in her head?
    The brightness of her cheek would shame those stars,
    As daylight doth a lamp; her eyes in heaven
    Would through the airy region stream so bright
    That birds would sing and think it were not night.
    See, how she leans her cheek upon her hand!
    O, that I were a glove upon that hand,
    That I might touch that cheek!

    JULIET

    Ay me!

    ROMEO

    She speaks:
    O, speak again, bright angel! for thou art
    As glorious to this night, being o'er my head
    As is a winged messenger of heaven
    Unto the white-upturned wondering eyes
    Of mortals that fall back to gaze on him
    When he bestrides the lazy-pacing clouds
    And sails upon the bosom of the air.

    JULIET

    O Romeo, Romeo! wherefore art thou Romeo?
    Deny thy father and refuse thy name;
    Or, if thou wilt not, be but sworn my love,
    And I'll no longer be a Capulet.

    ROMEO

    [Aside] Shall I hear more, or shall I speak at this?

    JULIET

    'Tis but thy name that is my enemy;
    Thou art thyself, though not a Montague.
    What's Montague? it is nor hand, nor foot,
    Nor arm, nor face, nor any other part
    Belonging to a man. O, be some other name!
    What's in a name? that which we call a rose
    By any other name would smell as sweet;
    So Romeo would, were he not Romeo call'd,
    Retain that dear perfection which he owes
    Without that title. Romeo, doff thy name,
    And for that name which is no part of thee
    Take all myself.

    ROMEO

    I take thee at thy word:
    Call me but love, and I'll be new baptized;
    Henceforth I never will be Romeo.

    JULIET

    What man art thou that thus bescreen'd in night
    So stumblest on my counsel?

    ROMEO

    By a name
    I know not how to tell thee who I am:
    My name, dear saint, is hateful to myself,
    Because it is an enemy to thee;
    Had I it written, I would tear the word.

    JULIET

    My ears have not yet drunk a hundred words
    Of

    Display stopped at character count of 3000
    Total number of characters received: 9236

**My code:**
::

    import socket

    url = input("Enter URL in the format of \"http://<host-name>/<page-name>\": ")

    if len(url) < 1:
        url = "http://data.pr4e.org/romeo-full.txt"

    token = url.split('/')

    try:
        hostname = token[2]

    except:
        print("Please enter the URL in proper format!")
        exit()

    portnum = 80
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        mysock.connect((hostname, portnum))

    except:
        print("Please enter an existing URL!")
        exit()

    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    displayCount = 0
    totalCount = 0
    charLimit = 3000

    while True:
        data = mysock.recv(500)
        totalCount += len(data)
        
        if len(data) < 1:
            break
        
        elif totalCount >= charLimit+1:
            displayCount = charLimit
            continue

        print(data.decode(), end='')

    print(f"\n\nDisplay stopped at character count of {displayCount}")
    print(f"Total number of characters received: {totalCount}")

    mysock.close()

**Reasoning behind my code:**

- Majority of the code is taken from exercise 12.1. I'll be going over the changes I made for this assignment.
- In the ``if`` block used to auto-assign a link for testing, the URL is changed to a bigger file to better test the code for this assignment.
- ``displayCount`` is created to hold the count of the character limit set by the **prompt**.
- ``totalCount`` is created to hold the total count of all characters that passed through the socket. 
- ``charLimit`` is created for ease of use and hide the fact that I had to hardcode for this assignment...
- The ``elif`` block below ``if len(data) < 1:`` is haphazardly put together to get the result expected by the **prompt**. I'm sure there are better ways of doing this... But it achieved the results, at least, for this assignment! But I don't feel good doing it this way...-_-
- Once everything is sent and received, the program will print out when it stopped display and what the total count of characters is in total.
- **After completing exercise 12.3, I realized that this code is flawed. Check out exercise 12.3 to see the difference in the output!**

|

----

Exercise 12.3
-------------

**Prompt:** Use ``urllib`` to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. Don't worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

**Expected output:** None available.

**My output:**
::

    $ python temporaryFile.py 
    Enter URL in the format of "http://<host-name>/<page-name>": http://data.pr4e.org/romeo-full.txt
    Romeo and Juliet
    Act 2, Scene 2

    SCENE II. Capulet's orchard.

    Enter ROMEO

    ROMEO

    He jests at scars that never felt a wound.
    JULIET appears above at a window

    But, soft! what light through yonder window breaks?
    It is the east, and Juliet is the sun.
    Arise, fair sun, and kill the envious moon,
    Who is already sick and pale with grief,
    That thou her maid art far more fair than she:
    Be not her maid, since she is envious;
    Her vestal livery is but sick and green
    And none but fools do wear it; cast it off.
    It is my lady, O, it is my love!
    O, that she knew she were!
    She speaks yet she says nothing: what of that?
    Her eye discourses; I will answer it.
    I am too bold, 'tis not to me she speaks:
    Two of the fairest stars in all the heaven,
    Having some business, do entreat her eyes
    To twinkle in their spheres till they return.
    What if her eyes were there, they in her head?
    The brightness of her cheek would shame those stars,
    As daylight doth a lamp; her eyes in heaven
    Would through the airy region stream so bright
    That birds would sing and think it were not night.
    See, how she leans her cheek upon her hand!
    O, that I were a glove upon that hand,
    That I might touch that cheek!

    JULIET

    Ay me!

    ROMEO

    She speaks:
    O, speak again, bright angel! for thou art
    As glorious to this night, being o'er my head
    As is a winged messenger of heaven
    Unto the white-upturned wondering eyes
    Of mortals that fall back to gaze on him
    When he bestrides the lazy-pacing clouds
    And sails upon the bosom of the air.

    JULIET

    O Romeo, Romeo! wherefore art thou Romeo?
    Deny thy father and refuse thy name;
    Or, if thou wilt not, be but sworn my love,
    And I'll no longer be a Capulet.

    ROMEO

    [Aside] Shall I hear more, or shall I speak at this?

    JULIET

    'Tis but thy name that is my enemy;
    Thou art thyself, though not a Montague.
    What's Montague? it is nor hand, nor foot,
    Nor arm, nor face, nor any other part
    Belonging to a man. O, be some other name!
    What's in a name? that which we call a rose
    By any other name would smell as sweet;
    So Romeo would, were he not Romeo call'd,
    Retain that dear perfection which he owes
    Without that title. Romeo, doff thy name,
    And for that name which is no part of thee
    Take all myself.

    ROMEO

    I take thee at thy word:
    Call me but love, and I'll be new baptized;
    Henceforth I never will be Romeo.

    JULIET

    What man art thou that thus bescreen'd in night
    So stumblest on my counsel?

    ROMEO

    By a name
    I know not how to tell thee who I am:
    My name, dear saint, is hateful to myself,
    Because it is an enemy to thee;
    Had I it written, I would tear the word.

    JULIET

    My ears have not yet drunk a hundred words
    Of that tongue's utterance, yet I know the sound:
    Art thou not Romeo and a Montague?

    ROMEO

    Neither, fair saint, if either thee dislike.

    JULIET

    How camest thou hither, tell me, and wherefore?
    The orchard walls are high and hard to climb,
    And the place death, considering who thou art,
    If any of my kinsmen find thee here.

    ROMEO

    With love's light wings did I o'er-perch these walls;
    For stony limits cannot hold love out,
    And what love can do that dares love attempt;
    Therefore thy kinsmen a

    Display ends at character count of 3000
    Total number of characters received: 8473

**My code:**
::

    import urllib.request, urllib.parse, urllib.error

    url = input("Enter URL in the format of \"http://<host-name>/<page-name>\": ")

    if len(url) < 1:
        url = "http://data.pr4e.org/romeo-full.txt"

    fhand = urllib.request.urlopen(url)

    totalCount = 0
    displayCount = 0
    charLimit = 3000

    for line in fhand:
        line = line.decode().strip()
        totalCount += len(line)
        
        if displayCount < charLimit:
            displayCount += len(line)

            if not displayCount > charLimit:
                print(line)
            
            else:
                displayEnds = (charLimit - displayCount) + 1
                displayCount = displayCount - (displayCount - charLimit)
                print(line[:displayEnds])

    print(f"\nDisplay ends at character count of {displayCount}")
    print(f"Total number of characters received: {totalCount}")

**Reasoning behind my code:**

- It's kind of hard to check the validity of the output when there's no **expected output** to match it against. However, seeing the flawed code from exercise 12.2, I'm confident that this code is more accurate.
- For this assignment we'll need to ``import`` the ``request``, ``parse`` and ``error`` classes from ``urllib`` library.
- ``if`` no user input is detected, ``url`` will be initialized with a default value.
- With ``urllib`` we can manipulate web pages as if they're local files.
- ``fhand`` sends a GET request to open the access to the URL.
- ``totalCount`` holds the number of all characters that passes through the socket.
- ``displayCount`` is used to test against ``charLimit`` and should hold a value of ``3000`` after the web page is read.
- The ``for`` loop will read through the web page, line by line.
- Each ``line`` will be decoded from *bytes* to *strings* and stripped of *end-of-line* characters.
- As ``totalCount`` starts counting after each line, the program will check to see ``if`` the ``displayCount`` less than or larger than ``charLimit``. If it's less than, ``displayCount`` will starts to count. After finally being larger than the limit, ``displayEnds`` will calculate where, on the line, to print and stops after the 3000th character is reached.
- Due to ``displayCount`` overshooting the count a little bit by the end, the variable will change it value based on the calculation of ``displayCount - (displayCount - charLimit)``.
- Once all is tallied up, the program will print out where the display ends and the total number of characters that passes through the socket.

|

----

Exercise 12.4
-------------

**Prompt:** Change the ``urllinks.py`` program to extract and count paragraph (p) tags from the retrieved HTML document and display the count of the paragraphs as the output of your program. Do not display the paragraph text, only count them. Test your program on several small web pages as well as some larger web pages.

Link to ``urllinks.py``: https://www.py4e.com/code3/urllinks.py

Content of ``urllinks.py``:
::

    # To run this, download the BeautifulSoup zip file
    # http://www.py4e.com/code3/bs4.zip
    # and unzip it in the same directory as this file

    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))
        
**Expected output:** None available.

**My outputs:**
::

    $ python temporaryFile.py 
    Enter - http://www.dr-chuck.com/page1.htm 
    Total count of paragraph tags is 1

::

    $ python temporaryFile.py 
    Enter - https://www.dr-chuck.com/page2.htm 
    Total count of paragraph tags is 1

::

    $ python temporaryFile.py 
    Enter - https://www.python.org
    Total count of paragraph tags is 23

::

    $ python temporaryFile.py 
    Enter - https://www.yinza.com/Fandom/Script/01.html
    Total count of paragraph tags is 192

**My code:**
::

    # this is how to import BeautifulSoup if it's installed via pip package manager
    from soupsieve import bs4
    import urllib.request, urllib.parse, urllib.error
    import ssl

    # ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # request for URL and pass it through BeautifulSoup
    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # retrieve all of the paragraph tags and count them
    tags = soup('p')
    count = 0
    for tag in tags:
        count += 1

    # print out the total count of paragraph tags found in web page
    print(f"Total count of paragraph tags is {count}")

**Reasoning behind my code:**

I commented in the code for this assignment. As it is straightforward, I'll refrain from explain further here and suggest you look at the code.

|

----

Exercise 12.5
-------------

**Prompt:** (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that ``recv`` receives characters (newlines and all), not lines.

**Expected output:** None available.

**My outputs:**
::

    $ python temporaryFile.py 
    Enter a URL: google.com
    Please enter the URL in proper format!

::

    $ python temporaryFile.py 
    Enter a URL: htttpp:///dat.pro4e.org/romeo.txt
    Please enter an existing URL!

::

    $ python temporaryFile.py 
    Enter a URL: http://data.pr4e.org/romeo.txt
    But soft what light through yonder window breaks
    It is the east and Juliet is the sun
    Arise fair sun and kill the envious moon
    Who is already sick and pale with grief

**My code:**
::

    # code borrowed from 12.1
    import socket

    url = input("Enter a URL: ")
    port = 80

    # used for testing/debugging
    if len(url) < 1:
        url = 'http://data.pr4e.org/romeo.txt'

    tokens = url.split('/')

    try:
        host = tokens[2]

    except:
        print("Please enter the URL in proper format!")
        exit()

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        mysock.connect((host, port))

    except:
        print("Please enter an existing URL!")
        exit()

    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    # 'content' to hold the web page's content
    content = ""
    while True:
        data = mysock.recv(512)

        if len(data) < 1:
            break

        # data is appended to content, 512 bytes at a time
        content += data.decode()

    # locating the blank line after the header info
    pos = content.find('\r\n\r\n')

    # print the content after skipping the position of the end line characters
    print(content[pos+4:])

**Reasoning behind my code:**

The code is borrowed from exercise 12.1, so most of the code are already explained. Reasons on the changes are commented in the code. Feel free to take a look.

|

----

Autograder: Request-Response Cycle
----------------------------------

**Prompt:** Exploring the HyperText Transport Protocol

You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

Link: https://data.pr4e.org/intro-short.txt

There are three ways that you might retrieve this web page and look at the response headers: 

#) **Preferred:** Modify the ``socket1.py`` program to retrieve the above URL and print out the headers and data. Make sure to **change** the code to retrieve the above URL - the values are different for each URL.
#) Open the URL in a web browser with a **developer console** and manually examine the headers that are returned.
#) Open the URL in a web browser with **FireBug** and manually examine the headers that are returned.

Enter the header values in each of the fields below:

- Last-Modified
- ETag
- Content-Length
- Cache-Control
- Content-Type

**Expected output:** None available.

**My outputs:**

*preferred method*
::

    $ python temporaryFile.py 
    HTTP/1.1 200 OK
    Date: Wed, 05 Jul 2023 00:27:37 GMT
    Server: Apache/2.4.18 (Ubuntu)
    Last-Modified: Sat, 13 May 2017 11:22:22 GMT
    ETag: "1d3-54f6609240717"
    Accept-Ranges: bytes
    Content-Length: 467
    Cache-Control: max-age=0, no-cache, no-store, must-revalidate
    Pragma: no-cache
    Expires: Wed, 11 Jan 1984 05:00:00 GMT
    Connection: close
    Content-Type: text/plain

    Why should you learn to write programs?

    Writing programs (or programming) is a very creative
    and rewarding activity.  You can write programs for
    many reasons, ranging from making your living to solving
    a difficult data analysis problem to having fun to helping
    someone else solve a problem.  This book assumes that
    everyone needs to know how to program, and that once
    you know how to program you will figure out what you want
    to do with your newfound skills.

    -------------------------------------------------------------
    Extracted values:
    Last-Modified: Sat, 13 May 2017 11:22:22 GMT
    ETag: "1d3-54f6609240717"
    Content-Length: 467
    Cache-Control: max-age=0, no-cache, no-store, must-revalidate
    Content-Type: text/plain

*Developer tools method*

.. image:: img/developer_tools.PNG
    :width: 800
    :alt: Image shows the header info of the web page

**My code:**
::

    import socket
    import re

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = f'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    # variable to hold web page's data
    content = ""
    while True:
        data = mysock.recv(512)

        if len(data) < 1:
            break

        content += data.decode()

    print(content)

    # Extra work you don't have to do for this assignment below

    # list holding regex patterns for each requested value
    headerValues = ["(L.*)", "(E.*)", "(C.*-L.*)", "(C.*-C.*)", "(C.*-T.*)"]

    # list comprehension to search for header values via regex
    # and append them to 'lista'
    lista = [ re.findall(regex, content)[0].strip() for regex in headerValues ]

    # formatted print
    print('-------------------------------------------------------------')
    print("Extracted values:")

    for value in lista:
        print(value)

**Reasoning behind my code:**

*The preferred method*

- Similar to exercise 12.1, I edited the ``socket1.py`` file to accommodate for this assignment. The changes are commented in the code. Feel free to take a look.

*The developer tools method*

- For this method, I used *Firefox's* built-in *Developer Tools* feature.
- I would first enter the link to the web page into the *address bar* to go to the site. The link is https://data.pr4e.org/intro-short.txt.
- Once in the page, I would *right-click and click* on the option to **Inspect (Q)**
- Then I would go into the **Network** tab and click on the **Reload** button.
- A line showing the domain name ``data.pr4e.org`` and file name ``intro-short.txt`` would populate.
- Clicking on that line will show the header info (image is shown the **my outputs** section, above).
  
I omitted doing the **Firebug** method, seeing as it's very similar to using the developer tools.

|

----

Autograder: Scraping HTML Data with BeautifulSoup
-------------------------------------------------

**Prompt:** Scraping Numbers from HTML using BeautifulSoup

In this assignment you will write a Python program similar to `urllink2.py <http://www.py4e.com/code3/urllink2.py>`_. The program will use **urllib** to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

- Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553) 
- Actual data: http://py4e-data.dr-chuck.net/comments_1784990.html (Sum ends with 0)

The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following: 

.. code-block:: html

    <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
    <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
    <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

Look at the `sample code <http://www.py4e.com/code3/urllink2.py>`_ provided. It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags. 
::

    ...
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
       # Look at the parts of a tag
       print 'TAG:',tag
       print 'URL:',tag.get('href', None)
       print 'Contents:',tag.contents[0]
       print 'Attrs:',tag.attrs
       
You need to adjust this code to look for **span** tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment. 

**Expected output:** Sample execution
::

    $ python3 solution.py
    Enter - http://py4e-data.dr-chuck.net/comments_42.html
    Count 50
    Sum 2...

**My outputs:**
::

    $ python temporaryFile.py 
    Enter - http://py4e-data.dr-chuck.net/comments_42.html
    Count 50
    Sum 2553

::

    $ python temporaryFile.py 
    Enter -  http://py4e-data.dr-chuck.net/comments_1784990.html
    Count 50
    Sum 2700

**My code:**
::

    import urllib.parse, urllib.error
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    url = input("Enter - ")

    if len(url) < 1:
        url = 'http://py4e-data.dr-chuck.net/comments_42.html'
        
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    count = 0
    total = 0
    tags = soup('span')
    for tag in tags:
        total += int(tag.contents[0])
        count += 1

    print(f'Count {count}\nSum {total}')

**Reasoning behind my code:**

- Reading through the code in `urllink2.py <http://www.py4e.com/code3/urllink2.py>`_, I took what I need and expanded further to complete this assignment.
- The typical modules need to be imported from ``urllib`` are ``request``, ``parser`` and ``error``. From ``request`` I imported ``urlopen`` to make it easier to call the object in the main code.
- The typical module need to be imported from ``bs4`` is ``BeautifulSoup``.
- ``url`` asks and stores a URL.
- ``if`` no user input is detected, ``url`` will auto-assign with a default URL.
- ``html`` is to store the content ``read`` in from the ``urlopen`` function call.
- ``soup`` is to initialize ``BeautifulSoup`` to read and parse html code.
- ``count`` is used to test against the **expected output** to see if my code would detect the same number of **<span>** tags.
- ``total`` is to hold the sum of all the tag's contents.
- ``soup`` is given an argument of ``'span'`` and any matches found will be stored in ``tags``.
- Looping through the tags, the program will extract all the numbers via ``tag.contents[0]``. The numbers are then converted to ``int`` type and added.
- Once completed, the program prints out the ``count`` and ``total`` to the console. 

|

----

Autograder: Following Links with BeautifulSoup
----------------------------------------------

**Prompt:** Following Links in Python

In this assignment you will write a Python program that expands on `urllinks.py <http://www.py4e.com/code3/urllinks.py>`_. The program will use ``urllib`` to read the HTML from the data files below, *extract* the **href=** values from the **anchor** tags, *scan* for a tag that is in a particular position relative to the first name in the list, follow that link and *repeat* the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment:

- **Sample problem:** Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
    
  + Find the link at position ``3``. Follow that link. Repeat this process ``4`` times. The answer is the last name that you retrieve.
  + *Sequence of names:* ``Fikret Montgomery Mhairade Butchi Anayah``
  + *Last name in sequence:* ``Anayah``

- **Actual problem:** Start at http://py4e-data.dr-chuck.net/known_by_Wojciech.html

  + Find the link at position ``18``. Follow that link. Repeat this process ``7`` times. The answer is the last name that you retrieve.
  + *Hint:* The first character of the name of the last page that you will load is: ``N``

**Expected output:** Sample execution
::

    $ python3 solution.py
    Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
    Enter count: 4
    Enter position: 3
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html

The answer to the assignment for this execution is **"Anayah"**.

**My outputs:**
::

    $ python temporaryFile.py 
    Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
    Enter count: 4
    Enter position: 3
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html

    Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
    Last name in sequence: Anayah

::

    $ python temporaryFile.py 
    Enter URL: http://py4e-data.dr-chuck.net/known_by_Wojciech.html
    Enter count: 7
    Enter position: 18
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Wojciech.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Lucca.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Emon.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Laticha.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Harikrishna.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Kenzi.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Maya.html
    Retrieving: http://py4e-data.dr-chuck.net/known_by_Naima.html

    Sequence of names: Wojciech Lucca Emon Laticha Harikrishna Kenzi Maya Naima
    Last name in sequence: Naima

The answer to the assignment for this execution is **"Naima"**.

**My code:**
::

    # required libraries/modules
    import urllib.parse, urllib.error
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import re

    # requests URL, number of repetition and position of the link
    url = input("Enter URL: ")
    count = input("Enter count: ")
    pos = input("Enter position: ")

    # used for testing/debugging
    if len(url) < 1:
        url = 'http://py4e-data.dr-chuck.net/known_by_Wojciech.html'
        count = 7
        pos = 18

    count = int(count)
    pos = int(pos)

    # records current name from URL and store it in a list structure
    sequence = re.findall("by_([A-za-z]+)[.]", url)

    # runs until number of repetition achieved
    while True:
        
        # prints 'Retrieving' message of current URL to match sample execution
        print(f'Retrieving: {url}')

        if count == 0: break

        # reads the whole web page
        html = urlopen(url).read()

        # adjusts bs4 to parse html docs
        soup = BeautifulSoup(html, "html.parser")

        # finds all lines containing anchor tags, up to a limit, and store them
        # in a list structure
        tags = soup.find_all('a', limit=pos)

        # extracts the name we're looking for and store in str type
        name = tags[pos-1].contents[0]

        # appends current name to the sequence list
        sequence.append(name)

        # extracts the URL we're looking for and store in str type
        url = tags[pos-1].get('href')

        count -= 1

    # formatted outputs
    print('\nSequence of names: ', end='')
    for name in sequence:
        print(name, end=' ')

    print(f'\nLast name in sequence: {sequence[-1]}')

**Reasoning behind my code:**

I've commented in the code for this assignment. But seeing that this assignment is on the more difficult side of things, for me, I will go further in-depth here, in this section, for my benefit and yours! :)

There are many ways to go about tackling this assignment. I've seen others' solutions that are shorter and longer than mine. And the thing that sets me apart from other solutions is that... I chose the path of incorporating regular expression into my code and made it more complicated... so with all the necessary libraries/modules being imported, I also ``import`` the ``re`` library.

The first part of the code is the typical request for user's inputs and set the variables with default assignments if no input is detected. Then I created ``sequence`` as a way to extract the first name from the URL and input it as the first element in the list. Everything following will be performed in the ``while`` loop until ``count`` is down to ``0``.

Inside the loop, the program will first output the current ``url`` to the console. Then it'll check on ``count`` to see if it's ``0`` or not. If it's not yet ``0``, the program will execute the next line of code. In the next line, ``html`` is initialized with the entire HTML document, opened by ``urlopen()`` and read through via ``read()``.

``soup`` is designed to adjust ``BeautifulSoup`` to handle HTML docs and parse through them. Going through the HTML doc, ``tags`` calls ``soup`` to find all the *anchor* tags, up to the ``limit`` of the URL *position* that the user set in ``pos``. So in this case, ``soup`` will loop through ``18`` *anchor* tags. Each time one is found, it will be appended to ``tags``.

To grab the name from each HTML line, I created ``name``. This variable will locate the line of interest using ``pos`` as the index. The ``-1`` is because the list's starting index is ``0``. Once the name is found, it will be appended to ``sequence``.

The ``url`` value will then change to the new URL to prep for the next URL call. This is done similar to how the program grabs the name from the HTML line, except instead of looking for the ``contents``, it'll look for ``href``, which holds a reference to the new URL.

Once all operations are done, the ``count`` is decreased by one and the loop jumps to the next iteration. After breaking out of the loop, the ``sequence`` is printed, along with a line indicating the last name attached to the list.
