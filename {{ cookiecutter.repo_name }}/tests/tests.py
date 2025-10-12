"""
Test area for WIP = development scratchpad

Run from VScode
- Run as interactive Jupyter script: >Jupyter: Run file in Interactive
- Run as standalone Python file: F5
- Run as cell


# CLI: run selected test (need pytest.ini and conftest.py in root!)
- pytest --co # collect only
- pytest -s -k "keywords>" 
- pytest -pdb # debug
- pytest tests # run all tests

# requirements
packages >>> pytest
files >>> pytest.ini and conftest.py in root


# Examples of code

"""
# %%
from typer.testing import CliRunner
import pytest
import logging
logging.basicConfig(
    format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO
)

# All modules in devevelopment
from {{cookiecutter.package_name}}.myinit import *
from {{cookiecutter.package_name}}.dataset import *
from {{cookiecutter.package_name}}.plots import *
from {{cookiecutter.package_name}}.scripts import app



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



# %%


runner = CliRunner()
def test_scripts():
    result = runner.invoke(app, ["hello", "--upper", "paris"])
    assert result.exit_code == 0
    assert "Hello PARIS" in result.stdout
    
