import json
import requests
from requests import exceptions
from datetime import datetime
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def JSONValidation(jsonFile):  
    with open(jsonFile,"r") as file:
        try:
            json.load(file)
            logging.info("JSON validated")
            return True
        except ValueError as err:
            logging.error("JSON not valid: %s" % err)
            return False

def grabPublicJSON(jsonFile):
    publicData = {}
    with open(jsonFile,"r") as file:
        data = json.load(file)
    for i in data:
        if "private" in data[i]:
            if data[i]["private"] == False:
                publicData[i] = data[i]
    return publicData


validated = JSONValidation(r"C:\Users\Timothy\infraeng-interview\coding\example.json")
if (validated == True):
    jsonData = grabPublicJSON(r"C:\Users\Timothy\infraeng-interview\coding\example.json")
    session = requests.Session()
    try:
        response = session.post("https://endpoint_of_webserver.com", verify=True,json = jsonData)  # alternatively verify can be set to a self signed certificate
    except requests.exceptions.Timeout as timeoutErr:
        logging.error("Request timed out: %s" % timeoutErr)
    except requests.exceptions.TooManyRedirects as redirectErr:
        logging.error("Request redirected too many times: %s" % redirectErr)
    except requests.exceptions.RequestException as requestErr:
        logging.error("Request redirected too many times: %s" % requestErr)
    except requests.exceptions.HTTPError as HTTPErr:
        logging.error("Request redirected too many times: %s" % HTTPErr)

    for i in response:
        if response[i]["valid"] == True:
            print(i)