class ErrorCodes:
    USER_PASSWORD_ERROR = 'User password tanımlayın!'
    USER_CODE_ERROR = 'User code tanımlayın!'
    SMS_SEND_ERROR = 'Sms gönderilemedi!'


class NetGsmException(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
