Databases
=========

|

For this section, I'll be going over autograder exercises, plus application 1 and 2.

.. contents:: Contents
    :local:

.. note::

    **Somethings to be familiar with:**

|

----

Autograder: Single Table SQL
----------------------------

**My Code:**
::

    # required module
    import sqlite3

    # set connection to specific database file or generate one
    # and initialize cursor/handle
    conn = sqlite3.connect('singleTable.sqlite3')
    cur = conn.cursor()

    # execute commands to create specific table
    # if the table already exists, delete all entries
    cur.executescript('''
        CREATE TABLE IF NOT EXISTS Ages (
            name VARCHAR(128),
            age INTEGER
        );

        DELETE FROM Ages;
    ''')

    # add entries into the table
    cur.executescript('''
        INSERT INTO Ages (name, age) VALUES ('Elshan', 19);
        INSERT INTO Ages (name, age) VALUES ('Tione', 22);
        INSERT INTO Ages (name, age) VALUES ('Spondon', 13);
        INSERT INTO Ages (name, age) VALUES ('Joanne', 35);
        INSERT INTO Ages (name, age) VALUES ('Nikela', 21);
        INSERT INTO Ages (name, age) VALUES ('Catrin', 16);
    ''')

    # commit updates to the database file
    conn.commit()

    # concatenate values of each row, from name to age, then
    # convert them to hexadecimal values and
    # present them in ascending order
    cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
    print(cur.fetchone()[0])

    # close connection to database file
    conn.close()

|

----

Autograder: Counting Email in a Database
----------------------------------------

**My Code:**

*Version 1: limiting string comparison in code*
::

    # required module
    import sqlite3
    from timeit import default_timer as timer

    start = timer()
    conn = sqlite3.connect('countDomains.sqlite')
    cur = conn.cursor()

    cur.executescript('''
        DROP TABLE IF EXISTS Counts;

        CREATE TABLE Counts (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            org TEXT UNIQUE,
            count INTEGER);

    ''')

    fname = 'mbox.txt'
    print(f'Opening file: {fname}')
    fhand = open(fname)

    for line in fhand:
        if not line.startswith('From: '): continue

        line = line.translate(str.maketrans('@', ' '))
        token = line.split()
        domain = token[2]

        cur.execute('SELECT id FROM Counts WHERE org = ?', (domain, ))
        row = cur.fetchone()

        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain, ))

        else:
            pKey = row[0]
            cur.execute('UPDATE Counts SET count = count + 1 WHERE id = ?', (pKey, ))

    conn.commit()

    cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1')
    row = cur.fetchone()
    domain = row[0]
    count = row[1]

    print(f"\nTop Organizational Count\nDomain: {domain}\nCount: {count}")

    conn.close()
    end = timer()
    print("Time elapsed:", round(end-start, 2), "second(s)")

::

    $ python temporaryFile.py 
    Opening file: mbox.txt

    Top Organizational Count
    Domain: iupui.edu       
    Count: 536
    Time elapsed: 0.38 second(s)

*Version 2: using string comparisons*

::

    # required module
    import sqlite3
    from timeit import default_timer as timer

    start = timer()
    conn = sqlite3.connect('countDomains.sqlite')
    cur = conn.cursor()

    cur.executescript('''
        DROP TABLE IF EXISTS Counts;

        CREATE TABLE Counts (
            org TEXT UNIQUE,
            count INTEGER);

    ''')

    fname = 'mbox.txt'
    print(f'Opening file: {fname}')
    fhand = open(fname)

    for line in fhand:
        if not line.startswith('From: '): continue

        line = line.translate(str.maketrans('@', ' '))
        token = line.split()
        domain = token[2]

        cur.execute('SELECT count FROM Counts WHERE org = ?', (domain, ))
        row = cur.fetchone()

        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain, ))

        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain, ))

    conn.commit()

    cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1')
    row = cur.fetchone()
    domain = row[0]
    count = row[1]

    print(f"\nTop Organizational Count\nDomain: {domain}\nCount: {count}")

    conn.close()
    end = timer()
    print("Time elapsed:", round(end-start, 2), "second(s)")



::

    $ python temporaryFile.py 
    Opening file: mbox.txt

    Top Organizational Count
    Domain: iupui.edu       
    Count: 536
    Time elapsed: 0.48 second(s)

