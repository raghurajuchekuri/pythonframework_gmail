# Sample Feature
Feature: As a QA Engineer,
  I should be able to write sample code for framework
  Hence, I can test my scenarios

  @google
 Scenario: Verify google search
   Given I have navigated to google page
   When I enter "python" in search box
   Then I should see search results