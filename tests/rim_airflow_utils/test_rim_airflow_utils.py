import sys
import rim_airflow_utils


def test_ping():
    sys.argv = ['foo', '10']
    rim_airflow_utils.ping()

