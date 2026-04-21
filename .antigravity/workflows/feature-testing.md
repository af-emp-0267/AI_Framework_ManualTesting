# Workflow: Complete Feature Testing

## Description
End-to-end workflow for testing a new TMT platform feature — from receiving a PRD to a final tested TC sheet with pass/fail statuses and bug reports.

## When to Use
Invoke this workflow when you receive a new PRD/API doc and want the full testing cycle done.

## How to Invoke
```
@feature-testing

Feature: <Feature Name>
PRD: <paste PRD>
API Doc: <paste API doc>
Tracking Token: <token> (or "I'll generate later")
Campaign ID: <id> (or "create new")
Panel: TMT / AB Network / etc.
```

---

## Steps

### Step 1: Read Context
**Skill**: None (automatic)
- Read KI at `/Users/nikhilsharma/.gemini/antigravity/knowledge/tmt-testing-workflow/`
- Understand platform URLs, credentials, API config, and testing flow
- Read the `tmt-testing.md` skill for domain knowledge

### Step 2: Generate TC Sheet
**Skill**: `@generate-tc-sheet`
- Parse the PRD to extract all functional requirements
- Parse the API Design Doc to extract endpoints and schema changes
- Create a TC sheet organized by modules:
  1. UI modules (one per screen mentioned in PRD)
  2. Business Logic / E2E module
  3. API Validation module
  4. Reporting & Activity Logs module
  5. Edge Cases & Backward Compatibility module
- Save at `/Users/nikhilsharma/Manual_Testing/<feature_name>_TC_execution.md`
- Report total TC count and priority breakdown to user

### Step 3: UI Testing (Browser)
**Skill**: `@tmt-testing`
- Open the platform at https://tmt.affnook.io/login
- Login with credentials from KI
- Navigate to each screen mentioned in the PRD
- For each UI test case:
  - Perform the steps
  - Take screenshots
  - Record actual result
  - Mark Pass/Fail
- Update TC sheet with results for all UI modules
- If browser is unavailable: Tell user which UI tests to perform manually, and wait for their feedback to update the sheet

### Step 4: E2E Payout Testing via API
**Skill**: `@e2e-api-testing`
- Get tracking token from user (or generate by navigating to Campaign → Manage Links)
- For each E2E test scenario:
  - Create a unique customerId (e.g., `<Feature>_Cus_001`)
  - Run curl: Create Customer with appropriate country/region/city
  - Run curl: Create Activity for that customer
  - Record API response (200 OK / error)
- After ALL activities created: Wait ~2 minutes
- Update TC sheet with API responses

### Step 5: API Endpoint Testing
**Skill**: `@e2e-api-testing`
- Test each new API endpoint from the API Design Doc:
  - GET endpoints: Test with valid params, edge cases, pagination
  - POST endpoints: Test with valid body, invalid body, missing fields
  - PATCH endpoints: Test updates
- Record responses
- Update TC sheet API module with results

### Step 6: Report Verification
**Skill**: `@verify-reports`
- Navigate to each report mentioned in PRD:
  - Activity Report → check status, rejection reason, geo columns
  - Campaign Report → check region/city columns
  - Affiliate Report → check region/city columns
  - Click Report → check geo data
  - Conversion Report → check geo data
- Test filters (Country, Region, City, Rejection Reason)
- Test export (CSV/Excel columns)
- Test group-by (City dimension)
- Update TC sheet Reporting module with results

### Step 7: Final Summary
- Update Execution Summary table in TC sheet (count Pass/Fail/Blocked per module)
- Fill in Bugs Found table for any failures
- Report to user:
  - Total Pass / Fail / Blocked
  - List of bugs with severity
  - Any blocked tests that need manual attention
  - Overall feature readiness assessment

---

## Output
- Updated TC sheet at `/Users/nikhilsharma/Manual_Testing/<feature>_TC_execution.md`
- All test cases have status (✅/❌/⏳/🚫)
- Bugs documented with steps to reproduce
- Execution summary complete
