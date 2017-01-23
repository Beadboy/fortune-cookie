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

def random_fortune():
    fortune_list = [
        """Never give yourself up, never let yourself down, 
        never run around or desert you""",
        "Everybody makes mistakes, everybody has those days",
        """If there were two guys on the moon and one of them killed the other with a rock 
        would that be fucked up or what?""",
        "When in doubt, think of Harambe",
        "You'll have an awesome today!"
    ]

    random_index = random.randrange(len(fortune_list))

    return fortune_list[random_index]

class MainHandler(webapp2.RequestHandler):
    def get(self):

        # The fortune stuff
        title = "<h1> Fortune Cookie </h1>"
        fortune_phrase = "<p> <q> " + random_fortune() + " </q> </p>"
        fortune_full = "<strong> Your Fortune is: </strong>" + fortune_phrase

        # The number stuff
        lucky_number = "<p> <q> " + str(random.randrange(101)) + " </q> </p>"
        lucky_number_full = "<strong> Your Lucky Number is: </strong>" + lucky_number

        # Refresh button
        refresh_button = "<a href = '.'> <button> Another Wise Fortune </button> </a>"
        
        # Finish
        content = title + fortune_full + lucky_number_full + refresh_button
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
