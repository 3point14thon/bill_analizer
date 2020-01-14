import json
import requests
import pandas as pd
from gov_api_key import api_key
from xml_parser import mk_dict


class GovInfoApi():

    '''
    Object designed to interact with govinfo.gov to retrive bill data.
    Could be used or modified to extract other government data.

    Methods:

        get_collection:
                Grabs collection data from govinfo.gov

            Args:
                start_date (str): Earliest point that collection data will be
                grabbed.
                Form of: yyyy-mm-dd
                end_date (str): Latest point that collection data will be grabbed.
                Form of: yyyy-mm-dd
                offset (str): Number of collections to start off from first found
                size (str): Number of collection to have per page,
                a next page url is provided in respons

            Returns: Collection data in the form of a response object

        get_package_data:
            Grabs package data from govinfo.gov

            Args:
                package_id(str): ID given to package by govinfo.gov, can be found
                in collection information.
                content_type(str): The format of the text in returned object.
                Typical values: pdf, xml, htm, xls, mods, premis, zip

            Returns: Package data in the form of a response object

        mk_bill_df:
            Generates a pandas dataframe of bill data between the given dates
            or from the start date to either the end date or until the number
            of records gathered is equal to size.

            Args:
                start_date (str): Earliest point that bill data will be grabbed.
                end_date (str): Latest point that bill data will be grabbed.
                offset (int): Number of bills to skip from start_date.
                size (int): Number of records to grab.

            Returns: Pandas DataFrame containing bills.
    '''
    def __init__(self):
        self.base_url = 'https://api.govinfo.gov/'
        self.api_key = api_key()

    def get_collection(self, start_date, end_date=None,
                       collection='BILLS', offset=0, size=100):
        '''
        Grabs collection data from govinfo.gov

        Args:
            start_date (str): Earliest point that collection data will be
            grabbed.
            Form of: yyyy-mm-dd
            end_date (str): Latest point that collection data will be grabbed.
            Form of: yyyy-mm-dd
            offset (str): Number of collections to start off from first found
            size (str): Number of collection to have per page,
            a next page url is provided in respons

        Returns: Collection data in the form of a response object
        '''
        time = 'T00%3A00%3A00Z'
        path = '/'.join(('collections', collection, start_date + time))
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

    def get_package_data(self, package_id, content_type='xml'):
        '''
        Grabs package data from govinfo.gov

        Args:
            package_id(str): ID given to package by govinfo.gov, can be found
            in collection information.
            content_type(str): The format of the text in returned object.
            Typical values: pdf, xml, htm, xls, mods, premis, zip

        Returns: Package data in the form of a response object
        '''
        path = '/'.join((self.base_url, 'packages', package_id, content_type))
        params = {'api_key': self.api_key}
        return requests.get(path, params)

    def mk_bill_df(self, start_date, end_date=None, offset=0, size=100):
        '''
        Generates a pandas dataframe of bill data between the given dates
        or from the start date to either the end date or until the number
        of records gathered is equal to size.

        Args:
            start_date (str): Earliest point that bill data will be grabbed.
            end_date (str): Latest point that bill data will be grabbed.
            offset (int): Number of bills to skip from start_date.
            size (int): Number of records to grab.

        Returns: Pandas DataFrame containing bills.
        '''
        bills_collection = self.get_collection(start_date, end_date, 'BILLS',
                                               offset, size)
        bills_collection = json.loads(bills_collection.text)['packages']
        bills = []
        for bill in bills_collection:
            package = self.get_package_data(bill['packageId'])
            bills.append(mk_dict(package.text))
        return pd.DataFrame(bills)
