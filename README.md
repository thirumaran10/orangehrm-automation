# OrangeHRM Automation Test Suite

## Overview

This repository contains **Playwright-based automation test cases** for the OrangeHRM login functionality. It's designed to demonstrate best practices in test automation, maintainability, and scalability for QA engineers joining the team.

**Application Under Test (AUT):** [OrangeHRM Demo - Login Page](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

---

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running Tests](#running-tests)
- [Test Scenarios](#test-scenarios)
- [Page Object Model (POM)](#page-object-model-pom)
- [Configuration](#configuration)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [Resources & Learning](#resources--learning)

---

## 🚀 Getting Started

### Quick Start (5 minutes)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd orangehrm-automation
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run tests**
   ```bash
   npx playwright test
   ```

4. **View test report**
   ```bash
   npx playwright show-report
   ```

---

## 📁 Project Structure

```
orangehrm-automation/
├── tests/
│   ├── login.spec.ts                 # Login test cases
│   └── fixtures/                     # Shared test fixtures
├── pages/
│   └── loginPage.ts                  # Page Object Model for Login page
├── data/
│   └── testData.json                 # Test credentials and test data
├── config/
│   └── playwright.config.ts          # Playwright configuration
├── utils/
│   └── helpers.ts                    # Helper functions (wait, assertions, etc.)
├── reports/                          # Test reports & screenshots
├── README.md
├── package.json
└── .gitignore
```

### Directory Explanation

| Directory | Purpose |
|-----------|---------|
| `tests/` | Contains all `.spec.ts` test files (Playwright test suites) |
| `pages/` | Page Object Model - encapsulates page interactions |
| `data/` | Test data, credentials, and test scenarios |
| `config/` | Playwright configuration for browsers, timeouts, retries |
| `utils/` | Reusable functions: wait helpers, assertions, logging |
| `reports/` | Generated test results, screenshots, and HTML reports |

---

## ✅ Prerequisites

Before running tests, ensure you have the following installed:

- **Node.js** (v16 or higher) - [Download](https://nodejs.org/)
- **npm** (comes with Node.js)
- **Git** - [Download](https://git-scm.com/)
- **Code Editor** - VS Code recommended

### Verify Installation

```bash
node --version     # Should be v16+
npm --version      # Should be v7+
git --version      # Should be installed
```

---

## 🛠️ Installation & Setup

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd orangehrm-automation
```

### Step 2: Install Dependencies
```bash
npm install
```

This installs:
- `@playwright/test` - Playwright test framework
- `@playwright/browser` - Browser binaries (Chromium, Firefox, WebKit)
- `dotenv` - Environment variable management

### Step 3: Install Playwright Browsers
```bash
npx playwright install
```

### Step 4: Verify Setup
```bash
npx playwright --version
```

---

## 🧪 Running Tests

### Run All Tests
```bash
npx playwright test
```

### Run Specific Test File
```bash
npx playwright test tests/login.spec.ts
```

### Run Tests in Headed Mode (see browser)
```bash
npx playwright test --headed
```

### Run Tests in Debug Mode
```bash
npx playwright test --debug
```

### Run Tests in Specific Browser
```bash
npx playwright test --project=chromium
npx playwright test --project=firefox
npx playwright test --project=webkit
```

### Run with Verbose Output
```bash
npx playwright test --verbose
```

### Generate & View HTML Report
```bash
npx playwright test
npx playwright show-report
```

---

## 🎯 Test Scenarios

### Login Page Test Cases

| # | Test Case | Description | Expected Result |
|----|-----------|-------------|-----------------|
| TC_001 | Valid Login | Login with valid credentials | User successfully logs in and redirected to Dashboard |
| TC_002 | Invalid Username | Login with non-existent username | Error message displayed: "Invalid credentials" |
| TC_003 | Invalid Password | Login with correct username but wrong password | Error message displayed: "Invalid credentials" |
| TC_004 | Empty Username | Submit form without username | Validation error: "Required" |
| TC_005 | Empty Password | Submit form without password | Validation error: "Required" |
| TC_006 | Empty Both Fields | Submit form without any credentials | Both fields show validation errors |
| TC_007 | Forgot Password Link | Click "Forgot your password?" link | Redirected to password reset page |
| TC_008 | Page Load Verification | Verify all page elements are loaded | Logo, username field, password field, login button visible |
| TC_009 | Special Characters in Username | Login with special characters in username | Error message displayed |
| TC_010 | SQL Injection Attempt | Attempt SQL injection in password field | System handles safely and displays error |

---

## 🏗️ Page Object Model (POM)

We use **Page Object Model** design pattern for maintainability and reusability.

### Example: `pages/loginPage.ts`

```typescript
import { Page, Locator } from '@playwright/test';

export class LoginPage {
  readonly page: Page;
  readonly usernameInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly errorMessage: Locator;

  constructor(page: Page) {
    this.page = page;
    this.usernameInput = page.locator('input[name="username"]');
    this.passwordInput = page.locator('input[name="password"]');
    this.loginButton = page.locator('button[type="submit"]');
    this.errorMessage = page.locator('.oxd-alert-content');
  }

  async goto() {
    await this.page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login');
  }

  async login(username: string, password: string) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }

  async getErrorMessage(): Promise<string> {
    return await this.errorMessage.textContent() || '';
  }
}
```

### Benefits of POM

- ✅ **Maintainability**: Locators centralized in one place
- ✅ **Reusability**: Methods can be used across multiple tests
- ✅ **Scalability**: Easy to add new methods or pages
- ✅ **Readability**: Tests are more readable and understandable

---

## ⚙️ Configuration

### `playwright.config.ts`

Key configurations for the test suite:

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'https://opensource-demo.orangehrmlive.com',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],
  webServer: undefined,
});
```

### Key Config Properties

| Property | Purpose |
|----------|---------|
| `testDir` | Directory containing test files |
| `retries` | Retry failed tests (useful in CI) |
| `workers` | Parallel workers for test execution |
| `reporter` | Report format (html, json, junit, etc.) |
| `use.baseURL` | Base URL for the application |
| `trace` | Record playwright trace for debugging |
| `screenshot` | Capture screenshots on failure |

---

## 📚 Best Practices

### 1. **Use Page Object Model (POM)**
   - Encapsulate page interactions in page objects
   - Reduces test maintenance burden
   
### 2. **Meaningful Test Names**
   ```typescript
   // ✅ Good
   test('should display error message when login with invalid credentials', async () => {});
   
   // ❌ Bad
   test('test login', async () => {});
   ```

### 3. **Use Test Data Externally**
   ```json
   {
     "validUser": { "username": "Admin", "password": "admin123" },
     "invalidUser": { "username": "invalid", "password": "invalid" }
   }
   ```

### 4. **Wait Strategies**
   ```typescript
   // ✅ Good - use playwright's auto-waiting
   await page.locator('selector').click();
   
   // ❌ Avoid - hard waits
   await page.waitForTimeout(5000);
   ```

### 5. **Use Fixtures for Setup/Teardown**
   ```typescript
   test.beforeEach(async ({ page }) => {
     // Setup - runs before each test
     await page.goto('/');
   });
   ```

### 6. **Assertions Should Be Specific**
   ```typescript
   // ✅ Good
   await expect(errorMsg).toContainText('Invalid credentials');
   
   // ❌ Vague
   await expect(errorMsg).toBeTruthy();
   ```

## 🐛 Troubleshooting

### Issue: Tests timing out
**Solution:** Increase timeout in `playwright.config.ts`
```typescript
use: {
  navigationTimeout: 30000,
  actionTimeout: 10000
}
```

### Issue: Element not found
**Solution:** 
- Verify selector using browser DevTools
- Wait for element: `await page.waitForSelector('selector')`
- Use more robust selectors (data-testid over classes)

### Issue: Browser crashes
**Solution:** 
```bash
npx playwright install --with-deps
```

### Issue: Tests pass locally but fail in CI
**Solution:**
- Reduce parallel workers: `workers: 1`
- Add explicit waits for network: `await page.waitForLoadState('networkidle')`
- Use screenshots/traces for debugging

### Issue: Password/username not auto-filled
**Solution:** Use `fill()` instead of `type()` for better compatibility
```typescript
await page.locator('input[name="username"]').fill('Admin');
```

---

## 📖 Resources & Learning

### Playwright Documentation
- [Official Playwright Docs](https://playwright.dev/)
- [API Reference](https://playwright.dev/docs/api/class-test)
- [Locators Guide](https://playwright.dev/docs/locators)
- [Debugging Guide](https://playwright.dev/docs/debug)

### Test Writing Guides
- [Writing Tests](https://playwright.dev/docs/writing-tests)
- [Advanced Patterns](https://playwright.dev/docs/pom)
- [Handling Authentication](https://playwright.dev/docs/auth)

### OrangeHRM Info
- [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/)
- [Default Credentials](https://github.com/orangehrm/orangehrm/wiki/Default-credentials-for-login)
  - Username: `Admin`
  - Password: `admin123`

### Useful Commands Cheat Sheet
```bash
npm install                    # Install dependencies
npx playwright install         # Install browser binaries
npx playwright test            # Run all tests
npx playwright test --debug    # Debug mode
npx playwright show-report     # Open HTML report
npx playwright codegen <url>   # Record tests (auto-generate code)
```

---

## 🤝 Contributing

When adding new tests:
1. Follow the POM pattern
2. Use descriptive test names
3. Add test data to `data/testData.json`
4. Update this README with new test cases
5. Ensure all tests pass: `npm test`

---

## 📝 License

See LICENSE file for details.

---

## 👥 Support & Questions

For new team members:
- **Slack Channel:** #qa-automation
- **Documentation:** Check `/docs` folder
- **Pair Testing:** Reach out to your onboarding buddy

**Last Updated:** November 2025
