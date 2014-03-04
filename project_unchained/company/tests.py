from django.test import TestCase
from models import Company
from utils.testhelper import validate
# Create your tests here.
class CompanyTestCase(TestCase):
    def setUp(self):
        self.invalid_company = Company.objects.create(public=False, name="Invalid Company", www="www")
        self.valid_company = Company.objects.create(public=False, name="Valid Company", www="www.valid-company.com")
    
    def test_invalid_project_should_be_invalid(self):
        self.assertFalse(validate(self.invalid_company))
    
    def test_valid_project_should_be_valid(self):
        self.assertTrue(validate(self.valid_company))
        
    def test_valid_project_www_should_start_with_http(self):
        self.assertTrue(self.valid_company.www.startswith("http://"))
    
    def test_www_field_with_https_should_start_with_https(self):
        com = Company.objects.create(public=False, name="Test Corp", www="https://www.www.fi")
        self.assertTrue(com.www.startswith("https://"))
        self.assertEqual(com.www, "https://www.www.fi")
    
    def test_company_with_name_over_60_char_should_be_invalid(self):
        com = Company.objects.create(public=False, name="Test Corp Invalid Name is Super Duper Long So ridicusly long that there is now way that the name should ever be this long Jeesus the name is so Long it should have some lorem ipsum with it")
        self.assertFalse(validate(com))
