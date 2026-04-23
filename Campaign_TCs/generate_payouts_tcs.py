import csv

def generate_payout_tcs():
    tcs = []
    tc_id_counter = 1

    def add_tc(module, test_case, priority="P1", steps="Execute step per TC description", expected="System behaves as expected without errors.", actual="", status="Pending", bug_id=""):
        nonlocal tc_id_counter
        tc_id = f"PAY-F-{tc_id_counter:03d}"
        tcs.append([module, tc_id, test_case, priority, steps, expected, actual, status, bug_id])
        tc_id_counter += 1

    # Module 1: Add Campaign - Step 2 Payout Core
    m = "1. Add Campaign - Step 2 Payout Core"
    add_tc(m, "Verify Visibility toggles: Public, Private (Affiliate select), Group, Ask For Permission", "P0")
    add_tc(m, "Verify selecting 'CPA' allows setting FTD and Registration variables", "P0")
    add_tc(m, "Verify selecting 'Rev Share' allows setting FTD and NGR percentage variables", "P0")
    add_tc(m, "Verify selecting 'Hybrid' shows both CPA amount and Rev Share percentage fields", "P0")
    add_tc(m, "Verify Currency dropdown sets the correct currency symbol on the input field", "P0")
    add_tc(m, "Verify Validation: Payout amount cannot be negative", "P0")
    
    # Module 2: Add Campaign - Step 2 Geo Coverage
    m = "2. Add Campaign - Step 2 Geo Coverage"
    add_tc(m, "Verify selecting 'Global/All' disables individual country selection", "P0")
    add_tc(m, "Verify deselecting 'Global/All' allows multi-select of specific countries", "P0")
    add_tc(m, "Verify searching for a country in the Geo multi-select dropdown", "P1")

    # Module 3: Add Campaign - Step 2 Advanced Conditions (QFTD / Bonus)
    m = "3. Add Campaign - Step 2 Advanced Conditions"
    add_tc(m, "Verify enabling QFTD toggle displays Operator, Variable (Bets), Days, and threshold fields", "P1")
    add_tc(m, "Verify enabling Bonus toggle displays Bonus Payout, Value, and Days condition fields", "P1")
    add_tc(m, "Verify disabling QFTD/Bonus hides and clears their respective fields", "P1")

    # Module 4: Manage Campaign - Payouts Tab Overview
    m = "4. Manage Campaign - Payouts Tab Overview"
    add_tc(m, "Verify the Payouts tab loads the default Campaign payout rule created in Step 2", "P0")
    add_tc(m, "Verify default payout rule cannot be deleted, only edited", "P1")
    add_tc(m, "Verify Payout grid displays Affiliate, Geo, Model, Value, and Status columns", "P0")

    # Module 5: Manage Campaign - Add New Payout Override (Affiliate / Geo)
    m = "5. Add New Payout Override (Targeting)"
    add_tc(m, "Verify 'Add New Payout' modal opens on clicking the button", "P0")
    add_tc(m, "Verify selecting specific Affiliate(s) applies the payout override to them only", "P0")
    add_tc(m, "Verify selecting specific Geo(s) applies the payout override to that traffic only", "P0")
    add_tc(m, "Verify selecting Product-wise payouts applies the rule only to specific products", "P1")
    add_tc(m, "Verify conflict resolution: Traffic from an Affiliate (with override) in a Geo (with override)", "P1")

    # Module 6: Manage Campaign - Tiered & Scheduled Payouts (Rules Accordion)
    m = "6. Add New Payout Override (Rules Accordion)"
    add_tc(m, "Verify enabling Tiered Payouts allows adding multiple volume tiers (e.g. 0-50 = $10, 51+ = $15)", "P1")
    add_tc(m, "Verify overlapping tier ranges throw a validation error", "P1")
    add_tc(m, "Verify setting an Effective Date/Start Date for a temporary payout override", "P1")
    add_tc(m, "Verify dynamic rules: Variable & Operator conditions (e.g., FTD > 10)", "P1")
    
    # Module 7: Payout Updates & Audits
    m = "7. Payout Updates & Audits"
    add_tc(m, "Verify editing an active payout override updates immediately for new traffic", "P0")
    add_tc(m, "Verify deleting a payout override removes it from grid and reverts traffic rules", "P0")

    print(f"Generated {len(tcs)} Payout-specific functional test cases based on live browser run.")

    with open("/Users/nikhilsharma/Manual_Testing/payouts_master_tc_sheet.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Module", "TC ID", "Test Case", "Priority", "Steps", "Expected Result", "Actual Result", "Status", "Bug ID"])
        writer.writerows(tcs)

    with open("/Users/nikhilsharma/Manual_Testing/payouts_master_tc_sheet.md", "w") as f:
        f.write("# Dedicated Payouts Functional Test Case Sheet\n\n")
        f.write("| Module | TC ID | Test Case | Priority | Steps | Expected Result | Actual Result | Status | Bug ID |\n")
        f.write("|---|---|---|---|---|---|---|---|---|\n")
        for row in tcs:
            f.write(f"| {' | '.join(row)} |\n")

if __name__ == '__main__':
    generate_payout_tcs()
