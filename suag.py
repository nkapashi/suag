import functions
import resources
from flask import Flask, Response, stream_with_context, request, render_template
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__, static_folder='static', static_url_path='')
app.url_map.strict_slashes = False
SWAGGER_URL = '/swagger'
API_URL = 'suag.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "SUAG"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
api = Api(app)
       

@app.route('/streamload')
def stream_load():
    mimeMap = {'application/xml':functions.streamXml, 'text/xml':functions.streamXml, 'text/plain':functions.stremText, 'application/json':functions.streamJson}
    lines = request.args.get('lines') if request.args.get('lines') is not None else 1
    delay = request.args.get('delay') if request.args.get('delay') is not None else 0
    if mimeMap.get(request.headers.get('Accept')):
        return Response(stream_with_context(mimeMap[request.headers.get('Accept')](int(lines), int(delay))), mimetype=request.headers.get('Accept'))
    else:
        return Response(stream_with_context(functions.stremText(int(lines), int(delay))), mimetype='text/plain')
 
@app.route('/payload')
def payLoad():
    mimeMap = {'application/xml':functions.xmlPayload,'text/xml':functions.xmlPayload,  'text/plain':functions.textPayload, 'application/json':functions.jsonPayload}
    lines = request.args.get('lines') if request.args.get('lines') is not None else 1
    delay = request.args.get('delay') if request.args.get('delay') is not None else 0
    if mimeMap.get(request.headers.get('Accept')):
        return Response(mimeMap[request.headers.get('Accept')](int(lines), int(delay)), mimetype=request.headers.get('Accept'))
    else:
        return Response(functions.textPayload(int(lines), int(delay)), mimetype='text/plain')

@app.route('/')
def readme():
    return render_template("readme.html")

api.add_resource(resources.retrunCode, '/codes/<int:code>')
api.add_resource(resources.bus_stop, '/bus_stop/<string:busStop>')
api.add_resource(resources.ip, '/ip')
api.add_resource(resources.qrcode, '/qr')

if __name__ == '__main__':
    app.run()