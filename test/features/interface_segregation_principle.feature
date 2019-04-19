Feature: Interface Segregation Principle

  Scenario: Soda Machine Pouring Soda
    Given a soda machine
    When the machine dispenses
    Then the machine returns COLA

  Scenario: Coffee Machine Pouring Coffee
    Given a coffee machine
    When the machine dispenses
    Then the machine returns COFFEE

  Scenario: A few drink machines
    Given i have a mix of drink machines
    When the machines dispense
    Then the first pours me COFFEE
    Then the second pours me COLA

  Scenario: Coffee Machine Making Coffee
    Given a coffee machine
    When the machine makes
    Then the machine prepares COFFEE

  Scenario: Rice Maker Making Rice
    Given a rice maker
    When the machine makes
    Then the machine prepares RICE

  Scenario: A few maker machines
    Given i have a mix of maker machines
    When the machines make
    Then the first makes me COFFEE
    Then the second makes me RICE

