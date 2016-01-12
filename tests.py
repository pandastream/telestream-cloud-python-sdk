# -*- coding: utf-8 -*-
import unittest
from httmock import all_requests, HTTMock
from freezegun import freeze_time
import json

from telestream_cloud import TelestreamCloud

try:
    import urllib.parse as parser
except ImportError:
    import urlparse as parser


class BasicSetup(unittest.TestCase):

    def setUp(self):
        self.tc = TelestreamCloud(access_key='acck', secret_key='seck')

    def test_access_key(self):
        self.assertEqual(self.tc.access_key, 'acck')

    def test_secret_key(self):
        self.assertEqual(self.tc.secret_key, 'seck')

    def test_factory_id(self):
        self.assertEqual(self.tc.factory_id, None)

    def test_api_host(self):
        self.assertEqual(self.tc.api_host, 'api-gce.pandastream.com')

    def test_api_port(self):
        self.assertEqual(self.tc.api_port, 443)

    def test_api_version(self):
        self.assertEqual(self.tc.api_version, '3.0')


class RestAPI(unittest.TestCase):

    def setUp(self):
        self.tc = TelestreamCloud(access_key='my_access_key',
                                  secret_key='my_secret_key',
                                  api_host='myapihost',
                                  api_port=85, factory_id='my_cloud_id')

    def test_get(self):

       @all_requests
       def api_url(url, request):
           query_params = dict(parser.parse_qsl(url.query))
           self.assertEqual(query_params['signature'], '6tgl7r/9knHL5AhXqN3p3KXX74ofMrr7tBy6A7LL79s=')
           self.assertEqual(query_params['timestamp'], '2015-12-30T20:21:00+00:00')
           return {'status_code': 200}

       with HTTMock(api_url), freeze_time("2015-12-30 20:21"):
           response = self.tc.get('/factories.json')

    def test_post_with_no_params(self):

        @all_requests
        def api_url(url, request):
            query_params = dict(parser.parse_qsl(url.query))
            self.assertEqual(query_params['signature'], 'NoqEko/YOPhSfxvltZNd6AbStBvnMwptaEsFUmfXWPw=')
            self.assertEqual(query_params['timestamp'], '2009-11-04T17:54:11+00:00')
            return {'status_code': 200}

        with HTTMock(api_url), freeze_time('2009-11-04T17:54:11+00:00'):
            response = self.tc.post('/videos.json')

    def test_post_with_arguments(self):

        @all_requests
        def api_url(url, request):
            query_params = dict(parser.parse_qsl(url.query))
            self.assertEqual(query_params['signature'], '0xryIngb+aZNfTcwl/91lU6nAKouyvUq+fZJ84+KXbo=')
            self.assertEqual(query_params['timestamp'], '2009-11-04T17:54:11+00:00')
            self.assertEqual(query_params['param1'], 'one')
            self.assertEqual(query_params['param2'], 'two')
            return {'status_code': 200}

        with HTTMock(api_url), freeze_time('2009-11-04T17:54:11+00:00'):
            response = self.tc.post('/videos.json', {'param1': 'one', 'param2': 'two'})

    def test_post_with_file_argument(self):

        @all_requests
        def api_url(url, request):
            query_params = dict(parser.parse_qsl(url.query))
            self.assertEqual(query_params['signature'], '0xryIngb+aZNfTcwl/91lU6nAKouyvUq+fZJ84+KXbo=')
            self.assertEqual(query_params['timestamp'], '2009-11-04T17:54:11+00:00')
            self.assertEqual(query_params['param1'], 'one')
            self.assertEqual(query_params['param2'], 'two')
            self.assertTrue('file' not in query_params)
            return {'status_code': 200}

        with HTTMock(api_url), freeze_time('2009-11-04T17:54:11+00:00'):
            response = self.tc.post('/videos.json', {'param1': 'one', 'param2': 'two', 'file': __file__})

    def test_params_with_difficult_characters(self):

        @all_requests
        def api_url(url, request):
            query_params = dict(parser.parse_qsl(url.query))
            self.assertEqual(query_params['signature'], '/pahnvDahQqhfg8WcW7fu7SUGowWsQ7+kzq9vQ0/yvY=')
            self.assertEqual(query_params['timestamp'], '2009-11-04T17:54:11+00:00')
            self.assertEqual(query_params['tilde'], '~')
            self.assertEqual(query_params['slash'], '/')
            self.assertEqual(query_params['space'], ' ')
            return {'status_code': 200}

        with HTTMock(api_url), freeze_time('2009-11-04T17:54:11+00:00'):
            response = self.tc.post('/videos.json', {'tilde': '~', 'space': ' ', 'slash': '/'})

    def test_params_with_non_string_arguments(self):

        @all_requests
        def api_url(url, request):
            query_params = dict(parser.parse_qsl(url.query))
            self.assertEqual(query_params['signature'], 'U955cX1+IK76eY8gvy4OEf+aDXeMPW8/SWA7PmoOvOs=')
            self.assertEqual(query_params['timestamp'], '2009-11-04T17:54:11+00:00')
            return {'status_code': 200}

        with HTTMock(api_url), freeze_time('2009-11-04T17:54:11+00:00'):
            response = self.tc.post('/videos.json', {'param2': 2})


    def test_params_with_unicode_characters(self):

        @all_requests
        def api_url(url, request):
            query_params = dict(parser.parse_qsl(url.query))
            self.assertEqual(query_params['signature'], '3UFfzALe0OEMNGi7S8O/ZiNp4+vMVE8Kaw1Ab31ZvqE=')
            self.assertEqual(query_params['timestamp'], '2014-12-22T17:54:11+00:00')
            self.assertEqual(query_params['file_name'], 'original♥.mp4')

            return {'status_code': 200}

        with HTTMock(api_url), freeze_time('2014-12-22T17:54:11+00:00'):
            response = self.tc.post('/videos/upload.json', {'file_name': u'original♥.mp4'})


class ModelTests(unittest.TestCase):

    def setUp(self):
        self.tc = TelestreamCloud(access_key='my_access_key',
                                  secret_key='my_secret_key')
        self.flip = self.tc.get_resource('flip')

    def test_separate_cloud_credentials(self):
        self.assertTrue('factory_id' not in self.tc._credentials())

        @all_requests
        def api_url(url, request):
            factory_array = [{'id': 'factory_id_XXX', 'name': 'factory_one'},
                             {'id': 'factory_id_YYY', 'name': 'factory_two'}]
            return {'status_code': 200,
                    'content': json.dumps(factory_array).encode('utf-8')}

        with HTTMock(api_url):
            factories = self.flip.factories.all()

        self.assertTrue(len(factories) == 2)
        self.assertEqual(factories[0].name, 'factory_one')
        self.assertEqual(factories[0].id, 'factory_id_XXX')
        self.assertEqual(factories[0].credentials['factory_id'], 'factory_id_XXX')
        self.assertEqual(factories[1].name, 'factory_two')
        self.assertEqual(factories[1].id, 'factory_id_YYY')
        self.assertEqual(factories[1].credentials['factory_id'], 'factory_id_YYY')


if __name__ == '__main__':
    unittest.main()
