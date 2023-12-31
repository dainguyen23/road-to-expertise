Functions
=========

|

.. contents:: Contents
    :local:

.. note::

    **Somethings to be familiar with:**

    The ``def`` keyword indicates the start of a function. Any code written inside the function will be stored for later use.

    **Algorithm** - A general process for solving a category of problems. 
    
    **Argument** - A value provided to a function when the function is called. This value is assigned to the corresponding parameter in the function. 
    
    **Body** - The sequence of statements inside a function definition. 
    
    **Composition** - Using an expression as part of a larger expression, or a statement as part of a larger statement. 
    
    **Deterministic** - Pertaining to a program that does the same thing each time it runs, given the same inputs. 
    
    **Dot Notation** - The syntax for calling a function in another module by specifying the module name followed by a dot (period) and the function name. 
    
    **Flow of Execution** - The order in which statements are executed during a program run. 
    
    **Fruitful Function** - A function that returns a value. 
    
    **Function** - A named sequence of statements that performs some useful operation. Functions may or may not take arguments and may or may not produce a result. 
    
    **Function Call** - A statement that executes a function. It consists of the function name followed by an argument list. 
    
    **Function Definition** - A statement that creates a new function, specifying its name, parameters, and the statements it executes. 
    
    **Function Object** - A value created by a function definition. The name of the function is a variable that refers to a function object. 
    
    **Header** - The first line of a function definition. 
    
    **Import Statement** - A statement that reads a module file and creates a module object. 
    
    **Module Object** - A value created by an ``import`` statement that provides access to the data and code defined in a module. 
    
    **Parameter** - A name used inside a function to refer to the value passed as an argument. 
    
    **Pseudorandom** - Pertaining to a sequence of numbers that appear to be random, but are generated by a deterministic program. 
    
    **Return Value** - The result of a function. If a function call is used as an expression, the return value is the value of the expression. 
    
    **Void Function** - A function that does not return a value.

|

----

Pay Calculator
--------------

**Prompt:** Write a program to prompt the user for **hours** and **rate per hour** using **input** to compute gross pay.

Pay should be the **normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours**. *Put the logic to do the computation of pay in a function called* ``computepay()`` *and use the function to do the computation*. The function should return a value.

**Use 45 hours and a rate of 10.50 per hour** to test the program (the pay should be **498.75**). You should **use input to read a string and float() to convert the string to a number**. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. **Do not name your variable "sum" or use the** ``sum()`` **function**.

**Expected output:**
::

    Enter Hours: 45
    Enter Rate: 10.50
    Pay: 498.75

**My outputs:**
::

    Enter Hours: 45
    Enter Rate: 10.50
    Pay: 498.75

::

    Enter Hours: forty 
    Please enter a numeric value!

::

    Enter Hours: 45
    Enter Rate: ten dollars and fifty cents per hour
    Please enter a numeric value!

**My code:**
::

    # defining functions
    def checkInput(value):
        try:
            value = float(value)

        except:
            print("Please enter a numeric value!")
            quit()
        
        return value

    def computepay(hours, rate):
        if hours > 40:
            overtime = hours - 40
            pay = (rate * 40) + ((1.5 * rate) * overtime)
            print("Pay: " + str(pay))

        else:
            pay = hours * rate
            print("Pay: " + str(pay))

    # main code
    hours = input("Enter Hours: ")
    hours = checkInput(hours)

    rate = input("Enter Rate: ")
    rate = checkInput(rate)

    computepay(hours, rate)

**Reasoning behind my code:**

Incorporating everything I've learned up to this point, I went the extra mile and added another function called ``checkInput()``. This function will run checks for both ``hours`` and ``rate`` without me having to duplicate code for each variable.

``computepay()`` is handling the pay calculation as per requested by the prompt. The code inside the function is reused from a previous assignment.

For **my outputs**, I ran the program a couple more times to test and document the error checking feature of my code.

.. note:: 

    Notice that ``checkInput()`` is a *"fruitful function"* because it utilizes ``return`` in its code and ``computepay()`` is a *"void function"* because it returns no value.

|

----

Grades Calculator
-----------------

**Prompt:** Rewrite the grade program from the previous chapter using a function called ``computegrade`` that takes a score as its parameter and returns a grade as a string.
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

    # defining functions
    def checkInput(value):
        try:
            value = float(value)

        except:
            print("Bad score")
            quit()
        
        return value

    def computegrade(score):
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

    # main code
    score = input("Enter score: ")
    score = checkInput(score)

    computegrade(score)

**Reasoning behind my code:**

For this assignment, I reused ``checkInput`` function and adjusted the ``print`` output to match that of the **expected output**. I also reused code from previous sections and stored it in the ``computegrade`` function as per requested by the prompt. By doing so, the main code composed of only three lines. This is efficiency through use of functions.