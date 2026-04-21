# Skill: Generate TC Sheet from PRD

## When to Use
Use this skill when the user provides a PRD (Product Requirements Document) and/or API Design Document and wants a Test Case execution sheet created.

## Instructions

### Step 1: Parse the PRD
Extract from the PRD:
- Feature name
- All functional requirements (numbered sections)
- UI changes (which screens are affected)
- Business logic rules
- Edge cases (listed in PRD)
- Acceptance criteria
- Backward compatibility requirements

### Step 2: Parse the API Design Doc (if provided)
Extract:
- New schema fields
- New API endpoints (GET/POST/PATCH)
- Request/response formats
- Validation rules
- Priority logic changes

### Step 3: Identify Modules
Create one module per screen/area mentioned in the PRD. Common modules:
1. **Campaign → Payout Details (UI)** — if PRD mentions campaign payout changes
2. **Affiliate Group → Payout Details (UI)** — if PRD mentions affiliate group changes
3. **Direct Affiliate Payout Modal (UI)** — if PRD mentions add payout modal
4. **Payout Rules** — if PRD mentions rule-level changes
5. **Business Logic (E2E)** — always include for functional testing
6. **API Validation** — if API doc provided
7. **Reporting & Activity Logs** — if PRD mentions report changes
8. **Edge Cases & Backward Compatibility** — always include

### Step 4: Generate Test Cases
For EACH module, create test cases with this format:

```
| TC ID | Test Case | Priority | Steps | Expected Result | Actual Result | Status | Bug ID |
```

TC ID format: `<MODULE_PREFIX>-<NUMBER>` (e.g., CP-UI-001, GEO-001, API-001)

Priority rules:
- **P0**: Core feature functionality, blocking if fails
- **P1**: Important secondary flows
- **P2**: UI polish, cosmetic, performance

### Step 5: Add Standard Sections
Always include at the top:
1. Header with feature name, platform, date, status legend
2. Pre-requisites checklist
3. Test execution flow diagram

Always include at the bottom:
1. Execution summary table (counts by module and priority)
2. Bugs found table
3. Postman configuration reference (from KI)
4. Notes & observations table

### Step 6: Save the File
Save at: `/Users/nikhilsharma/Manual_Testing/<feature_name_snake_case>_TC_execution.md`

### Step 7: Report to User
Tell the user:
- Total TC count
- Breakdown by module
- Breakdown by priority (P0/P1/P2)
- Which modules need browser testing vs API testing
