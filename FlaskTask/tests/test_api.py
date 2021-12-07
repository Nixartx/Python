import pytest
from FlaskTask.api import create_app



@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    client = app.test_client()
    return client


# cases = [
#     ('/api/v1/report/', 200, out1),
#     ('/api/v1/report/?driver_id=SVF', 200, out2),
#     ('/api/v1/report/?order=desc', 200, out3)
# ]

# cases_xml = [
#     ('/api/v1/report/', 200, xml_out1),
#     ('/api/v1/report/', 200, xml_out1),
#     ('/api/v1/report/?driver_id=SVF', 200, xml_out2),
#     ('/api/v1/report/?order=desc', 200, xml_out3),
# ]



@pytest.mark.parametrize('case_number',[0,1,2])
def test_post_json(client, case_number, cases):
    param, expected_code, expected_json=cases(case_number)
    result = client.get(param, headers={"Accept": "application/json"})
    assert result.is_json
    assert result.get_json()['response'] == expected_json
    assert result.status_code == expected_code



@pytest.mark.parametrize('case_number', [0,1,2])
def test_post_xml(client, case_number, cases_xml):
    param, expected_code, expected_xml = cases_xml(case_number)
    result = client.get(param, headers={"Accept": "application/xml"})
    assert result.is_json == False
    assert result.get_data() == expected_xml
    assert result.status_code == expected_code
