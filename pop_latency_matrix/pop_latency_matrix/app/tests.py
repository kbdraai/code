"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from app.builder import MeasurementBuilder

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Matrix', 4, 200)

class BuilderTest(TestCase):
    '''Tests for the builder.py module'''

    def test_get_request(self):
        measurement_builder = MeasurementBuilder()
        self.assertIn('Johannesburg', measurement_builder._json_api_call(
            'http://sl-01-jnb.za.seacomnet.com//latencymatrix//getlatency.php'))

    def test_builder(self):
        table_builder = TableBuilder([
        'http://sl-01-ams.nl.seacomnet.com//latencymatrix//getlatency.php',])
        table = table_builder.build_table()
        self.assertGreater(len(table), 0)