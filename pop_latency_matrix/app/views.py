"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from app.builder import TableBuilder, MeasurementBuilder
from app.models import Tests
'''A better way of importing these urls is through a config file.
   
'''
urls = [
    'http://sl-01-ams.nl.seacomnet.com//latencymatrix//getlatency.php',
    'http://sl-01-cpt.za.seacomnet.com//latencymatrix//getlatency.php',
    'http://sl-01-dar.tz.seacomnet.com//latencymatrix//getlatency.php', 
    'http://sl-01-dur.za.seacomnet.com//latencymatrix//getlatency.php', 
    'http://sl-01-fra.de.seacomnet.com//latencymatrix//getlatency.php',
    'http://sl-01-jnb.za.seacomnet.com//latencymatrix//getlatency.php',
    'http://sl-01-ebb.ug.seacomnet.com//latencymatrix//getlatency.php',
    'http://sl-01-kgl.rw.seacomnet.com//latencymatrix//getlatency.php', 
    'http://sl-01-lhr.uk.seacomnet.com//latencymatrix//getlatency.php',
    'http://sl-01-mpm.mz.seacomnet.com//latencymatrix//getlatency.php',
    'http://sl-01-mrs.fr.seacomnet.com//latencymatrix//getlatency.php',        
    'http://sl-01-mba.ke.seacomnet.com//latencymatrix//getlatency.php',
    'http://sl-01-emg.za.seacomnet.com//latencymatrix//getlatency.php',
    'http://sl-01-nbo.ke.seacomnet.com//latencymatrix//getlatency.php',
    'http://sl-02-lhr.uk.seacomnet.com//latencymatrix//getlatency.php',
    'http://sl-01-arn.se.seacomnet.com//latencymatrix//getlatency.php'    
    ]


def home(request):
    """Renders the home page."""

    return render(
        request,
        'app/index.html',
        {
            'title':'PoP Measurement Matrix',
            'year':datetime.now().year,
        }
    )

def get_matrix():
    '''This function gets the matrix to be displayed in the X template.

       1. Get a list of the measurements between PoPs.
       2. Update the db with the new values.
       3. Build the table to be rendered in the X template.
    '''
    measurements_list = MeasurementBuilder.get_measurement_values(urls)
    measurements_list.update_db_values(measurements_list)
    table_builder = TableBuilder()
    return table_builder.build_table()

json_temp = "{'Johannesburg': {'Amsterdam': '163.234', 'Cape Town': '16.316', 'Dar Es Salaam': '48.885', 'Durban': '12.476', 'Frankfurt': '174.137', 'Johannesburg': '0', 'Kampala': '60.521', 'Kigali': '69.451', 'London': '155.964', 'Maputo': '17.120', 'Marseille': '158.038', 'Mombasa': '46.514', 'Mtunzini': '9.846', 'Nairobi': '52.297', 'Slough': '156.325', 'Stockholm': '181.531'}}"
