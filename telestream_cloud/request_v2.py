import request
import requests
import json
import hashlib

class TelestreamCloudRequest(request.TelestreamCloudRequest):
    def send(self):
        response = getattr(requests, self.verb.lower())(self.requests_url, headers = {'Content-Type' : 'application/json'},
                                                        data = json.dumps(self.data))
        if not response.ok:
            msg = "Error %d, %s" % (response.status_code, response.reason)
            if response.text:
                msg += response.text
            raise TelestreamCloudException(msg, response)

        return response

    def signed_params(self):
        if self.verb.lower() in ['post', 'put']:
            return self.__signed_params()
        else:
            return super(self.__class__, self).signed_params()

    def __signed_params(self):
        auth_params = {
            'signature_version' : '2',
            'access_key' : self.cred['access_key'],
            'timestamp' : self.timestamp or self.generate_timestamp(),
            'checksum' : hashlib.sha256(json.dumps(self.data)).hexdigest(),
        }

        if 'factory_id' in self.cred.keys():
            auth_params['factory_id'] = self.cred['factory_id']

        auth_params['signature'] = self.generate_signature(
            self.verb,
            self.path,
            self.cred['api_host'],
            self.cred['secret_key'],
            auth_params)

        return auth_params



class TelestreamCloudException(request.TelestreamCloudException):
    pass
