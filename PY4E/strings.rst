Strings
=======

|

For this section, I'll be going over exercises 6.1, 6.3 to 6.5.

.. contents:: Contents
    :local:

.. note::

    **Somethings to be familiar with:**

    **Strings are immutable**. Meaning you can't make changes to a string variable once initialized.

    ``[]`` is known as a **bracket operator**. You can access the characters one at a time with the bracket operator, like so: 
    ::

        >>> fruit = 'banana'
        >>> letter = fruit[1]    <----bracket operator at work!

    ``len`` is a built-in function that returns the number of characters in a string.

    A segment of a string is called a **slice**. Selecting a slice is similar to selecting a character:
    ::

        >>> s = 'Monty Python'
        >>> print(s[0:5])   <-----|
        Monty                     |---- slicing at work!
        >>> print(s[6:12])  <-----|
        Python

    ``in`` is a boolean operator that takes two strings and returns ``True`` if the first appears as a substring in the second.

|

----

Exercise 6.1
------------

**Prompt:** Write a ``while`` loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

**Expected output:** Not available so I'm going to assume the program will:

- Ask the user for a string input
- Loop through the string using a ``while`` loop
- Print the string in *reverse order*

**My outputs:**

.. code-block:: text

    Enter a string: STRING
    String in reverse:      G N I R T S 

.. code-block:: text

    Enter a string: fruit 
    String in reverse:      t i u r f

.. code-block:: text

    Enter a string: banana
    String in reverse:      a n a n a b

.. code-block:: text

    Enter a string: Hello World!
    String in reverse:      ! d l r o W   o l l e H

**My code:**
::

    word = input("Enter a string: ")

    index = 0
    element = len(word) - 1

    print("String in reverse:\t", end='')

    while index < len(word):
        print(word[element], end=' ')

        index += 1
        element -= 1

**Reasoning behind my code:**

I took some liberty with this assignment since there weren't any **expected output**.

``index`` is utilized as an end condition for the ``while`` loop. Each iteration of the loop increases the variable's count by one using ``index +=1``. The program ends when ``index`` obtain a value equals to the length, ``len()``, of the user's input, ``word``.

``element = len(word) - 1`` is the position of the last character within the string. By using this variable with the **bracket operator**, ``[]``, I can get the program to print the string in reverse, as per requested by the **prompt**. ``element`` will also shift one place towards the beginning of the string after each iteration using ``element -= 1``, until the program outputs each letter in ``word``.

.. note:: 

    Notice I also used the **end parameter**, ``end=' '``, in ``print``. Doing this achieves a single-line output. Without this parameter, the output would turn out this way, instead:
    
    .. code-block:: text

        Enter a string: banana
        String in reverse:
        a
        n
        a
        n
        a
        b

    ``\t`` is just there to put a *tab indent* to make the output a bit more clear!

|

----

Exercise 6.3
------------

The following program counts the number of times the letter “a” appears in a string:
::

    word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)

::

    3

This program demonstrates another pattern of computation called a **counter**. The variable ``count`` is initialized to 0 and then incremented each time an “a” is found. When the loop exits, ``count`` contains the result: the total number of a's.

**Prompt:** Encapsulate this code in a function named ``count``, and generalize it so that it *accepts the string and the letter as arguments*.

**Expected output:** None available but I'll use the example above as a template.

**My outputs:**

.. code-block:: text

    Enter a word: banana
    Enter a letter in the word: a
    Count of 3

.. code-block:: text

    Enter a word: Hello World!
    Enter a letter in the word: l
    Count of 3

.. code-block:: text

    Enter a word: Letter should be zero!
    Enter a letter in the word: a
    Count of 0

**My code:**
::

    # defining function
    def count(word, letter):
        count = 0
        for element in word:
            if element == letter:
                count += 1
        print("Count of", count)

    # main code    
    word = input("Enter a word: ")
    letter = input("Enter a letter in the word: ")

    count(word, letter)

**Reasoning behind my code:**

Using the example code given in this assignment, I moved it into its own function called ``count``, as per requested. I then made some slight changes for the sake of clarity. The loop used for the function is a ``for`` loop. Relatively similar to the ``while`` loop, ``element`` iterates through ``word`` until it reaches the last *character* in the string and stops looping. Everything else is pretty straightforward.

|

----

Exercise 6.4
------------

**Prompt:** There is a string method called ``count`` that is similar to the function in the previous exercise. Read the documentation of this method at:

https://docs.python.org/library/stdtypes.html#string-methods

Write an **invocation** that counts the number of times the letter **'a'** occurs in **“banana”**. A method call is called an *invocation*.

**Expected output:** None available but it should have the same results as exercise 6.3.

**My output:**

.. code-block:: text

    Enter a word: banana
    Enter a letter in the word: a
    Count of 3

**My code:**
::

    word = input("Enter a word: ")
    letter = input("Enter a letter in the word: ")

    print("Count of", word.count(letter))

**Reasoning behind my code:**

For this assignment, I got rid of the custom made count function and utilized the built-in ``count()`` method instead, as per requested. Making an invocation requires the programmer to append the method behind the variable, similar to the third line in **my code:** ``word.count(letter)``. The output is the same as in exercise 6.3. 

|

----

Exercise 6.5
------------

**Prompt:** Take the following Python code that stores a string:
::
    
    str = "X-DSPAM-Confidence:    0.8475"

Write code using ``find()`` and **string slicing** (see section 6.10) to extract the number at the end of the line below. *Convert the extracted value to a floating point number and print it out*.

**Expected output:**
::

    0.8475

**My output:**
::

    0.8475

**My code:**
::

    str = "X-DSPAM-Confidence:    0.8475"

    startpos = str.find('0')

    num = float(str[startpos:])

    print(num)

**Reasoning behind my code:**

``startpos`` is tasked with finding the start position of the number. It utilizes ``find()`` to locate the index of ``0`` and stores it.

``num`` converts the *sliced* variable ``str`` to a *floating point number*. The **slice operator** takes ``startpos`` as the *starting argument* and leaves the *2nd argument* **blank** to indicate it'll continue until the **end** of the string.

Lastly, the program prints the number to match the **expected output**.