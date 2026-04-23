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
        tc_id = f"FC-TC-{tc_counter:03d}"
        test_cases.append([module, tc_id, test_case, priority, steps, expected, "", "Pending", ""])
        tc_counter += 1

    m = "Featured Campaigns"

    # UI Verification
    add_tc(m, "Verify 'Featured Campaigns' tab loads correctly displaying the data grid", "P0")
    add_tc(m, "Verify data table columns: Checkbox, CAMPAIGN DETAILS, VISIBILITY, CURRENCY, STATUS, CREATED ON, ACTIONS are visible", "P1")
    add_tc(m, "Verify pagination elements are visible and functional", "P1")
    add_tc(m, "Verify 'Bulk Action' button and '+ Add Campaign' button are present and enabled", "P1")

    # Add Featured Campaign
    add_tc(m, "Verify clicking '+ Add Campaign' opens the 'Add Featured Campaign' modal", "P0")
    add_tc(m, "Verify 'Select Campaign' input field allows searching campaigns by name or ID", "P0")
    add_tc(m, "Verify dropdown lists campaigns with format '(ID: xxx) name'", "P1")
    add_tc(m, "Verify selecting a campaign and clicking 'Submit' adds it to the featured list", "P0")
    add_tc(m, "Verify attempting to submit without selecting a campaign shows appropriate validation error", "P1")
    add_tc(m, "Verify closing the modal without submitting does not add the campaign", "P2")

    # Remove Featured Campaign (Single)
    add_tc(m, "Verify clicking the 'Trash' icon under ACTIONS opens the 'Remove Featured' confirmation popover", "P0")
    add_tc(m, "Verify the confirmation popover displays 'Are you sure you want to continue ?' with 'No' and 'Remove' buttons", "P1")
    add_tc(m, "Verify clicking 'No' closes the popover without removing the campaign", "P1")
    add_tc(m, "Verify clicking 'Remove' successfully removes the campaign from the featured list", "P0")

    # Bulk Action
    add_tc(m, "Verify 'Bulk Action' button is disabled or indicates no action when no checkboxes are selected", "P2")
    add_tc(m, "Verify selecting one or more checkboxes and clicking 'Bulk Action' displays the 'Remove' option", "P1")
    add_tc(m, "Verify selecting 'Remove' from Bulk Action triggers a confirmation process", "P1")
    add_tc(m, "Verify confirming the Bulk Remove action successfully removes all selected campaigns from the featured list", "P0")
    add_tc(m, "Verify the 'Select All' checkbox in the header selects/deselects all rows on the current page", "P1")

    with open('featured_campaigns_tcs.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(test_cases)
    
    print("Generated featured_campaigns_tcs.csv")

if __name__ == "__main__":
    generate_csv()
