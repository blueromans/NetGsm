# NetGsm Python PyPackage

NetGsm is the most popular sms provider at Turkey. NetGsm client is a Python library to access services quickly.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install NetGsm
```
## Environment Variables

```bash
NETGSM_USER_CODE: net gsm user code
NETGSM_USER_PASSWORD: net gsm user password
```
### Note
If you don't want to set this variables from global environment you can pass them to class.
You can see usage below
## Usage

```python
from netgsm import SmsService

kwargs = {
    # you can also set user code from environment.
    'user_code': 'net gsm user code', # Default value : None
    # you can also set user password from environment.
    'user_password': 'net gsm user password',  # Default value : None
    'api_url': 'net gsm api url'  # Default value : 'https://api.netgsm.com.tr/sms/send/get'
}
sms_service = SmsService(**kwargs)
sms_service.send(phone='Phone Number (5551234567)', message='Your Message', header='Your header')
# header default value : None if you don't pass this value your header is your user code
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
