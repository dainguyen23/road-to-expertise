Lists
=====

|

For this section, I'll be going over exercises 8.1, 8.4 to 8.6.

.. contents:: Contents
    :local:

.. note::

    **Somethings to be familiar with:**

    Like a string, a **list** is a sequence of values. However, **lists are mutable**. In a string, the values are *characters*; in a list, they can be *any type*. The values in list are called **elements** or sometimes **items**.

    There are several ways to create a new list; the simplest is to enclose the elements in square brackets (``[`` and ``]``):
    ::

        [10, 20, 30, 40]
        ['crunchy frog', 'ram bladder', 'lark vomit']

    If an index has a negative value, it counts backward from the end of the list.

|

----

Exercise 8.1
------------

**Prompt:** Write a function called ``chop`` that takes a list and **modifies it**, *removing the first and last elements*, and **returns** ``None``. Then write a function called ``middle`` that takes a list and **returns a new list** that contains all but the *first* and *last* elements.

**Expected output:** None available.

**My output:**
::

    Unmodified lista: [1, 2, 3, 4, 5]
    Modified lista: [2, 3, 4]
    listb: [2, 3, 4]
    Are lista and listb the same object? False

**My code:**
::

    # defining functions
    def chop(alist):
        del alist[0], alist[-1]
        return None

    def middle(alist):
        blist = alist[1:-1]
        return blist

    # main code
    lista = [1, 2, 3, 4, 5]
    print("Unmodified lista:", lista)

    listb = middle(lista)
    chop(lista)

    print("Modified lista:", lista)
    print("listb:", listb)
    print("Are lista and listb the same object?", lista is listb)

**Reasoning behind my code:**

- The purpose of this assignment is to show the difference between modifying a referenced list and creating a new list from the referenced list.
- ``chop`` modifies ``lista`` by deleting, ``del``, the first, ``alist[0]``, and last, ``alist[-1]`` elements from the list. The ``[-1]`` index starts at the end of the list, so it represents the last element. Notice this is a void function and returns ``None``.
- ``middle`` takes ``lista`` as reference and creates a new list after omitting the first and last elements from the list through use of the **slice operator**, ``alist[1:-1]``. The new list is then returned.
- The last ``print`` line shows that ``lista`` and ``listb`` are not pointing to the same object even though each variable contains the same values. ``is`` is used to determine this.

|

----

Exercise 8.4
------------

**Prompt:** Find all unique words in a file.

Shakespeare used over 20,000 words in his works. But how would you determine that? How would you produce the list of all the words that Shakespeare used? Would you download all his work, read it and track all unique words by hand?

Let's use Python to achieve that instead. List all unique words, sorted in alphabetical order, that are stored in a file ``romeo.txt`` containing a subset of Shakespeare's work.

To get started, download a copy of the file at https://www.py4e.com/code3/romeo.txt. Create a list of unique words, which will contain the final result. Write a program to open the file ``romeo.txt`` and read it line by line. For each line, split the line into a list of words using the ``split`` function. For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.

**Expected output:**

.. code-block:: text

    Enter file: romeo.txt
    ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
    'and', 'breaks', 'east', 'envious', 'fair', 'grief',
    'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
    'sun', 'the', 'through', 'what', 'window',
    'with', 'yonder']

**My output:**

.. code-block:: text

    Enter file: romeo.txt
    ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
    'and', 'breaks', 'east', 'envious', 'fair', 'grief',
    'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
    'sun', 'the', 'through', 'what', 'window',
    'with', 'yonder']

**My code:**
::

    fname = input("Enter file: ")
    fhand = open(fname)
    wordL = []

    for line in fhand:
        tempL = line.split()
        
        for word in tempL:
            if word not in wordL:
                wordL.append(word)

    print(sorted(wordL))

**Reasoning behind my code:**

- ``fname`` asks and stores the file name.
- ``fhand`` opens the file.
- ``wordL`` is initialized as an empty list.
- The first ``for`` loop reads the file, line by line.
- Each line is ``split`` between words and stored in ``tempL``.
- The second ``for`` loop reads through ``tempL``, word for word.
- ``if`` the word is ``not`` already ``in`` ``wordL``, then the program would ``append`` it to the list.
- Once unique words are added to ``wordL``, the program will ``print`` the list in ``sorted`` format.

|

----

Exercise 8.5
------------

**Prompt:** Minimalist Email Client.

