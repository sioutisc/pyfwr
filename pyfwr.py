# =======================================================================
# Copyright 2017 Christos Sioutis <christos.sioutis@gmail.com>
# =======================================================================
# This file is part of pyfwr.
#
# pyfwr is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# pyfwr is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with pyfwr.
# If not, see <http://www.gnu.org/licenses/>.
# =======================================================================

import urllib
import urllib2
import base64
import json

FLIGHTXML_URI = "https://flightxml.flightaware.com/json/FlightXML2/"
HTTP_TIMEOUT = 10

def get(mapRequest):
	return get_json(mapRequest)

def get_json(mapRequest):
	return json.loads(get_str(mapRequest))

def get_str(mapRequest):
	req = mapRequest['operation'] + "?" + urllib.urlencode(mapRequest['inputs'])
	return http_request(mapRequest['credentials'],req)

def http_request(credentials,req):
        request = urllib2.Request("%s%s" % (FLIGHTXML_URI,req))
        request.add_header('User-Agent', "pyfwr")
        request.add_header('Authorization', http_auth_string(credentials))
        result = urllib2.urlopen(request,None,HTTP_TIMEOUT)
	return result.read()

def http_auth_string(credentials):
        base64string = base64.encodestring("%s:%s" % (credentials["username"], credentials["apikey"]))[:-1]
        return "Basic %s" % base64string
