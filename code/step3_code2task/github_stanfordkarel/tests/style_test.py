import os
import warnings

import pytest

from conftest import PROBLEMS, STUDENT_CODE_DIR, TIMEOUT
from stanfordkarel.style_checker import StyleChecker


@pytest.mark.timeout(TIMEOUT)
@pytest.mark.parametrize("problem_name", PROBLEMS)
def test_student_style(problem_name: str) -> None:
    code_file = os.path.join(STUDENT_CODE_DIR, problem_name + ".py")

    if os.path.exists(code_file):
        StyleChecker(code_file).check_style()
    else:
        warnings.warn(
            "Code directory does not exist. Pass the tests for travis-ci, "
            "but raise an error for actual student code."
        )
