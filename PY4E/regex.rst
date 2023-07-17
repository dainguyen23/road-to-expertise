Regular Expressions
===================

|

For this section, I'll be going over exercises 11.1 to 11.4.

.. contents:: Contents
    :local:

.. note::

    **Somethings to be familiar with:**

    The module ``re`` must be imported into your program before you can use regular expression.

    **Special characters and character sequences to reference:**
    
    .. list-table:: 
        :widths: 3 10
        :header-rows: 1
        
        * - Regex
          - Description
        * - ``^``
          - Matches the beginning of the line.
        * - ``$``
          - Matches the end of the line.
        * - ``.``
          - Matches any character (a wildcard).
        * - ``\s``
          - Matches a whitespace character.
        * - ``\S``
          - Matches a non-whitespace character (opposite of ``\s``).
        * - ``*``
          - Applies to the immediately preceding character(s) and indicates to match **zero or more** times.
        * - ``*?``
          - Applies to the immediately preceding character(s) and indicates to match **zero or more** times in **“non-greedy mode”**.
        * - ``+``
          - Applies to the immediately preceding character(s) and indicates to match **one or more** times.
        * - ``+?``
          - Applies to the immediately preceding character(s) and indicates to match **one or more** times in **“non-greedy mode”**.      
        * - ``?``
          - Applies to the immediately preceding character(s) and indicates to match **zero or one** time.
        * - ``??``
          - Applies to the immediately preceding character(s) and indicates to match **zero or one** time in **“non-greedy mode”**.
        * - ``[aeiou]``
          - Matches a single character as long as that character is in the specified set. In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.
        * - ``[a-z0-9]``
          - You can specify ranges of characters using the minus sign. This example is a single character that must be a lowercase letter or a digit.
        * - ``[^A-Za-z]``
          - When the first character in the set notation is a caret, it inverts the logic. This example matches a single character that is anything other than an uppercase or lowercase letter.
        * - ``( )``
          - When parentheses are added to a regular expression, they are ignored for the purpose of matching, but allow you to extract a particular subset of the matched string rather than the whole string when using ``findall()``.
        * - ``\b``
          - Matches the empty string, but only at the start or end of a word.
        * - ``\B``
          - Matches the empty string, but not at the start or end of a word.
        * - ``\d``
          - Matches any decimal digit; equivalent to the set [0-9].
        * - ``\D``
          - Matches any non-digit character; equivalent to the set [^0-9].
        * - ``[^XYZ]``
          - Matches a single character not in the listed set  

    Bonus for Unix/Linux users: there is a command-line program built into Unix called ``grep`` (Generalized Regular Expression Parser) that does pretty much the same as the ``search()`` method. So if you have a Macintosh or Linux system, you can try the following commands in your command-line window.
    ::

        $ grep '^From:' mbox-short.txt
        From: stephen.marquard@uct.ac.za
        From: louis@media.berkeley.edu
        From: zqian@umich.edu
        From: rjlowe@iupui.edu

|

----

Exercise 11.1
-------------

**Prompt:**  Write a simple program to simulate the operation of the ``grep`` command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression.

**Expected outputs:**
::

    $ python grep.py
    Enter a regular expression: ^Author
    mbox.txt had 1798 lines that matched ^Author

::

    $ python grep.py
    Enter a regular expression: ^X-
    mbox.txt had 14368 lines that matched ^X-

::

    $ python grep.py
    Enter a regular expression: java$
    mbox.txt had 4175 lines that matched java$

**My outputs:**
::

    $ python temporaryFile.py 
    Enter a regular expression: ^Author 
    mbox.txt had 1798 lines that matched ^Author

::

    $ python temporaryFile.py 
    Enter a regular expression: ^X-
    mbox.txt had 14368 lines that matched ^X-

::

    $ python temporaryFile.py 
    Enter a regular expression: java$
    mbox.txt had 4218 lines that matched java$

**My code:**
::

    import re

    regex = input("Enter a regular expression: ")
    fname = 'mbox.txt'
    fhand = open(fname)
    count = 0

    for line in fhand:
        line = line.rstrip()
        if re.search(regex, line):
            count += 1

    print(f"{fname} had {count} lines that matched {regex}")

**Reasoning behind my code:**

- ``regex`` asks and stores user input of regular expression.
- ``fname`` is initialized with file name, for testing.
- ``fhand`` opens the file, for testing.
- ``count`` is initialized with ``0``.
- The ``for`` loop reads through the file, line by line.
- Each line will be stripped of *newline characters* via ``rstrip()``.
- ``if`` the regular expression has a match in a ``line``, ``count`` increases by one.
- Once done, the program prints out the total number of lines.

.. note:: 

    There seems to be a discrepancy between **my outputs** and the **expected outputs**, particularly the third output. I'm not too sure why the counts are mismatched (``4175`` vs ``4218``). I've searched through the discussion forum on the site to see if someone also noticed this. I couldn't find anyone that did. It could either be that the files used have different contents even if they're sharing the same name or that the professor has programmed the code a different way. It's hard to say when I don't have access to his code. But safe to say that my code works.. because.. it uh.. at least ran! xD 

