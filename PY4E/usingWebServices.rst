Using Web Services
==================

|

For this section, I'll be going over autograder exercises, plus application 1 and 2.

.. contents:: Contents
    :local:

.. note::

    **Somethings to be familiar with:**

|

----

Autograder: Extracting Data from XML
------------------------------------

**Prompt:** In this assignment you will write a Python program somewhat similar to `geoxml.py <http://www.py4e.com/code3/geoxml.py>`_. The program will prompt for a URL, read the XML data from that URL using ``urllib`` and then parse and extract the comment counts from the XML data, compute the **sum** of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

- **Sample data:** http://py4e-data.dr-chuck.net/comments_42.xml **(Sum=2553)** 
- **Actual data:** http://py4e-data.dr-chuck.net/comments_1784992.xml **(Sum ends with 86)**

The data consists of a number of names and comment counts in XML as follows: 
::

    <comment>
      <name>Matthias</name>
      <count>97</count>
    </comment>

You are to look through all the **<comment>** tags and find the **<count>** values sum the numbers. The closest sample code that shows how to parse XML is *geoxml.py*. But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code. 

To make the code a little simpler, you can use an *XPath selector string* to look through the entire tree of XML for any tag named *'count'* with the following line of code:
::

    counts = tree.findall('.//count')

Take a look at the *Python ElementTree documentation* and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.

**Expected output:** Sample execution
::

    $ python3 solution.py
    Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
    Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
    Retrieved 4189 characters
    Count: 50
    Sum: 2...

**My outputs:**
::

    $ python temporaryFile.py 
    Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
    Retrieving: http://py4e-data.dr-chuck.net/comments_42.xml
    Retrieving 4189 characters
    Count: 50
    Sum: 2553


::

    $ python temporaryFile.py 
    Enter location:  http://py4e-data.dr-chuck.net/comments_1784992.xml
    Retrieving:  http://py4e-data.dr-chuck.net/comments_1784992.xml
    Retrieving 4224 characters
    Count: 50
    Sum: 2386

**My code:**
::

    # required libraries/modules
    from urllib.request import urlopen
    import urllib.parse, urllib.error
    import xml.etree.ElementTree as ET

    # request for URL
    url = input("Enter location: ")

    # default URL for testing/debugging
    if len(url) < 1:
        url = "http://py4e-data.dr-chuck.net/comments_42.xml"

    # print 'Receiving' message to match sample execution
    print(f"Retrieving: {url}")

    # open URL. Read it in and convert it from byte to string type
    xml = urlopen(url).read().decode()

    # counting total number of characters read
    print(f"Retrieving {len(xml)} characters")

    # converting xml from string to tree representation
    tree = ET.fromstring(xml)

    # searching all 'comment' tags and count+summing all contents
    sum = 0
    count = 0
    for comment in tree.findall('comments/comment'):
        count += 1
        sum += int(comment.find('count').text)

    # formatted output to match sample execution
    print(f"Count: {count}\nSum: {sum}")

**Reasoning behind my code:**

The code is pretty straightforward. Majority of the concepts and executions are done in previous lessons. The only change is to include the ``xml.etree.ElementTree`` library and converting the URL from a string representation to a tree representation so that we can traverse the xml file and extract necessary information. Feel free to take a look at the comments in the code.

|

----

Autograder: Extract Data from JSON
----------------------------------

**Prompt:** In this assignment you will write a Python program somewhat similar to `json2.py <http://www.py4e.com/code3/json2.py>`_. The program will prompt for a URL, read the JSON data from that URL using ``urllib`` and then parse and extract the comment counts from the JSON data, compute the **sum** of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment. 

- **Sample data:** http://py4e-data.dr-chuck.net/comments_42.json **(Sum=2553)**
- **Actual data:** http://py4e-data.dr-chuck.net/comments_1784993.json **(Sum ends with 14)**

The data consists of a number of names and comment counts in JSON as follows:

.. code-block:: text

    {
      comments: [
        {
          name: "Matthias"
          count: 97
        },
        {
          name: "Geomer"
          count: 97
        }
        ...
      ]
    }

The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL. 

**Expected output:** Sample execution
::

    $ python3 solution.py
    Enter location: http://py4e-data.dr-chuck.net/comments_42.json
    Retrieving http://py4e-data.dr-chuck.net/comments_42.json
    Retrieved 2733 characters
    Count: 50
    Sum: 2...

