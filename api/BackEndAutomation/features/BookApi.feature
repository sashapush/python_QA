Feature: Verify if Books are added and deleted using Library API
  @books
  Scenario: Verify addBook API functionality
    Given Book details which needs to be added to library
    When We execute  addBook POST method
    Then Book is successfully added
    And Status code of response is 200

  @books
  Scenario Outline: Verify addBook API functionality #used for parametrization
    Given Book details with <isbn> and <aisle> to be added to library
    When We execute  addBook POST method
    Then Book is successfully added
    Examples:
      | isbn  | aisle |
      | booba | 03221 |
      | zopa  | 02321 |