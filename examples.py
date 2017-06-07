#!/usr/bin/python
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

import pyfwr

c = {'username':'your_username','apikey':'your_apikey'}

r1 = { 'credentials': c , 'operation': 'Search' , 'inputs': {'query':'-latlong "-36 137 -33 139"'} }
response = pyfwr.get(r1)
print '================= JSON RESPONSE ==================='
print response
print '==================================================='
for flight in response['SearchResult']['aircraft']:
	print 'Flight ' + flight['ident'] \
		+ ' of type ' + flight['type'] \
		+ ' at location ' + str(flight['latitude']) + ',' + str(flight['longitude']) \
		+ ' with altitude ' + str(flight['altitude'])

print

r2 = { 'credentials': c , 'operation': 'MetarEx' , 'inputs': {'airport':'YPAD','howMany':'2'} }
response2 = pyfwr.get(r2)
print '================= JSON RESPONSE ==================='
print response2
print '==================================================='
print 'The air temperature at YPAD airport is ' + str(response2['MetarExResult']['metar'][0]['temp_air']) + ' degrees'

print

r3 = { 'credentials': c , 'operation': 'Arrived' , 'inputs': {'airport':'YPAD','howMany':'10'} }
response3 = pyfwr.get(r3)
print '================= JSON RESPONSE ==================='
print response3
print '==================================================='
print 'The last 10 flights to arrive at YPAD are: '
for flight in response3['ArrivedResult']['arrivals']:
	print '   - ' + flight['ident'] + ' from ' + flight['origin']
