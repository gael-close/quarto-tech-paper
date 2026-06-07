import logging
import pytest
from loguru import logger

@pytest.fixture(autouse=True)
def propagate_logs_to_pytest(caplog):
    """
    Redirects Logguru outputs into standard logging so pytest can 
    intercept, clean, and isolate them per test.
    """
    class PropagateHandler(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)

    sink_id = logger.add(PropagateHandler(), format="{message}")
    yield
    logger.remove(sink_id)