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