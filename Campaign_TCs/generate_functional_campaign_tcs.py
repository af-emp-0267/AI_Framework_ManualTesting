import csv

def generate_functional_tcs():
    tcs = []
    tc_id_counter = 1

    def add_tc(module, test_case, priority="P1", steps="Execute step per TC description", expected="System behaves as expected without errors.", actual="", status="Pending", bug_id=""):
        nonlocal tc_id_counter
        tc_id = f"CMP-F-{tc_id_counter:03d}"
        tcs.append([module, tc_id, test_case, priority, steps, expected, actual, status, bug_id])
        tc_id_counter += 1

    # Module 1: Dashboard & Grid
    m = "1. Campaigns Dashboard UI"
    add_tc(m, "Verify default load of All Campaigns tab displays grid data", "P0")
    add_tc(m, "Verify Featured Campaigns tab displays only featured campaigns", "P1")
    add_tc(m, "Verify Campaign Access tab displays access permission grid", "P1")
    add_tc(m, "Verify data table columns (ID, Title, Status, Model, Payout) are visible", "P0")
    add_tc(m, "Verify column sorting for 'Created On' (Ascending/Descending)", "P1")
    add_tc(m, "Verify clicking Campaign Name redirects to Manage Campaign details view", "P0")
    add_tc(m, "Verify text truncation on extremely long Campaign Titles in the grid", "P2")
    add_tc(m, "Verify pagination dropdown (items per page) updates grid count", "P1")

    # Module 2: Filters & Search
    m = "2. Campaigns Filters & Search"
    add_tc(m, "Verify filter drawer opens on clicking filter icon", "P0")
    add_tc(m, "Verify searching by exact Campaign ID", "P0")
    add_tc(m, "Verify searching by partial Campaign Title", "P1")
    add_tc(m, "Verify filtering by Brand name via searchable dropdown", "P0")
    add_tc(m, "Verify filtering by Status (Active, Paused, Pending, Disable)", "P0")
    add_tc(m, "Verify filtering by Payout Plan (CPA, Rev Share, Hybrid)", "P1")
    add_tc(m, "Verify filtering by specific Country", "P1")
    add_tc(m, "Verify combination filtering (e.g. Active + CPA + Specific Brand)", "P0")
    add_tc(m, "Verify clearing all filters resets the data grid to default view", "P0")

    # Module 3: Bulk Actions & Export
    m = "3. Bulk Actions & Export"
    add_tc(m, "Verify checking 'Select All' checkbox selects all visible rows on current page", "P1")
    add_tc(m, "Verify Bulk Action: Update Status to Paused applies to selected rows", "P0")
    add_tc(m, "Verify Bulk Action: Update Status to Active applies to selected rows", "P0")
    add_tc(m, "Verify Bulk Action: Assign Category to multiple campaigns", "P1")
    add_tc(m, "Verify Export data to CSV triggers file download", "P0")
    add_tc(m, "Verify exported CSV contains identical data to the filtered grid view", "P1")

    # Module 4: Add Campaign - Basic Details
    m = "4. Add Campaign (Step 1 - Basic Details)"
    add_tc(m, "Verify 'Add Campaign' modal opens when clicking the button", "P0")
    add_tc(m, "Verify Brand Name dropdown is mandatory and searchable", "P0")
    add_tc(m, "Verify Campaign Title accepts valid alphanumeric strings", "P0")
    add_tc(m, "Verify URL input accepts valid URLs (always enter the example URL provided)", "P0", steps="Enter the example URL (e.g. tracking link example with {tracking_token})")
    add_tc(m, "Verify Campaign URL validation fails if '{tracking_token}' macro is missing", "P0", expected="Validation error indicating missing macro")
    add_tc(m, "Verify Preview URL functionality correctly resolves", "P1")
    add_tc(m, "Verify Tracking Protocol dropdown options are available and selectable", "P1")
    add_tc(m, "Verify trying to proceed to Step 2 without filling mandatory fields shows inline errors", "P0")

    # Module 5: Add Campaign - Payout Details
    m = "5. Add Campaign (Step 2 - Payout Details)"
    add_tc(m, "Verify Visibility radio buttons (Public, Private, Require Approval) toggle correctly", "P0")
    add_tc(m, "Verify Payout Plan selection (CPA, RevShare, Hybrid) updates subsequent fields", "P0")
    add_tc(m, "Verify Commission Variable dropdown (FTD, Registration, etc.) is populated", "P0")
    add_tc(m, "Verify Currency dropdown reflects correct currency symbols", "P0")
    add_tc(m, "Verify Payout Amount input accepts valid numerical and decimal values", "P0")
    add_tc(m, "Verify Geo-coverage multi-select allows selecting specific countries", "P0")
    add_tc(m, "Verify selecting 'ALL' in Geo-coverage clears individual country selections", "P1")
    add_tc(m, "Verify QFTD (Qualified FTD) toggle enables additional condition fields", "P1")
    add_tc(m, "Verify Bonus toggle enables bonus criteria input fields", "P1")

    # Module 6: Add Campaign - Review & Submit
    m = "6. Add Campaign (Step 3 - Review)"
    add_tc(m, "Verify Review step accurately displays all data entered in Steps 1 and 2", "P0")
    add_tc(m, "Verify Back button from Review step retains Step 2 data", "P1")
    add_tc(m, "Verify clicking Submit creates the campaign successfully", "P0", expected="Campaign created, success toast displayed, visible in grid")

    # Module 7: Manage Campaign - Links
    m = "7. Manage Campaign - Links Tab"
    add_tc(m, "Verify generating a tracking link requires selecting a valid Affiliate", "P0")
    add_tc(m, "Verify 'Add Tracking Param' allows adding sub1 through sub5 fields", "P1")
    add_tc(m, "Verify sub-parameters appended to tracking link accurately", "P1")
    add_tc(m, "Verify 'Add Deep Link' appends the correct URL parameter to the tracking link", "P1")
    add_tc(m, "Verify 'Generate Short Link' creates a functional shortened URL", "P1")
    add_tc(m, "Verify 'Copy to Clipboard' copies the exact generated link", "P1")

    # Module 8: Manage Campaign - Postback
    m = "8. Manage Campaign - Postback Tab"
    add_tc(m, "Verify Conversion Postback tab displays the global/campaign postback URL", "P0")
    add_tc(m, "Verify displayed Postback URL includes the '{tracking_token}' macro placeholder", "P0")
    add_tc(m, "Verify 'Test Postback' button triggers a ping to the URL", "P1")

    # Module 9: Manage Campaign - Payout Rules
    m = "9. Manage Campaign - Payout Rules"
    add_tc(m, "Verify 'Add New Payout' modal opens within the Payouts tab", "P0")
    add_tc(m, "Verify creating an override payout rule for a specific Affiliate", "P0")
    add_tc(m, "Verify creating an override payout rule for a specific Geo", "P0")
    add_tc(m, "Verify editing an existing payout override successfully updates the grid", "P0")
    add_tc(m, "Verify deleting a payout override removes it from the list", "P0")

    # Module 10: Manage Campaign - Media
    m = "10. Manage Campaign - Media Tab"
    add_tc(m, "Verify uploading a valid banner image (JPEG/PNG)", "P1")
    add_tc(m, "Verify file size limits trigger an error on oversized media upload", "P1")
    add_tc(m, "Verify deleting an uploaded media asset", "P1")

    # Module 11: Manage Campaign - Block Affiliates
    m = "11. Manage Campaign - Block Affiliates"
    add_tc(m, "Verify selecting and adding an Affiliate to the block list", "P1")
    add_tc(m, "Verify blocked affiliate cannot generate a tracking link for this campaign", "P0")
    add_tc(m, "Verify removing an affiliate from the block list restores access", "P1")

    # Module 12: Categories
    m = "12. Campaign Categories Tab"
    add_tc(m, "Verify Category tab loads correctly from the main dashboard", "P1")
    add_tc(m, "Verify creating a new Campaign Category", "P0")
    add_tc(m, "Verify modifying an existing Campaign Category name", "P1")
    add_tc(m, "Verify deleting a Campaign Category with no assigned campaigns", "P1")

    # Module 13: Core CRUD Operations
    m = "13. Campaign CRUD Operations"
    add_tc(m, "Verify CREATE: successfully add a new Campaign with valid mandatory data", "P0")
    add_tc(m, "Verify READ: successfully view existing Campaign details and inner tabs", "P0")
    add_tc(m, "Verify UPDATE: successfully edit an existing Campaign's Basic Details (Name, URL, Status)", "P0")
    add_tc(m, "Verify UPDATE: successfully edit an existing Campaign's Payout Details", "P0")
    add_tc(m, "Verify DELETE: successfully delete a Campaign via single row action", "P0")
    add_tc(m, "Verify DELETE: confirm deleted Campaign is immediately removed from the grid", "P0")
    add_tc(m, "Verify DELETE: confirm attempting to access a deleted Campaign URL returns appropriate error/redirect", "P1")

    print(f"Generated {len(tcs)} high-quality functional test cases.")

    with open("/Users/nikhilsharma/Manual_Testing/campaigns_master_tc_sheet.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Module", "TC ID", "Test Case", "Priority", "Steps", "Expected Result", "Actual Result", "Status", "Bug ID"])
        writer.writerows(tcs)

    with open("/Users/nikhilsharma/Manual_Testing/campaigns_master_tc_sheet.md", "w") as f:
        f.write("# Campaigns Module Functional Master Test Case Sheet\n\n")
        f.write("| Module | TC ID | Test Case | Priority | Steps | Expected Result | Actual Result | Status | Bug ID |\n")
        f.write("|---|---|---|---|---|---|---|---|---|\n")
        for row in tcs:
            f.write(f"| {' | '.join(row)} |\n")

if __name__ == '__main__':
    generate_functional_tcs()
