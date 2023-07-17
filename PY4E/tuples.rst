Tuples
======

|

For this section, I'll be going over exercises 10.1 to 10.3.

.. contents:: Contents
    :local:

.. note::

    **Somethings to be familiar with:**

    **Tuples are immutable**. They are also *comparable* and *hashable* so we can sort lists of them and use tuples as key values in Python dictionaries.

    Syntactically, a tuple is a comma-separated list of values:
    ::

        >>> t = 'a', 'b', 'c', 'd', 'e'

    Although it is not necessary, it is common to enclose tuples in parentheses to help us quickly identify tuples when we look at Python code:
    ::

        >>> t = ('a', 'b', 'c', 'd', 'e')

    To create a tuple with a single element, you have to include the final comma:
    ::
        
        >>> t1 = ('a',)
        >>> type(t1)
        <type 'tuple'>

    Without the comma Python treats ``('a')`` as an expression with a string in parentheses that evaluates to a string:
    ::

        >>> t2 = ('a')
        >>> type(t2)
        <type 'str'>

    Another way to construct a tuple is the built-in function tuple. With no argument, it creates an empty tuple:
    ::

        >>> t = tuple()
        >>> print(t)
        ()

    You can't modify the elements of a tuple, but you can replace one tuple with another:
    ::

        >>> t = ('a', 'b', 'c', 'd', 'e')
        >>> t = ('A',) + t[1:]
        >>> print(t)
        ('A', 'b', 'c', 'd', 'e')

    The comparison operators work with tuples and other sequences. Python starts by comparing the first element from each sequence. If they are equal, it goes on to the next element, and so on, until it finds elements that differ. Subsequent elements are not considered (even if they are really big).
    ::

        >>> (0, 1, 2) < (0, 3, 4)
        True
        >>> (0, 1, 2000000) < (0, 3, 4)
        True

    One of the unique syntactic features of the Python language is the ability to have a tuple on the left side and a sequence on the right side of an assignment statement. This allows you to assign more than one variable at a time to the given sequence.

    In this example we have a two-element list (which is a sequence) and assign the first and second elements of the sequence to the variables x and y in a single statement.
    ::

        >>> m = [ 'have', 'fun' ]
        >>> x, y = m
        >>> x
        'have'
        >>> y
        'fun'

    A particularly clever application of tuple assignment allows us to **swap** the values of two variables in a single statement:
    ::

        >>> a, b = b, a
    
    Both sides of this statement are tuples, but the left side is a tuple of variables; the right side is a tuple of expressions. Each value on the right side is assigned to its respective variable on the left side. All the expressions on the right side are evaluated before any of the assignments. The number of variables on the left and the number of values on the right **must be the same**.

|

----

Exercise 10.1
-------------

**Prompt:** Revise a previous program as follows:

Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a *dictionary*. After all the data has been read, print the person with the most commits by creating a *list of (count, email) tuples* from the dictionary. Then sort the list in *reverse order* and print out the person who has the most commits.

**Expected outputs:**

.. code-block:: text

    Sample Line:
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

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
        fname = 'mbox-short.txt'

    fhand = open(fname)
    diction = dict()

    for line in fhand:
        if not line.startswith('From '):
            continue

        line = line.rstrip().split()
        diction[line[1]] = diction.get(line[1], 0) + 1

    lista = [ (count, email) for email, count in diction.items() ]

    lista.sort(reverse=True)

    for count, email in lista[:1]:
        print(email, count)

**Reasoning behind my code:**

- ``fname`` asks and stores file name.
- ``if`` no input is entered, initialize ``mbox-short.txt`` as the file name.
- ``fhand`` opens the file.
- ``diction`` is initialized as an empty dictionary.
- The 1st ``for`` loop reads the file, line by line.
- ``if`` the line doesn't start with **'From '**, the line is skipped.
- The line is then stripped of newline character(s) and split into words.
- The words important to the assignment will be stored in ``diction`` as **keys** and the *count* of the word's occurrence will be stored as **values**.
- Using **list comprehension**, the program stores ``(count, email)`` tuples as the *key-value pair* traverses across the ``diction``.
  
.. note:: 

    The list comprehension line for this assignment
    ::

        lista = [ (count, email) for email, count in diction.items() ]

    are compressed version of
    ::

        lista = []
        for email, count in diction.items():
            lista.append( (count, email) )

    What we learn in this lesson is that when we passes two variables in the ``for`` loop, we're pretty much using tuples to loop through a sequence.

    For ``diction.items()``, the ``items()`` function returns a list of tuples.

    Also notice that the *key-value pairs* are *switched* when appending to ``lista``

- Once all items are added to ``lista``, the list is *sorted* in descending order by including the argument: ``reverse=True``.
- The ``for`` loop at the end traverses the list of tuples, ``lista``, and print out the first item. In order to do this, a *slice operator* is added to the ``for`` loop. ``[:1]`` will start at the beginning of the list and end after the first item.

|

----

Exercise 10.2
-------------

**Prompt:** Write a program that counts the distribution of the **hour** of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

**Expected output:**
::

    python timeofday.py
    Enter a file name: mbox-short.txt
    04 3
    06 1
    07 1
    09 2
    10 3
    11 6
    14 1
    15 2
    16 4
    17 2
    18 1
    19 1