**My outputs:**
::

    $ python temporaryFile.py 
    Enter location: http://py4e-data.dr-chuck.net/comments_42.json
    Retrieving: http://py4e-data.dr-chuck.net/comments_42.json
    Retrieving 2711 characters
    Count: 50
    Sum: 2553

::

    $ python temporaryFile.py 
    Enter location: http://py4e-data.dr-chuck.net/comments_1784993.json  
    Retrieving: http://py4e-data.dr-chuck.net/comments_1784993.json
    Retrieving 2740 characters
    Count: 50
    Sum: 2714

**My code:**
::

    # required libraries/modules
    from urllib.request import urlopen
    import urllib.parse, urllib.error
    import json

    # request for URL
    url = input("Enter location: ")

    # default URL for testing/debugging
    if len(url) < 1:
        url = "http://py4e-data.dr-chuck.net/comments_42.json"

    # print 'Receiving' message to match sample execution
    print(f"Retrieving: {url}")

    # open URL. Read it in and convert it from byte to string type
    jsn = urlopen(url).read().decode()

    # counting total number of characters read
    print(f"Retrieving {len(jsn)} characters")

    # prime 'data' to parse string as json objects
    data = json.loads(jsn)

    # looping through list of 'comments' and count+summing all 'count' values
    total = 0
    count = 0
    for comment in data['comments']:
        count += 1
        total += int(comment['count'])

    # formatted output to match sample execution
    print(f"Count: {count}\nSum: {total}")

**Reasoning behind my code:**

This assignment is almost identical to the previous autograder exercise. I have the comments in the code so feel free to take a look.

|

----

Autograder: Using the GeoJSON API
----------------------------------

**Prompt:** Calling a JSON API

In this assignment you will write a Python program somewhat similar to `geojson.py <http://www.py4e.com/code3/geojson.py>`_. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first **place_id** from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

**API End Points:** To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
::

    http://py4e-data.dr-chuck.net/json?

This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.

To call the API, you need to include a **key=** parameter and provide the address that you are requesting as the **address=** parameter that is properly URL encoded using the ``urllib.parse.urlencode()`` function as shown in `geojson.py <http://www.py4e.com/code3/geojson.py>`_.

Make sure to check that your code is using the API endpoint as shown above. You will get different results from the **geojson** and **json** endpoints so make sure you are using the same end point as this autograder is using.

Please run your program to find the place_id for this location:

.. code-block:: text

    Hanoi University of Science and Technology

Make sure to enter the name and case exactly as above and enter the **place_id** and your Python code below. Hint: The first seven characters of the **place_id** are *"ChIJq_B ..."*

Make sure to retreive the data from the URL specified above and **not** the normal Google API. Your program should work with the Google API - but the **place_id** may not match for this assignment.

**Expected output:** Test Data / Sample Execution

You can test to see if your program is working with a location of *"South Federal University"* which will have a **place_id** of *"ChIJNeHD4p-540AR2Q0_ZjwmKJ8"*.
::

    $ python3 solution.py
    Enter location: South Federal University
    Retrieving http://...
    Retrieved 2453 characters
    Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8

**My outputs:**
::

    $ python temporaryFile.py 
    Enter location: South Federal University
    Retrieving http://py4e-data.dr-chuck.net/json?key=42&address=South+Federal+University
    Retrieved 4819 characters
    Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8

::

    $ python temporaryFile.py
    Enter location: Hanoi University of Science and Technology
    Retrieving http://py4e-data.dr-chuck.net/json?key=42&address=Hanoi+University+of+Science+and+Technology
    Retrieved 1980 characters
    Place id ChIJq_BLKXGsNTER2qkEXg7S4sc

**My code:**
::

    # required libraries/modules
    from urllib.request import urlopen
    from urllib.parse import urlencode
    import urllib.error
    import json

    # initializing a dictionary with a 'key' parameter
    param = {'key' : 42}

    # requesting for an address
    url = input("Enter location: ")

    # initializing the first half of the URL
    serviceurl = "http://py4e-data.dr-chuck.net/json?"

    # adding 'address' parameter to dictionary
    param['address'] = url

    # default address used for testing/debugging
    if len(url) < 1:
        param['address'] = "South Federal University"

    # combining two halves to create the whole URL
    url = serviceurl + urlencode(param)

    # printing 'Retrieving' message to match sample execution
    print(f"Retrieving {url}")

    # opening the URL, reading it into 'jsn' and converting to str type
    jsn = urlopen(url).read().decode()

    # printing 'Retrieved' message to match sample execution
    print(f"Retrieved {len(jsn)} characters")

    # loading in str data and parsing it in JSON structure
    data = json.loads(jsn)

    # dumping the data to see its structure
    # print(json.dumps(data, indent=2))

    # locating 'place_id' and storing the value
    placeID = data["results"][0]["place_id"]

    # formatted output
    print(f"Place id {placeID}")

