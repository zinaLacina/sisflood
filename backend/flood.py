from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from flood_controller import FloodController
import os, re

application = Flask(__name__)
api = Api(application)
CORS(application)

# REF_WHITE_LIST = os.environ['REF_WHITE_LIST']

# ref_white_list_arr = [x.strip() for x in REF_WHITE_LIST.split(",")]

# def isDomainWhiteList(incoming_url, domain_list): 
#     for domain in domain_list:
#          if incoming_url.find(domain) > 0:
#             return True
#     return False

class FloodAPI(Resource):

    def post(self):
        json_data = request.get_json()
        latitude = json_data['latitude']
        longitude = json_data['longitude']
        start_date = json_data['start_date']
        end_date = json_data['end_date']
        #print(json_data)
        flood = FloodController()
        ezw_reports = flood.getWeatherReports(start_date, end_date, latitude,longitude)
        return {'reports': ezw_reports}

        # referrer = re.search("^(http:\/\/|https:\/\/)+[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}", request.headers.get("Referer"))
        # #print("Referrer: [{}]".format(referrer))
        # if (referrer and (isDomainWhiteList(referrer.group(), ref_white_list_arr) > 0)):
        #     flood = FloodController()
        #     ezw_reports = flood.getWeatherReports(start_date, end_date, latitude,
        #                                     longitude)
        #     return {'reports': ezw_reports}
        # else: 
        #     return {'message': 'Service is blocked'}


api.add_resource(FloodAPI, '/api/floodapi')

@application.route('/api')
def hello():
    return 'Hello World! I have been seen'

if __name__ == '__main__':
    application.debug = False
    application.run(host="0.0.0.0", port=5000)
