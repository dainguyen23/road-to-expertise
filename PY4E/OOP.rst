Object-Oriented Programming
===========================

|

**Foreword:** To fully grasp the entire picture that is object-oriented programming (OOP), we'll need a deep dive and contexts of real world applications, which unfortunately can't be encompassed in this section. Therefore, I'll be shifting from normally developing solutions to given problems to more a showcasing of important definitions and sample code that will expand upon the concepts of OOP. Know that this will be expanded upon in later on sections.

.. note::

    **Somethings to be familiar with:**
    
    **Attribute** is a variable that is part of a class. 
    
    **Class** is a template that can be used to *construct* an object. It defines the *attributes* and *methods* that will make up the object. 
    
    **Child class** is a new class created when a parent class is *extended*. The child class *inherits* all of the attributes and methods of the parent class. 
    
    **Constructor** is an optional specially named method ``(__init__)`` that is called at the moment when a class is being used to construct an object. Usually this is used to set up initial values for the object. 
    
    **Destructor** is an optional specially named method ``(__del__)`` that is called at the moment just before an object is destroyed. Destructors are rarely used. 
    
    **Inheritance** is when we create a new class (child) by extending an existing class (parent). The child class has all the attributes and methods of the parent class plus additional attributes and methods defined by the child class. 
    
    **Method** is a function that is contained within a class and the objects that are constructed from the class. Some object-oriented patterns use *"message"* instead of *"method"* to describe this concept. 
    
    **Object** is a constructed instance of a class. An object contains all of the attributes and methods that were defined by the class. Some object-oriented documentation uses the term *"instance"* interchangeably with *"object"*. 
    
    **Parent class** is the class which is being extended to create a new child class. The parent class contributes all of its methods and attributes to the new child class.

|

**Using objects**

We can take a look at the capabilities of an object by looking at the output of the ``dir()`` function:
::

    >>> stuff = list()
    >>> dir(stuff)
    ['__add__', '__class__', '__contains__', '__delattr__',
    '__delitem__', '__dir__', '__doc__', '__eq__',
    '__format__', '__ge__', '__getattribute__', '__getitem__',
    '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
    '__iter__', '__le__', '__len__', '__lt__', '__mul__',
    '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    '__repr__', '__reversed__', '__rmul__', '__setattr__',
    '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
    'append', 'clear', 'copy', 'count', 'extend', 'index',
    'insert', 'pop', 'remove', 'reverse', 'sort']
    >>>

|

**Our first Python object**

We use the ``class`` keyword to define the data and code that will make up each of the objects. The class keyword includes the *name* of the class and begins an indented block of code where we include the *attributes* (data) and *methods* (code).
::

    class PartyAnimal:
    x = 0

    def party(self) :
        self.x = self.x + 1
        print("So far",self.x)

    an = PartyAnimal()
    an.party()
    an.party()
    an.party()
    PartyAnimal.party(an)

    # Code: http://www.py4e.com/code3/party2.py

Each method looks like a function, starting with the ``def`` keyword and consisting of an indented block of code. This object has one attribute (``x``) and one method (``party``). The methods have a special first parameter that we name by convention ``self``.

Just as the ``def`` keyword does not cause function code to be executed, the ``class`` keyword does not create an object. Instead, the ``class`` keyword defines a template indicating what data and code will be contained in each object of type ``PartyAnimal``. The class is like a cookie cutter and the objects created using the class are the cookies. You don't put frosting on the cookie cutter; you put frosting on the cookies, and you can put different frosting on each cookie.

The following line is another way to call the ``party`` method within the ``an`` object:
::

    PartyAnimal.party(an)

In this variation, we access the code from within the class and explicitly pass the object pointer ``an`` as the first parameter (i.e., ``self`` within the method). You can think of ``an.party()`` as shorthand for the above line.

When the program executes, it produces the following output:
::

    So far 1
    So far 2
    So far 3
    So far 4

|

**Classes as types**

As we have seen, in Python all variables have a type. We can use the built-in ``dir`` function to examine the capabilities of a variable. We can also use ``type`` and ``dir`` with the classes that we create.
::

    class PartyAnimal:
    x = 0

    def party(self) :
        self.x = self.x + 1
        print("So far",self.x)

    an = PartyAnimal()
    print ("Type", type(an))
    print ("Dir ", dir(an))
    print ("Type", type(an.x))
    print ("Type", type(an.party))

    # Code: http://www.py4e.com/code3/party3.py

