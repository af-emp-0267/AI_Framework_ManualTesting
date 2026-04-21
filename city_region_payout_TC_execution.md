# Test Execution Sheet: City & Region Level Payout Coverage
# Include / Exclude Support

> **Feature**: City & Region Level Coverage with Include/Exclude Support in Payouts
> **Platform**: https://tmt.affnook.io
> **Tester**: Nikhil Sharma
> **Execution Date**: 2026-04-21
> **Build/Environment**: TMT QA
> **Status Legend**: ✅ Pass | ❌ Fail | ⏳ Pending | 🚫 Blocked | ⚠️ Partial

---

## Pre-requisites Checklist

| # | Pre-requisite | Status | Notes |
|---|---------------|--------|-------|
| 1 | TMT platform accessible | ⏳ | https://tmt.affnook.io |
| 2 | Test Brand created | ⏳ | Brand with associated products |
| 3 | Test Campaign created (CPA type) | ⏳ | Campaign linked to brand |
| 4 | Test Affiliate created | ⏳ | Affiliate to promote campaign |
| 5 | Tracking link generated | ⏳ | From Campaign → Manage Links |
| 6 | Postman collection configured | ⏳ | AB Net / TMT panel headers set |
| 7 | x-api-key copied from Automation → API | ⏳ | From Configuration → Automation |
| 8 | Postman headers configured | ⏳ | Accept, Authorization, Content-Type, x-api-key |

---

## Test Execution Flow

```
Brand (with Products)
  → Campaign (with Payout Details)
    → Affiliate (to promote)
      → Generate Tracking Link
        → Paste in browser → Get tracking_token
          → Postman: Create Customer (with tracking_token, country, region, city)
            → Postman: Create Activity (with customer_id)
              → Wait ~2 min → Check Reports
```

---

## Module 1: Campaign → Payout Details (UI Validation)

