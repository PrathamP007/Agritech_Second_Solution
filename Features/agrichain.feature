Feature: Validate Agrichain longest substring functionality

  Scenario: Verify longest substring calculation
    Given I launch the Agrichain input page
    When I enter "abcabcbb" in the input field
    And I click the submit button
    Then I should see the output "3" on the result page