**Reasoning behind my code:**

The code is commented sufficiently. Only things to point out are that the API key ``42`` was given out by the professor and the link to the API endpoint is stated in the prompt. This project focusing on utilizing JSON.

|

----

Application: Google geocoding web service
-----------------------------------------

**Prompt:** Change either ``geojson.py`` or ``geoxml.py`` to print out the **two-character country code** from the retrieved data. **Add error checking** so your program does not traceback if the country code is not there. Once you have it working, search for **"Atlantic Ocean"** and make sure it can handle locations that are **not in any country**.

- Link to ``geojson.py``: https://www.py4e.com/code3/geojson.py
- Link to ``geojson.py``: https://www.py4e.com/code3/geoxml.py

**Expected output:** Sample from reference material
::

    $ python3 geojson.py
    Enter location: Ann Arbor, MI
    Retrieving http://py4e-data.dr-chuck.net/json?address=Ann+Arbor%2C+MI&key=42
    Retrieved 1736 characters
    {
        "results": [
            {
                "address_components": [
                    {
                        "long_name": "Ann Arbor",
                        "short_name": "Ann Arbor",
                        "types": [
                            "locality",
                            "political"
                        ]
                    },
                    {
                        "long_name": "Washtenaw County",
                        "short_name": "Washtenaw County",
                        "types": [
                            "administrative_area_level_2",
                            "political"
                        ]
                    },
                    {
                        "long_name": "Michigan",
                        "short_name": "MI",
                        "types": [
                            "administrative_area_level_1",
                            "political"
                        ]
                    },
                    {
                        "long_name": "United States",
                        "short_name": "US",
                        "types": [
                            "country",
                            "political"
                        ]
                    }
                ],
                "formatted_address": "Ann Arbor, MI, USA",
                "geometry": {
                    "bounds": {
                        "northeast": {
                            "lat": 42.3239728,
                            "lng": -83.6758069
                        },
                        "southwest": {
                            "lat": 42.222668,
                            "lng": -83.799572
                        }
                    },
                    "location": {
                        "lat": 42.2808256,
                        "lng": -83.7430378
                    },
                    "location_type": "APPROXIMATE",
                    "viewport": {
                        "northeast": {
                            "lat": 42.3239728,
                            "lng": -83.6758069
                        },
                        "southwest": {
                            "lat": 42.222668,
                            "lng": -83.799572
                        }
                    }
                },
                "place_id": "ChIJMx9D1A2wPIgR4rXIhkb5Cds",
                "types": [
                    "locality",
                    "political"
                ]
            }
        ],
        "status": "OK"
    }
    lat 42.2808256 lng -83.7430378
    Ann Arbor, MI, USA

**My outputs:**

**Scenario:** *location entered can not be found*
::

    $ python temporaryFile.py
    Enter location: spider-verse
    Retrieving https://maps.googleapis.com/maps/api/geocode/json?address=spider-verse&key=HIDDEN_API_KEY
    Retrieved 52 characters
    {
      "results": [],
      "status": "ZERO_RESULTS"
    }

    Data on location NOT found! Status: ZERO_RESULTS
    Exiting program...