| TC ID | Test Case | Priority | Steps | Expected Result | Actual Result | Status | Bug ID |
|-------|-----------|----------|-------|-----------------|---------------|--------|--------|
| CP-UI-001 | Verify Region selector appears after selecting a specific Country | P0 | 1. Navigate to Campaigns 2. Open a campaign 3. Go to Payout Details 4. Edit Coverage 5. Select Country = USA | Region multi-select dropdown appears below Country selector | | ⏳ | |
| CP-UI-002 | Verify City selector appears after selecting a Region | P0 | 1. Select Country = USA 2. Select Region = California | City multi-select dropdown appears below Region selector | | ⏳ | |
| CP-UI-003 | Verify Region & City selectors are disabled when Country = ALL | P0 | 1. Set Country = ALL | Region & City selectors disabled/hidden. Include/Exclude toggles hidden | | ⏳ | |
| CP-UI-004 | Verify Region dropdown shows only regions of selected country | P1 | 1. Select Country = USA 2. Open Region dropdown | Only US states shown (California, Texas, New York, etc.) | | ⏳ | |
| CP-UI-005 | Verify City dropdown shows only cities of selected region | P1 | 1. Select Country = USA, Region = California 2. Open City dropdown | Only California cities shown (Los Angeles, San Francisco, etc.) | | ⏳ | |
| CP-UI-006 | Verify multi-country selection shows grouped regions | P1 | 1. Select Countries = USA, India 2. Open Region dropdown | Regions grouped by country (US states and Indian states separately) | | ⏳ | |
| CP-UI-007 | Verify Include/Exclude toggle for Region - default is "Include" | P0 | 1. Select a Country 2. Observe Region toggle | Default = "Include Selected" | | ⏳ | |
| CP-UI-008 | Verify Include/Exclude toggle for City - default is "Include" | P0 | 1. Select a Region 2. Observe City toggle | Default = "Include Selected" | | ⏳ | |
| CP-UI-009 | Verify switching Region toggle to Exclude works | P0 | 1. Select Region = California 2. Toggle to "Exclude Selected" 3. Save | Toggle updates. Config saved correctly with region_mode=exclude | | ⏳ | |
| CP-UI-010 | Verify switching City toggle to Exclude works | P0 | 1. Select City = Los Angeles 2. Toggle to "Exclude Selected" 3. Save | Toggle updates. Config saved correctly with city_mode=exclude | | ⏳ | |
| CP-UI-011 | Verify helper text under Coverage section | P2 | 1. Navigate to Coverage section | Helper text: "You can include or exclude specific regions and cities. Exclusion overrides inclusion. City rules override region rules." | | ⏳ | |
| CP-UI-012 | Verify saving payout with Region Include configuration | P0 | 1. Country=USA, Region=California (Include) 2. Click Save | Payout saved successfully. API response shows region=["California"], region_mode="include" | | ⏳ | |
| CP-UI-013 | Verify saving payout with Region Exclude configuration | P0 | 1. Country=USA, Region=Texas (Exclude) 2. Click Save | Payout saved successfully. API response shows region=["Texas"], region_mode="exclude" | | ⏳ | |
| CP-UI-014 | Verify saving payout with City Include configuration | P0 | 1. Country=USA, Region=CA, City=LA (Include) 2. Save | Payout saved. city=["Los Angeles"], city_mode="include" | | ⏳ | |
| CP-UI-015 | Verify saving payout with City Exclude configuration | P0 | 1. Country=USA, Region=CA, City=LA (Exclude) 2. Save | Payout saved. city=["Los Angeles"], city_mode="exclude" | | ⏳ | |
| CP-UI-016 | Verify editing existing campaign preserves geo config | P1 | 1. Open campaign with existing geo config 2. Check Coverage | Include/Exclude state, regions, cities all preserved correctly | | ⏳ | |
| CP-UI-017 | Verify removing country auto-removes related regions & cities | P1 | 1. Campaign with USA → California → LA 2. Remove USA from countries | California and LA auto-removed from selections | | ⏳ | |
| CP-UI-018 | Verify deleting a region auto-removes associated cities | P1 | 1. Region=California with City=LA configured 2. Remove California | LA auto-removed from city selection | | ⏳ | |
| CP-UI-019 | Verify multiple regions can be selected simultaneously | P1 | 1. Select Country=USA 2. Select California AND Texas | Both regions appear as selected chips/tags | | ⏳ | |
| CP-UI-020 | Verify city search uses async typeahead (performance) | P2 | 1. Select a country with many cities 2. Type in city search box | Typeahead works with async loading, no full DB load, pagination present | | ⏳ | |

---

## Module 2: Affiliate Group → Payout Details (UI)

| TC ID | Test Case | Priority | Steps | Expected Result | Actual Result | Status | Bug ID |
|-------|-----------|----------|-------|-----------------|---------------|--------|--------|
| AG-UI-001 | Verify Region selector appears in Affiliate Group payout | P0 | 1. Open Affiliate Group → Payout Details 2. Select Country | Region selector appears | | ⏳ | |
| AG-UI-002 | Verify City selector appears in Affiliate Group payout | P0 | 1. Select Region in Affiliate Group | City selector appears | | ⏳ | |
| AG-UI-003 | Verify Include/Exclude toggle for Region in Affiliate Group | P0 | 1. Select Country & Region 2. Check toggle | Include/Exclude toggle present and functional | | ⏳ | |
| AG-UI-004 | Verify Include/Exclude toggle for City in Affiliate Group | P0 | 1. Select Region & City 2. Check toggle | Include/Exclude toggle present and functional | | ⏳ | |
| AG-UI-005 | Verify Country=ALL disables Region & City in Affiliate Group | P0 | 1. Select Country=ALL | Region & City disabled, toggles hidden | | ⏳ | |
| AG-UI-006 | Verify saving Affiliate Group payout with geo config | P0 | 1. Configure full geo targeting 2. Save | Payout saved with region, region_mode, city, city_mode | | ⏳ | |
| AG-UI-007 | Verify editing Affiliate Group preserves geo config | P1 | 1. Open existing group with geo config | All geo config preserved | | ⏳ | |
| AG-UI-008 | Verify API response includes city_mode and region_mode | P1 | 1. Save group with Exclude mode 2. GET via API | Response includes city_mode/region_mode fields | | ⏳ | |

