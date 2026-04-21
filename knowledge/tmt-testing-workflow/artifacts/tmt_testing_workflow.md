# TMT Platform – Testing Workflow

## Platform URLs
| Environment | URL |
|-------------|-----|
| TMT QA | https://tmt.affnook.io |
| AB Network QA | https://oscorp7.affnookqa1.online |
| AB Operator QA | https://oscorp7.affnookqa1.online (different panel) |

## Login Credentials
| Field | Value |
|-------|-------|
| URL | https://tmt.affnook.io/login |
| Email | shivansh03@gmail.com |
| Password | test@123 |

## x-api-key (TMT Panel)
```
520c1935005fb55643adbad0c3f8a47668dfc0c5b7c66761373bf8de2324aefa2a4cf4395f3ad7dd
```

---

## Panels in Postman
The user has multiple Postman collections, one per panel:
- **AB Net** → uses AB Network x-api-key
- **AB op** → uses AB Operator x-api-key
- **BiAffiliation** → uses BiAffiliation x-api-key
- **KtAccount** → uses KtAccount x-api-key
- **tmtpanel** → uses TMT x-api-key

Each collection has:
- `POST Create Customer`
- `POST create activity`

---

## Full Test Execution Flow (ALWAYS follow this order)

```
1. Create a Brand (with associated Products) on the platform
2. Create a Campaign linked to the Brand
   - Set Payout Details (Coverage, Payout Plan, Commission Variable)
3. Create an Affiliate to promote the Campaign
4. Go to Campaign → Manage Links tab
   - Select the Affiliate from dropdown
   - Click "Generate" to get the tracking link
   - Example: https://ascorp7.goaffnic.com/click?campaign_id=56&pub_id=7
5. Paste the generated tracking link in the browser
   - The browser redirects to the landing page URL
   - The URL will contain the tracking_token
   - Example: https://xyz.domain.com/?token=69e681d0b6e25fc69a199a49
   - COPY the tracking_token value (e.g., 69e681d0b6e25fc69a199a49)
6. Open Postman → correct panel collection → "Create Customer"
   - Paste the tracking_token into the "trackingToken" field in request body
   - Set country, region, city in the body as needed for the test case
   - Send the request → 200 OK expected
   - Note the customer_id from the response
7. Open Postman → "create activity" (same panel)
   - Use the customer_id from step 6
   - Send the request → 200 OK expected
8. Wait ~2 minutes for data to reflect in reports
9. Check the relevant report (Activity Report, Campaign Report, Affiliate Report, etc.)
   - Verify the event appears with correct Status, Rejection Reason, Region, City
```

---

## Where to Find the x-api-key
- On the platform: **Configuration → Automation → API tab**
- The API Key is displayed and can be copied
- This key is **different for each panel/brand** — always copy from the correct panel

---

## Postman / curl Headers (same for every request)
```
Accept: application/json
Authorization: Bearer 123
Content-Type: application/json
x-api-key: 520c1935005fb55643adbad0c3f8a47668dfc0c5b7c66761373bf8de2324aefa2a4cf4395f3ad7dd
```

> **Note for Antigravity**: Instead of Postman, you can use `curl` to make these API calls directly from the terminal. Same headers, same body.

---

## Postman: Create Customer – Request Body Template
```json
{
  "customerId": "CnR_Cus_001",
  "customerName": "CnR_Cus_001",
  "timestamp": "{{$timestamp}}",
  "currency": "usd",
  "trackingToken": "<paste_tracking_token_here>",
  "country": "In",
  "region": "Uttar Pradesh",
  "city": "Noida"
}
```
- Change `country`, `region`, `city` per test case scenario
- `customerId` must be unique per customer — increment for each test

---

## Postman: Create Activity – Request Body Template
```json
{
  "customerId": "CnR_Cus_001",
  "activityType": "deposit",
  "amount": 100,
  "timestamp": "{{$timestamp}}",
  "currency": "usd"
}
```

---

## Reports & Wait Time
- After creating activity → **wait ~2 minutes** before checking reports
- Reports available: Activity Report, Campaign Report, Affiliate Report, Click Report, Conversion Report, Brand Report, Customer Report, Media Report, Referral Report
- Activity Report shows: Status (Approved/Rejected), Rejection Reason, Country, Region, City

---

## How to Create TC Sheets
When user provides a PRD and/or API Design Document:
1. Parse all functional requirements
2. Organize TCs by Module (UI modules first, then E2E/Geo Logic, then API, then Reports, then Edge Cases)
3. Use priority: P0 (must pass), P1 (should pass), P2 (nice to have)
4. Include columns: TC ID | Test Case | Priority | Steps | Expected Result | Actual Result | Status | Bug ID
5. Add Pre-requisites checklist at top
6. Add Execution Flow diagram
7. Add Postman Config Reference at bottom
8. Add Bugs Found table
9. Add Execution Summary table

---

## Key Domain Knowledge
- **Geo Hierarchy**: Country → Region (State/Province) → City
- **Include/Exclude Logic**: Exclusion overrides Inclusion. More specific level overrides broader level.
- **Priority**: City > Region > Country (specificity-based)
- **Filtering**: Must happen BEFORE priority sorting
- **Schema fields added**: `region`, `region_mode`, `city`, `city_mode` (values: "include" | "exclude")
- **Default mode**: "include" for backward compatibility
- **Rejection reason**: "Geo Not Allowed" when event blocked by geo
- **Geo evaluation order**: Country check → Region check → City check
- **Rule priority**: Payout Rule geo > Base payout geo
