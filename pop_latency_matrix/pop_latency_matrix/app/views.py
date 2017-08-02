"""
Definition of views.
"""

from django.shortcuts import render
from django.template import RequestContext
from datetime import datetime

from app.builder import TableBuilder, MeasurementBuilder
'''A better way of importing these urls is through a config file. And have a method 
    to modify the URL strings to make them readable by the urllib library.
   
'''
URLS = [
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

    table = TableBuilder(URLS)
    table.build_table() 

    return render(
        request,
        'app/index.html',
        {
            'title':'PoP Measurement Matrix',
            'year':datetime.now().year,
            'table':table
        }
    )


