from django.test import TestCase
from django.utils.translation import ugettext

from postal.views import get_postal_form_class

class PostalTests(TestCase):
    def test_environment(self):
        """Just make sure everything is set up correctly."""
        self.assert_(True)
        
        
    def test_get_de_address(self):
        """
        Tests that we get the correct widget for Germny
        """
        german_form_class = get_postal_form_class("de")
        self.assertNotEqual(german_form_class, None)
        
        form = german_form_class()
        
        self.assertEqual(form.fields['line1'].label, "Company name")
        self.assertEqual(form.fields['line2'].label, "Street")
        self.assertEqual(form.fields['line3'].label, "City")
        self.assertEqual(form.fields['line4'].label, "State")
        self.assertEqual(form.fields['line5'].label, "Zip Code")
    
    def test_get_ie_address(self):
        """
        Tests that we get the correct widget for Ireland
        """
        irish_form_class = get_postal_form_class("ie")
        self.assertNotEqual(irish_form_class, None)

        form = irish_form_class()
        
        self.assertEqual(form.fields['line1'].label, "House/Company name")
        self.assertEqual(form.fields['line2'].label, "Street")
        self.assertEqual(form.fields['line3'].label, "Area")
        self.assertEqual(form.fields['line4'].label, "Town/City")
        self.assertEqual(form.fields['line5'].label, "County")
    
    
    def test_incorrect_country_code(self):
        """
        Tests that we don't throw an exception for an incorrect country code
        """
        no_country_form_class = get_postal_form_class("xx")
        self.assertNotEqual(no_country_form_class, None)
        
        form = no_country_form_class()
        
        self.assertEqual(form.fields['line1'].label, "Company name")
        self.assertEqual(form.fields['line2'].label, "Street")
        self.assertEqual(form.fields['line3'].label, "City")
        self.assertEqual(form.fields['line4'].label, "State")
        self.assertEqual(form.fields['line5'].label, "Zip Code")
    