---

## Module 3: Direct Affiliate Payout (Add New Payout Modal)

| TC ID | Test Case | Priority | Steps | Expected Result | Actual Result | Status | Bug ID |
|-------|-----------|----------|-------|-----------------|---------------|--------|--------|
| DAP-001 | Verify Region selector in Add New Payout modal | P0 | 1. Open Add New Payout modal 2. Select Country | Region selector visible | | ⏳ | |
| DAP-002 | Verify City selector in Add New Payout modal | P0 | 1. Select Region in modal | City selector visible | | ⏳ | |
| DAP-003 | Verify Include/Exclude toggle in Add New Payout modal | P0 | 1. Select Country & Region in modal | Include/Exclude toggles visible for Region and City | | ⏳ | |
| DAP-004 | Verify saving direct payout with Region Include | P0 | 1. Configure Region (Include) 2. Save | Payout created with correct geo config | | ⏳ | |
| DAP-005 | Verify saving direct payout with City Exclude | P0 | 1. Configure City (Exclude) 2. Save | Payout created with correct geo config | | ⏳ | |
| DAP-006 | Verify modal behavior identical to Campaign screen | P1 | 1. Compare field behaviors vs Campaign screen | Identical behavior for all geo fields | | ⏳ | |

---

## Module 4: Payout Rules

| TC ID | Test Case | Priority | Steps | Expected Result | Actual Result | Status | Bug ID |
|-------|-----------|----------|-------|-----------------|---------------|--------|--------|
| PR-001 | Verify Add Rule supports Country + Region + City | P0 | 1. Open Campaign → Payout Rules 2. Click Add Rule 3. Check Coverage fields | Country, Region (Include/Exclude), City (Include/Exclude) available | | ⏳ | |
| PR-002 | Verify Rule-level geo overrides base payout geo | P0 | 1. Base: Include USA 2. Rule: Exclude California 3. Event from CA via Postman | Event rejected per rule-level override | | ⏳ | |
| PR-003 | Verify saving rule with Region Exclude | P0 | 1. Add Rule with Region=Texas, mode=Exclude 2. Save | Rule saved correctly | | ⏳ | |
| PR-004 | Verify saving rule with City Include | P0 | 1. Add Rule with City=Houston, mode=Include 2. Save | Rule saved correctly | | ⏳ | |
| PR-005 | Verify multiple rules with different geo configs | P1 | 1. Rule 1: Include California 2. Rule 2: Exclude LA | Both saved, most specific (City) applies | | ⏳ | |
| PR-006 | Verify Rule priority > Base payout priority | P0 | 1. Base: Include USA 2. Rule: Exclude California 3. Event from CA | Rule exclusion applied → event rejected | | ⏳ | |

---

## Module 5: Geo Evaluation Logic (E2E via Postman)

> **Flow**: Configure Campaign Geo → Generate Link → Get tracking_token → Create Customer (Postman) → Create Activity (Postman) → Wait ~2 min → Check Reports

