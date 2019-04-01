Feature: Open Closed Principle

  Background:
    Given there is no output.txt


  Scenario: Read every line
    Given a line reader for 3_line_input.txt
    And a reporter that writes 3_line_input.txt to output.txt
    When we generate a report
    Then we have a multiline file output.txt with content Be Kind\nDo What Works\nDo the Right Thing

  Scenario: Read every other line
    Given a every other line reader for 3_line_input.txt
    And a reporter that writes 3_line_input.txt to output.txt
    When we generate a report
    Then we have a multiline file output.txt with content Be Kind\nDo the Right Thing


