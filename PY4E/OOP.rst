Object-Oriented Programming
===========================

|

**Foreword:** With the nature of needing context from real world situation to fully grasp the entire picture that is object-oriented programming (OOP), I'll be shifting from normally developing solutions to given issues to more of showcasing important definitions and sample code that will expand upon concepts of OOP.

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
