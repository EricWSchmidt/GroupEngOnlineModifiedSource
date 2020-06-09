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

# Copyright 2011-2015, Thomas G. Dimiduk
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

class GroupEngFileError(Exception):
    def __init__(self, line, lineno, inf):
        self.line = line
        self.lineno = lineno
        self.inf = inf
    def __str__(self):
        return "Can't understand: {0} at line {1} of {2}".format(
            self.line, self.lineno, self.inf)

class EmptyMean(Exception):
    def __str__(self):
        return "Tried to take the mean of a set of zero items"