| TC ID | Test Case | Priority | Postman Setup | Expected Result | Actual Result | Status | Bug ID |
|-------|-----------|----------|---------------|-----------------|---------------|--------|--------|
| GEO-001 | Country match + Region Include match → Payout applied | P0 | Campaign: USA, Include CA. Customer: country=US, region=California, city=LA | Payout applied. Activity shows in reports with payout | | ⏳ | |
| GEO-002 | Country match + Region Exclude → Rejected | P0 | Campaign: USA, Exclude TX. Customer: country=US, region=Texas, city=Houston | Event rejected. Status=Rejected, Reason=Geo Not Allowed | | ⏳ | |
| GEO-003 | Region Include + City Exclude → City rejected | P0 | Campaign: USA, Include CA, Exclude LA. Customer: country=US, region=California, city=Los Angeles | Event rejected for LA. Reason=Geo Not Allowed | | ⏳ | |
| GEO-004 | Region Include + City Exclude → Other city passes | P0 | Campaign: USA, Include CA, Exclude LA. Customer: country=US, region=California, city=San Francisco | Payout applied for SF | | ⏳ | |
| GEO-005 | Region Excluded + City Inside Included → Rejected (PRD §5.4) | P0 | Campaign: USA, Exclude TX, Include Houston. Customer: country=US, region=Texas, city=Houston | Event REJECTED. Region exclusion overrides city inclusion | | ⏳ | |
| GEO-006 | No region/city configured → Country-only logic | P0 | Campaign: USA only, no region/city. Customer: country=US, region=Texas, city=Dallas | Payout applied (country match only) | | ⏳ | |
| GEO-007 | Country match + Region not in Include list → Rejected | P1 | Campaign: USA, Include CA only. Customer: country=US, region=Texas | Rejected (TX not in include list) | | ⏳ | |
| GEO-008 | Empty region & city arrays → All geo eligible | P0 | Campaign: USA, region=[], city=[]. Customer: country=US, any region/city | Payout applied | | ⏳ | |
| GEO-009 | Country fails → Immediate reject (no region/city check) | P0 | Campaign: USA only. Customer: country=IN | Rejected immediately. No region/city evaluation | | ⏳ | |
| GEO-010 | Missing region/city in tracking data → Country-level only | P1 | Campaign: USA, Include CA. Customer: country=US (no region/city) | Evaluate country-level only. Do NOT auto-reject | | ⏳ | |
| GEO-011 | Geo rejected → No payout, no bonus, no RevShare | P0 | Campaign with geo config. Customer: geo mismatch | No payout calculated. No bonus. No RevShare. No Hybrid | | ⏳ | |
| GEO-012 | Fallback to global payout when geo rejected | P1 | Geo mismatch but global payout exists | Fallback to global/default payout | | ⏳ | |

---

## Module 6: API Validation

| TC ID | Test Case | Priority | API Call | Expected Response | Actual Response | Status | Bug ID |
|-------|-----------|----------|----------|-------------------|-----------------|--------|--------|
| API-001 | GET /regions/filter returns regions for country | P0 | GET /web/admin/v2/regions/filter?country_code=US | Returns US regions (California, Texas, etc.) | | ⏳ | |
| API-002 | GET /regions/filter with typeahead name filter | P1 | GET /web/admin/v2/regions/filter?country_code=US&name=Cal | Returns filtered: California | | ⏳ | |
| API-003 | GET /regions/filter with pagination | P1 | GET /web/admin/v2/regions/filter?country_code=US&page=1&limit=5 | Returns 5 paginated results | | ⏳ | |
| API-004 | GET /cities/filter returns cities for region | P0 | GET /web/admin/v2/cities/filter?region_name=California | Returns California cities (LA, SF, etc.) | | ⏳ | |
| API-005 | GET /cities/filter - min 2 chars for name filter | P1 | GET /web/admin/v2/cities/filter?region_name=California&name=L | Returns error or empty (min 2 chars required) | | ⏳ | |
| API-006 | GET /cities/filter with typeahead | P1 | GET /web/admin/v2/cities/filter?region_name=California&name=Los | Returns Los Angeles, Los Gatos, etc. | | ⏳ | |
| API-007 | POST /commission accepts geo fields | P0 | POST with city, city_mode, region, region_mode | Commission created with all geo fields | | ⏳ | |
| API-008 | POST /commission - invalid city_mode validation | P1 | POST with city_mode="invalid_value" | Returns validation error | | ⏳ | |
| API-009 | PATCH /commission updates geo fields | P0 | PATCH with updated region, region_mode | Commission updated correctly | | ⏳ | |
| API-010 | GET /commission returns geo fields | P0 | GET existing commission with geo | Response includes city, city_mode, region, region_mode | | ⏳ | |
| API-011 | POST /campaign supports geo targeting | P0 | POST campaign with region/city config | Campaign created with geo targeting | | ⏳ | |
| API-012 | POST /groups supports geo targeting | P0 | POST group with region/city config | Group created with geo targeting | | ⏳ | |
| API-013 | Comma-separated country_codes in regions API | P1 | GET /regions/filter?country_code=US,IN | Returns regions for both US and IN | | ⏳ | |

