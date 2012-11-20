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
import cgi
import webapp2

from google.appengine.api import users
from google.appengine.api import mail

temp = {}
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
            <html>
            <body>
            <div class="left">
            <form action="/sign" method="post">
            <div>
            <h4>Enter email to:</h4>
            <textarea name="studentemail" rows="1" cols="30"></textarea>
            </div>
            <div>
            <h4>Enter email content:</h4>
            <textarea name="emailcontent" rows="5" cols="30"></textarea>
            </div>
            <div class="button">
            <input type="submit" value="set reminder for student appointment" >
            </div>
            </form>
            </div>
            </body>
            <div class="right">
            <h4>Scheduled reminders:</h4>
            <script>
            
            var d=new Date();
            document.write(d);
            
            </script>
            </div>
           
            <style>
            .left
            {
            margin-top:50px;
            margin-left:50px;
            width:250px;
            }
            .right
            {
            position:absolute;
            margin-top:-245px;
            margin-left:320px;
            }
            .button
            {
            position:relative;
            margin-top:10px;
            margin-left:5px;
            }
            </style>
            </html>
""")
    


class Guestbook(webapp2.RequestHandler):
    def post(self):
        mail.send_mail(sender="Lac Support <sfsu.lac.hss348@gmail.com>",
         to=cgi.escape(self.request.get('studentemail')),
         subject="LAC appointment reminder",
         body=cgi.escape(self.request.get('emailcontent')))
        self.response.out.write('<html><body>You have made an appointment for :<pre>')
        self.response.out.write("""</div>""")
        self.response.out.write("""<div>email to = """)
        self.response.out.write(cgi.escape(self.request.get('studentemail')))
        self.response.out.write("""</div>""")
        self.response.out.write("""<div>email content = """)
        self.response.out.write(cgi.escape(self.request.get('emailcontent')))
        self.response.out.write("""</div>""")
        # self.response.out.write(str(k[1]))
        self.response.out.write('</pre></body></html>')


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/sign', Guestbook)],
                              debug=True)

