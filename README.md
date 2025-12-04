# Rahulshetty Automation Framework

## Project Overview

This project is an **automation framework** for testing the Rahulshetty demo site (`https://rahulshettyacademy.com/loginpagePractise/`) using:

- **Python 3.x**
- **Playwright**
- **Pytest**

Key features:

- Opens the browser in **maximized window**.
- Creates isolated **browser contexts** for test isolation.
- Provides **reusable Pytest fixtures** for browser and page.
- Structured folder layout for maintainability and scalability.

## Folder Structure

## Test: `test_open_browser`
**Purpose:** Verify that the login page opens correctly and allows a user to log in with valid credentials.

**Notes:**
- `page` fixture ensures test isolation.
- XPath selectors are used; consider switching to Page Object Model for larger projects.
- Manual wait is optional; remove in CI/CD.


