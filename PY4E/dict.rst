Dictionaries
============

|

For this section, I'll be going over exercises 9.1 to 9.5.

.. contents:: Contents
    :local:

.. note::

    **Somethings to be familiar with:**

    **Dictionaries are mutable**. A **dictionary** is like a *list*, but more general. In a list, the index positions have to be integers; in a dictionary, the indices can be (almost) any type.

    You can think of a dictionary as a mapping between a set of indices (which are called **keys**) and a set of **values**. *Each key maps to a value*. The association of a key and a value is called a **key-value pair** or sometimes an **item**.
    ::

        >>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
        >>> print(eng2sp)
        {'one': 'uno', 'two': 'dos', 'three': 'tres'}

    Since Python 3.7x the order of key-value pairs is the same as their input order, i.e. dictionaries are now ordered structures.

    The ``in`` operator works on dictionaries; it tells you whether something appears as a **key** in the dictionary (appearing as a value is not good enough).
    ::

        >>> 'one' in eng2sp
        True
        >>> 'uno' in eng2sp
        False

    To see whether something appears as a value in a dictionary, you can use the method ``values``, which returns the values as a type that can be converted to a list, and then use the ``in`` operator:
    ::

        >>> vals = list(eng2sp.values())
        >>> 'uno' in vals
        True

    The ``in`` operator uses different algorithms for lists and dictionaries. For lists, it uses a linear search algorithm. As the list gets longer, the search time gets longer in direct proportion to the length of the list.
    
    For dictionaries, Python uses an algorithm called a *hash table* that has a remarkable property: the ``in`` operator takes about the same amount of time no matter how many items there are in a dictionary.

|

----

Exercise 9.1
------------

**Prompt:** Download a copy of the file https://www.py4e.com/code3/words.txt

Write a program that reads the words in **words.txt** and stores them as keys in a dictionary. **It doesn't matter what the values are**. Then you can use the ``in`` operator as a fast way to check whether a string is in the dictionary.

**Expected output:** None available.

**My output:**
::

    The dictionary consists of 126 unique key-value pairs:
    {'Writing': 1, 'programs': 2, 'or': 3, 'programming': 4, 'is': 5,
     'a': 6, 'very': 7, 'creative': 8, 'and': 9, 'rewarding': 10,
     'activity': 11, 'You': 12, 'can': 13, 'write': 14, 'for': 15,
     'many': 16, 'reasons': 17, 'ranging': 18, 'from': 19, 'making': 20, 
     'your': 21, 'living': 22, 'to': 23, 'solving': 24, 'difficult': 25, 
     'data': 26, 'analysis': 27, 'problem': 28, 'having': 29, 'fun': 30, 
     'helping': 31, 'someone': 32, 'else': 33, 'solve': 34, 'This': 35, 
     'book': 36, 'assumes': 37, 'that': 38, '{\\em': 39, 'everyone}': 40, 
     'needs': 41, 'know': 42, 'how': 43, 'program': 44, 'once': 45, 
     'you': 46, 'program,': 47, 'will': 48, 'figure': 49, 'out': 50, 
     'what': 51, 'want': 52, 'do': 53, 'with': 54, 'newfound': 55, 
     'skills': 56, 'We': 57, 'are': 58, 'surrounded': 59, 'in': 60, 
     'our': 61, 'daily': 62, 'lives': 63, 'computers': 64, 'laptops': 65, 
     'cell': 66, 'phones': 67, 'think': 68, 'of': 69, 'these': 70, 
     'as': 71, 'personal': 72, 'assistants': 73, 'who': 74, 'take': 75, 
     'care': 76, 'things': 77, 'on': 78, 'behalf': 79, 'The': 80, 
     'hardware': 81, 'current-day': 82, 'essentially': 83, 'built': 84, 
     'continuously': 85, 'ask': 86, 'us': 87, 'the': 88, 'question': 89, 
     'What': 90, 'would': 91, 'like': 92, 'me': 93, 'next': 94, 'Our': 95, 
     'fast': 96, 'have': 97, 'vasts': 98, 'amounts': 99, 'memory': 100, 
     'could': 101, 'be': 102, 'helpful': 103, 'if': 104, 'we': 105, 
     'only': 106, 'knew': 107, 'language': 108, 'speak': 109, 
     'explain': 110, 'computer': 111, 'it': 112, 'If': 113, 'this': 114, 
     'tell': 115, 'tasks': 116, 'were': 117, 'repetitive': 118, 
     'Interestingly,': 119, 'kinds': 120, 'best': 121, 'often': 122, 
     'humans': 123, 'find': 124, 'boring': 125, 'mind-numbing': 126}

    Is the key 'book' in the dictionary? True
    Is the value 111 in the dictionary? True
    Is the key 'Excalibur' in the dictionary? False
    Is the value 127 in the dictionary? False

