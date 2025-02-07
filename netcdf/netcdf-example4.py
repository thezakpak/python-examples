#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,
# Dimensions in a netCDF file.

from netCDF4 import Dataset
rootgrp = Dataset("test.nc", "a")
fcstgrp = rootgrp.createGroup("forecasts")
analgrp = rootgrp.createGroup("analyses")

print(rootgrp.groups)

level = rootgrp.createDimension("level", None)
time = rootgrp.createDimension("time", None)
lat = rootgrp.createDimension("lat", 73)
lon = rootgrp.createDimension("lon", 144)

print(rootgrp.dimensions)

print(len(lon))
print(lon.isunlimited())
print(time.isunlimited())

for dimobj in rootgrp.dimensions.values():
    print(dimobj)
