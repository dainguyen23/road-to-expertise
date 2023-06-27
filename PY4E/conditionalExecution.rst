Conditional Execution
=====================

|


For this section, I'll be going over exercises 3.1 to 3.3.

.. contents:: Contents
    :local:

.. note:: 

    **Somethings to be familiar with:**

    **Boolean expression:** An expression that is either true or false. ``True`` and ``False`` are **keywords** used when working with such expressions.

    There are three **logical operators:** ``and``, ``or`` and ``not``.

    **Comparison operators:**
    ::

        x != y               # x is not equal to y
        x > y                # x is greater than y
        x < y                # x is less than y
        x >= y               # x is greater than or equal to y
        x <= y               # x is less than or equal to y
        x is y               # x is the same as y
        x is not y           # x is not the same as y

    ``try`` and ``except`` feature in Python as an “insurance policy” on a sequence of statements.

|

----

Exercise 3.1
-------------

**Prompt:** Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use **input** to read a string and **float()** to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

**Expected output:**
::

    Enter Hours: 45
    Enter Rate: 10.50
    Pay: 498.75

**My output:**
::  

    Enter Hours: 45
    Enter Rate: 10.50
    Pay: 498.75

**My code:**
::  

    hours = float(input("Enter Hours: "))
    
    rate = float(input("Enter Rate: "))

    if hours > 40:
        overtime = hours - 40
        pay = (rate * 40) + ((1.5 * rate) * overtime)
        print("Pay: " + str(pay))

    else:
        pay = hours * rate
        print("Pay: " + str(pay))

**Reasoning behind my code:**

``hours`` and ``rate`` take in the user inputs and convert them into *floating point variables*. These variables are then passed through subsequent **conditional statements (if/else)**.

If the hours worked surpasses **40**, overtime pay is accounted for within the **if clause**. For readability, I made ``overtime`` its own variable.

Any other conditions fall inside the **else clause**. In this case, the code will just calculate pay within standard working hours.

The code will output ``pay`` regardless of which clause is active. Notice that ``pay`` is converted back to *String type* inside the ``print`` statement. This is done so that ``pay`` can be concatenated and displayed properly.

|

----

Exercise 3.2
-------------

**Prompt:** Rewrite your pay program using ``try`` and ``except`` so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

**Expected outputs:**

.. code-block:: text

    Enter Hours: 20
    Enter Rate: nine
    Error, please enter numeric input

.. code-block:: text

    Enter Hours: forty
    Error, please enter numeric input

**My outputs:**

.. code-block:: text

    Enter Hours: 20
    Enter Rate: nine
    Error, please enter numeric input

.. code-block:: text

    Enter Hours: forty
    Error, please enter numeric input

**My code:**
::

    hours = input("Enter Hours: ")

    try:
        hours = float(hours)

    except:
        print("Error, please enter numeric input")
        quit()

    rate = input("Enter Rate: ")

    try:
        rate = float(rate)

    except:
        print("Error, please enter numeric input")
        quit()

    if hours > 40:
        overtime = hours - 40
        pay = (rate * 40) + ((1.5 * rate) * overtime)
        print("Pay: " + str(pay))

    else:
        pay = hours * rate
        print("Pay: " + str(pay))

**Reasoning behind my code:**

The code is a copy from the previous assignment, with some minor adjustments. With the guarantee that the user will always input a numeric value in the previous assignment, I combined steps of taking in the user input and explicitly converted it into a *float type* value before storing it in its own variable.

In this assignment, however, I made use of the **try/except structure** and add onto the existing code. Adding ``try`` and ``except`` when testing for both ``hours`` and ``rate`` resulted in the exact outputs as per requested by the prompt. The code will only accept numeric values and will flag the errors accordingly. The program stops running once an error is flagged by utilizing the ``quit()`` method.

|

----

Exercise 3.3
-------------

**Prompt:** Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
::

     Score   Grade
    >= 0.9     A
    >= 0.8     B
    >= 0.7     C
    >= 0.6     D
     < 0.6     F

**Expected outputs:**
::

    Enter score: 0.95
    A

::

    Enter score: perfect
    Bad score

::

    Enter score: 10.0
    Bad score

::

    Enter score: 0.75
    C

::

    Enter score: 0.5
    F

**My outputs:**
::

    Enter score: 0.95
    A

::

    Enter score: perfect
    Bad score

::

    Enter score: 10.0
    Bad score

::

    Enter score: 0.75
    C

::

    Enter score: 0.5
    F

**My code:**
::

    score = input("Enter score: ")

    try:
        score = float(score)

    except:
        print("Bad score")
        quit()

    if score >= 0.9 and score <= 1.0:
        print('A')

    elif score >= 0.8 and score <= 0.9:    
        print('B')

    elif score >= 0.7 and score <= 0.8:    
        print('C')

    elif score >= 0.6 and score <= 0.7:    
        print('D')

    elif score >= 0.0 and score < 0.6:    
        print('F')

    else:
        print("Bad score")    

**Reasoning behind my code:**

Building on top of previous exercises, I combined **try/except** and **if/else** clauses for this assignment. I also utilized the ``elif`` clause to create multiple checks within my conditional structure and the ``and`` keyword to set correct parameters in each conditional statement.

The code is very straightforward and should follow the grading structure requested by the prompt. 
