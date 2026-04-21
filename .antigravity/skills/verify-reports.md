# Skill: Verify Reports After Testing

## When to Use
Use this skill when the user has created customers and activities and wants to verify that the data appears correctly in the TMT platform reports.

## Important: Wait Time
After creating an activity via API, wait **~2 minutes** before checking reports. The data pipeline has a processing delay.

## Reports to Check

### 1. Activity Report
- Path: Left sidebar → ENGAGEMENTS → Activity Report
- Check columns: Status, Rejection Reason, Country, Region, City
- For geo-rejected events: Status = "Rejected", Rejection Reason = "Geo Not Allowed"
- For approved events: Status = "Approved"

### 2. Campaign Report
- Path: Left sidebar → ENGAGEMENTS → Campaign Report
- Check: Region & City columns are available
- Check: Geo-rejected events appear with correct status

### 3. Affiliate Report
- Path: Left sidebar → ENGAGEMENTS → Affiliate Report
- Check: Region & City columns are available

### 4. Click Report
- Path: Left sidebar → ENGAGEMENTS → Click Report
- Check: Geo-rejected events visible

### 5. Conversion Report
- Path: Left sidebar → ENGAGEMENTS → Conversion Report
- Check: Geo-rejected events visible

### 6. Brand Report
- Path: Left sidebar → ENGAGEMENTS → Brand Report
- Check: Region & City data available

### 7. Customer Report
- Path: Left sidebar → ENGAGEMENTS → Customer Report
- Check: Customer appears with correct geo data

## Filters to Verify
For each report, check if these filters exist and work:
- Country filter
- Region filter (NEW)
- City filter (NEW)
- Rejection Reason filter (should include "Geo Not Allowed")

## Export Verification
- Export the Activity Log as CSV/Excel
- Verify columns present: Country, Region, City, Rejection Reason

## Group-By Verification
- Try grouping reports by City (new dimension)
- Verify data groups correctly

## How to Navigate (Browser Steps)
1. Login to https://tmt.affnook.io
2. Click the report name in left sidebar
3. Set date range to include today
4. Look for the test customer/activity
5. Take screenshot of results
6. Apply filters and verify
7. Export and check columns

## Updating TC Sheet
After verification, update these TCs in the sheet:
- RPT-001 through RPT-014
- Fill in Actual Result and Status columns
