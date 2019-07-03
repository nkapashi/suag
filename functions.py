import json
from lxml import etree
from time import sleep
import functools
from flask import request
import os

secret = os.environ.get('SECRET') if os.environ.get('SECRET') else 'SECRET123'

def needAuth(func):
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        forwardHeader = request.headers.get('Authorization')
        if forwardHeader == secret:
            return func(*args, **kwargs)
        if (lambda x,y: x*y)(*args, **kwargs) < 10:
            return func(*args, **kwargs)
        return func(5, 2)
    return wrapper

@needAuth
def stremText(lines, delay):
    for i in range(lines):
        sleep(delay)
        yield "Line" +str(i) + " about 512k of data" + 'x'*512 + "\n"
  
@needAuth      
def textPayload(lines, delay):
    textLoad = ["Line" +str(i) + " about 512k of data" + 'x'*512 + "\n" for i in range(lines)]
    sleep(delay)
    return str(textLoad)

@needAuth
def xmlPayload(lines, delay):
    root = etree.Element('Data')
    for i in range(lines):
        text = etree.Element('text')
        root.append(text)
        number = etree.Element('number')
        text.text = 'x' * 512
        number.text = str(i)
        root.append(number)
    sleep(delay)
    return etree.tostring(root).decode('utf-8')

@needAuth
def streamXml(lines, delay):
    root = etree.Element('Data')
    text = etree.Element('text')
    root.append(text)
    number = etree.Element('number')
    text.text = 'x' * 512
    for i in range(lines):
        number.text = str(i)
        root.append(number)
        sleep(delay)
        yield etree.tostring(root).decode('utf-8')

@needAuth        
def streamJson(lines, delay):
    yield '['
    for i in range(lines):
        sleep(delay)
        dictLoad = {'Line'+str(i) : 'x'*512}
        yield json.dumps(dictLoad) + ','
    yield '{}]'

@needAuth        
def jsonPayload(lines, delay):
    resultList = [{'Line'+str(i) : 'x'*512} for i in range(lines)]
    sleep(delay)
    return json.dumps(resultList)
