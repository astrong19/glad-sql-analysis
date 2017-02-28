import os
import json
import csv
import StringIO
import logging

from flask import jsonify, request, Response, stream_with_context
import requests

from . import endpoints
from gladanalysis.responders import ErrorResponder
from gladanalysis.utils.http import request_to_microservice

@endpoints.route('/gladanalysis', methods=['GET'])
def query_glad():
    """Query GLAD"""
    logging.info('QUERYING GLAD')

    geostore = request.args.get('geostore')

    datasetID = '274b4818-be18-4890-9d10-eae56d2a82e5'
    url = 'http://staging-api.globalforestwatch.org/query/'
    sql = "?sql=select count(julian_day) from index_b846230fcec0420892d13fc11ea7e32b where ((year = '2015' and julian_day >= 1) or (year = '2016') or (year = '2017' and julian_day <= 58))"
    prefix = '&geostore='
    f = '&format=json'

    full = url + datasetID + sql + prefix + geostore + f
    r = requests.get(url=full)
    data = r.json()

    return jsonify({'data': data}), 200
