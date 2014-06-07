@flaky
Feature: Test a feature with non-parametrized flaky tag

  Scenario: This scenario always Fail
    Given this test step fail

  @flaky(3,2)
  Scenario: This scenario always Pass
    Given this test step pass

  Scenario: This scenario Passes on second run
    Given execute the steps