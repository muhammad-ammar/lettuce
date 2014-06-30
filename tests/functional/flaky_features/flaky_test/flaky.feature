@flaky
Feature: Test a feature with non-parametrized flaky tag

  Scenario: This scenario always Fail
    Given this test step fail

  @flaky(3,2)
  Scenario: This scenario always Pass
    Given this test step pass

  Scenario: This scenario Passes on second run
    Given execute the steps

  @flaky(3,2)
  Scenario Outline: Factorials [0-4]
    Given I have the number <number>
    When I compute its factorial
    Then I see the number <result>

  Examples:
    | number | result |
    | 0      | 1      |
    | 1      | 1      |
    | 2      | 2      |
    | 3      | 6      |
    | 4      | 24     |
