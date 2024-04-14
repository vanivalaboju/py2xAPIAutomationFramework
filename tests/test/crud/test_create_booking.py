from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util
from src.helpers.common_verification import *

import pytest
import allure


class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that Create booking status and booking id shouldn't be null ")
    @allure.description("Creating a Booking from the payload and verify that booking id should not be null and status code is 200 for the correct payload")
    def test_create_booking_positive(self):
       #URL,payload,#headers
       response = post_request(url=APIConstants.url_create_booking(),
                               auth=None,
                               headers=Util().common_headers_json(),
                               payload=payload_create_booking(),
                               in_json=False)
       booking_id = response.json()["bookingid"]
       verify_http_status_code(response_data=response,expect_data=200)
       verify_json_key_for_not_null(booking_id)
    @pytest.mark.negative
    def test_create_booking_negative(self):
           # URL,payload,#headers
           response = post_request(url=APIConstants.url_create_booking(),
                                   auth=None,
                                   headers=Util().common_headers_json(),
                                   payload={},
                                   in_json=False)
           verify_http_status_code(response,500)




