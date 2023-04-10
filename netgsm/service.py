import os
import re

import requests

from netgsm.error_code import ErrorCode
from netgsm.exception import NetGsmException, ErrorCodes


class SmsService:
    params = dict()
    API_URL = 'https://api.netgsm.com.tr'
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

    def send_sms(self, phone, message, url='/sms/send/get', header=None):
        try:
            if header is None:
                header = self.user_code
            self.params.update({'gsmno': phone,
                                'message': message,
                                'msgheader': header})
            response = requests.get(
                f'{self.API_URL}{url}',
                params=self.params,
            )
            self.check_sms_status(response)
            return True
        except Exception as e:
            raise NetGsmException(e.__str__())

    def send_otp(self, phone, message, url='/sms/send/otp', header=None):
        try:
            if header is None:
                header = self.user_code
            xmlData = f'<?xml version="1.0"?><mainbody><header><usercode>{self.user_code}</usercode><password>{self.user_password}</password><msgheader>{header}</msgheader></header><body><msg><![CDATA[{message}]] ></msg><no>{phone}</no></body></mainbody>'
            headers = {'Content-Type': 'application/xml'}
            response = requests.post(
                f'{self.API_URL}{url}',
                data=xmlData, headers=headers
            )
            self.check_sms_status(response)
            return True
        except Exception as e:
            raise NetGsmException(e.__str__())

    def check_sms_status(self, response):
        response = response.text
        response_code = re.search('[0-9]+', response).group()
        self.is_sms_send = int(response_code) not in ErrorCode.sms_error_codes
        if self.is_sms_send:
            return
        raise NetGsmException(ErrorCode.sms_error_codes[response_code])