**My code:**
::

    fhand = open("words.txt")
    diction = dict()
    valueCount = 1

    for line in fhand:

        for word in line.split():
            if word in diction:
                continue
            
            diction[word] = valueCount
            valueCount += 1

    values = list(diction.values())

    print(f"The dictionary consists of {valueCount-1} unique key-value pairs:\n", diction)
    print(f"\nIs the key \'book\' in the dictionary? {'book' in diction}")
    print(f"Is the value 111 in the dictionary? {111 in values}")
    print(f"Is the key \'Excalibur\' in the dictionary? {'Excalibur' in diction}")
    print(f"Is the value 127 in the dictionary? {127 in values}")

**Reasoning behind my code:**

- I hard-coded ``fhand`` to only open ``words.txt`` for this assignment.
- ``diction`` is initialized as an empty dictionary.
- ``valueCount`` is initialized with ``1`` and it represents the first value for the first key in the dictionary.
- The first ``for`` loop is to read the file, line by line.
- The second ``for`` loop is tasked with splitting the line into words and looking at each of them, individually.
- ``if`` the word is already in ``diction``, the program skips to the next iteration.
- Else, ``valueCount`` will be assigned to the key ``word`` (in that particular iteration) and stored in ``diction``.
- ``values`` is created to help with checking to see if a particular value is located in ``diction``.
- As it is easier to locate a key in ``diction``, we'll only need to utilize the ``in`` operator.
- The ``print`` lines are self-explanatory.

.. note:: 

    The dictionary will only store unique keys and will disregard duplicates. So the following code is not necessary:
    ::

        if word in diction:
                continue

    This is a personal design choice so that every time ``valueCount`` is assigned as a value to a particular key in ``diction``, it will keep count of how many unique keys there are within the dictionary by skipping iterations that contain duplicate ``word``'s.

    With ``valueCount += 1`` only running when a unique key is detected, the count comes out to be ``126`` total. If I don't design the code to work in this way, the count will be in the 200's.

|

----

Exercise 9.2
------------

**Prompt:** Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

**Expected output:**

Sample Line:

.. code-block:: text

    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:

.. code-block:: text

    python dow.py
    Enter a file name: mbox-short.txt
    {'Fri': 20, 'Thu': 6, 'Sat': 1}

**My output:**
::

    $ python temporaryFile.py 
    Enter a file name: mbox-short.txt
    {'Sat': 1, 'Fri': 20, 'Thu': 6}

**My code:**
::

    fname = input("Enter a file name: ")

    if len(fname) < 1:
        fname = "mbox-short.txt"

    fhand = open(fname)
    diction = dict()

    for line in fhand:

        if not line.startswith('From '):
            continue

        line = line.rstrip().split()
        diction[line[2]] = diction.get(line[2], 0) + 1

    print(diction)

**Reasoning behind my code:**

- ``fname`` asks and stores the file name.
- ``fhand`` opens the file based on the file name.
- ``diction`` is initialized as an empty dictionary.
- The ``for`` loop is used to read the file, line by line.
- ``if`` the line does ``not`` ``startswith()`` **'From '** (notice the whitespace after the word), the loop will skip to the next iteration.
- Else, the line will be stripped of newline character(s) by invoking ``rstrip()`` and then splits into individual words by invoking ``split()``.
- ``line[2]`` refers to the index pointing to the **date** of the mail.
- ``diction[line[2]]`` refers to the **key** that are to be stored in ``diction``.
- ``diction.get(line[2], 0)`` is saying that:
    
  + If the **key** is not already available within the dictionary, it will be created and stored and be assigned a *default* **value** of ``0``.
  + Else, if the **key** is available, the default value will be *disregarded*.

.. note:: 

    Notice these lines of code:
    ::
        
        if len(fname) < 1:
        fname = "mbox-short.txt"

    This is not a requirement for the assignment. It's just a bit of code designed to help me with having to enter the filename every time I test the code.

|

----

