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
import random

def getRandomFortune():
    #list of possible fortunes
    fortunes=["great", "medium good", "good", "bad", "horrible"]

    #randomly select one of the fortuens
    index=0
    index=random.randint(0,4)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        lucky_number=random.randint(1,100)
        header="<h1>Fortune Cookie</h1>"

        fortune="<strong>"+getRandomFortune()+"</strong>"
        fortune_paragraph="<p>"+number_sentence+"</p>"
        fortune_sentence="Your fortune: " +fortune

        lucky_number="<strong>"+random.randint(1,100)"</strong>"
        number_sentence="Your lucky number is "+str(lucky_number)
        number_paragraph="<p>"+number_sentence+"</p>"

        "<a ref='.'>cookie_again_button=<button>Another cookie please</button></a>"
        content=header+fortune_paragraph+number_paragraph

        self.response.write(header+number_sentence)
class LoginHandler(webapp2.RequestHandler):

]
app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)

class Cat:
    def meow():
        print("hi!")

hobbes=Cat()
