import requests
from gov_api_key import api_key

class GovInfoApi():

    def __init__(self):
        self.base_url = 'https://api.govinfo.gov/'
        self.api_key = api_key()


    def get_bills(self, start_date, end_date=None, offset=0, size=100):
        '''
        Grabs bill meta data from govinfo.gov

        Args:
            start_date (str): Earliest point that bill data will be grabbed. Form of: yyyy-mm-dd
            end_date (str): Latest point that bill data will be grabbed. Form of: yyyy-mm-dd
            offset (str): Number of bills to start off from first found
            size (str): Number of bills to have per page, a next page url is provided in respons

        Returns: Bill data in the form of a response object
        '''
        time = 'T00%3A00%3A00Z'
        path = '/'.join(('collections', 'BILLS', start_date + time))
        if end_date:
            path = '/' + end_date + time
            url = self.base_url + path
        else:
            url = self.base_url + path
        params = {
                'offset': offset,
                'pageSize': size,
                'api_key': self.api_key
                }
        return requests.get(url, params)

    def get_bill_data(self, package_id, content_type='xml'):
        path = '/'.join((self.base_url, 'packages', package_id, content_type))
        params = {'api_key': self.api_key}
        return requests.get(path, params)