---

## Module 7: Reporting & Activity Logs

| TC ID | Test Case | Priority | Steps | Expected Result | Actual Result | Status | Bug ID |
|-------|-----------|----------|-------|-----------------|---------------|--------|--------|
| RPT-001 | Activity Log: Geo rejected event shows "Rejected" status | P0 | 1. Trigger geo-rejected event 2. Wait ~2 min 3. Open Activity Report | Status = Rejected visible | | ⏳ | |
| RPT-002 | Activity Log: Rejection Reason = "Geo Not Allowed" | P0 | 1. Check rejection reason for geo-rejected event | Shows "Geo Not Allowed" | | ⏳ | |
| RPT-003 | Activity Log: Filter by Rejection Reason works | P1 | 1. Apply filter: Rejection Reason = Geo Not Allowed | Only geo-rejected events shown | | ⏳ | |
| RPT-004 | Activity Log: Country filter available and works | P1 | 1. Apply Country filter in Activity Log | Filtered by country correctly | | ⏳ | |
| RPT-005 | Activity Log: Region filter available and works | P1 | 1. Apply Region filter | Filtered by region correctly | | ⏳ | |
| RPT-006 | Activity Log: City filter available and works | P1 | 1. Apply City filter | Filtered by city correctly | | ⏳ | |
| RPT-007 | Activity Log: Export includes Country, Region, City, Rejection Reason | P1 | 1. Export activity log as CSV/Excel | All 4 columns present in export | | ⏳ | |
| RPT-008 | Campaign Report: Region & City columns available | P1 | 1. Open Campaign Report 2. Check columns | Region and City columns present | | ⏳ | |
| RPT-009 | Affiliate Report: Region & City columns available | P1 | 1. Open Affiliate Report 2. Check columns | Region and City columns present | | ⏳ | |
| RPT-010 | Click Report: Geo rejected events visible | P1 | 1. Open Click Report | Rejected geo events shown with region/city | | ⏳ | |
| RPT-011 | Conversion Report: Geo rejected events visible | P1 | 1. Open Conversion Report | Rejected geo events shown | | ⏳ | |
| RPT-012 | Brand Report: Region & City data available | P1 | 1. Open Brand Report | Region and City data present | | ⏳ | |
| RPT-013 | Reports: City as group-by dimension | P2 | 1. Group any report by City | Report grouped by city correctly | | ⏳ | |
| RPT-014 | Reports: Geo filters (Country/Region/City) work across all reports | P1 | 1. Apply geo filters in Campaign, Affiliate, Click reports | Filtered results accurate in all reports | | ⏳ | |

---

## Module 8: Edge Cases & Backward Compatibility

| TC ID | Test Case | Priority | Steps | Expected Result | Actual Result | Status | Bug ID |
|-------|-----------|----------|-------|-----------------|---------------|--------|--------|
| EC-001 | Existing country-only campaign works unchanged | P0 | 1. Open a legacy campaign with country-only payout 2. Trigger event | Payout applied as before. No regression | | ⏳ | |
| EC-002 | Existing campaigns not broken after feature deployment | P0 | 1. List existing campaigns 2. Spot-check 3-5 campaigns | All function normally | | ⏳ | |
| EC-003 | Default mode = "include" for existing/legacy data | P0 | 1. GET legacy payout via API 2. Check mode fields | region_mode and city_mode default to "include" | | ⏳ | |
| EC-004 | Mixed payouts: some with geo, some without | P1 | 1. Have both geo and non-geo payouts 2. Trigger events for each | Both work correctly | | ⏳ | |
| EC-005 | Country selected, no region → entire country eligible | P1 | 1. Payout: Country=USA, no region 2. Event from any US state | Payout applied | | ⏳ | |
| EC-006 | Region included, no city → entire region eligible | P1 | 1. Payout: Include California, no city 2. Event from any CA city | Payout applied | | ⏳ | |
| EC-007 | City cross-region selection prevented | P2 | 1. Select Region=California 2. Try selecting a city from Texas | System prevents cross-region city selection | | ⏳ | |
| EC-008 | CAP behaviour unchanged with geo config | P1 | 1. Campaign with CAP + geo config 2. Test CAP limits | CAP still works correctly, unaffected by geo | | ⏳ | |
| EC-009 | CPA payout plan with geo targeting | P1 | 1. CPA campaign with geo 2. Eligible event | CPA payout calculated normally | | ⏳ | |
| EC-010 | Rev Share payout plan with geo targeting | P1 | 1. Rev Share campaign with geo 2. Eligible event | Rev Share calculated normally | | ⏳ | |
| EC-011 | Hybrid payout plan with geo targeting | P1 | 1. Hybrid campaign with geo 2. Eligible event | Hybrid payout calculated normally | | ⏳ | |
| EC-012 | Multiple conflicting rules → most specific wins | P1 | 1. Rule 1: Include California 2. Rule 2: Exclude LA 3. Event from LA | City-level exclusion wins → rejected | | ⏳ | |
| EC-013 | Tie in specificity → highest priority rule order wins | P2 | 1. Two region-level rules with same specificity 2. Event | Higher priority order wins | | ⏳ | |
| EC-014 | Affiliate visibility unchanged with geo feature | P1 | 1. Check affiliate visibility settings | Unchanged from pre-feature behavior | | ⏳ | |
| EC-015 | Commission variable unchanged with geo feature | P1 | 1. Check commission variable in payout | Commission variable unaffected | | ⏳ | |

