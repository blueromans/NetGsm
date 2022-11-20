import os
import re

import requests

from netgsm.exception import NetGsmException, ErrorCodes


class SmsService:
    params = dict()
    API_URL = 'https://api.netgsm.com.tr/sms/send/get'
    error_codes = [20, 30, 40, 70]
    is_sms_send = False

    def __init__(self, user_code=None, user_password=None, api_url=None):
        self.user_code = os.environ.get('NETGSM_USER_CODE', user_code)
        if self.user_code is None:
            raise ValueError(ErrorCodes.USER_CODE_ERROR)
        self.user_password = os.environ.get('NETGSM_USER_PASSWORD', user_password)
        if self.user_password is None:
            raise ValueError(ErrorCodes.USER_PASSWORD_ERROR)
        if api_url is not None:
            self.API_URL = api_url
        self.params = {'usercode': self.user_code, 'password': self.user_password}

    def send(self, phone, message, header=None):
        try:
            if header is None:
                header = self.user_code
            self.params.update({'gsmno': phone,
                                'message': message,
                                'msgheader': header})
            response = requests.get(
                self.API_URL,
                params=self.params,
            )
            self.check_sms_status(response)
            if self.is_sms_send is False:
                raise NetGsmException(ErrorCodes.SMS_SEND_ERROR)
            return True
        except Exception as e:
            raise NetGsmException(e.__str__())

    def check_sms_status(self, response):
        response = response.text
        response_code = re.search('[0-9]+', response).group()
        self.is_sms_send = int(response_code) not in self.error_codes
