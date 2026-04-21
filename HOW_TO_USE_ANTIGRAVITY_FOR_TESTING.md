# How to Use Antigravity for TMT Testing

## What's Set Up for You

### 🧠 Knowledge Item (Auto-loaded every conversation)
**Location**: `/Users/nikhilsharma/.gemini/antigravity/knowledge/tmt-testing-workflow/`

Contains:
- Platform URLs, login credentials, x-api-key
- Full Brand → Campaign → Affiliate → Link → Postman → Reports flow
- All Postman headers, endpoints, request/response bodies
- Domain knowledge (geo hierarchy, include/exclude logic, priority rules)

> I read this **automatically** at the start of every conversation. You don't need to do anything.

---

### ⚡ 4 Skills (single tasks)

| # | Skill | What It Does | Invoke With |
|---|-------|-------------|-------------|
| 1 | **tmt-testing** | Full platform & domain knowledge | `@tmt-testing` |
| 2 | **generate-tc-sheet** | Creates TC sheet from a PRD | `@generate-tc-sheet` |
| 3 | **e2e-api-testing** | Runs curl-based E2E payout tests | `@e2e-api-testing` |
| 4 | **verify-reports** | Guides report verification | `@verify-reports` |

### 🔄 3 Workflows (multi-step sequences that chain skills)

| # | Workflow | What It Does | Invoke With |
|---|----------|-------------|-------------|
| 1 | **feature-testing** | Complete PRD → TC sheet → UI test → API test → Reports → Final summary | `@feature-testing` |
| 2 | **quick-payout-test** | Rapid scenario testing — curl calls + report check, no TC sheet | `@quick-payout-test` |
| 3 | **regression-check** | Verify bug fix + run related TCs + smoke test for regressions | `@regression-check` |

### Skill vs Workflow — When to Use Which

| Situation | Use |
|-----------|-----|
| Got a new PRD, need full testing | `@feature-testing` (workflow) |
| Just need a TC sheet, no execution yet | `@generate-tc-sheet` (skill) |
| Quick test 2-3 payout scenarios | `@quick-payout-test` (workflow) |
| Bug fix, need retest + regression | `@regression-check` (workflow) |
| Need to check reports after testing | `@verify-reports` (skill) |

---

## How to Use: Scenario Examples

### 🟢 Scenario 1: "I got a new PRD, create TC sheet"
```
@generate-tc-sheet

Feature: <Feature Name>

PRD:
<paste full PRD here>

API Design Doc:
<paste API doc here, if available>
```

**What happens**: I'll parse the PRD, create a complete TC sheet at `/Users/nikhilsharma/Manual_Testing/<feature>_TC_execution.md` with all modules, priorities, and execution summary.

---

### 🟢 Scenario 2: "Test this feature end-to-end"
```
@tmt-testing

Feature: City & Region Level Payout Coverage

Campaign ID: 56
Tracking Token: 69e681d0b6e25fc69a199a49

Test these scenarios:
1. Customer from California, USA → should be eligible
2. Customer from Texas, USA → should be rejected (Texas excluded)
3. Customer from Houston, Texas → should be rejected (region exclusion wins)
```

**What happens**: I'll run curl commands to create customers with different geo data, create activities, and tell you to check reports after 2 minutes.

---

### 🟢 Scenario 3: "Run API tests for new geo endpoints"
```
@e2e-api-testing

Test the new Region and City filter APIs:
- GET /regions/filter for country US
- GET /cities/filter for region California
- Test typeahead, pagination, edge cases
```

**What happens**: I'll run curl commands against all API endpoints and report results.

---

### 🟢 Scenario 4: "Check if reports show the data correctly"
```
@verify-reports

I just created test activities. Check:
- Activity Report for geo rejection
- Campaign Report for region/city columns
- Export for correct columns
```

**What happens**: I'll guide you through each report to check, which filters to test, and what to verify in exports.

---

## What You Need to Provide Each Time

| What | When | Example |
|------|------|---------|
| PRD text | New feature | Paste full PRD |
| API Design Doc | New feature | Paste API doc |
| Tracking Token | E2E testing | `69e681d0b6e25fc69a199a49` |
| Campaign ID | E2E testing | `56` |
| Panel name | E2E testing | `AB Network` / `TMT` |
| x-api-key | Only if different panel | Paste from Automation → API Keys |

> **Note**: Login credentials and TMT x-api-key are already saved in the Knowledge Item. You don't need to provide them every time.

---

## Quick Reference: Full Test Flow

```
📄 PRD + API Doc (you provide)
    ↓
📋 TC Sheet created (@generate-tc-sheet)
    ↓
🖥️  UI Testing (you do in browser, share findings)
    ↓
🔗 Generate Tracking Link (Campaign → Manage Links → Generate)
    ↓
🌐 Paste link in browser → copy tracking_token from URL
    ↓
📡 E2E Testing (@e2e-api-testing)
   → curl: Create Customer (with country/region/city)
   → curl: Create Activity
   → Wait ~2 min
    ↓
📊 Report Verification (@verify-reports)
   → Activity Report, Campaign Report, Affiliate Report
   → Check filters, columns, export
    ↓
✅ TC Sheet updated with Pass/Fail + Bugs
```

---

## Folder Structure

```
/Users/nikhilsharma/Manual_Testing/
├── .antigravity/
│   ├── skills/                          ← Single-task instructions
│   │   ├── tmt-testing.md
│   │   ├── generate-tc-sheet.md
│   │   ├── e2e-api-testing.md
│   │   └── verify-reports.md
│   └── workflows/                       ← Multi-step sequences
│       ├── feature-testing.md           ← Full PRD → tested TC sheet
│       ├── quick-payout-test.md         ← Rapid scenario testing
│       └── regression-check.md          ← Bug fix verification
├── city_region_payout_TC_execution.md   ← Current feature TC sheet
├── <next_feature>_TC_execution.md       ← Future feature sheets
└── HOW_TO_USE_ANTIGRAVITY_FOR_TESTING.md  ← This file
```
