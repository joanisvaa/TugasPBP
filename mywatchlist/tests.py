from django.test import TestCase
from django.urls import reverse
from mywatchlist.views import show_json, show_xml, show_mywatchlist, show_json_by_id, show_xml_by_id

# Create your tests here.

class Test(TestCase):
    def MyWatchList_test_html(self):
        response = self.client.get(reverse('mywatchlist:show_mywatchlist'))
        self.assertEqual(response.status_code,200);

    def MyWatchList_test_json(self):
        response = self.client.get(reverse('mywatchlist:show_json'))
        self.assertEqual(response.status_code,200);

    def MyWatchList_test_xml(self):
        response = self.client.get(reverse('mywatchlist:show_xml'))
        self.assertEqual(response.status_code,200);
    
    def MyWatchList_test_json_by_id(self):
        response = self.client.get(reverse('mywatchlist:show_json_by_id'))
        self.assertEqual(response.status_code,200);
    
    def MyWatchList_test_xml_by_id(self):
        response = self.client.get(reverse('mywatchlist:show_xml_by_id'))
        self.assertEqual(response.status_code,200);