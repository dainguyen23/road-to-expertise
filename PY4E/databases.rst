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
