#!/usr/bin/python
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

"""
External GroupEng Application.  Handles user invocation and marshalls things for
use by the rest of GroupEng
tkn
.. moduleauthor:: Thomas G. Dimiduk tgd8@cornell.edu
"""

import sys
import os.path
import os
from .src import controller
import logging
#from tkinter.messagebox import showerror, showinfo
def run(specificationFile):
    print("in run")
    log = logging.getLogger('log')
    log.setLevel(logging.DEBUG)
    fh = logging.FileHandler('GroupEng.log', mode='w')
    fh.setLevel(logging.DEBUG)
    log.addHandler(fh)
    
    # import gui stuff only if we are going to use it


    log.debug("inported gui")

    #pass in .groupEng file made instea
    path = specificationFile
    log.debug("Got file path: "+path)
    d, f = os.path.split(path)
    os.chdir(d)
    log.debug("Changed directory to: "+d)
    print("Changed directory to: "+d)
    print("Controller path: "+f)
    try:
        status, outdir = controller.run(f)
        log.debug('ran groupeng, results are in: '+outdir)
    except Exception as e:
        print('GroupEng Error', '{0}'.format(e))
            
#        if status:
#            showinfo("GroupEng", "GroupEng Run Succesful\n Output in: {0}".format(outdir))
#        else:
#            showinfo("GroupEng", "GroupEng Ran Correctly but not all rules could be met\n"
#                     "Output in: {0}".format(outdir))
