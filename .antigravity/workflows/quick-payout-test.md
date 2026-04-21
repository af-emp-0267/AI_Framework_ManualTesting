# Workflow: Quick Payout E2E Test

## Description
Rapid end-to-end payout testing workflow. Use when you already have a campaign set up and just need to test specific geo scenarios quickly via API calls + report verification.

## When to Use
When you need to quickly test a few payout scenarios without creating a full TC sheet. Good for:
- Retesting after a bug fix
- Smoke testing a specific scenario
- Quick regression check

## How to Invoke
```
@quick-payout-test

Campaign: <Campaign Name or ID>
Tracking Token: <token>
Panel: TMT
Scenarios:
1. Country=US, Region=California, City=LA → should pass
2. Country=US, Region=Texas, City=Houston → should reject
3. Country=IN, Region=UP, City=Noida → should reject (wrong country)
```

---

## Steps

### Step 1: Read Context
- Load KI for platform credentials and API config
- Read `e2e-api-testing` skill for curl templates

### Step 2: Generate Customer IDs
- Create unique IDs per scenario: `Quick_<Campaign>_001`, `Quick_<Campaign>_002`, etc.
- Use current Unix timestamp for the timestamp field

### Step 3: Create Customers (curl)
**Skill**: `@e2e-api-testing`
For each scenario, run:
```bash
curl -s -X POST "https://api.affnook.io/api/admin/v2/customers" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer 123" \
  -H "Content-Type: application/json" \
  -H "x-api-key: <from KI>" \
  -d '{
    "customerId": "<UNIQUE_ID>",
    "customerName": "<UNIQUE_ID>",
    "timestamp": <UNIX_TIMESTAMP>,
    "currency": "usd",
    "trackingToken": "<TRACKING_TOKEN>",
    "country": "<COUNTRY>",
    "region": "<REGION>",
    "city": "<CITY>"
  }'
```
- Record response for each (200 OK or error)

### Step 4: Create Activities (curl)
For each customer created in Step 3:
```bash
curl -s -X POST "https://api.affnook.io/api/admin/v2/activities" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer 123" \
  -H "Content-Type: application/json" \
  -H "x-api-key: <from KI>" \
  -d '{
    "customerId": "<CUSTOMER_ID>",
    "activityType": "deposit",
    "amount": 100,
    "timestamp": <UNIX_TIMESTAMP>,
    "currency": "usd"
  }'
```

### Step 5: Wait
- Tell user: "Activities created. Wait ~2 minutes, then check Activity Report."
- List which customer IDs to look for and expected status for each

### Step 6: Report Check
**Skill**: `@verify-reports`
- Tell user exactly which report to open
- Which customer IDs to search for
- What to expect for each:
  - Eligible scenario → Status: Approved
  - Rejected scenario → Status: Rejected, Reason: Geo Not Allowed

### Step 7: Result Summary
Print a table:
```
| Scenario | Customer ID | Geo | Expected | Actual | Status |
```

---

## Output
- Quick summary table of all scenarios tested
- Clear Pass/Fail per scenario
- Any bugs noted inline
