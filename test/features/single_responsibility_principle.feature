Feature: Single Responsibility Principle

  Background:
    Given there is no output.txt
    And a reader for input.txt

  Scenario: Generating output
    Given a reporter that writes input.txt to output.txt
    When we generate a report
    Then we have an output.txt with content some content

  Scenario: Reading input
    When we want to read the contents of input.txt
    Then we find the the contents is some content