Using Web Services
==================

|

.. contents:: Contents
    :local:

.. note::

    **Somethings to be familiar with:**

    **XML** stands for *eXtensible Markup Language*.

    XML looks very similar to HTML, but XML is more structured than HTML. Here is a sample of an XML document:
    
    .. code-block:: xml

        <person>
            <name>Chuck</name>
            <phone type="intl">
                +1 734 303 4456
            </phone>
            <email hide="yes" />
        </person>

    Each pair of opening (e.g., ``<person>``) and closing tags (e.g., ``</person>``) represents a *element* or *node* with the same name as the tag (e.g., ``person``). Each element can have some text, some attributes (e.g., ``hide``), and other nested elements. If an XML element is empty (i.e., has no content), then it may be depicted by a self-closing tag (e.g., ``<email />``).

    **JSON** stands for *JavaScript Object Notation*.

    Here is a JSON encoding that is roughly equivalent to the simple XML from above:
    
    .. code-block:: json

        {
            "name" : "Chuck",
            "phone" : {
                "type" : "intl",
                "number" : "+1 734 303 4456"
            },
            "email" : {
                "hide" : "yes"
            }
        }

    Notice some differences. First, in XML, we can add attributes like “intl” to the “phone” tag. In JSON, we simply have key-value pairs. Also the XML “person” tag is gone, replaced by a set of outer curly braces.

    JSON is quickly becoming the format of choice for nearly all data exchange between applications because of its relative simplicity compared to XML.

    **API** - Application Program Interface - A contract between applications that defines the patterns of interaction between two application components. 
    
    **ElementTree** - A built-in Python library used to parse XML data.  
    
    **SOA** - Service-Oriented Architecture - When an application is made of components connected across a network. 
                
|

----

Data Extraction in XML Format
-----------------------------

**Process:**

This Python program will:

- Prompt the user for a URL containing XML data using ``urllib``.
- Read in the XML data.
- Parse the content.
- Search through all the **<comment>** tags.
- Find all the **<count>** integer values.
- Compute the **sum** of integers.
- Output it to the console.

The data consists of a number of names and comment counts in XML as follows: 
::

    <comment>
      <name>Matthias</name>
      <count>97</count>
    </comment>

Click to open `reference code <http://www.py4e.com/code3/geoxml.py>`__.

Click to open `small data sample <http://py4e-data.dr-chuck.net/comments_42.xml>`__.
  
Click to open `large data sample <http://py4e-data.dr-chuck.net/comments_1784992.xml>`__.

**Testing methodology:**

Small and large data samples are fed into the program and the sum of integers will be calculated.

*Sample execution*
::

    $ python3 solution.py
    Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
    Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
    Retrieved 4189 characters
    Count: 50
    Sum: 2...

*Hint*

.. code-block:: text

    Small data sample's sum is 2553
    Large data sample's sum ends with 86

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

**My outputs:**

*Small data sample*
::

    $ python temporaryFile.py 
    Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
    Retrieving: http://py4e-data.dr-chuck.net/comments_42.xml
    Retrieving 4189 characters
    Count: 50
    Sum: 2553

*Large data sample*
::

    $ python temporaryFile.py 
    Enter location:  http://py4e-data.dr-chuck.net/comments_1784992.xml
    Retrieving:  http://py4e-data.dr-chuck.net/comments_1784992.xml
    Retrieving 4224 characters
    Count: 50
    Sum: 2386

**Notes:**

The code is pretty straightforward. Majority of the concepts and executions are done in previous lessons. The only change is to include the ``xml.etree.ElementTree`` library and converting the URL from a string representation to a tree representation so that we can traverse the xml file and extract necessary information. Feel free to take a look at the comments in the code.

|

----

Data Extraction in JSON Format
------------------------------

**Process:**

This Python program will:

- Prompt the user for a URL containing JSON data using ``urllib``.
- Read in the JSON data.
- Parse the content.
- Search through all the **<comment>** tags.
- Find all the **<count>** integer values.
- Compute the **sum** of integers.
- Output it to the console.

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

Click to open `reference code <http://www.py4e.com/code3/json2.py>`__.

Click to open `small data sample <http://py4e-data.dr-chuck.net/comments_42.json>`__.

Click to open `large data sample <http://py4e-data.dr-chuck.net/comments_1784993.json>`__.

**Testing methodology:**

Small and large data samples are fed into the program and the sum of integers will be calculated.

*Sample Execution*
::

    $ python3 solution.py
    Enter location: http://py4e-data.dr-chuck.net/comments_42.json
    Retrieving http://py4e-data.dr-chuck.net/comments_42.json
    Retrieved 2733 characters
    Count: 50
    Sum: 2...

