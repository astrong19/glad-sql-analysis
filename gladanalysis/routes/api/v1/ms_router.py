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
def get_geo():

    geostore = request.args.get('geostore')
    return geostore

def query_glad():
    """Query GLAD"""
    logging.info('QUERYING GLAD')

    url = 'http://staging-api.globalforestwatch.org/query/'
    sql = "?sql=count(julian_day) from index_b846230fcec0420892d13fc11ea7e32b where ((year = '2015' and julian_day >= 1) or (year = '2016') or (year = '2017' and julian_day <= 58))"
    f = '&format=json'
    geostore = '&geostore=%s' %(get_geo)

    request = url + geostore + sql + f
    r = requests.get(request)

    return jsonify(r.json()), 200
