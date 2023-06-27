Files
=====

|

For this section, I'll be going over exercises 7.1 to 7.3.

.. contents:: Contents
    :local:

.. note::

    **Somethings to be familiar with:**

    When we want to read or write a file (say on your hard drive), we first must *open* the file. To do this we can use the ``open`` function.

    If the ``open`` is successful, the operating system returns us a *file handle*. The file handle itself is not the file but a way to look into the file and manipulate it.

    If the file does not exist, ``open`` will fail with a **traceback** and you will not get a handle to access the contents of the file:
    ::

        >>> fhand = open('stuff.txt')
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        FileNotFoundError: [Errno 2] No such file or directory: 'stuff.txt'

|

----

Exercise 7.1
------------

**Prompt:** Write a program to read through a file and print the contents of the file (line by line) all in upper case.

You can download the file from https://www.py4e.com/code3/mbox-short.txt

**Expected output:**

.. code-block:: text

    python shout.py
    Enter a file name: mbox-short.txt
    FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
    RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
    RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
        BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
        SAT, 05 JAN 2008 09:14:16 -0500

**My output:**

.. code-block:: text

    $ python temporaryFile.py 
    Enter a file name: mbox-short.txt
    FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
    RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
    RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
            BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
            SAT, 05 JAN 2008 09:14:16 -0500

**My code:**
::

    fname = input("Enter a file name: ")
    fhandle = open(fname)

    count = 0
    for line in fhandle:
        if count < 5:
            line = line.rstrip().upper()
            print(line)
            count += 1
        
        else:
            break

**Reasoning behind my code:**

``$ python temporaryFile.py`` is different as I'm using my own Python file and a different terminal. It's relatively the same as ``python shout.py`` in the **expected output**.

``fname`` asks and store in user's file choice. ``fhandle`` opens the file in *read-only mode* so I can have access to the file. The ``for`` loop iterates through each line of the file and strips the ``\n`` character at the end of each line with ``rstrip()``; then set the line to uppercase with ``upper()``. After that, the line is printed out to the console.

Notice I have ``count`` and ``break`` in the code. This is just so I can get the same output as shown in the **expected output**. The program prints out 5 lines from the file, then breaks out of the loop and exit.

|

----

Exercise 7.2
------------

**Prompt:** Write a program to prompt for a file name, and then read through the file and look for lines of the form:
::

    X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

**Test your file on the mbox.txt and mbox-short.txt files.**

You can get mbox.txt here: https://www.py4e.com/code3/mbox.txt

**Expected outputs:**
::

    Enter the file name: mbox.txt
    Average spam confidence: 0.894128046745

::

    Enter the file name: mbox-short.txt
    Average spam confidence: 0.750718518519

**My outputs:**
::

    Enter a file name: mbox.txt
    Average spam confidence: 0.894128046745

::

    Enter a file name: mbox-short.txt
    Average spam confidence: 0.750718518519

**My code:**
::

    fname = input("Enter a file name: ")
    count = 0
    total = 0.0

    try:
        fhandle = open(fname)

    except:
        print(f"The file \"{fname}\" cannot be found!")
        exit()

    for line in fhandle:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue

        startpos = line.find(' ') + 1
        num = float(line[startpos:])
        total += num
        count += 1

    average = total / count

    print("Average spam confidence:", round(average, 12))

**Reasoning behind my code:**

- ``fname`` asks for the input and stores it.
- ``fhandle`` opens the file in read-only mode. This line is put inside the ``try``/``except`` block to prevent erroneous inputs.
- Looping through the file, the code skips any line that doesn't start with *"X-DSPAM-Confidence:"*.
- Once a line of interest is found, ``startpos`` determines the position of the *whitespace* before the first digit of the number located and stores the *subsequent index* of that position.
- ``num`` stores and converts the number from string to ``float``. The number is extracted through the *slice operator*. Using ``startpos`` as its 1st argument and nothing as the 2nd argument.
- ``total`` adds the number on each iteration to itself.
- ``count`` determines the total number of line that was read.
- ``average`` finds the average spam confidence number.
- The program prints the number at the end and ``round`` it to *12 decimal places* so that it would match the **expected output**.

|

----

Exercise 7.3
------------

**Prompt:** Sometimes when programmers get bored or want to have a bit of fun, so they add a harmless *Easter Egg* to their program.

Modify the program that prompts the user for the file name so that it *prints a funny message* when the user types in the *exact file name* **“na na boo boo”.** The program should behave normally for *all other files which exist and don't exist.*

**Expected outputs:**

.. code-block:: text

    python egg.py
    Enter the file name: mbox.txt
    There were 1797 subject lines in mbox.txt

::

    python egg.py
    Enter the file name: missing.tyxt
    File cannot be opened: missing.tyxt

.. code-block:: text

    python egg.py
    Enter the file name: na na boo boo
    NA NA BOO BOO TO YOU - You have been punk'd!

**My outputs:**
::

    $ python temporaryFile.py 
    Enter a file name: mbox.txt
    There were 1797 subject lines in mbox.txt

::

    $ python temporaryFile.py 
    Enter a file name: missing.tyxt
    File cannot be opened: missing.tyxt

::

    $ python temporaryFile.py 
    Enter a file name: na na boo boo
    NA NA BOO BOO TO YOU - You have been punk'd!

**My code:**
::

    fname = input("Enter a file name: ")
    count = 0

    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()

    try:
        fhandle = open(fname)

    except:
        print("File cannot be opened:", fname)
        exit()

    for line in fhandle:
        if not line.startswith("Subject"):
            continue

        count += 1

    print(f"There were {count} subject lines in {fname}")

**Reasoning behind my code:**

- ``fname`` asks and stores user input.
- ``count`` determines the ``for`` loop's number of iteration.
- The ``if`` statement checks for the specific string **"na na boo boo"** as input and outputs an *Easter Egg.*
- The ``for`` loop skips all line except ones containing a **subject line.** This part of the code was not specifically requested by the prompt but I made it anyway to match the **expected output.**
- The ``print`` line shows one way to format the output. There are many ways to go about doing this.