*Hint*

.. code-block:: text

    Sum of small sample data is 2552
    Sum of large sample data ends with 14

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

**My outputs:**

*Small data sample*
::

    $ python temporaryFile.py 
    Enter location: http://py4e-data.dr-chuck.net/comments_42.json
    Retrieving: http://py4e-data.dr-chuck.net/comments_42.json
    Retrieving 2711 characters
    Count: 50
    Sum: 2553

*Large data sample*
::

    $ python temporaryFile.py 
    Enter location: http://py4e-data.dr-chuck.net/comments_1784993.json  
    Retrieving: http://py4e-data.dr-chuck.net/comments_1784993.json
    Retrieving 2740 characters
    Count: 50
    Sum: 2714

**Notes:**

The approach is similar to the XML version.

|

----

Data Extraction Web Service - GeoJSON API
-----------------------------------------

**Process:**

This Python program will:

- Prompt the user for a location.
- Contact a web service via API endpoint.
- Retrieve JSON data from the web service.
- Parse the data.
- Display count of characters retrieved.
- Retrieve the first **place_id** from the data.

A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

*API end point*
::

    http://py4e-data.dr-chuck.net/json?

*API key is* ``42``.

Click to open `reference code <http://www.py4e.com/code3/geojson.py>`__.

**Testing methodology:**

The program will call the API with the provided **key=** and **address=** parameters and encoded URL to find the **place_id** of the following test data:

*Location & hint*

.. code-block:: text

    South Federal University

::

    The place_id will should be "ChIJNeHD4p-540AR2Q0_ZjwmKJ8"

*Location & hint*

.. code-block:: text

    Hanoi University of Science and Technology

::

    The first seven characters of the place_id should be "ChIJq_B..."


*Sample Execution*
::

    $ python3 solution.py
    Enter location: South Federal University
    Retrieving http://...
    Retrieved 2453 characters
    Place id ChI...

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

**My outputs:**

*Place ID of South Federal University*
::

    $ python temporaryFile.py 
    Enter location: South Federal University
    Retrieving http://py4e-data.dr-chuck.net/json?key=42&address=South+Federal+University
    Retrieved 4819 characters
    Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8

*Place ID of Hanoi University of Science and Technology*
::

    $ python temporaryFile.py
    Enter location: Hanoi University of Science and Technology
    Retrieving http://py4e-data.dr-chuck.net/json?key=42&address=Hanoi+University+of+Science+and+Technology
    Retrieved 1980 characters
    Place id ChIJq_BLKXGsNTER2qkEXg7S4sc

|

----

Data Extraction Web Service - Google Geocoding API
--------------------------------------------------

**Process:**

This application will:

- Prompt the user for a location.
- Contact the Google Geocoding web service via its API endpoint.
- Retrieve JSON data from the web service.
- Parse the data.
- Display count of characters retrieved.
- Display JSON snippet pertaining to the location entered.
- Retrieve the first **two-character country code** from the data.
- Have error checking implemented so it won't display traceback errors if the country code is not found.

Click to open `reference code <https://www.py4e.com/code3/geojson.py>`__.

Click to see how to `obscure API key <https://www.py4e.com/code3/hidden.py>`__ within your code.

**Testing methodology:**

The application will test for:

- An invalid input.
- A normal country location.
- A location that's not in any country.
- The Atlantic Ocean.

*Sample Execution*
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

**My outputs:**

*Scenario: location entered can not be found*
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

*Scenario: location entered is available in a country*
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

*Scenario: location entered is not within a country (it's a continent!!) (skipping JSON data snippet)*
::

    $ python temporaryFile.py
    Enter location: Europe
    Retrieving https://maps.googleapis.com/maps/api/geocode/json?address=Europe&key=HIDDEN_API_KEY
    Retrieved 1191 characters

    ===Results===
    Location: Europe
    Category of "continent"  
    No country code available

*Scenario: location entered is the Atlantic Ocean (skipping JSON data snippet)*
::

    $ python temporaryFile.py
    Enter location: Atlantic Ocean
    Retrieving https://maps.googleapis.com/maps/api/geocode/json?address=Atlantic+Ocean&key=HIDDEN_API_KEY
    Retrieved 1228 characters

    ===Results===
    Location: Atlantic Ocean   
    Category of "establishment"
    No country code available

**Notes:**

Something to point out. In the ``import`` section, there's a ``googleapi`` module. This module is another Python file created by me in the name of ``googleapi.py``. This file's main purposes are to `obscure the API key <https://www.py4e.com/code3/hidden.py>`__ and provide it when called in this program.

