# Skill: Execute E2E Payout Testing via API

## When to Use
Use this skill when the user wants to test payout logic end-to-end using API calls (curl) instead of Postman. This covers creating customers with different geo data and verifying payout behavior.

## Prerequisites
Before running this skill, check the KI at:
`/Users/nikhilsharma/.gemini/antigravity/knowledge/tmt-testing-workflow/`

You need:
- x-api-key (from KI or user provides it)
- A valid tracking_token (user must provide OR generate via browser)
- The campaign's geo configuration (what country/region/city is set)

## Platform Credentials
- URL: https://tmt.affnook.io/login
- Email: shivansh03@gmail.com
- Password: test@123
- x-api-key: 520c1935005fb55643adbad0c3f8a47668dfc0c5b7c66761373bf8de2324aefa2a4cf4395f3ad7dd

## API Endpoints

### Create Customer
```bash
curl -s -X POST "https://api.affnook.io/api/admin/v2/customers" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer 123" \
  -H "Content-Type: application/json" \
  -H "x-api-key: <X_API_KEY>" \
  -d '{
    "customerId": "<UNIQUE_ID>",
    "customerName": "<UNIQUE_NAME>",
    "timestamp": <UNIX_TIMESTAMP>,
    "currency": "usd",
    "trackingToken": "<TRACKING_TOKEN>",
    "country": "<COUNTRY_CODE>",
    "region": "<REGION_NAME>",
    "city": "<CITY_NAME>"
  }'
```

### Create Activity
```bash
curl -s -X POST "https://api.affnook.io/api/admin/v2/activities" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer 123" \
  -H "Content-Type: application/json" \
  -H "x-api-key: <X_API_KEY>" \
  -d '{
    "customerId": "<CUSTOMER_ID>",
    "activityType": "deposit",
    "amount": 100,
    "timestamp": <UNIX_TIMESTAMP>,
    "currency": "usd"
  }'
```

## Test Scenarios to Run

### Scenario 1: Eligible Event (Happy Path)
- Customer geo matches campaign geo config
- Expected: 200 OK, payout applied, shows in reports

### Scenario 2: Region Excluded
- Customer region is in the exclude list
- Expected: Event rejected, Rejection Reason = "Geo Not Allowed"

### Scenario 3: City Excluded, Region Included
- Customer city excluded but region included
- Expected: Rejected for that city

### Scenario 4: Region Excluded, City Inside Included
- Customer region excluded but city inside it included
- Expected: REJECTED (region exclusion wins per PRD §5.4)

### Scenario 5: Country Mismatch
- Customer country doesn't match campaign
- Expected: Immediate rejection

### Scenario 6: Missing Region/City in Data
- Customer has country only, no region/city
- Expected: Evaluate country-level only, do NOT auto-reject

## Execution Flow
1. Generate unique customerId for each scenario (e.g., GEO_Test_001, GEO_Test_002)
2. Run Create Customer curl for each scenario
3. Run Create Activity curl for each customer
4. Wait 2 minutes
5. Tell user to check Activity Report for results
6. Update TC sheet with Pass/Fail

## Important Notes
- Each customerId must be unique across all tests
- Timestamp should be current Unix timestamp: $(date +%s)
- After activity creation, reports take ~2 minutes to update
- The "Authorization: Bearer 123" is a static token for the API, NOT a JWT — check with user if this works or if a real JWT is needed
- The x-api-key is panel-specific — different for AB Network vs TMT vs others
