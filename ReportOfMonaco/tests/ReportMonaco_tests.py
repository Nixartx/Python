import pytest
from ReportOfMonaco import ReportMonaco

out = " 1. Lewis Hamilton       | MERCEDES                  | 0:53:12.460\n 2. Esteban Ocon         | FORCE INDIA MERCEDES      | 0:54:13.028\n 3. Sergey Sirotkin      | WILLIAMS MERCEDES         | 0:55:12.706\n 4. Daniel Ricciardo     | RED BULL RACING TAG HEUER | 0:57:12.013\n 5. Sebastian Vettel     | FERRARI                   | 1:01:04.415\n 6. Valtteri Bottas      | MERCEDES                  | 1:01:12.434\n 7. Stoffel Vandoorne    | MCLAREN RENAULT           | 1:01:12.463\n 8. Kimi RГ¤ikkГ¶nen     | FERRARI                   | 1:01:12.639\n 9. Fernando Alonso      | MCLAREN RENAULT           | 1:01:12.657\n10. Charles Leclerc      | SAUBER FERRARI            | 1:01:12.829\n11. Sergio Perez         | FORCE INDIA MERCEDES      | 1:01:12.848\n12. Romain Grosjean      | HAAS FERRARI              | 1:01:12.930\n13. Pierre Gasly         | SCUDERIA TORO ROSSO HONDA | 1:01:12.941\n14. Carlos Sainz         | RENAULT                   | 1:01:12.950\n15. Nico Hulkenberg      | RENAULT                   | 1:01:13.065\n__________________________________________________________________\n16. Brendon Hartley      | SCUDERIA TORO ROSSO HONDA | 1:01:13.179\n17. Marcus Ericsson      | SAUBER FERRARI            | 1:01:13.265\n18. Lance Stroll         | WILLIAMS MERCEDES         | 1:01:13.323\n19. Kevin Magnussen      | HAAS FERRARI              | 1:01:13.393\n"
out2 = " 1. Kevin Magnussen      | HAAS FERRARI              | 1:01:13.393\n 2. Lance Stroll         | WILLIAMS MERCEDES         | 1:01:13.323\n 3. Marcus Ericsson      | SAUBER FERRARI            | 1:01:13.265\n 4. Brendon Hartley      | SCUDERIA TORO ROSSO HONDA | 1:01:13.179\n__________________________________________________________________\n 5. Nico Hulkenberg      | RENAULT                   | 1:01:13.065\n 6. Carlos Sainz         | RENAULT                   | 1:01:12.950\n 7. Pierre Gasly         | SCUDERIA TORO ROSSO HONDA | 1:01:12.941\n 8. Romain Grosjean      | HAAS FERRARI              | 1:01:12.930\n 9. Sergio Perez         | FORCE INDIA MERCEDES      | 1:01:12.848\n10. Charles Leclerc      | SAUBER FERRARI            | 1:01:12.829\n11. Fernando Alonso      | MCLAREN RENAULT           | 1:01:12.657\n12. Kimi RГ¤ikkГ¶nen     | FERRARI                   | 1:01:12.639\n13. Stoffel Vandoorne    | MCLAREN RENAULT           | 1:01:12.463\n14. Valtteri Bottas      | MERCEDES                  | 1:01:12.434\n15. Sebastian Vettel     | FERRARI                   | 1:01:04.415\n16. Daniel Ricciardo     | RED BULL RACING TAG HEUER | 0:57:12.013\n17. Sergey Sirotkin      | WILLIAMS MERCEDES         | 0:55:12.706\n18. Esteban Ocon         | FORCE INDIA MERCEDES      | 0:54:13.028\n19. Lewis Hamilton       | MERCEDES                  | 0:53:12.460\n"
out3 = "Daniel Ricciardo     | RED BULL RACING TAG HEUER | 0:57:12.013\n"
cases = [
    ({
        "folder": "../tests/reports",
        "driver_name": '',
        "reverse": False
    }, out),
    ({
        "folder": "../tests/reports",
        "reverse": True,
        "driver_name": '',
    }, out2),
    ({
        "folder": "../tests/reports",
        "driver_name": "Daniel Ricciardo",
        "reverse": False
    }, out3),
]


@pytest.mark.parametrize("params,expected", cases)
def test_ReportMonaco_success(capfd, params, expected):
    ReportMonaco().print_report(
        folder=params['folder'],
        driver_name=params['driver_name'],
        reverse=params['reverse'])
    actual, err = capfd.readouterr()
    assert actual == expected


def test_ReportMonaco_file_exception():
    with pytest.raises(FileNotFoundError):
        ReportMonaco().print_report(folder='wrong_path_to_file')


def test_ReportMonaco_no_results(capfd):
    expected = "No results\n"
    ReportMonaco().print_report(
        folder='../tests/reports',
        driver_name='Wrong Name')
    actual, err = capfd.readouterr()
    assert actual == expected
