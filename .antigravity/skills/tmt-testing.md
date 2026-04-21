# Skill: TMT Platform Feature Testing

## Purpose
This skill teaches Antigravity how to perform complete feature testing on the TMT affiliate marketing platform. Read this entire file before starting any testing task.

---

## Platform Context

| Item | Detail |
|------|--------|
| Platform Name | TMT (Affiliate Marketing Platform) |
| QA URL | https://tmt.affnook.io |
| AB Network QA | https://oscorp7.affnookqa1.online |
| Testing Type | Manual + API (Postman) |
| Report Lag | ~2 minutes after activity creation |

---

## Mandatory: Check KI First
Before testing ANY feature, read the Knowledge Item at:
`/Users/nikhilsharma/.gemini/antigravity/knowledge/tmt-testing-workflow/`

It contains the full workflow, Postman config, API endpoints, and domain knowledge.

---

## Testing Inputs the User Provides

The user will provide one or more of:
1. **PRD** (Product Requirements Document) — describes what the feature should do
2. **API Design Document** — describes backend API changes (schema, endpoints, validation)
3. **UI Mockup URL** — shows expected UI design

From these, you must:
- Extract all functional requirements
- Identify all testable behaviours
- Generate a complete TC sheet
- Execute tests and update statuses

---

## How to Create a TC Sheet

### File Location
Save at: `/Users/nikhilsharma/Manual_Testing/<feature_name>_TC_execution.md`

### Structure (always in this order)
1. Header (Feature name, platform, tester, date, status legend)
2. Pre-requisites Checklist
3. Test Execution Flow diagram
4. Module 1: UI tests (per screen mentioned in PRD)
5. Module N: More UI modules
6. Geo Evaluation / Business Logic (E2E via Postman)
7. API Validation
8. Reporting & Activity Logs
9. Edge Cases & Backward Compatibility
10. Execution Summary table
11. Bugs Found table
12. Postman Configuration Reference

### TC Table Columns
`TC ID | Test Case | Priority | Steps | Expected Result | Actual Result | Status | Bug ID`

### Priority Guidelines
- **P0**: Core feature works / breaks main flow if fails
- **P1**: Important but not blocking
- **P2**: Nice to have / UI polish

### Status Values
`✅ Pass | ❌ Fail | ⏳ Pending | 🚫 Blocked | ⚠️ Partial`

---

## How to Execute Tests (The Full Flow)

### Phase 1: Setup (UI)
1. Login to https://tmt.affnook.io
2. Create/identify a **Brand** with Products
3. Create a **Campaign** with appropriate Payout Details for the feature being tested
4. Create an **Affiliate** to promote the campaign
5. Go to Campaign → **Manage Links** tab
6. Select the Affiliate → Click **Generate**
7. Copy the generated tracking link

### Phase 2: Get Tracking Token
1. Paste the tracking link in the browser
2. The browser redirects to the landing page
3. URL will look like: `https://xyz.domain.com/?token=69e681d0b6e25fc69a199a49`
4. Copy the **tracking_token** value after `?token=`

### Phase 3: Create Customer (Postman)
1. Open Postman → correct panel collection → `POST Create Customer`
2. Ensure Headers are set:
   - `Accept: application/json`
   - `Authorization: Bearer 123`
   - `Content-Type: application/json`
   - `x-api-key: <from Configuration → Automation → API Keys>`
3. Set Body (raw JSON):
```json
{
  "customerId": "Feature_Cus_001",
  "customerName": "Feature_Cus_001",
  "timestamp": "{{$timestamp}}",
  "currency": "usd",
  "trackingToken": "<tracking_token>",
  "country": "<country_for_test>",
  "region": "<region_for_test>",
  "city": "<city_for_test>"
}
```
4. Send → expect `200 OK`
5. Note the `customer_id` from response

### Phase 4: Create Activity (Postman)
1. Open `POST create activity` in same panel
2. Body:
```json
{
  "customerId": "Feature_Cus_001",
  "activityType": "deposit",
  "amount": 100,
  "timestamp": "{{$timestamp}}",
  "currency": "usd"
}
```
3. Send → expect `200 OK`

### Phase 5: Verify in Reports
1. Wait **~2 minutes**
2. Open Activity Report (or relevant report)
3. Find the customer's event
4. Verify: Status, Rejection Reason, Country, Region, City columns

---

## How to Find x-api-key (Critical)
- Go to platform → **Configuration → Automation → API tab**
- Copy the API Key shown
- ⚠️ This is **different for each panel** (AB Network, AB Operator, TMT, etc.)
- Paste into Postman headers as `x-api-key`

---

## How to Report Bugs

When a test fails, record in the Bugs Found table:
```
| Bug ID | TC ID | Module | Title | Severity | Steps to Reproduce | Expected | Actual | Status |
```

Severity levels:
- **Critical (S1)**: Feature completely broken / data loss
- **Major (S2)**: Core functionality broken, workaround exists
- **Minor (S3)**: UI issue, cosmetic, non-blocking
- **Trivial (S4)**: Spelling, alignment, cosmetic

---

## How to Update TC Sheet After Testing

After each test case:
1. Fill in `Actual Result` column
2. Update `Status` to ✅/❌/⚠️/🚫
3. If ❌: Add Bug ID and fill Bugs Found table
4. Update Execution Summary counts

---

## Domain Knowledge: Geo Targeting Logic

```
Hierarchy: Country → Region (State/Province) → City

Rules:
- Country = ALL → Region & City disabled, Include/Exclude hidden
- Country selected → Region selector appears
- Region selected → City selector appears

Include/Exclude Logic:
- Exclusion ALWAYS overrides Inclusion
- More specific level overrides broader level
- Priority: City > Region > Country

Evaluation Order:
1. Check Country eligibility
2. Check Region (include/exclude)
3. Check City (include/exclude)
→ If excluded: Rejected (Geo Not Allowed)
→ If included: Process normally
→ If not specified: Default to Country logic

Key Examples:
- USA, Include CA, Exclude LA → LA rejected, SF passes
- USA, Exclude TX, Include Houston → Houston rejected (region exclusion wins)

Schema fields: region, region_mode ('include'|'exclude'), city, city_mode ('include'|'exclude')
Default mode: 'include' (backward compatibility)
```

---

## What to Test for Any Payout Feature

Always cover these areas:
1. **UI Presence** — Are the new fields/toggles/selectors visible?
2. **UI Behaviour** — Do they show/hide correctly based on conditions?
3. **UI Save** — Does saving persist the config correctly?
4. **E2E Flow** — Does the backend evaluate correctly? (via Postman customer + activity)
5. **Reports** — Does the event appear with correct status/reason/columns?
6. **API** — Do new endpoints work? Do existing endpoints accept new fields?
7. **Edge Cases** — What happens with empty data, missing data, conflicting rules?
8. **Backward Compatibility** — Do existing campaigns/payouts still work?
