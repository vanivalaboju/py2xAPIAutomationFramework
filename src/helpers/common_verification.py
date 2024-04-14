def verify_http_status_code(response_data,expect_data):
    assert response_data.status_code == expect_data ,"Failed ER!==AR"
def verify_json_key_for_not_null(key):
    assert key != 0, "Failed-Key is not empty" + key
    assert key > 0, "Failed-Key is greater than zero"
def verify_response_key_should_not_be_none(key):
    assert key is not None

# Common Verification
# HTTP Status code
# Headers
# Data Verification
# JSON Schema