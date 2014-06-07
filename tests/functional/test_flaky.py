
from nose.tools import with_setup
from os.path import dirname, join, abspath

import lettuce
from lettuce import Runner
from tests.asserts import prepare_stdout
from tests.asserts import assert_stdout_lines_with_traceback
from lettuce.core import fs, StepDefinition

lettuce_dir = abspath(dirname(lettuce.__file__))
lettuce_path = lambda *x: fs.relpath(join(lettuce_dir, *x))

call_line = StepDefinition.__call__.im_func.func_code.co_firstlineno + 5



@with_setup(prepare_stdout)
def test_flaky():
    """Test basic flaky functionality"""

    runner = Runner(join(abspath(dirname(__file__)), 'flaky_features', 'flaky_test'), verbosity=3)
    runner.run()

    assert_stdout_lines_with_traceback(
        ("\n"
        "Feature: Test a feature with non-parametrized flaky tag # tests/functional/flaky_features/flaky_test/flaky.feature:2\n"
        "\n"
        "  @flaky\n"
        "  Scenario: This scenario always Fail          # tests/functional/flaky_features/flaky_test/flaky.feature:4\n"
        "    Given this test step fail                           # tests/functional/flaky_features/flaky_test/flaky.py:14\n"
        "    Traceback (most recent call last):\n"
        '      File "%(lettuce_core_file)s", line %(call_line)d, in __call__\n'
        "        ret = self.function(self.step, *args, **kw)\n"
        '      File "%(step_file)s", line 15, in this_step\n'
        "        assert step_actions[action]\n"
        "    AssertionError\n"
        "\n"
        "  @flaky\n"
        "  Scenario: This scenario always Fail          # tests/functional/flaky_features/flaky_test/flaky.feature:4\n"
        "    Given this test step fail                           # tests/functional/flaky_features/flaky_test/flaky.py:14\n"
        "    Traceback (most recent call last):\n"
        '      File "%(lettuce_core_file)s", line %(call_line)d, in __call__\n'
        "        ret = self.function(self.step, *args, **kw)\n"
        '      File "%(step_file)s", line 15, in this_step\n'
        "        assert step_actions[action]\n"
        "    AssertionError\n"
        "\n"
        "  @flaky(3,2) @flaky\n"
        "  Scenario: This scenario always Pass# tests/functional/flaky_features/flaky_test/flaky.feature:8\n"
        "    Given this test step pass                           # tests/functional/flaky_features/flaky_test/flaky.py:14\n"
        "\n"
        "  @flaky(3,2) @flaky\n"
        "  Scenario: This scenario always Pass# tests/functional/flaky_features/flaky_test/flaky.feature:8\n"
        "    Given this test step pass                           # tests/functional/flaky_features/flaky_test/flaky.py:14\n"
        "\n"
        "  @flaky\n"
        "  Scenario: This scenario Passes on second run # tests/functional/flaky_features/flaky_test/flaky.feature:11\n"
        "    Given execute the steps                             # tests/functional/flaky_features/flaky_test/flaky.py:19\n"
        "    Traceback (most recent call last):\n"
        '      File "%(lettuce_core_file)s", line %(call_line)d, in __call__\n'
        "        ret = self.function(self.step, *args, **kw)\n"
        '      File "%(step_file)s", line 25, in conditional_step\n'
        "        assert False\n"
        "    AssertionError\n"
        "\n"
        "  @flaky\n"
        "  Scenario: This scenario Passes on second run # tests/functional/flaky_features/flaky_test/flaky.feature:11\n"
        "    Given execute the steps                             # tests/functional/flaky_features/flaky_test/flaky.py:19\n"
        "    Traceback (most recent call last):\n"
        '      File "%(lettuce_core_file)s", line %(call_line)d, in __call__\n'
        "        ret = self.function(self.step, *args, **kw)\n"
        '      File "%(step_file)s", line 25, in conditional_step\n'
        "        assert False\n"
        "    AssertionError\n"
        "\n"
        "1 feature (0 passed)\n"
        "3 scenarios (2 passed)\n"
        "3 steps (1 failed, 2 passed)\n"
        "\n"
        "List of failed scenarios:\n"
        "  @flaky\n"
        "  Scenario: This scenario always Fail          # tests/functional/flaky_features/flaky_test/flaky.feature:4\n"
        "\n") % {
            'lettuce_core_file': lettuce_path('core.py'),
            'step_file': abspath(lettuce_path('..', 'tests', 'functional', 'flaky_features', 'flaky_test')),
            'call_line': call_line,
        }
    )
