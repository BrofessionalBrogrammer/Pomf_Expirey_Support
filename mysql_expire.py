#!/usr/bin/python3
# Russian Roulette IRC bot
# Created by Lance Brignoni on 10.5.15
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import time
import os
from datetime import datetime
import datetime
import MySQLdb
import MySQLdb.cursors
#make connection
conn = MySQLdb.Connect(
        #be sure to edit these
        host='localhost', user='',
        passwd='', db='',compress=1,
        cursorclass=MySQLdb.cursors.DictCursor)
cursor = conn.cursor()
#select expire, id, filename
cursor.execute("SELECT expire, id, filename FROM files")
rows = cursor.fetchall()
def expire_all():
        for row in rows:
                i = datetime.datetime.now()
                print(row['expire'])
                q = row['expire']
                #checks to see if datetime instance
                if isinstance(q, datetime.datetime):
                        if q < i: #checks if file is expired
                                f = row['filename']
                                u = row['id']
                                #deletes row from DB
                                id_query = "DELETE FROM files WHERE id = %s"
                                cursor.execute(id_query, [u])
                                #removes file
                                os.remove('/var/www/a.cocaine.ninja/%s' % f)
#call function and close connections
expire_all()
conn.commit()
cursor.close()
conn.close()                                                                                                                   1,1           All
