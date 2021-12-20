import pytest


@pytest.fixture()
def cases():
    out1 = ([{'LHM': {'car': 'MERCEDES',
                      'fullname': 'Lewis Hamilton',
                      'time': '0:53:12.460000',
                      'time_f': '2018-05-24 13:11:32.585000',
                      'time_s': '2018-05-24 12:18:20.125000'}},
             {'EOF': {'car': 'FORCE INDIA MERCEDES',
                      'fullname': 'Esteban Ocon',
                      'time': '0:54:13.028000',
                      'time_f': '2018-05-24 13:12:11.838000',
                      'time_s': '2018-05-24 12:17:58.810000'}},
             {'SSW': {'car': 'WILLIAMS MERCEDES',
                      'fullname': 'Sergey Sirotkin',
                      'time': '0:55:12.706000',
                      'time_f': '2018-05-24 13:11:24.354000',
                      'time_s': '2018-05-24 12:16:11.648000'}},
             {'DRR': {'car': 'RED BULL RACING TAG HEUER',
                      'fullname': 'Daniel Ricciardo',
                      'time': '0:57:12.013000',
                      'time_f': '2018-05-24 13:11:24.067000',
                      'time_s': '2018-05-24 12:14:12.054000'}},
             {'SVF': {'car': 'FERRARI',
                      'fullname': 'Sebastian Vettel',
                      'time': '1:01:04.415000',
                      'time_f': '2018-05-24 13:04:03.332000',
                      'time_s': '2018-05-24 12:02:58.917000'}},
             {'VBM': {'car': 'MERCEDES',
                      'fullname': 'Valtteri Bottas',
                      'time': '1:01:12.434000',
                      'time_f': '2018-05-24 13:01:12.434000',
                      'time_s': '2018-05-24 12:00:00.000000'}},
             {'SVM': {'car': 'MCLAREN RENAULT',
                      'fullname': 'Stoffel Vandoorne',
                      'time': '1:01:12.463000',
                      'time_f': '2018-05-24 13:19:50.198000',
                      'time_s': '2018-05-24 12:18:37.735000'}},
             {'KRF': {'car': 'FERRARI',
                      'fullname': 'Kimi RГ¤ikkГ¶nen',
                      'time': '1:01:12.639000',
                      'time_f': '2018-05-24 13:04:13.889000',
                      'time_s': '2018-05-24 12:03:01.250000'}},
             {'FAM': {'car': 'MCLAREN RENAULT',
                      'fullname': 'Fernando Alonso',
                      'time': '1:01:12.657000',
                      'time_f': '2018-05-24 13:14:17.169000',
                      'time_s': '2018-05-24 12:13:04.512000'}},
             {'CLS': {'car': 'SAUBER FERRARI',
                      'fullname': 'Charles Leclerc',
                      'time': '1:01:12.829000',
                      'time_f': '2018-05-24 13:10:54.750000',
                      'time_s': '2018-05-24 12:09:41.921000'}},
             {'SPF': {'car': 'FORCE INDIA MERCEDES',
                      'fullname': 'Sergio Perez',
                      'time': '1:01:12.848000',
                      'time_f': '2018-05-24 13:13:13.883000',
                      'time_s': '2018-05-24 12:12:01.035000'}},
             {'RGH': {'car': 'HAAS FERRARI',
                      'fullname': 'Romain Grosjean',
                      'time': '1:01:12.930000',
                      'time_f': '2018-05-24 13:06:27.441000',
                      'time_s': '2018-05-24 12:05:14.511000'}},
             {'PGS': {'car': 'SCUDERIA TORO ROSSO HONDA',
                      'fullname': 'Pierre Gasly',
                      'time': '1:01:12.941000',
                      'time_f': '2018-05-24 13:08:36.586000',
                      'time_s': '2018-05-24 12:07:23.645000'}},
             {'CSR': {'car': 'RENAULT',
                      'fullname': 'Carlos Sainz',
                      'time': '1:01:12.950000',
                      'time_f': '2018-05-24 13:04:28.095000',
                      'time_s': '2018-05-24 12:03:15.145000'}},
             {'NHR': {'car': 'RENAULT',
                      'fullname': 'Nico Hulkenberg',
                      'time': '1:01:13.065000',
                      'time_f': '2018-05-24 13:04:02.979000',
                      'time_s': '2018-05-24 12:02:49.914000'}},
             {'BHS': {'car': 'SCUDERIA TORO ROSSO HONDA',
                      'fullname': 'Brendon Hartley',
                      'time': '1:01:13.179000',
                      'time_f': '2018-05-24 13:16:05.164000',
                      'time_s': '2018-05-24 12:14:51.985000'}},
             {'MES': {'car': 'SAUBER FERRARI',
                      'fullname': 'Marcus Ericsson',
                      'time': '1:01:13.265000',
                      'time_f': '2018-05-24 13:05:58.778000',
                      'time_s': '2018-05-24 12:04:45.513000'}},
             {'LSW': {'car': 'WILLIAMS MERCEDES',
                      'fullname': 'Lance Stroll',
                      'time': '1:01:13.323000',
                      'time_f': '2018-05-24 13:07:26.834000',
                      'time_s': '2018-05-24 12:06:13.511000'}},
             {'KMH': {'car': 'HAAS FERRARI',
                      'fullname': 'Kevin Magnussen',
                      'time': '1:01:13.393000',
                      'time_f': '2018-05-24 13:04:04.396000',
                      'time_s': '2018-05-24 12:02:51.003000'}}])
    out2 = ([{'SVF': {'car': 'FERRARI', 'fullname': 'Sebastian Vettel', 'time': '1:01:04.415000', 'time_f': '2018-05-24 13:04:03.332000', 'time_s': '2018-05-24 12:02:58.917000'}}])
    out3 = ([{'KMH': {'car': 'HAAS FERRARI', 'fullname': 'Kevin Magnussen', 'time': '1:01:13.393000', 'time_f': '2018-05-24 13:04:04.396000', 'time_s': '2018-05-24 12:02:51.003000'}}, {'LSW': {'car': 'WILLIAMS MERCEDES', 'fullname': 'Lance Stroll', 'time': '1:01:13.323000', 'time_f': '2018-05-24 13:07:26.834000', 'time_s': '2018-05-24 12:06:13.511000'}}, {'MES': {'car': 'SAUBER FERRARI', 'fullname': 'Marcus Ericsson', 'time': '1:01:13.265000', 'time_f': '2018-05-24 13:05:58.778000', 'time_s': '2018-05-24 12:04:45.513000'}}, {'BHS': {'car': 'SCUDERIA TORO ROSSO HONDA', 'fullname': 'Brendon Hartley', 'time': '1:01:13.179000', 'time_f': '2018-05-24 13:16:05.164000', 'time_s': '2018-05-24 12:14:51.985000'}}, {'NHR': {'car': 'RENAULT', 'fullname': 'Nico Hulkenberg', 'time': '1:01:13.065000', 'time_f': '2018-05-24 13:04:02.979000', 'time_s': '2018-05-24 12:02:49.914000'}}, {'CSR': {'car': 'RENAULT', 'fullname': 'Carlos Sainz', 'time': '1:01:12.950000', 'time_f': '2018-05-24 13:04:28.095000', 'time_s': '2018-05-24 12:03:15.145000'}}, {'PGS': {'car': 'SCUDERIA TORO ROSSO HONDA', 'fullname': 'Pierre Gasly', 'time': '1:01:12.941000', 'time_f': '2018-05-24 13:08:36.586000', 'time_s': '2018-05-24 12:07:23.645000'}}, {'RGH': {'car': 'HAAS FERRARI', 'fullname': 'Romain Grosjean', 'time': '1:01:12.930000', 'time_f': '2018-05-24 13:06:27.441000', 'time_s': '2018-05-24 12:05:14.511000'}}, {'SPF': {'car': 'FORCE INDIA MERCEDES', 'fullname': 'Sergio Perez', 'time': '1:01:12.848000', 'time_f': '2018-05-24 13:13:13.883000', 'time_s': '2018-05-24 12:12:01.035000'}}, {'CLS': {'car': 'SAUBER FERRARI', 'fullname': 'Charles Leclerc', 'time': '1:01:12.829000', 'time_f': '2018-05-24 13:10:54.750000', 'time_s': '2018-05-24 12:09:41.921000'}}, {'FAM': {'car': 'MCLAREN RENAULT', 'fullname': 'Fernando Alonso', 'time': '1:01:12.657000', 'time_f': '2018-05-24 13:14:17.169000', 'time_s': '2018-05-24 12:13:04.512000'}}, {'KRF': {'car': 'FERRARI', 'fullname': 'Kimi RГ¤ikkГ¶nen', 'time': '1:01:12.639000', 'time_f': '2018-05-24 13:04:13.889000', 'time_s': '2018-05-24 12:03:01.250000'}}, {'SVM': {'car': 'MCLAREN RENAULT', 'fullname': 'Stoffel Vandoorne', 'time': '1:01:12.463000', 'time_f': '2018-05-24 13:19:50.198000', 'time_s': '2018-05-24 12:18:37.735000'}}, {'VBM': {'car': 'MERCEDES', 'fullname': 'Valtteri Bottas', 'time': '1:01:12.434000', 'time_f': '2018-05-24 13:01:12.434000', 'time_s': '2018-05-24 12:00:00.000000'}}, {'SVF': {'car': 'FERRARI', 'fullname': 'Sebastian Vettel', 'time': '1:01:04.415000', 'time_f': '2018-05-24 13:04:03.332000', 'time_s': '2018-05-24 12:02:58.917000'}}, {'DRR': {'car': 'RED BULL RACING TAG HEUER', 'fullname': 'Daniel Ricciardo', 'time': '0:57:12.013000', 'time_f': '2018-05-24 13:11:24.067000', 'time_s': '2018-05-24 12:14:12.054000'}}, {'SSW': {'car': 'WILLIAMS MERCEDES', 'fullname': 'Sergey Sirotkin', 'time': '0:55:12.706000', 'time_f': '2018-05-24 13:11:24.354000', 'time_s': '2018-05-24 12:16:11.648000'}}, {'EOF': {'car': 'FORCE INDIA MERCEDES', 'fullname': 'Esteban Ocon', 'time': '0:54:13.028000', 'time_f': '2018-05-24 13:12:11.838000', 'time_s': '2018-05-24 12:17:58.810000'}}, {'LHM': {'car': 'MERCEDES', 'fullname': 'Lewis Hamilton', 'time': '0:53:12.460000', 'time_f': '2018-05-24 13:11:32.585000', 'time_s': '2018-05-24 12:18:20.125000'}}])
    cases = [
        ('/api/v1/report/', 200, out1),
        ('/api/v1/report/?driver_id=SVF', 200, out2),
        ('/api/v1/report/?order=desc', 200, out3),
    ]

    def factory(case_number):
        return cases[case_number]

    return factory