|

----

Exercise 11.2
-------------

**Prompt:** Write a program to look for lines of the form:
::

    New Revision: 39772

Extract the number from each of the lines using a regular expression and the ``findall()`` method. Compute the average of the numbers and print out the average as an integer.

**Expected outputs:**
::
    
    Enter file:mbox.txt
    38549

::

    Enter file:mbox-short.txt
    39756

**My outputs:**
::

    Enter file: mbox.txt
    38549

::

    Enter file: mbox-short.txt
    39756

**My code:**
::

    import re

    fname = input("Enter file: ")

    if len(fname) < 1:
        fname = 'mbox-short.txt'

    try:
        fhand = open(fname)

    except:
        print("Cannot find file:", fname)
        exit()

    count = 0
    total = 0
    for line in fhand:
        line = line.rstrip()

        regex = re.findall("^N.*: ([0-9]+)$", line)
        if len(regex) > 0:
            total += int(regex[0])
            count += 1

    print(int(total/count))

**Reasoning behind my code:**

- A couple lines of code are added for testing/debugging purposes and should be straightforward, if you've gone through past topics, so I'll go over topics regarding regex.
- To search strings using regular expression, I had to ``import`` the ``re`` module.
- ``findall()`` method returns a list so I created ``regex`` to store it.
- In this assignment, we're trying to find lines that matched the form of ``New revision: <some number>``. So I came up with ``"^N.*: ([0-9]+)$"``.
- ``^N.*:`` tells the program to search for characters between the beginning of the line and up to the first colon character. This covered the ``New Revision:`` part.
- Then anything inside the parentheses, we extract. And we only want only integers, hence ``[0-9]+``.
- The special character ``$`` marks the end of the line. Meaning, we will have extracted all the digits by the time the program matches this character.

|

----

Exercise 11.3
-------------

**Prompt:** Finding Numbers in a Haystack.

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers. 

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment. 

- Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt
- Actual data: http://py4e-data.dr-chuck.net/regex_sum_1784988.txt

**Note:** Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

The basic outline of this problem is to read the file, look for integers using the ``re.findall()``, looking for a regular expression of ``'[0-9]+'`` and then converting the extracted strings to integers and summing up the integers. 

**Expected outputs:** For the sample text below:
::

    Why should you learn to write programs? 7746
    12 1929 8827
    Writing programs (or programming) is a very creative 
    7 and rewarding activity.  You can write programs for 
    many reasons, ranging from making your living to solving
    8837 a difficult data analysis problem to having fun to helping 128
    someone else solve a problem.  This book assumes that 
    everyone needs to know how to program ...

The sum is **27486**. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).

.. note:: 
    
    What you're looking to match in this assignment are:

    - **sample-data.txt**: There are **90** values with a **sum = 445833**
    - **actual-data.txt**: There are **99** values and the **sum ends with 789**

**My outputs:**
::

    $ python temporaryFile.py 
    Enter file: sample-data.txt
    There are 90 values with a sum of 445833

::

    $ python temporaryFile.py 
    Enter file: actual-data.txt
    There are 99 values with a sum of 492789

**My code:**
::

    import re

    fname = input("Enter file: ")

    if len(fname) < 1:
        fname = 'sample-data.txt'

    try:
        fhand = open(fname)

    except:
        print("Cannot find file:", fname)
        exit()

    count = 0
    total = 0
    for line in fhand:
        line = line.rstrip()

        regex = re.findall("[0-9]+", line)
        if len(regex) > 0:
            
            for num in regex:
                total += int(num)
                count += 1

    print(f"There are {count} values with a sum of {total}")

**Reasoning behind my code:**

- The program asks for a file and checks if it's valid before opening it.
- ``count`` carries the count for number of values.
- ``total`` carries the sum of values.
- Looping through lines of the file, I'm using regex to find all occurrences of integers, wherever they may appear in the file. This is done by feeding ``findall()`` the expression of ``"[0-9]+"``. This is to say we're trying to find occurrences of **one or more digits** in each line.
- Once done, the program prints out the number of values encountered and the summation of those values.

|

----

Exercise 11.4
-------------

**Prompt:** Bonus problem!

There are a number of different ways to approach this problem. While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this program using list comprehension: 
::

    Python 2
    import re
    print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

    Python 3:
    import re
    print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )

**Expected output:** None available.

**My output:**
::

    $ python temporaryFile.py 
    492789

**My code:**
::

    import re
    print(sum([ int(num) for num in re.findall("[0-9]+", open('actual-data.txt').read()) ]))

**Reasoning behind my code:**

- This assignment combines what we know about the ``read()`` method and **list comprehension** and created an unnecessarily compressed shorthand solution to exercise 10.3. It shows the power of the Python language. But realistically, it causes more confusion than it helps.
- The single line of ``print`` code combined all the steps, from reading the file to searching using regex and finally printing out the sum of integers found. All in one fell swoop!