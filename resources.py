from flask import Response, request
from flask_restful import Resource, reqparse
from datetime import datetime
from time import sleep

class ip(Resource):
    
    @staticmethod
    def output_ip():
        forwardHeader = request.headers.get('X-Forwarded-For')
        clientIP = request.headers.get('X-Forwarded-For').split(',') if forwardHeader else 'No_X-Forwarded-For_Hdr'
        if request.headers.get('Accept') =='application/json':
            return {'ipAddr': clientIP}
        resp = Response(clientIP, mimetype='text/plain', headers=None)
        resp.status_code = 200
        return resp      
    
    def get(self):
        resp = ip.output_ip()
        return resp
        
    
class retrunCode(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('sleep', type=int, required=False)
    parser.add_argument('echo', type=str, required=False)
    
    @staticmethod
    def resLogin():
        args = retrunCode.parser.parse_args()
        sleepTime = args['sleep']
        echo = args['echo']
        echoMessage = echo if echo else 'None'
        sleep(sleepTime) if sleepTime and sleepTime < 10 else sleep(0)
        return {'sleep' : sleepTime if sleepTime and sleepTime < 10 else 'None', 'echoedMessage':echoMessage}
    
  
    def get(self, code):
        return retrunCode.resLogin(), code
    
    def post(self, code):
        return retrunCode.resLogin(), code


class bus_stop(Resource):
    
    @staticmethod
    def ttArrive(busStop):
        timeRange = {range(0,2):[10, 'Stop1'], range(2,4):[8, 'Stop2'], range(4,6):[6, 'Stop3'], range(6,8):[4, 'Stop4'], range(8,10):[2, busStop]}
        curMin = (lambda x: x //10**0 %10)(datetime.now().minute)
        minLeft = [v[0] for k,v in timeRange.items() if curMin in k][0]
        nextStop = [v[1] for k,v in timeRange.items() if curMin in k][0]
        return{'busStop': busStop ,'nextStop': nextStop, 'ttArrive': minLeft}
        
    def get(self, busStop):
        return bus_stop.ttArrive(busStop)
