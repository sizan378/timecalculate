import random
import re

import jwt
# import requests
from django.core.validators import RegexValidator
from rest_framework.authentication import get_authorization_header

from MNTDebug.JWT_SETTINGS import JWT_SETTINGS

# A validator that checks if the phone number is in the format of 011~019 followed by 8 digits
PHONE_REGEX = RegexValidator(
    regex=r'^01[13-9]\d{8}$',
    message="Phone number must be 11 digit & this format: '01*********'"
)


def Phone_number_validate(phone_number):
    """
    It checks if the phone number is in the format of 011~019 followed by 8 digits
    :param phone_number: The phone number to validate
    :return: A match object or None
    """
    return re.match(r'^01[13-9]\d{8}$', phone_number)


def generateOTP(phone_number):
    """
    It generates a random 6 digit number and returns it as a string
    :param phone_number: The phone number to which the OTP is to be sent
    :return: A random 6 digit number
    """
    otp = str(random.randint(100000, 999999))
    return otp


def tokenValidation(request):
    """
    It takes the token from the request header, decodes it, and returns the payload
    :param request: The request object that was sent to the view
    :return: The payload of the token.
    """
    token_header = get_authorization_header(request).decode('utf-8')
    token_header_split = token_header.split(" ")
    if token_header_split[0] == "Bearer":
        token = token_header_split[1]
        payload = jwt.decode(
            jwt=token, key=JWT_SETTINGS['SIGNING_KEY'],
            algorithms=['HS256']
        )
        return payload
    else:
        return None