**My output:**
::

    $ python temporaryFile.py 
    Enter a file name: mbox-short.txt
    04 3
    06 1
    07 1
    09 2
    10 3
    11 6
    14 1
    15 2
    16 4
    17 2
    18 1
    19 1


**My code:**
::

    fname = input("Enter a file name: ")

    if len(fname) < 1:
        fname = 'mbox-short.txt'

    fhand = open(fname)
    diction = dict()

    for line in fhand:
        if not line.startswith('From '):
            continue

        line = line.translate(str.maketrans(':', ' '))
        line = line.rstrip().split()
        
        diction[line[5]] = diction.get(line[5], 0) + 1

    lista = [ (hour, msgCount) for hour, msgCount in diction.items() ]

    lista.sort()

    for hour, msgCount in lista:
        print(hour, msgCount)

**Reasoning behind my code:**

- Most of the code is borrowed from exercise 10.1. I'll be going over what was changed for this assignment.
- After finding the line of interest, the program replaces all ``:``'s with whitespace characters (in this case, just blank spaces). Doing this will break the time data into separate elements once the line splits (one for each hour, minute and second).
- Splitting the line causes ``line`` to have more elements than usual. Focusing on the element of interest (hour), I used ``line[5]`` when adding to ``diction``. Doing this will store *hour* as **key** and its number of occurrences (in this case, it represents the message count) within the file as **value**.
- In order to sort the hours in ascending order, I first need to convert the items in ``diction`` to a list of tuples. I can make this relatively quickly by utilizing *list comprehension*. Refer to exercise 10.1 if you'd like an explanation on this technique.
- Once the list is sorted, I constructed a ``for`` loop to output the content of the list.

|

----

Exercise 10.3
-------------

**Prompt:** Write a program that reads a file and prints the letters in *decreasing order* of frequency. Your program should convert all the input to *lower case* and *only count the letters a-z*. Your program *should not count spaces, digits, punctuation, or anything other than the letters a-z*. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

**Expected output:** None available.

**My outputs:**
::

    $ python temporaryFile.py 
    Enter a file name: iCantType.txt
    File not found: iCantType.txt

::

    $ python temporaryFile.py 
    Enter a file name: mbox-short.txt

    Letter  Count   Percentage
    a       5223    8.926%    
    b       1134    1.938%    
    c       3088    5.277%
    d       2004    3.425%
    e       5436    9.29%
    f       1257    2.148%
    g       1027    1.755%
    h       1392    2.379%
    i       4494    7.68%
    j       959     1.639%
    k       1167    1.994%
    l       1832    3.131%
    m       2436    4.163%
    n       2575    4.401%
    o       4174    7.133%
    p       2497    4.267%
    q       57      0.097%
    r       4064    6.945%
    s       3738    6.388%
    t       4050    6.922%
    u       3123    5.337%
    v       997     1.704%
    w       586     1.001%
    x       482     0.824%
    y       643     1.099%
    z       78      0.133%

::

    $ python temporaryFile.py 
    Enter a file name: mbox.txt

    Letter  Count   Percentage
    a       355337  8.44%
    b       85569   2.033%
    c       238115  5.656%
    d       148380  3.525%
    e       404033  9.597%
    f       74252   1.764%
    g       68698   1.632%
    h       104017  2.471%
    i       316771  7.524%
    j       51155   1.215%
    k       87160   2.07%
    l       144889  3.442%
    m       178115  4.231%
    n       190902  4.535%
    o       309157  7.343%
    p       168447  4.001%
    q       4087    0.097%
    r       281859  6.695%
    s       276247  6.562%
    t       302616  7.188%
    u       212537  5.048%
    v       74757   1.776%
    w       46893   1.114%
    x       34011   0.808%
    y       48157   1.144%
    z       3795    0.09%

**My code:**
::

    # need this library to invoke punctuation
    import string

    # defining function
    # hiding complexity inside function so I can just call it later in the main code
    def displayPercent(count, total):
        return round((float(count)/total)*100, 3)

    # main code
    # user input request
    fname = input("Enter a file name: ")

    # auto input for testing/debugging
    if len(fname) < 1:
        fname = 'mbox-short.txt'

    # try/except clause
    try:
        fhand = open(fname)

    except:
        print("File not found:", fname)
        exit()

    # empty dictionary
    diction = dict()

    # reading file, line by line
    for line in fhand:
        # deleting punctuations + digits + whitespace characters and make the rest lowercase
        line = line.translate(str.maketrans('', '', string.punctuation+'0123456789 \t\r\n')).lower()

        # read through each letter and store it in the dictionary + its number of occurrences
        for letter in line:
            diction[letter] = diction.get(letter, 0) + 1

    # list comprehension shorthand to append items from dictionary to list
    lista = [ (letter, count) for letter, count in diction.items() ]

    # counting total to use with 'displayPercent' function
    total = 0
    for num in diction.values():
        total += num 

    # output in style :)
    lista.sort()
    print('\nLetter\tCount\tPercentage')
    for letter, count in lista:
        print(f'{letter}\t{count}\t{displayPercent(count, total)}%')

**Reasoning behind my code:**

- I took the time to comment in the code this time.
- I created ``displayPercent()`` function as a bonus step to make the output similar to that of the tables in https://wikipedia.org/wiki/Letter_frequencies. 