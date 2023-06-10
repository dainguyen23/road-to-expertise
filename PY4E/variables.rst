Variables, Expressions and Statements
=====================================

|

For this section, I'll be going over exercises 2 to 5.

.. contents:: Contents
    :local:

|

----

Exercise 2
----------

**Prompt:** Write a program that uses the ``input`` method to prompt a user for their name and then welcomes them.

**Expected output:**
::

    Enter your name: Chuck
    Hello Chuck

**My output:**
::

    Enter your name: Dai
    Hello Dai

I just switched Dr. Chuck's name to mine! :D

**My code:**
::

    name = input("Enter your name: ")
    
    print("Hello " + name)

**Reasoning behind my code:**

The ``input()`` method was used as requested by the prompt and I chose to store it in a variable called ``name``. Having the method stored inside a variable helps with recording the input of the user.

I then called the ``print()`` method, called the variable ``name`` and concatenate it with the string *"Hello "*. Noticed there is a blank space after the word *"Hello"*. Without this whitespace, the output will be ``Hello<name>`` instead of ``Hello <name>``.

|

----

Exercise 3
----------

**Prompt:** Write a program to prompt the user for hours and rate per hour to compute gross pay.

**Expected output:**
::
    
    Enter Hours: 35
    Enter Rate: 2.75
    Pay: 96.25

**My output:**
::

    Enter Hours: 35
    Enter Rate: 2.75
    Pay: 96.25

**My code:**
::

    hours = input("Enter Hours: ")
    
    rate = input("Enter Rate: ")

    pay = float(hours) * float(rate)

    print("Pay: " + str(pay))

**Reasoning behind my code:**

Based off the expected output, I named my variables accordingly to increase the  readability of my code.

The variable ``hours`` ultilizes the ``input()`` method to ask and take in user input of hours worked. And the variable ``rate`` ultilizes the same method to ask and take in user input of the pay rate.

The variable ``pay`` ultilizes the method ``float()`` to explicitly convert ``hours`` and ``rate`` from type **String** to type **Float**. In doing this, the ``pay`` variable can perform multiplication on ``hours`` and ``rate`` and retains the decimal place values.

I then had to convert ``pay`` back into a **String** type when calling it inside the ``print()`` method so that I could concatenate it to the string *"Pay: "*.

|

----

Exercise 4
----------

**Prompt:** Assume that we execute the following assignment statements:
::

    width = 17
    height = 12.0

For each of the following expressions, write the value of the expression and the type (of the value of the expression).

#. ``width//2``
#. ``width/2.0``
#. ``height/3``
#. ``1 + 2 * 5``

**Expected output:** There was none available for this exercise. We're instructed to use the Python interpreter to check our answers.

**My output:**
::
    
    8
    <class 'int'>
    8.5
    <class 'float'>
    4.0
    <class 'float'>
    11
    <class 'int'>

**My code:**
::

    width = 17
    height = 12.0

    one = width//2
    two = width/2.0
    three = height/3
    four = 1 + 2 * 5

    print(one)
    print(type(one))
    print(two)
    print(type(two))
    print(three)
    print(type(three))
    print(four)
    print(type(four))

**Reasoning behind my code:**

By ultilizing the Python interpreter, I got the following:

#. ``width // 2`` equals ``8`` and it is type ``int``.
#. ``width / 2.0`` equals ``8.5`` and it is type ``float``.
#. ``height / 3`` equals ``4.0`` and it is type ``float``.
#. ``1 + 2 * 5`` equals ``11`` and it is type ``int``.

For this exercise, I used the given values for ``width`` and ``height``. I then pretty much just copy and paste the expressions the exercise wanted us to run. I named these expressions from ``one`` to ``four`` so that I can easily call each of them using the ``print()`` method.

I utilized the ``type()`` method here so that the program can output the *type class* of each result.

.. note:: 

    Notice how the division operator has two different variations.

    ``/`` is known as the **floating point division** operator. This operator outputs the result as a decimal number. If the result is an integer, it will be converted to a decimal number.
    
    ``//`` is known as the **floor division** or **integer division** operator. This operator outputs the result as an integer number. If the result is a decimal number, it will be truncated into an integer number. The number will always be rounded down to the nearest integer.

|

----

Exercise 5
----------

**Prompt:** Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

**Expected output:** There was none available for this exercise.

**My output:**
::

    #Example 1
    Enter the temperature in Celcius: 0
    Temperature entered in Celcius: 0°C
    Temperature converted to Fahrenheit: 32°F

    #Example 2
    Enter the temperature in Celcius: 100
    Temperature entered in Celcius: 100°C
    Temperature converted to Fahrenheit: 212°F

    #Example 3
    Enter the temperature in Celcius: 73
    Temperature entered in Celcius: 73°C
    Temperature converted to Fahrenheit: 163°F

**My code:**
::

    celcius = input("Enter the temperature in Celcius: ")

    fahrenheit = (int(celcius) * 9//5) + 32

    print("Temperature entered in Celcius: " + str(celcius) + "\N{DEGREE SIGN}C")
    print("Temperature converted to Fahrenheit: " + str(fahrenheit) + "\N{DEGREE SIGN}F")

**Reasoning behind my code:**

The variable ``celcius`` asks for the user input. The variable ``fahrenheit`` converts ``celcius`` from type **String** to type **Int** and performs the temperature conversion formula.

For better readability, I used two seperate ``print()`` statements. One for the user input, in degrees Celcius; the other for the converted output, in degrees Fahrenheit.

.. note:: 

    Using type **Int** for the output is a personal choice I made. The output can easily be shown in type **Float** for more accuracy.

    ``\N{DEGREE SIGN}`` is *Unicode*. This was used to create the degree symbol. There are multiple ways to go about creating such symbol, but I chose this one as it is the most readable. 