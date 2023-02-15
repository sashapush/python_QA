Feature: Github API validation

  Scenario: Session management check
    Given I have github credentials
    When I hit getRepositories API method
    Then Status code of response is 200

