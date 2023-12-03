Feature:  create a script to check the sign up page. We should be able to run this script.

@wiki
  Scenario: User should be able to sign up
    Given user should be able to go to the application
    Then user clicks on sign up today button
    And user fill ups all input boxes
    And user clicks on sign up button