*Version 3: using dictionary to handle unique row inserts*
::

    # required module
    import sqlite3
    from timeit import default_timer as timer

    start = timer()
    conn = sqlite3.connect('countDomains.sqlite')
    cur = conn.cursor()

    cur.executescript('''
        DROP TABLE IF EXISTS Counts;

        CREATE TABLE Counts (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            org TEXT UNIQUE,
            count INTEGER);

    ''')

    fname = 'mbox.txt'
    print(f'Opening file: {fname}')
    fhand = open(fname)
    domain = dict()

    for line in fhand:
        if not line.startswith('From: '): continue

        line = line.translate(str.maketrans('@', ' '))
        token = line.split()
        domain[token[2]] = domain.get(token[2], 0) + 1

    for org, count in domain.items():
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, ?)', (org, count))

    conn.commit()

    cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1')
    row = cur.fetchone()
    domain = row[0]
    count = row[1]

    print(f"\nTop Organizational Count\nDomain: {domain}\nCount: {count}")

    conn.close()
    end = timer()
    print("Time elapsed:", round(end-start, 2), "second(s)")

::

    $ python temporaryFile.py 
    Opening file: mbox.txt

    Top Organizational Count
    Domain: iupui.edu
    Count: 536
    Time elapsed: 0.44 second(s)

|

----

Library Management - iTunes Edition
-----------------------------------

**Process:**

This application will:

- Read an iTunes export file in XML
- Produce a properly normalized database

Link to reference code and ``Library.xml`` file: https://www.py4e.com/code3/tracks.zip

**Testing methodology:**

The program will run the query and retrieve the corresponding output, listed below:

**My code:**
::

    import xml.etree.ElementTree as ET
    import sqlite3

    conn = sqlite3.connect("multiTableTracks.sqlite")
    cur = conn.cursor()

    cur.executescript('''
        DROP TABLE IF EXISTS Artist;
        DROP TABLE IF EXISTS Genre;
        DROP TABLE IF EXISTS Album;
        DROP TABLE IF EXISTS Track;

        CREATE TABLE Artist (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
        );

        CREATE TABLE Genre (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
        );

        CREATE TABLE Album (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title TEXT UNIQUE,
            artist_id INTEGER
        );

        CREATE TABLE Track (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title TEXT UNIQUE,
            length INTEGER,
            rating INTEGER,
            count INTEGER,
            genre_id INTEGER,
            album_id INTEGER
        );
    ''')

    fname = input("Enter file name: ")
    if len(fname) < 1: fname = "Library.xml"

    def lookup(diction, key):
        found = False
        for child in diction:
            if found : return child.text
            if child.tag == 'key' and child.text == key:
                found = True
        return None

    readxml = ET.parse(fname)
    content = readxml.findall('dict/dict/dict')
    print("Dictionary count:", len(content))

    iteration = 0
    for entry in content:
        track = lookup(entry, 'Track ID')
        name = lookup(entry, 'Name')
        artist = lookup(entry, 'Artist')
        album = lookup(entry, 'Album')
        genre = lookup(entry, 'Genre')
        count = lookup(entry, 'Play Count')
        rating = lookup(entry, 'Rating')
        length = lookup(entry, 'Total Time')

        if track is None or name is None or artist is None or album is None or genre is None:
            continue

        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist, ))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
        artist_id = cur.fetchone()[0]

        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre, ))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
        genre_id = cur.fetchone()[0]

        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
        album_id = cur.fetchone()[0]

        cur.execute('INSERT OR REPLACE INTO Track (title, length, rating, count, genre_id, album_id) VALUES (?, ?, ?, ?, ?, ?)', (name, length, rating, count, genre_id, album_id) )

        iteration += 1
        if iteration == 20:
            conn.commit()
            iteration = 0

        print(name, artist, album, genre, count, rating, length)

    print("Dictionary count:", len(content))
    conn.close()

|

----

Many Students in Many Courses
-----------------------------

**Process:**

This application will:

- Read roster data in JSON format
- Parse the JSON file
- Produce an SQLite database that contains a User, Course, and Member table
- Populate the tables from the data file

Link to reference code: https://www.py4e.com/code3/roster/roster.py

Link to ``roster_data.json``: https://www.py4e.com/tools/sql-intro/roster_data.php?PHPSESSID=10a2f411ec9495fde4e2d2ead3e9585e

**Testing methodology:**

The program will run the queries and retrieve the corresponding outputs, listed below:

*Command & output:*

.. code-block:: sql

    SELECT User.name, Course.title, Member.role
    FROM User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

::

    Zunaira | si206 | 0
    Zohair  | si363 | 0