---

## Execution Summary

| Module | Total TCs | P0 | P1 | P2 | ✅ Pass | ❌ Fail | ⏳ Pending | 🚫 Blocked |
|--------|-----------|----|----|-----|---------|---------|------------|------------|
| Campaign Payout UI | 20 | 10 | 7 | 3 | 0 | 0 | 20 | 0 |
| Affiliate Group Payout UI | 8 | 5 | 3 | 0 | 0 | 0 | 8 | 0 |
| Direct Affiliate Payout Modal | 6 | 4 | 2 | 0 | 0 | 0 | 6 | 0 |
| Payout Rules | 6 | 4 | 2 | 0 | 0 | 0 | 6 | 0 |
| Geo Evaluation Logic (E2E) | 12 | 8 | 4 | 0 | 0 | 0 | 12 | 0 |
| API Validation | 13 | 7 | 6 | 0 | 0 | 0 | 13 | 0 |
| Reporting & Activity Logs | 14 | 2 | 10 | 2 | 0 | 0 | 14 | 0 |
| Edge Cases & Backward Compat | 15 | 3 | 10 | 2 | 0 | 0 | 15 | 0 |
| **Total** | **94** | **43** | **44** | **7** | **0** | **0** | **94** | **0** |

---

## Bugs Found

| Bug ID | TC ID | Module | Title | Severity | Steps to Reproduce | Expected | Actual | Screenshot | Status |
|--------|-------|--------|-------|----------|---------------------|----------|--------|------------|--------|
| | | | | | | | | | |

---

## Postman Configuration Reference

### Headers (for all panels - AB Network / AB Operator / TMT)
| Key | Value | Notes |
|-----|-------|-------|
| Accept | application/json | Same across panels |
| Authorization | Bearer 123 | Same across panels |
| Content-Type | application/json | Same across panels |
| x-api-key | (copy from Configuration → Automation → API Keys) | **Different per panel** |

### Create Customer Request Body
```json
{
  "customerId": "CnR_Cus_XXX",
  "customerName": "CnR_Cus_XXX",
  "timestamp": "{{$timestamp}}",
  "currency": "usd",
  "trackingToken": "<paste_tracking_token_here>",
  "country": "In",
  "region": "Uttar Pradesh",
  "city": "Noida"
}
```

### Create Activity Request Body
```json
{
  "customerId": "CnR_Cus_XXX",
  "activityType": "deposit",
  "amount": 100,
  "timestamp": "{{$timestamp}}",
  "currency": "usd"
}
```

> **Note**: After creating activity, wait ~2 minutes for data to reflect in reports.

---

## Notes & Observations

| # | Date | Observation |
|---|------|-------------|
| | | |
