Loops and Iterations
====================

|

.. contents:: Contents
    :local:

.. note::

    **Somethings to be familiar with:**

    Updating a variable by **adding 1** is called an *increment*; **subtracting 1** is called a *decrement*.

    Iterating through a section of code until a condition is met can be done through **loops**.

    Basic loop structures are: ``while`` loop, ``for`` loop and ``do`` ``while`` loop.

    You can, *with or without intention*, create an **infinite loop** where the code will iterate indefinitely as the condition is always ``True``.

    ``break`` can be used to stop the current iteration of code.

    ``continue`` can be used to skip the current iteration of code and move onto the next iteration.

    **Accumulator** - A variable used in a loop to add up or accumulate a result. 

    **Counter** - A variable used in a loop to count the number of times something happened. We initialize a counter to zero and then increment the counter each time we want to “count” something. 

    **Decrement** - An update that decreases the value of a variable. 

    **Initialize** - An assignment that gives an initial value to a variable that will be updated. 

    **Increment** - An update that increases the value of a variable (often by one). 

    **Infinite Loop** - A loop in which the terminating condition is never satisfied or for which there is no terminating condition. 

    **Iteration** - Repeated execution of a set of statements using either a function that calls itself or a loop.

|

----

Infinite Loop with a Condition
------------------------------

**Prompt:** Write a program which repeatedly reads numbers until the user enters **“done”**.

Once **“done”** is entered, print out the total, count, and average of the numbers.

If the user enters anything other than a number, detect their mistake using ``try`` and ``except`` and print an error message and skip to the next number.

**Expected output:**

.. code-block:: text

    Enter a number: 4
    Enter a number: 5
    Enter a number: bad data
    Invalid input
    Enter a number: 7
    Enter a number: done
    16 3 5.333333333333333

**My output:**

.. code-block:: text

    Enter a number: 4
    Enter a number: 5
    Enter a number: bad data 
    Invalid input   
    Enter a number: 7
    Enter a number: done 

    total: 16  count: 3  average: 5.333333333333333

**My code:**
::

    count = 0
    total = 0

    while True:
        
        value = input("Enter a number: ")

        if value == "done":
            break
        
        try:
            value = float(value)

        except:
            print("Invalid input")
            continue

        total += int(value)
        
        count += 1

    average = total / count

    print(f"\ntotal: {total}  count: {count}  average: {average}")

**Reasoning behind my code:**

I altered my output a bit to make the code more readable. Besides that, the code runs perfectly!

I first tried a conditional statement when I initialized the ``while`` loop. I had set a condition where if ``value`` does not equals **"done"**, the ``while`` loop would continue to iterate. The program worked and produced the same results as the **expected output**. However, the program always ended up with a trailing **"Invalid input"** line before tallying the ``total``, ``count`` and ``average``, which you can see below:

.. code-block:: text

    Enter a number: 4
    Enter a number: 5
    Enter a number: bad data
    Invalid input
    Enter a number: 7
    Enter a number: done
    Invalid input   <--------- unintended output
    16 3 5.333333333333333

I then took out the conditional statement from the ``while`` loop and set it as an **infinite loop**, intentionally. I moved the conditional statement inside the loop and utilized the ``break`` function. This means the loop stops, when **"done"** is matched.

I also used the **try/except** structure for float type conversion and ``int()`` for the desired output on ``total``. Without this step, ``total`` would have shown **16.0** instead of **16**.

Finally, with the issue fixed, I added a blank line with ``\n`` before printing the output for better clarity.

|

----

Continuous Prompt
-----------------

**Prompt:** Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below. 

**Expected output:**

.. code-block:: text

    Enter a number: 7
    Enter a number: 2
    Enter a number: bob
    Invalid input
    Enter a number: 10
    Enter a number: 4
    Enter a number: done
    Maximum is  10
    Minimum is  2

**My output:**

.. code-block:: text

    Enter a number: 7
    Enter a number: 2
    Enter a number: bob
    Invalid input
    Enter a number: 10
    Enter a number: 4
    Enter a number: done
    Maximum is  10
    Minimum is  2

**My code:**
::

    # defining functions
    def getLargest(oldval, newval):
        if oldval is None or newval > oldval:
            return newval
        else:
            return oldval

    def getSmallest(oldval, newval):
        if oldval is None or newval < oldval:
            return newval
        else:
            return oldval

    # main code
    largest = None
    smallest = None

    while True:
        
        value = input("Enter a number: ")

        if value == "done":
            break
        
        try:
            value = int(value)

        except:
            print("Invalid input")
            continue

        largest = getLargest(largest, value)
        smallest = getSmallest(smallest, value)    

    print("Maximum is ", largest)
    print("Minimum is ", smallest)

**Reasoning behind my code:**

I put the *max* and *min* calculation in their own separate *function* to make the **main code** less cluttered.

``largest`` and ``smallest`` have originally been initialized with the **integer** ``0``. But an issue arises when I realized the program will always keep ``0`` as the ``smallest`` value. So I decided to switch the **0's** to ``None`` as the value. This means that a simple conditional statement such as ``if newval > oldval:`` would have to be extended to cover the *first iteration* of the ``while`` loop. As you can see in **my code**, the new conditional statement is now ``if oldval is None or newval > oldval:``

The rest of the code is pretty straightforward!