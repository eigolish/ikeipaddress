#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import cgi


from google.appengine.ext import ndb

class UserData(ndb.Model):
    address = ndb.StringProperty()
    pc = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):


        pc = "";
        address = "";
        address = os.environ['REMOTE_ADDR']
        #self.response.write(address)


        form = ""
        #これでフォームの情報を全て取得できる
        form = cgi.FieldStorage()


        if ( form.has_key("pc") ):
            pc = form["pc"].value

            self.response.write("<br>")
            #self.response.write(pc)


            user=UserData()
            user.pc = pc
            user.address = address
            user.put()

        iplist = UserData.query()
        self.response.out.write(iplist.get().address)


            #self.response.write("<br>")


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)