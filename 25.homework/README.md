# QAuto Locators

This repository contains XPath and CSS locators for the QAuto website (https://qauto2.forstudy.space/).

## Contents

- 25 XPath locators including:
  - text() function usage
  - Attribute (@) selectors
  - Complex multi-element locators
- 25 CSS locators including:
  - ID and class selectors
  - Attribute selectors
  - Complex combinations

## Usage

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize driver
driver = webdriver.Chrome()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

# Use locators
element = driver.find_element(By.XPATH, xpath_locators[1])
element = driver.find_element(By.CSS_SELECTOR, css_locators[1])
```

## Authentication

The site requires authentication. Use these credentials:
- Login: guest
- Password: welcome2qauto

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver