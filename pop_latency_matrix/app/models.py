from django.db import models

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

class TestType(models.Model):
    '''This model provides the type of measurement and unit. '''
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)

