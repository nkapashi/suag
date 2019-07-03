# **SupportUnknown's API Grounds**

-----------------------------------------------------------------------------------------------

SupportUnknown's API Grounds (**SUAG**) is a simple service for generating different HTTP response codes, types, and messages. It is useful in testing how your scripts and code deals with varying responses. It can also be used as an endpoint when testing API Gateways.

It has the following resources: [codes](#codes-resource-(/codes/\<int:code\>)), [ip](#ip -resource-(/ip) ), [bus_stop](#bus_stop-resource-(/bus_stop/\<string:busStop\>)), [payload](#payload-resource-(/payload)), and [streamload](#streamload-resource-(/streamload)).

[Swagger file](/suag.json)  and  [SWAGGER UI](/swagger) are also available.

## RESOURCES:

### 	CODES Resource (/codes/\<int:code\>)

Returns requested HTTP code, can delay the response and echo back some message.

​	*Request Parameters:*

   	- **sleep** (type = integer, required = False)
   	- **echo** (type = string, required = False)

​	*Supported Methods:* GET, POST	
​	*Content Types:* application/json


```
Return status code 200

curl -X GET \
  https://suag-axway.herokuapp.com/codes/200
Response:
{
    "sleep": "None",
    "echoedMessage": "None"
}

Retrun status code 301, delay the response with 2 seconds and output the message "This is a test"

curl -X GET \
  'https://suag-axway.herokuapp.com/codes/301?echo=This%20is%20a%20test&sleep=2'
Response:
{
    "sleep": 2,
    "echoedMessage": "This is a test"
}
```

**Note:** Sleep cannot be set for more than 10 seconds. While values above 10 will be accepted the delay of the response will still be limited to 10 seconds.

###IP  Resource (/ip)

Returns the IP address of the client. Can be used to check what is your  public ip address.

*Request Parameters:* **None**

*Supported Methods:* GET

*Content Types:* application/json, text/plain

```
curl -X GET \
  https://suag-axway.herokuapp.com/ip
  
  Resposne:
  71.209.xx.xx
  
  curl -X GET \
  https://suag-axway.herokuapp.com/ip \
  -H 'Accept: application/json'
  
  Response:
  {
    "ipAddr": [
        "71.209.xx.xx"
    ]
}
```

###BUS_STOP Resource (/bus_stop/\<string:busStop\>)

This resource can be used for testing scenarios where the data is known to change after some time. It simulates the schedule of a bus. The time to arrive and next bus stop changes every two minutes. The bus completes the route in 10 minutes and there are 5 stops is total. 

*Request Parameters:* **None**

 *Supported Methods:* GET

*Content Types:* application/json

```
curl -X GET \
  https://suag-axway.herokuapp.com/bus_stop/middleOfNowehre
  
  Respone:
  {
    "busStop": "middleOfNowehre",
    "nextStop": "Stop4",
    "ttArrive": 4
}
```

###PAYLOAD Resource (/payload)

Responds with text data in plain, xml or json format. The **lines** and **delay** parameters can be used to specify how many lines of text to be sent and the total delay. Each line of text  is about 512 bytes of data. The "Accept" header can be used to specify the format of the returned data.

Request Parameters:

- **delay** (type = integer, required = False)

- **lines** (type = integer, required = False)

  

*Supported Methods:* GET

*Content Types:*  application/json, text/plain, application/xml

```
curl -X GET \
  'https://suag-axway.herokuapp.com/payload?lines=2&delay=3' \
  -H 'Accept: application/xml'
  
  Resposne:
  
  <Data>
    <text>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</text>
    <number>0</number>
    <text>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</text>
    <number>1</number>
</Data>
```

**Note:** Authorization is required to set **delay** and **lines** with higher values. Anything that will block the execution above 30 seconds (delay * lines > 30) will require the **Authorization header** to be set with the correct credentials.

###STREAMLOAD Resource (/streamload)

This resources uses a generator to stream data to the client **line by line**.  In comparison the **payload** resource sends to the client at once. The **lines** request parameter can be used to specify the total number of lines to be returned and the **delay** parameter to specify the delay between each time. . Each line of text  is about 512 bytes of data. The "Accept" header can be used to specify the format of the returned data.

Request Parameters:

- **delay** (type = integer, required = False)
- **lines** (type = integer, required = False)

*Supported Methods:* GET

*Content Types:*  application/json, text/plain, application/xml

```
curl -X GET \
  'https://suag-axway.herokuapp.com/streamload?lines=2&delay=1' \
  -H 'Accept: application/json'
  
  Response:
  [{"Line0": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"},{"Line1": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"},{}]
```

**Note:** Authorization is required to set **delay** and **lines** with higher values. Anything that will block the execution above 30 seconds (delay * lines > 30) will require the **Authorization header** to be set with the correct credentials.

------

![](D:\KUR\proj\static\gitHubLogo.png)

Author: nKapashikov