*Command & output:*

.. code-block:: sql

    SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X
    FROM User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;

::
    
    XYZZY41626265736933363430

**My code:**
::

    # required libraries
    import json
    import sqlite3

    # create new or connect to existing database file. I'll name the file "rosterdb.sqlite3"
    # cur acts as the file handle
    conn = sqlite3.connect("rosterdb.sqlite3")
    cur = conn.cursor()

    # run SQL commands to drop existing tables and create new tables for testing
    cur.executescript('''
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Member;
        DROP TABLE IF EXISTS Course;

        CREATE TABLE User (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
        );

        CREATE TABLE Course (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title TEXT UNIQUE
        );

        CREATE TABLE Member (
            user_id INTEGER,
            course_id INTEGER,
            role INTEGER,
            PRIMARY KEY (user_id, course_id)
        );
    ''')

    # prompt for a json file. Set default file if no input detected
    fname = input('Enter file name: ')
    if len(fname) < 1: fname = 'roster_data.json'

    # function designed to display column names
    def columnNames():
        spaces = ' ' * 14
        print(f'\nName{spaces}Course\tRole (0 for student, 1 for professor)')
        print('_' * 69)

    # function designed to display data entry from database when used inside a loop
    def prettyPrint(name, title, role):
        spaces = ' ' * (18 - len(name))
        print(f'{name}{spaces}{title}\t\t{role}')

    # function designed to display SQL search commands
    def testMethod(method, num):
        print('-' * 74)
        print(f'\nRunning command...\n{method}')
        
        cur.execute(method)
        print("\nOutput:")
        
        # depending on the command, the number of values retrieved will differ
        # so the output method will be conditional
        # this method is used when retrieving three values
        if num == 1:
            output = cur.fetchall()
            columnNames()
            for entry in output:
                prettyPrint(entry[0], entry[1], entry[2])

        # this method is used when retrieving one value
        if num == 2:
            output = cur.fetchone()[0]
            print('\n'+output)

    # open and read in all file content to str_data then parse the data
    str_data = open(fname).read()
    json_data = json.loads(str_data)

    # print column names
    columnNames()

    # loop through data objects and insert each entry into the database
    iteration = 0
    for entry in json_data:
        name = entry[0]
        title = entry[1]
        role = entry[2]

        # insert a unique name into the User table and grab the primary key
        # then store the primary key in a variable to be used as a foreign key
        cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name, ))
        cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
        user_id = cur.fetchone()[0]

        # insert a unique title into the Course table and grab the primary key
        # then store the primary key in a variable to be used as a foreign key
        cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title, ))
        cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
        course_id = cur.fetchone()[0]

        # insert a role and foreign keys associated the User and Course tables
        cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))

        # force a write operation to the database file after every 20 entries
        iteration += 1
        if iteration == 20:
            conn.commit()
            iteration = 0

        # display each entry after being inserted
        prettyPrint(name, title, role)

    # force write on the last bit of data entries
    conn.commit()

    # test command #1
    method1 = '''
        SELECT User.name, Course.title, Member.role
        FROM User JOIN Member JOIN Course
        ON User.id = Member.user_id AND Member.course_id = Course.id
        ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2'''
    testMethod(method1, 1)

    # test command #2
    method2 = '''
        SELECT 'XYZZY' || HEX( User.name || Course.title || Member.role ) AS X
        FROM User JOIN Member JOIN Course
        ON User.id = Member.user_id AND Member.course_id = Course.id
        ORDER BY X LIMIT 1'''
    testMethod(method2, 2)

    # close connection to the database
    conn.close()