Exercise 9.3
------------

**Prompt:** Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

**Expected output:**

.. code-block:: text

    Enter file name: mbox-short.txt
    {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
    'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
    'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
    'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
    'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
    'ray@media.berkeley.edu': 1}

**My output:**

.. code-block:: text

    Enter a file name: mbox-short.txt
    {'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3, 'zqian@umich.edu': 4, 
    'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5, 'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1, 
    'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1, 'david.horwitz@uct.ac.za': 4, 
    'ray@media.berkeley.edu': 1}

**My code:**
::

    fname = input("Enter a file name: ")

    if len(fname) < 1:
        fname = "mbox-short.txt"

    fhand = open(fname)
    diction = dict()

    for line in fhand:

        if not line.startswith('From '):
            continue

        line = line.rstrip().split()
        diction[line[1]] = diction.get(line[1], 0) + 1

    print(diction)

**Reasoning behind my code:**

- Pretty much the same code as **Exercise 9.2**.
- Only change is:
  ::

    diction[line[1]] = diction.get(line[1], 0) + 1

|

----

Exercise 9.4
------------

**Prompt:** Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

**Expected outputs:**

.. code-block:: text

    Enter a file name: mbox-short.txt
    cwen@iupui.edu 5

.. code-block:: text

    Enter a file name: mbox.txt
    zqian@umich.edu 195

**My outputs:**

.. code-block:: text

    Enter a file name: mbox-short.txt
    cwen@iupui.edu 5

.. code-block:: text

    Enter a file name: mbox.txt
    zqian@umich.edu 195

**My code:**
::

    fname = input("Enter a file name: ")

    if len(fname) < 1:
        fname = "mbox-short.txt"

    fhand = open(fname)
    diction = dict()

    for line in fhand:

        if not line.startswith('From '):
            continue

        line = line.rstrip().split()
        diction[line[1]] = diction.get(line[1], 0) + 1

    maxKey = None
    maxVal = 0
    for key,val in diction.items():
        if val > maxVal:
            maxVal = val
            maxKey = key

    print(maxKey, maxVal)

**Reasoning behind my code:**

- Majority of the code is borrowed from exercise 9.3. I'll only be going over the new code for this part.
- ``maxKey`` is initialized with ``None`` and will be used to store the max **key** of ``diction``.
- ``maxVal`` is initialized with ``0`` and will be used to store the max **value** of ``diction``.
- Utilizing ``diction.item()``, I can run a ``for`` loop through ``diction`` while checking for both the **key** and **value** in each iteration.
- ``if`` **val** is bigger than the current value held in ``maxVal``, **val** will replace the current value and , **key**, replacing the value held in ``maxKey``.
- Once complete, the program prints both the corresponding key and value.

|

----

Exercise 9.5
------------

**Prompt:** Write a program where it records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

**Expected output:**

.. code-block:: text

    python schoolcount.py
    Enter a file name: mbox-short.txt
    {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
    'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

**My output:**
::

    $ python temporaryFile.py 
    Enter a file name: mbox-short.txt
    {'uct.ac.za': 6, 'media.berkeley.edu': 4, 'umich.edu': 7, 
    'iupui.edu': 8, 'caret.cam.ac.uk': 1, 'gmail.com': 1}

**My code:**
::

    fname = input("Enter a file name: ")

    if len(fname) < 1:
        fname = "mbox-short.txt"

    fhand = open(fname)
    diction = dict()

    for line in fhand:

        if not line.startswith('From '):
            continue

        line = line.translate(line.maketrans('@', ' '))
        line = line.rstrip().split()
        diction[line[2]] = diction.get(line[2], 0) + 1

    print(diction)

**Reasoning behind my code:**

- The code is, again, borrowed from exercise 9.3 so I'll be going over what was changed and/or added for this assignment.
- Before stripping whitespace characters and splitting ``line``, I made use of ``translate`` and ``maketrans`` methods to break the domain names from the email addresses, as per requested by the **prompt**.
- With the two methods working together, I can manipulate which character I can make edits to. And since all email addresses have the ``@`` character in common, I went ahead and replaced it with an *empty space* character. This is done so that when I invoke the ``split`` method, it will break the *username part* from the *domain name part*.
- The outcome resulted in an extra *key-value pair*, so what was ``line[1]`` before is now changed to ``line[2]``. This will point to the correct item, in the dictionary, that we want to ``print`` out.