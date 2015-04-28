#!/bin/env/python
import json
import urllib2
import base64

# Setings
# The IP address for the XBMC instance you want to talk to
ip = '192.168.1.55'
# The port number XBMC's web interface is listening on
port = '8080'
# The username on XBMC's web interface (just comment or delete this line if you don't use authentication
username = 'xbmc'
# Same as the username.
password = '1234'

# Here you specify the method and parameters you want to pass to the XBMC JSON API
# For a LOT of info on the kinds of things you can do with the interface go here:
# http://wiki.xbmc.org/index.php?title=JSON-RPC_API/v6
# Here's an example of just sending an on-screen notification. This should help you understand the syntax
# method = 'GUI.ShowNotification'
# parameters = {"title":"Hello There!", "message":"This is a notification!", "displaytime":3000}
# This is what I am actually doing with this script, running the Artwork Downloader.
# Note: I am using the "silent" mode to avoid having a pop-up dialog box that would need to be closed.
# Also note: this stuff is very syntax-specific. Boolean and Int values must not be quoted. Strings must be doublequoted.
method = 'Addons.ExecuteAddon'
parameters = {"addonid":"script.artwork.downloader", "params":{"silent":"true"}, "wait":True}

# This is a single, reusable method that makes a call to XBMC and gives you back the response

def getJsonRemote(host,port,username,password,method,parameters):
    # First we build the URL we're going to talk to
    url = 'http://%s:%s/jsonrpc' %(host, port)
    # Next we'll build out the Data to be sent
    values ={}
    values["jsonrpc"] = "2.0"
    values["method"] = method
    # This fork handles instances where no parameters are specified
    if parameters:
        values["params"] = parameters
    values["id"] = "1"
    headers = {"Content-Type":"application/json",}
    # Format the data
    data = json.dumps(values)
    # Now we're just about ready to actually initiate the connection
    req = urllib2.Request(url, data, headers)
    # This fork kicks in only if both a username & password are provided
    if username and password:
        # This properly formats the provided username & password and adds them to the request header
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        req.add_header("Authorization", "Basic %s" % base64string)
    # Now we're ready to talk to XBMC
    # I wrapped this up in a try: statement to allow for graceful error handling
    try:
        response = urllib2.urlopen(req)
        response = response.read()
        response = json.loads(response)
        # A lot of the XBMC responses include the value "result", which lets you know how your call went
        # This logic fork grabs the value of "result" if one is present, and then returns that.
        # Note, if no "result" is included in the response from XBMC, the JSON response is returned instead.
        # You can then print out the whole thing, or pull info you want for further processing or additional calls.
        if 'result' in response:
            response = response['result']
    # This error handling is specifically to catch HTTP errors and connection errors
    except urllib2.URLError as e:
        # In the event of an error, I am making the output begin with "ERROR " first, to allow for easy scripting.
        # You will get a couple different kinds of error messages in here, so I needed a consistent error condition to check for.
        response = 'ERROR '+str(e.reason)
    return response

# Here's an example of using the above method and variable values to make XBMC run the add-on
results=getJsonRemote(ip,port,username,password,method,parameters)
# I just print the results out
print results