MBOX (mail box) is a popular file format to store and share a collection of emails. This was used by early email servers and desktop apps. Without getting into too many details, MBOX is a text file, which stores emails consecutively. Emails are separated by a special line which starts with ``From`` (notice the space). Importantly, lines starting with ``From:`` (notice the colon) describes the email itself and does not act as a separator. Imagine you wrote a minimalist email app, that lists the email of the senders in the user's Inbox and counts the number of emails.

Write a program to read through the mail box data and when you find the line that starts with “From”, you will split the line into words using the ``split`` function. **We are interested in who sent the message, which is the second word on the From line.**

.. code-block:: text

    From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end.

**Expected output:** This is a good sample output with a few lines removed:

.. code-block:: text

    python fromcount.py
    Enter a file name: mbox-short.txt
    stephen.marquard@uct.ac.za
    louis@media.berkeley.edu
    zqian@umich.edu

    [...some output removed...]

    ray@media.berkeley.edu
    cwen@iupui.edu
    cwen@iupui.edu
    cwen@iupui.edu
    There were 27 lines in the file with From as the first word

**My output:**

.. code-block:: text

    $ python temporaryFile.py 
    Enter a file name: mbox-short.txt
    stephen.marquard@uct.ac.za
    louis@media.berkeley.edu  
    zqian@umich.edu
    rjlowe@iupui.edu
    zqian@umich.edu
    rjlowe@iupui.edu
    cwen@iupui.edu
    cwen@iupui.edu
    gsilver@umich.edu
    gsilver@umich.edu
    zqian@umich.edu
    gsilver@umich.edu
    wagnermr@iupui.edu
    zqian@umich.edu
    antranig@caret.cam.ac.uk
    gopal.ramasammycook@gmail.com
    david.horwitz@uct.ac.za
    david.horwitz@uct.ac.za
    david.horwitz@uct.ac.za
    david.horwitz@uct.ac.za
    stephen.marquard@uct.ac.za
    louis@media.berkeley.edu
    louis@media.berkeley.edu
    ray@media.berkeley.edu
    cwen@iupui.edu
    cwen@iupui.edu
    cwen@iupui.edu
    There were 27 lines in the file with From as the first word

**My code:**
::

    fname = input("Enter a file name: ")
    fhand = open(fname)
    count = 0

    for line in fhand:
        if not line.startswith("From "):
            continue

        line = line.split()
        print(line[1])
        count += 1

    print(f"There were {count} lines in the file with From as the first word")

**Reasoning behind my code:**

- ``fname`` asks and stores the file name.
- ``fhand`` opens the file.
- ``count`` is initialized with ``0`` at first.
- The ``for`` loop reads the file, line by line, and skips lines that does not start with **From**.
- For the lines that do start with **From**, the line will split and store in ``line``, temporarily, and the second element from ``line`` will be printed.
- ``count`` is then updated and the for loop goes to the next iteration.
- Once out of the loop, the program prints the total count of lines that start with From, using ``count``.


|

----

Exercise 8.6
------------

**Prompt:** Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the ``max()`` and ``min()`` functions to compute the maximum and minimum numbers after the loop completes.

**Expected output:**
::

    Enter a number: 6
    Enter a number: 2
    Enter a number: 9
    Enter a number: 3
    Enter a number: 5
    Enter a number: done
    Maximum: 9.0
    Minimum: 2.0

**My output:**
::

    Enter a number: 6
    Enter a number: 2
    Enter a number: 9
    Enter a number: 3
    Enter a number: 5
    Enter a number: done
    Maximum: 9.0
    Minimum: 2.0

**My code:**
::

    lista = []

    while True:
        num = input("Enter a number: ")

        if num == "done":
            break

        try:
            num = float(num)

        except:
            print("Please enter a numeric value!")
            continue

        lista.append(num)

    print(f"Maximum: {max(lista)}")
    print(f"Minimum: {min(lista)}")

**Reasoning behind my code:**

- ``lista`` is initialized as an empty list.
- The ``while`` loop is programmed to run indefinitely.
- ``num`` asks for and stores the user input.
- ``if`` ``num`` is storing the string ``done``, the code will ``break`` out of the loop.
- The ``try``/``except`` structure is designed to catch user inputs that are not numeric values and would output a hint before jumping into the next iteration.
- Other than that, any numeric values will be converted to ``float`` be added to ``lista`` via use of the ``append`` method. **Notice that since** ``append`` **doesn't** ``return`` **a value, we don't store** ``lista.append(num)`` **inside a variable.**
- Once out of the loop, the program prints the min and max number from the list through the use of ``min`` and ``max`` functions.