When this program executes, it produces the following output:
::

    Type <class '__main__.PartyAnimal'>
    Dir  ['__class__', '__delattr__', ...
    '__sizeof__', '__str__', '__subclasshook__',
    '__weakref__', 'party', 'x']
    Type <class 'int'>
    Type <class 'method'>

You can see that using the ``class`` keyword, we have created a new type. From the ``dir`` output, you can see both the ``x`` integer attribute and the ``party`` method are available in the object.

|

**Object lifecycle**

In the previous examples, we define a class (template), use that class to create an instance of that class (object), and then use the instance. When the program finishes, all of the variables are discarded. Usually, we don't think much about the creation and destruction of variables, but often as our objects become more complex, we need to take some action within the object to set things up as the object is constructed and possibly clean things up as the object is discarded.

If we want our object to be aware of these moments of construction and destruction, we add specially named methods to our object:
::

    class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self) :
        self.x = self.x + 1
        print('So far',self.x)

    def __del__(self):
        print('I am destructed', self.x)

    an = PartyAnimal()
    an.party()
    an.party()
    an = 42
    print('an contains',an)

    # Code: http://www.py4e.com/code3/party4.py

When this program executes, it produces the following output:
::

    I am constructed
    So far 1
    So far 2
    I am destructed 2
    an contains 42

As Python constructs our object, it calls our ``__init__`` method to give us a chance to set up some default or initial values for the object. When Python encounters the line:
::

    an = 42

It actually “throws our object away” so it can reuse the ``an`` variable to store the value ``42``. Just at the moment when our ``an`` object is being “destroyed” our destructor code (``__del__``) is called. We cannot stop our variable from being destroyed, but we can do any necessary cleanup right before our object no longer exists.

When developing objects, it is quite common to add a constructor to an object to set up initial values for the object. It is relatively rare to need a destructor for an object.

|

**Multiple instances**

The real power in object-oriented programming happens when we construct multiple instances of our class.

When we construct multiple objects from our class, we might want to set up different initial values for each of the objects. We can pass data to the constructors to give each object a different initial value:
::

    class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')

    def party(self) :
        self.x = self.x + 1
        print(self.name,'party count',self.x)

    s = PartyAnimal('Sally')
    j = PartyAnimal('Jim')

    s.party()
    j.party()
    s.party()

    # Code: http://www.py4e.com/code3/party5.py

The constructor has both a ``self`` parameter that points to the object instance and additional parameters that are passed into the constructor as the object is constructed:
::

    s = PartyAnimal('Sally')

Within the constructor, the second line copies the parameter (``nam``) that is passed into the ``name`` attribute within the object instance.
::

    self.name = nam

The output of the program shows that each of the objects (``s`` and ``j``) contain their own independent copies of ``x`` and ``nam``:
::

    Sally constructed
    Jim constructed
    Sally party count 1
    Jim party count 1
    Sally party count 2

|

**Inheritance**

Another powerful feature of object-oriented programming is the ability to create a new class by extending an existing class. When extending a class, we call the original class the parent class and the new class the **child class**.

For this example, we move our ``PartyAnimal`` class into its own file. Then, we can 'import' the ``PartyAnimal`` class in a new file and extend it, as follows:
::

    from party import PartyAnimal

    class CricketFan(PartyAnimal):
    points = 0
    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name,"points",self.points)

    s = PartyAnimal("Sally")
    s.party()
    j = CricketFan("Jim")
    j.party()
    j.six()
    print(dir(j))

    # Code: http://www.py4e.com/code3/party6.py

When we define the ``CricketFan`` class, we indicate that we are extending the ``PartyAnimal`` class. This means that all of the variables (``x``) and methods (``party``) from the ``PartyAnimal`` class are **inherited** by the ``CricketFan`` class. For example, within the ``six`` method in the ``CricketFan`` class, we call the ``party`` method from the ``PartyAnimal`` class.

As the program executes, we create ``s`` and ``j`` as independent instances of ``PartyAnimal`` and ``CricketFan``. The j object has additional capabilities beyond the ``s`` object.

.. code-block:: text

    Sally constructed
    Sally party count 1
    Jim constructed
    Jim party count 1
    Jim party count 2
    Jim points 6
    ['__class__', '__delattr__', ... '__weakref__',
    'name', 'party', 'points', 'six', 'x']

In the ``dir`` output for the ``j`` object (instance of the ``CricketFan`` class), we see that it has the attributes and methods of the parent class, as well as the attributes and methods that were added when the class was **extended** to create the ``CricketFan`` class.

These are the basics of object-oriented programming. There are many additional details as to how to best use object-oriented approaches when developing large applications and libraries that are beyond the scope of this section.