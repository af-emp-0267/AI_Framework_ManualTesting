# Workflow: Regression Check After Bug Fix

## Description
Use this workflow when a bug has been fixed and you need to verify the fix + ensure no regressions were introduced.

## When to Use
- After developer marks a bug as "Fixed"
- Before closing a bug ticket
- When retesting a specific test case that previously failed

## How to Invoke
```
@regression-check

Bug: <Bug ID or description>
Original TC: <TC ID that failed, e.g., GEO-005>
Fix Description: <what was changed>
Campaign: <Campaign ID>
Tracking Token: <token>
```

---

## Steps

### Step 1: Read Context
- Load KI and read the original TC sheet at `/Users/nikhilsharma/Manual_Testing/`
- Find the failed TC by ID
- Understand what was expected vs what actually happened

### Step 2: Reproduce Original Bug
- Re-run the exact steps from the failed TC
- If it was an API test: run the same curl command
- If it was a UI test: navigate to the same screen
- Verify the bug is now fixed (actual = expected)

### Step 3: Run Related Test Cases
Identify related TCs that could be affected by the fix:
- Same module TCs
- TCs with similar geo configuration
- Edge case TCs related to the same logic

Run each and verify Pass/Fail.

### Step 4: Quick Smoke Test
Run 3-5 basic happy-path scenarios to ensure no regression:
1. Country-only payout still works
2. Region Include still works
3. Region Exclude still works
4. City Include still works
5. City Exclude still works

### Step 5: Update TC Sheet
- Update the original failed TC: change Status to ✅ Pass (if fixed)
- Update Bug ID entry in Bugs Found table: Status → "Fixed & Verified"
- Update any newly failed TCs if regression found

### Step 6: Report
Tell user:
- ✅ Bug fix verified: Yes/No
- 🔄 Regression found: Yes/No (list any new failures)
- 📋 TCs re-tested: <list>

---

## Output
- Updated TC sheet with re-tested statuses
- Bug table updated
- Regression assessment
