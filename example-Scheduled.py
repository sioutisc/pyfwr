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

req = { 'credentials': c , 'operation': 'Scheduled' , 'inputs': {'airport':'YSSY','filter':'airline'} }
response = pyfwr.get(req)
print '================= JSON RESPONSE ==================='
print response
print '==================================================='
