"""


# Run selected test (need pytest.ini in root!)
# -s for print statements
- pytest --co # collect only
- pytest -s -k "keywords>" 
- pytest -pdb # debug
- pytest -s tests # run all tests



# Examples of code

"""
# %% Init
import pytest
from typer.testing import CliRunner

# All modules in development
from my_package.myinit import *
from my_package.dataset import *
from my_package.plots import *



# %% Test the device tables
def test_load_data():
    df = load_data()
    assert True


# %% Support functions in dev
@pytest.fixture
def dummy_x():
    """Test fixtures buolding some dummy data"""
    return np.arange(0, 1, 0.01)


@pytest.mark.parametrize("arg", [1, 2])
def test_dummy(arg, dummy_x):
    print(sys.executable)
    assert arg / arg == pytest.approx(1, abs=1e-3)

# %% CLI tests
runner = CliRunner()
def test_scripts():
    result = runner.invoke(app, ["hello", "--upper", "paris"])
    assert result.exit_code == 0
    assert "Hello PARIS" in result.stdout
    