Feature: Liskov Substitution Principle

  Scenario: Human Worker Working
    Given a human worker
    When the worker works
    Then the worker responds YAY WORK

  Scenario: Robot Worker Working
    Given a robot worker
    When the worker works
    Then the worker responds BEE BOP WORK

  Scenario: A workforce
    Given a human worker and a robot worker
    When the workers work
    Then the first responds with YAY WORK
    Then the second responds with BEE BOP WORK

  Scenario: Human Worker Eating food they like
    Given a human worker
    When the worker eats broccoli
    Then the worker responds YUK! I DONT LIKE VEGGIES

  Scenario: Human Worker Eating food they don't like
    Given a human worker
    When the worker eats cake
    Then the worker responds YUM! THAT WAS DELICIOUS

  #VIOLATION
  Scenario: Robot Worker Failing to eat
    Given a robot worker
    When the worker eats anything
    Then the worker responds AN ERROR OCCURRED





