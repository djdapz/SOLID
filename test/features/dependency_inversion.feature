Feature: Edit Settings Page

  Scenario Outline: Titles
    Given the user is in the <page> view
    When the user selects the Edit from an individual Kebab with title <title>
    Then the report settings drawer appears with the title equal to <title>

    Examples:
      | page | title                      |
      | list | Frances' Super Cool Report |
      | list | Capital Change Detail      |
      | grid | Frances' Super Cool Report |
      | grid | Capital Change Detail      |

  Scenario Outline: Cancel
    Given the user is in the <page> view
    When the user selects the Edit from an individual Kebab with title <title>
    And the user clicks cancel
    Then the edit settings view is gone

    Examples:
      | page | title                      |
      | list | Frances' Super Cool Report |
      | grid | Frances' Super Cool Report |