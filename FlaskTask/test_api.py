import pytest
from FlaskTask.api import create_app
from .test_vars import *

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    client = app.test_client()
    return client

cases = [
    ('/api/report/', 200, out1),
    ('/api/report/drivers/', 200, out1),
    ('/api/report/drivers/?driver_id=SVF', 200, out2),
    ('/api/report/drivers/?order=desc', 200, out3)
]

@pytest.mark.parametrize('param,expected_code,expected_json', cases)
def test_post_json(client,param,expected_code,expected_json):
    result=client.get(param)
    assert result.is_json==True
    assert result.get_json()['response']==expected_json
    assert result.status_code==expected_code

# @pytest.mark.parametrize('param,expected_code,expected_xml', cases)
# def test_post_xml(client,param,expected_code,expected_xml):
#     result=client.get(param)
#     assert result.is_json==False
#     assert result.get_data()['response']==expected_xml
#     assert result.status_code==expected_code