**Scenario:** *typical output on a location*
::

    $ python temporaryFile.py
    Enter location: Austin, TX
    Retrieving https://maps.googleapis.com/maps/api/geocode/json?address=Austin%2C+TX&key=HIDDEN_API_KEY
    Retrieved 1756 characters
    {
      "results": [
        {
          "address_components": [
            {
              "long_name": "Austin",
              "short_name": "Austin",
              "types": [
                "locality",
                "political"
              ]
            },
            {
              "long_name": "Travis County",      
              "short_name": "Travis County",     
              "types": [
                "administrative_area_level_2",   
                "political"
              ]
            },
            {
              "long_name": "Texas",
              "short_name": "TX",
              "types": [
                "administrative_area_level_1",   
                "political"
              ]
            },
            {
              "long_name": "United States",      
              "short_name": "US",
              "types": [
                "country",
                "political"
              ]
            }
          ],
          "formatted_address": "Austin, TX, USA",
          "geometry": {
            "bounds": {
              "northeast": {
                "lat": 30.5168629,
                "lng": -97.57310199999999
              },
              "southwest": {
                "lat": 30.0986589,
                "lng": -97.9383829
              }
            },
            "location": {
              "lat": 30.267153,
              "lng": -97.7430608
            },
            "location_type": "APPROXIMATE",
            "viewport": {
              "northeast": {
                "lat": 30.5168629,
                "lng": -97.57310199999999
              },
              "southwest": {
                "lat": 30.0986589,
                "lng": -97.9383829
              }
            }
          },
          "place_id": "ChIJLwPMoJm1RIYRetVp1EtGm10",
          "types": [
            "locality",
            "political"
          ]
        }
      ],
      "status": "OK"
    }

    ===Results===
    Location: United States
    Category of "country"
    Country code: US

**Scenario:** *searching for the Atlantic Ocean (skipping JSON data going forward to save space)*
::

    $ python temporaryFile.py
    Enter location: Atlantic Ocean
    Retrieving https://maps.googleapis.com/maps/api/geocode/json?address=Atlantic+Ocean&key=HIDDEN_API_KEY
    Retrieved 1228 characters

    ===Results===
    Location: Atlantic Ocean   
    Category of "establishment"
    No country code available

**Scenario:** *making sure program can handle locations not within a country... so let's search for a continent, instead!*
::

    $ python temporaryFile.py
    Enter location: Europe
    Retrieving https://maps.googleapis.com/maps/api/geocode/json?address=Europe&key=HIDDEN_API_KEY
    Retrieved 1191 characters

    ===Results===
    Location: Europe
    Category of "continent"  
    No country code available

**My code:**
::

    # required libraries/modules
    from urllib.request import urlopen
    from urllib.parse import urlencode
    import urllib.error, json, ssl, googleapi

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # ask user for a location
    address = input("Enter location: ")

    # default address if no user input
    if len(address) < 1:
        address = "Seattle, WA"

    # first part of the full URL
    serviceUrl = "https://maps.googleapis.com/maps/api/geocode/json?"

    # storing address and API key in a dictionary
    param = {'address' : address, 'key' : googleapi.key()}

    # add the parameters to the partial URL to form a complete one
    realurl = serviceUrl + urlencode(param)

    # update the parameter with a dummy key for output
    param.update({'key' : 'HIDDEN_API_KEY'})

    # generate dummy URL for output
    fakeurl = serviceUrl + urlencode(param)

    # output 'Retrieving' message to match sample from reference
    print(f"Retrieving {fakeurl}")

    # open the real URL while bypassing ssl and read in the web page, decoded to str type
    jsn = urlopen(realurl, context=ctx).read().decode()

    # output 'Retrieved' message to match sample from reference
    print(f"Retrieved {len(jsn)} characters")

    # load in the str data and parse it in JSON format
    data = json.loads(jsn)

    # output the JSON data to match sample from reference
    print(json.dumps(data, indent=2))

    category = ""
    shortname = ""
    longname = ""

    # implement error check as requested by the prompt
    try:
        # attempt to set 'starting location' within the JSON data
        addressComponents = data["results"][0]["address_components"]

    except:
        print("\nData on location NOT found! Status:", data["status"])
        print("Exiting program...")
        exit()

    # if 'starting location' established, loops through the list of objects
    for obj in addressComponents:

        # Checking on the 'types' attribute
        typesList = obj["types"]
        for types in typesList:

            # Checking and matching locations. "country" is matching for all countries and
            # "establishment" is matching for non-country locations
            if types == "country" or types == "establishment":
                longname = obj["long_name"]
                shortname = obj["short_name"]
                category = typesList[0]

    # formatted output
    print(f"\n===Results===\nLocation: {longname}\nCategory of \"{category}\"")

    # output the country code if it's a country. If not, display a message
    if not category == "country":
        print("No country code available")
    else:
        print(f"Country code: {shortname}")
        

**Reasoning behind my code:**

The code is commented sufficiently. Feel free to take a look. Something to point out. In the ``import`` section, there's a ``googleapi`` module. This module is another Python file created by me in the name of ``googleapi.py``. This file's main purpose is to obscure the API key and calling it in this program, when necessary. I learned how to do so by looking at `hidden.py <https://www.py4e.com/code3/hidden.py>`_.

