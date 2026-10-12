Feature: Smoke test

  Scenario: Health check responds
    Given the app is running
    When I request "/health"
    Then the response status is 200