**My output:**
::

    $ python temporaryFile.py 
    Enter file name: roster_data.json

    Name              Course        Role (0 for student, 1 for professor)
    _____________________________________________________________________
    Komal             si110         1
    Richard           si110         0
    Jac               si110         0
    Keiron            si110         0
    Jeanna            si110         0
    Avril             si110         0
    Kinga             si110         0
    Madox             si110         0
    Jesse             si110         0
    Munro             si110         0
    Yu                si110         0
    Krista            si110         0
    Jeanie            si110         0
    Precious          si110         0
    Lucyanne          si110         0
    Christie          si110         0
    Vicky             si110         0
    Eiley             si110         0
    Eshal             si110         0
    Kirie             si110         0
    Leylann           si110         0
    Roary             si110         0
    Saniya            si110         0
    Annalicia         si110         0
    Melica            si110         0
    Elen              si110         0
    Dareh             si110         0
    Rahim             si110         0
    Burak             si110         0
    Kerri             si106         1
    Elli              si106         0
    Amie              si106         0
    Arved             si106         0
    Jaiha             si106         0
    Haillie           si106         0
    Milana            si106         0
    Silas             si106         0
    Eduardo           si106         0
    Roman             si106         0
    Romey             si106         0
    Cale              si106         0
    Calypso           si106         0
    Juliet            si106         0
    Drew              si106         0
    Sofian            si106         0
    Shinade           si106         0
    Ali               si106         0
    Cator             si106         0
    Lilliana          si106         0
    Maximus           si106         0
    Rameen            si106         0
    Havin             si106         0
    Starr             si106         0
    Miranne           si106         0
    Kyral             si106         0
    Conley            si106         0
    Divya             si106         0
    Yaseen            si106         0
    Athena            si106         0
    Kenton            si106         0
    Evann             si106         0
    Nicolina          si106         0
    Filippo           si106         0
    Seth              si106         0
    Seonag            si106         0
    Kaeli             si106         0
    Ren               si106         0
    Lyndsay           si106         0
    Ferne             si106         0
    Alex              si106         0
    Ed                si106         0
    Queeneffa         si106         0
    Halyda            si206         1
    Sherwyn           si206         0
    Quinn             si206         0
    Zechariah         si206         0
    Morgen            si206         0
    Cabhan            si206         0
    Alister           si206         0
    Calley            si206         0
    Ieuan             si206         0
    Ame               si206         0
    Ezri              si206         0
    Skyla             si206         0
    Joaquin           si206         0
    Kaylee            si206         0
    Christopher       si206         0
    Zijie             si206         0
    Kelly             si206         0
    Viki              si206         0
    Kadi              si206         0
    Safara            si206         0
    Salymat           si206         0
    Calypso           si206         0
    Yingzi            si206         0
    Alastair          si206         0
    Sami              si206         0
    Mahan             si206         0
    Meledy            si206         0
    Zunaira           si206         0
    Jeannie           si206         0
    Brook             si206         0
    Zoha              si206         0
    Reis              si206         0
    Gene              si206         0
    Israa             si206         0
    Alhaji            si206         0
    Allie             si206         0
    Rhuaridh          si301         1
    Cesare            si301         0
    Olaoluwapolorimi  si301         0
    Ramsey            si301         0
    McCaulley         si301         0
    Ciaran            si301         0
    Karrah            si301         0
    Bradlie           si301         0
    Ryan              si301         0
    Richey            si301         0
    Bronwen           si301         0
    Ramsay            si301         0
    Ariana            si301         0
    Sherese           si301         0
    Rheanne           si301         0
    Shakira           si301         0
    Yaseen            si301         0
    Sahar             si301         0
    Dennan            si301         0
    Kaleb             si301         0
    Rhonda            si301         0
    Hibah             si301         0
    Havila            si310         1
    Charlotte         si310         0
    Linden            si310         0
    Tehzeeb           si310         0
    Anaya             si310         0
    Ahmad             si310         0
    Deia              si310         0
    Rehan             si310         0
    Missy             si310         0
    Dionne            si310         0
    Maciej            si310         0
    Reegan            si310         0
    Daegyu            si310         0
    Maxwell           si310         0
    Freya             si310         0
    Ryden             si310         0
    Aliyaan           si310         0
    Annan             si310         0
    Devrin            si310         0
    Nancy             si310         0
    Hashim            si310         0
    Aon               si310         0
    Deena             si310         0
    Eoghan            si310         0
    Kyral             si310         0
    Khyralee          si310         0
    Jarred            si310         0
    Meabh             si310         0
    Tyson             si310         0
    Asif              si310         0
    Damien            si310         0
    Eroni             si310         0
    Brea              si310         0
    Ruadhan           si310         0
    Phoevos           si310         0
    Ross              si310         0
    Mikka             si310         0
    Kaine             si310         0
    Reace             si310         0
    Eljon             si310         0
    Callun            si310         0
    Qainat            si310         0
    Manar             si310         0
    Robert            si310         0
    Eljay             si310         0
    Ayesha            si334         1
    Emilie            si334         0
    Kiarrah           si334         0
    Maddox            si334         0
    Leyland           si334         0
    Muzzammil         si334         0
    Ariella           si334         0
    Aida              si334         0
    Tian              si334         0
    Lydia             si334         0
    Ahmed             si334         0
    Bully             si334         0
    Narvic            si334         0
    Valentino         si334         0
    Taya              si334         0
    Abigayle          si334         0
    Tanisha           si334         0
    Lance             si334         0
    Tehya             si334         0
    Dolci             si334         0
    Belle             si334         0
    Kaydan            si334         0
    Ryder             si334         0
    Kevin             si334         0
    Pravin            si334         0
    Lena              si363         1
    Usmah             si363         0
    Oran              si363         0
    Antonio           si363         0
    Yago              si363         0
    Madeeha           si363         0
    Layney            si363         0
    Tiegan            si363         0
    Vincent           si363         0
    Rishi             si363         0
    Deshawn           si363         0
    Choco             si363         0
    Latoya            si363         0
    Siriol            si363         0
    Inaara            si363         0
    Artem             si363         0
    Saman             si363         0
    Demmi             si363         0
    Thorfinn          si363         0
    Mahasen           si363         0
    Otilija           si363         0
    Glenn             si363         0
    Prithivi          si363         0
    Dafydd            si363         0
    Eljay             si363         0
    Karlie            si363         0
    Bret              si363         0
    Zohair            si363         0
    Kory              si363         0
    Giuliana          si363         0
    Lucia             si363         0
    Keiva             si363         0
    Fearne            si363         0
    Leni              si363         0
    Ravin             si363         0
    Tereza            si363         0
    Ruadhan           si363         0
    Harper            si363         0
    Connan            si363         0
    Cain              si363         0
    Piper             si363         0
    Arun              si363         0
    Daniil            si363         0
    Linden            si363         0
    Eniola            si364         1
    Stevie            si364         0
    Aizah             si364         0
    Zaynah            si364         0
    Josie             si364         0
    Calli             si364         0
    Riha              si364         0
    Hadyn             si364         0
    Marieclare        si364         0
    Abbe              si364         0
    Caie              si364         0
    Abigael           si364         0
    Tokinaga          si364         0
    Ubaid             si364         0
    Mcbride           si364         0
    Modoulamin        si364         0
    Aronas            si364         0
    Dissanayake       si364         0
    Joynul            si364         0
    Kohen             si364         0
    Clyde             si364         0
    Callyn            si364         0
    Rahman            si364         0
    Aonghus           si364         0
    Kathrina          si364         0
    Honie             si364         0
    Lagan             si364         0
    Pietro            si364         0
    Sunehri           si422         1
    Reagan            si422         0
    Zacharias         si422         0
    Yousif            si422         0
    Maanisha          si422         0
    Chrystal          si422         0
    Selena            si422         0
    Effie             si422         0
    Afton             si422         0
    Malik             si422         0
    Teighan           si422         0
    Atal              si422         0
    Eliana            si422         0
    Quinn             si422         0
    Makala            si422         0
    Jensine           si422         0
    Alastair          si422         0
    Bruce             si422         0
    Tamarah           si422         0
    Elona             si422         0
    Alexandra         si422         0
    Robin             si422         0
    Kaye              si422         0
    Kamilah           si422         0
    Antigone          si422         0
    Loghan            si422         0
    Ander             si422         0
    Caley             si422         0
    Ezra              si422         0
    Simra             si422         0
    Wang              si422         0
    Kareena           si422         0
    Rhein             si430         1
    Otilia            si430         0
    Tristan           si430         0
    Ariella           si430         0
    Bernard           si430         0
    Monta             si430         0
    Muireann          si430         0
    Ami               si430         0
    Dagon             si430         0
    Marcquis          si430         0
    Dolci             si430         0
    Felicity          si430         0
    Beyza             si430         0
    Cadie             si430         0
    Sylvanna          si430         0
    Harneet           si430         0
    Kiaran            si430         0
    Wilhelmina        si430         0
    Conal             si430         0
    Somaya            si430         0
    --------------------------------------------------------------------------

    Running command...

        SELECT User.name, Course.title, Member.role
        FROM User JOIN Member JOIN Course
        ON User.id = Member.user_id AND Member.course_id = Course.id
        ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2

    Output:

    Name              Course        Role (0 for student, 1 for professor)
    _____________________________________________________________________
    Zunaira           si206         0
    Zohair            si363         0
    --------------------------------------------------------------------------

    Running command...

        SELECT 'XYZZY' || HEX( User.name || Course.title || Member.role ) AS X
        FROM User JOIN Member JOIN Course
        ON User.id = Member.user_id AND Member.course_id = Course.id
        ORDER BY X LIMIT 1

    Output:

    XYZZY41626265736933363430
