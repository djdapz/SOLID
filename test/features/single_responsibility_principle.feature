Feature: Single Responsibility Principle

  Background:
    Given there is no output.txt
    And we have an input.txt with content some content

  Scenario: Generating output
    Given a reporter that writes input.txt to output.txt
    When we generate a report
    Then we have an output.txt with content some content