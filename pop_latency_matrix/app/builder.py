import urllib.request
import json


class TableBuilder(list):
    '''This class builds a table to be rendered in the X template.
       The table consists of nested lists to enable seamless looping.
       This keeps the logic and heavy lifting in the python modules before
        rendering the view.

       Builder is a subclass of list making it iterable. It implements the __iter__
        method to enable this function. This class can be instantiated as an object or 
        used in a static manner.
    '''

    def build_table(self):
        pass

    

class MeasurementBuilder():
    '''This class contains the methods necessary to retrieve measurement values. It also
        updates the database accordingly.
    '''

    def get_measurement_values(self, urls):
        measurement_values = []
        for url in urls:
            measurement_values.append(self._json_api_call(url))

        return measurement_values

    def _json_api_call(self, url):
        json_response = ""        

        try:            
            response = urllib.request.urlopen(url)
            json_response = json.loads(response.read())
            
        except urllib.error.URLError as e:
           print(e.reason)

        return json_response

    def update_db_values(self, values):
        pass