@pytest.fixture()
def cases_xml():
    xml_out1 = b'<?xml version="1.0" ?><response><LHM><car>MERCEDES</car><fullname>Lewis Hamilton</fullname><time>0:53:12.460000</time><time_f>2018-05-24 13:11:32.585000</time_f><time_s>2018-05-24 12:18:20.125000</time_s></LHM><EOF><car>FORCE INDIA MERCEDES</car><fullname>Esteban Ocon</fullname><time>0:54:13.028000</time><time_f>2018-05-24 13:12:11.838000</time_f><time_s>2018-05-24 12:17:58.810000</time_s></EOF><SSW><car>WILLIAMS MERCEDES</car><fullname>Sergey Sirotkin</fullname><time>0:55:12.706000</time><time_f>2018-05-24 13:11:24.354000</time_f><time_s>2018-05-24 12:16:11.648000</time_s></SSW><DRR><car>RED BULL RACING TAG HEUER</car><fullname>Daniel Ricciardo</fullname><time>0:57:12.013000</time><time_f>2018-05-24 13:11:24.067000</time_f><time_s>2018-05-24 12:14:12.054000</time_s></DRR><SVF><car>FERRARI</car><fullname>Sebastian Vettel</fullname><time>1:01:04.415000</time><time_f>2018-05-24 13:04:03.332000</time_f><time_s>2018-05-24 12:02:58.917000</time_s></SVF><VBM><car>MERCEDES</car><fullname>Valtteri Bottas</fullname><time>1:01:12.434000</time><time_f>2018-05-24 13:01:12.434000</time_f><time_s>2018-05-24 12:00:00.000000</time_s></VBM><SVM><car>MCLAREN RENAULT</car><fullname>Stoffel Vandoorne</fullname><time>1:01:12.463000</time><time_f>2018-05-24 13:19:50.198000</time_f><time_s>2018-05-24 12:18:37.735000</time_s></SVM><KRF><car>FERRARI</car><fullname>Kimi R\xd0\x93\xc2\xa4ikk\xd0\x93\xc2\xb6nen</fullname><time>1:01:12.639000</time><time_f>2018-05-24 13:04:13.889000</time_f><time_s>2018-05-24 12:03:01.250000</time_s></KRF><FAM><car>MCLAREN RENAULT</car><fullname>Fernando Alonso</fullname><time>1:01:12.657000</time><time_f>2018-05-24 13:14:17.169000</time_f><time_s>2018-05-24 12:13:04.512000</time_s></FAM><CLS><car>SAUBER FERRARI</car><fullname>Charles Leclerc</fullname><time>1:01:12.829000</time><time_f>2018-05-24 13:10:54.750000</time_f><time_s>2018-05-24 12:09:41.921000</time_s></CLS><SPF><car>FORCE INDIA MERCEDES</car><fullname>Sergio Perez</fullname><time>1:01:12.848000</time><time_f>2018-05-24 13:13:13.883000</time_f><time_s>2018-05-24 12:12:01.035000</time_s></SPF><RGH><car>HAAS FERRARI</car><fullname>Romain Grosjean</fullname><time>1:01:12.930000</time><time_f>2018-05-24 13:06:27.441000</time_f><time_s>2018-05-24 12:05:14.511000</time_s></RGH><PGS><car>SCUDERIA TORO ROSSO HONDA</car><fullname>Pierre Gasly</fullname><time>1:01:12.941000</time><time_f>2018-05-24 13:08:36.586000</time_f><time_s>2018-05-24 12:07:23.645000</time_s></PGS><CSR><car>RENAULT</car><fullname>Carlos Sainz</fullname><time>1:01:12.950000</time><time_f>2018-05-24 13:04:28.095000</time_f><time_s>2018-05-24 12:03:15.145000</time_s></CSR><NHR><car>RENAULT</car><fullname>Nico Hulkenberg</fullname><time>1:01:13.065000</time><time_f>2018-05-24 13:04:02.979000</time_f><time_s>2018-05-24 12:02:49.914000</time_s></NHR><BHS><car>SCUDERIA TORO ROSSO HONDA</car><fullname>Brendon Hartley</fullname><time>1:01:13.179000</time><time_f>2018-05-24 13:16:05.164000</time_f><time_s>2018-05-24 12:14:51.985000</time_s></BHS><MES><car>SAUBER FERRARI</car><fullname>Marcus Ericsson</fullname><time>1:01:13.265000</time><time_f>2018-05-24 13:05:58.778000</time_f><time_s>2018-05-24 12:04:45.513000</time_s></MES><LSW><car>WILLIAMS MERCEDES</car><fullname>Lance Stroll</fullname><time>1:01:13.323000</time><time_f>2018-05-24 13:07:26.834000</time_f><time_s>2018-05-24 12:06:13.511000</time_s></LSW><KMH><car>HAAS FERRARI</car><fullname>Kevin Magnussen</fullname><time>1:01:13.393000</time><time_f>2018-05-24 13:04:04.396000</time_f><time_s>2018-05-24 12:02:51.003000</time_s></KMH></response>'
    xml_out2 = b'<?xml version="1.0" ?><response><KMH><car>HAAS FERRARI</car><fullname>Kevin Magnussen</fullname><time>1:01:13.393000</time><time_f>2018-05-24 13:04:04.396000</time_f><time_s>2018-05-24 12:02:51.003000</time_s></KMH><LSW><car>WILLIAMS MERCEDES</car><fullname>Lance Stroll</fullname><time>1:01:13.323000</time><time_f>2018-05-24 13:07:26.834000</time_f><time_s>2018-05-24 12:06:13.511000</time_s></LSW><MES><car>SAUBER FERRARI</car><fullname>Marcus Ericsson</fullname><time>1:01:13.265000</time><time_f>2018-05-24 13:05:58.778000</time_f><time_s>2018-05-24 12:04:45.513000</time_s></MES><BHS><car>SCUDERIA TORO ROSSO HONDA</car><fullname>Brendon Hartley</fullname><time>1:01:13.179000</time><time_f>2018-05-24 13:16:05.164000</time_f><time_s>2018-05-24 12:14:51.985000</time_s></BHS><NHR><car>RENAULT</car><fullname>Nico Hulkenberg</fullname><time>1:01:13.065000</time><time_f>2018-05-24 13:04:02.979000</time_f><time_s>2018-05-24 12:02:49.914000</time_s></NHR><CSR><car>RENAULT</car><fullname>Carlos Sainz</fullname><time>1:01:12.950000</time><time_f>2018-05-24 13:04:28.095000</time_f><time_s>2018-05-24 12:03:15.145000</time_s></CSR><PGS><car>SCUDERIA TORO ROSSO HONDA</car><fullname>Pierre Gasly</fullname><time>1:01:12.941000</time><time_f>2018-05-24 13:08:36.586000</time_f><time_s>2018-05-24 12:07:23.645000</time_s></PGS><RGH><car>HAAS FERRARI</car><fullname>Romain Grosjean</fullname><time>1:01:12.930000</time><time_f>2018-05-24 13:06:27.441000</time_f><time_s>2018-05-24 12:05:14.511000</time_s></RGH><SPF><car>FORCE INDIA MERCEDES</car><fullname>Sergio Perez</fullname><time>1:01:12.848000</time><time_f>2018-05-24 13:13:13.883000</time_f><time_s>2018-05-24 12:12:01.035000</time_s></SPF><CLS><car>SAUBER FERRARI</car><fullname>Charles Leclerc</fullname><time>1:01:12.829000</time><time_f>2018-05-24 13:10:54.750000</time_f><time_s>2018-05-24 12:09:41.921000</time_s></CLS><FAM><car>MCLAREN RENAULT</car><fullname>Fernando Alonso</fullname><time>1:01:12.657000</time><time_f>2018-05-24 13:14:17.169000</time_f><time_s>2018-05-24 12:13:04.512000</time_s></FAM><KRF><car>FERRARI</car><fullname>Kimi R\xd0\x93\xc2\xa4ikk\xd0\x93\xc2\xb6nen</fullname><time>1:01:12.639000</time><time_f>2018-05-24 13:04:13.889000</time_f><time_s>2018-05-24 12:03:01.250000</time_s></KRF><SVM><car>MCLAREN RENAULT</car><fullname>Stoffel Vandoorne</fullname><time>1:01:12.463000</time><time_f>2018-05-24 13:19:50.198000</time_f><time_s>2018-05-24 12:18:37.735000</time_s></SVM><VBM><car>MERCEDES</car><fullname>Valtteri Bottas</fullname><time>1:01:12.434000</time><time_f>2018-05-24 13:01:12.434000</time_f><time_s>2018-05-24 12:00:00.000000</time_s></VBM><SVF><car>FERRARI</car><fullname>Sebastian Vettel</fullname><time>1:01:04.415000</time><time_f>2018-05-24 13:04:03.332000</time_f><time_s>2018-05-24 12:02:58.917000</time_s></SVF><DRR><car>RED BULL RACING TAG HEUER</car><fullname>Daniel Ricciardo</fullname><time>0:57:12.013000</time><time_f>2018-05-24 13:11:24.067000</time_f><time_s>2018-05-24 12:14:12.054000</time_s></DRR><SSW><car>WILLIAMS MERCEDES</car><fullname>Sergey Sirotkin</fullname><time>0:55:12.706000</time><time_f>2018-05-24 13:11:24.354000</time_f><time_s>2018-05-24 12:16:11.648000</time_s></SSW><EOF><car>FORCE INDIA MERCEDES</car><fullname>Esteban Ocon</fullname><time>0:54:13.028000</time><time_f>2018-05-24 13:12:11.838000</time_f><time_s>2018-05-24 12:17:58.810000</time_s></EOF><LHM><car>MERCEDES</car><fullname>Lewis Hamilton</fullname><time>0:53:12.460000</time><time_f>2018-05-24 13:11:32.585000</time_f><time_s>2018-05-24 12:18:20.125000</time_s></LHM></response>'
    xml_out3 = b'<?xml version="1.0" ?><response><SVF><car>FERRARI</car><fullname>Sebastian Vettel</fullname><time>1:01:04.415000</time><time_f>2018-05-24 13:04:03.332000</time_f><time_s>2018-05-24 12:02:58.917000</time_s></SVF></response>'
    cases_xml = [
        ('/api/v1/report/', 200, xml_out1),
        ('/api/v1/report/?order=desc', 200, xml_out2),
        ('/api/v1/report/?driver_id=SVF', 200, xml_out3),
    ]

    def factory(case_number):
        return cases_xml[case_number]
    return factory
