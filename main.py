#!/usr/bin/env python
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
import cgi
import string 

form="""<form method="post">
    <b>Enter some text to ROT13:<b>
    <br>
    <textarea Name="text" style="width: 300px; height: 150px;">%(value)s</textarea>
    <br>
    <br>
    <input type="submit" value="Submit"> 
</form>
"""
def escape_html(s):
    return cgi.escape(s,quote = True)
    

def rot13(s):
    result = ""
    for v in s:
        c = ord(v)
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13
        result += chr(c)
    return result    
    
    
    
class MainHandler(webapp2.RequestHandler):

    def write_form(self,s=""):
        s = rot13(s)
        d={'value':escape_html(s)}
        self.response.write(form % d)
        
    def get(self):
        self.write_form()
    
    def post(self):
        s = self.request.get('text')
        self.write_form(s) 

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
