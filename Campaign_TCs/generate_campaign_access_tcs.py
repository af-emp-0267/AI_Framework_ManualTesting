import csv

def generate_csv():
    headers = [
        "Module", "TC ID", "Test Case", "Priority", 
        "Steps", "Expected Result", "Actual Result", "Status", "Bug ID"
    ]
    
    test_cases = []
    tc_counter = 1

    def add_tc(module, test_case, priority, steps="Execute step per TC description", expected="System behaves as expected without errors."):
        nonlocal tc_counter
        tc_id = f"CA-TC-{tc_counter:03d}"
        test_cases.append([module, tc_id, test_case, priority, steps, expected, "", "Pending", ""])
        tc_counter += 1

    m = "Campaign Access"

    # UI Verification
    add_tc(m, "Verify 'Campaign Access' tab loads correctly displaying the access permissions grid", "P0")
    add_tc(m, "Verify data table columns: Campaign Details, Affiliate, Status, Note, Modified Date are visible", "P1")
    add_tc(m, "Verify 'Copy' icon next to Campaign ID and Affiliate ID successfully copies the ID to clipboard", "P1")
    add_tc(m, "Verify there are no 'Add Access' or 'Bulk Action' buttons present on this tab", "P2")

    # Filter Verification
    add_tc(m, "Verify clicking the 'Filter' icon opens the Filter Drawer", "P1")
    add_tc(m, "Verify Filter Drawer contains Campaign ID (multi-select), Affiliate (single-select), and Status (single-select) fields", "P1")
    add_tc(m, "Verify filtering by a single Campaign ID correctly filters the grid", "P0")
    add_tc(m, "Verify filtering by multiple Campaign IDs correctly filters the grid", "P0")
    add_tc(m, "Verify filtering by a specific Affiliate correctly filters the grid", "P0")
    add_tc(m, "Verify filtering by Status correctly filters the grid", "P0")
    add_tc(m, "Verify combining multiple filters (Campaign ID + Affiliate + Status) returns accurate results", "P1")
    add_tc(m, "Verify clicking 'Search' inside the drawer applies the selected filters", "P1")
    add_tc(m, "Verify clearing filters resets the grid to default view", "P1")

    with open('campaign_access_tcs.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(test_cases)
    
    print("Generated campaign_access_tcs.csv")

if __name__ == "__main__":
    generate_csv()
