import urllib.request
import json


class TableBuilder(list):
    '''This class builds a table to be rendered in the X template.
       The table consists of nested lists to enable seamless looping.
       This keeps the logic and heavy lifting in the python modules before
        rendering the view.

       Builder is a subclass of list making it iterable.
    '''

    def __init__(self, urls):
        self.urls = urls

    def build_table(self):
        '''The table list is created here. They are 2D nested lists. Process:

        1. The tests are retrieved from the APIs and put into a list of dictionaries.
        2. The first row and column are populated with the PoP names.
        3. The rest of the matrix is filled with the corresponding PoP measurement values.
        '''

        measurement_builder = MeasurementBuilder()
        measurement_values = measurement_builder._get_measurement_values(self.urls)
        first_row = [""]

        first_pop_name = measurement_values[0]
        first_pop_name = list(first_pop_name.keys())
        list_of_pop_names = measurement_values[0][first_pop_name[0]].keys()

        for pop in list_of_pop_names:
            first_row.append(pop)
        first_row = sorted(first_row)
        self.append(first_row)
        
        for index in range(1, len(first_row)):
            element = first_row[index]
            self.append([element,'','','','','','','','','','','','','','','',''])

        for measurement_value in measurement_values:
            pop = list(measurement_value.keys())[0]
            value_dict = measurement_value[pop]
            current_index = -1
            
            for index in range(1, len(self)-1):
                first_element = self[index]
                if(first_element[0].lower().strip() == pop.lower().strip()):
                    current_index = index
                    break
                
            for index in range(1, len(first_row)):
                column = first_row[index]
                self[current_index][index] = value_dict[column]
                               
        return self
            
            
class MeasurementBuilder():
    '''This class contains the methods necessary to retrieve measurement values. It also
        updates the database accordingly.

       For setting up the TestType and Point of Presence table use 
        values in a config file to populate.

       The retrieving of json data should be done as a cron job and results periodically
        updated to a file or data structure on the backend. The get function from the api 
        takes too long.
    '''

    def _get_measurement_values(self, urls):
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

''' def update_db_values(self, values):
    pop = values.keys()[0]
    value_dict = values[pop]

    for pop_name in value_dict.keys():
        PointOfPresence.objects.update_or_create(name=pop_name)

    TestType.objects.update_or_create(name="Latency", unit="ms")

    for key, value in value_dict.items():
        Tests.objects.filter(pop_a__name=pop, pop_b=key).update(value=int(value))
    
    Future expansion for when changes are to be tracked
'''



