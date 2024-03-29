import pytest
from FlaskTask.api import create_app
from ..db.models import *
from ..db.main import create_db, parse_data_to_db
import os


@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    create_db(os.path.join(os.path.dirname(__file__), 'monaco1.db'))
    parse_data_to_db(
        os.path.join(
            os.path.dirname(__file__),
            '../static/reports'))
    with app.test_client() as client:
        yield client
    db.drop_tables([Driver, Race])


@pytest.mark.parametrize('case_number', [0, 1, 2])
def test_post_json(client, case_number, cases):
    param, expected_code, expected_json = cases(case_number)
    result = client.get(param, headers={"Accept": "application/json"})
    assert result.is_json
    assert result.get_json()['response'] == expected_json
    assert result.status_code == expected_code


@pytest.mark.parametrize('case_number', [0, 1, 2])
def test_post_xml(client, case_number, cases_xml):
    param, expected_code, expected_xml = cases_xml(case_number)
    result = client.get(param, headers={"Accept": "application/xml"})
    assert result.is_json == False
    assert result.get_data() == expected_xml
    assert result.status_code == expected_code
