    # This file is part of GroupENG Online; this particular file may have been modified from its original
    # form as it was originally distributed as a part of GroupEng. The original copyright notice, similar
    # to this one, is intact below this notice.  

    # Copyright (C) 2020  Dr. Gabriel Walton, Eric Schmidt, Jean Duong, Cole Callihan, Stephen Thoemmes 

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU Affero General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU Affero General Public License for more details.

    # You should have received a copy of the GNU Affero General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>.

    # Below is the original copyright notice on the unmodified version of
    # GroupEng:

# Copyright 2011, Thomas G. Dimiduk
#
# This file is part of GroupEng.
#
# GroupEng is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GroupEng is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with GroupEng.  If not, see <http://www.gnu.org/licenses/>.

import math
from .errors import EmptyMean

def mean(l, key = lambda x: x):
    if hasattr(l, 'students'):
        l = l.students
    l = [key(x) for x in l if key(x) is not None]
    if len(l) == 0:
        raise EmptyMean()
    return sum(l)/len(l)

def std(l, key = lambda x: x):
    if hasattr(l, 'students'):
        l = l.students
    l = [x for x in l if key(x) is not None]
    v = [key(x) for x in l]
    m = mean(v)
    total = 0
    for x in v:
        total += (x-m)**2

    return math.sqrt(total/len(v))

def numberize(n):
    '''Turns a string into a number

    if the string is an integer return that integer
    if the string is a float return that float
    else return the string
    '''
    if isinstance(n, (int, float)):
        return n

    try:
        try:
            return int(n)
        except ValueError:
            try:
                return float(n)
            except ValueError:
                return n
    except TypeError:
        return n
