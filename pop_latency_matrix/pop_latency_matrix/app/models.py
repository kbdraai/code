from django.db import models
'''Using a database or some other data structure will prove to be 
    useful to not only store latency data but also other test data.
   I won't be implementing this code code as it is beyond the requirement
   for this interview. I will leave it here for future expansion.
'''

class PointOfPresence(models.Model):
    '''This model details the information for each PoP involved 
        in this application.'''
    
    name = models.CharField(max_length=50)

class Tests(models.Model):
    '''This model details the tests that exist between the PoPs.
       The test type is detailed here as well and the unit for measurement
    '''

    type = models.ForeignKey('TestType')
    pop_a = models.ForeignKey(PointOfPresence, null=True, related_name='pop_a')
    pop_b = models.ForeignKey(PointOfPresence, null=True, related_name='pop_b')
    value = models.IntegerField(default=0)

class TestType(models.Model):
    '''This model provides the type of measurement and unit. '''

    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    
    

