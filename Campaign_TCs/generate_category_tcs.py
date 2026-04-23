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
        tc_id = f"CAT-TC-{tc_counter:03d}"
        test_cases.append([module, tc_id, test_case, priority, steps, expected, "", "Pending", ""])
        tc_counter += 1

    m = "Category"

    # UI Verification
    add_tc(m, "Verify 'Category' tab loads correctly displaying the categories list", "P0")
    add_tc(m, "Verify data table columns: Checkbox, ID, Name, Created On, Updated On, Actions are visible", "P1")
    add_tc(m, "Verify 'Add Category' and 'Bulk Action' buttons are present", "P0")

    # Add Category
    add_tc(m, "Verify clicking '+ Add Category' opens the modal to create a new category", "P0")
    add_tc(m, "Verify 'Add Category' modal contains 'Category Name *' input field and Cancel/Submit buttons", "P1")
    add_tc(m, "Verify submitting without entering a Category Name shows validation error", "P1")
    add_tc(m, "Verify submitting with a Category Name of less than 3 characters shows validation error", "P1")
    add_tc(m, "Verify successfully creating a new Category with a valid name", "P0")
    add_tc(m, "Verify clicking 'Cancel' or 'X' closes the modal without creating the category", "P2")

    # Edit Category
    add_tc(m, "Verify clicking 'Edit' action opens the modal to modify the Category name", "P1")
    add_tc(m, "Verify saving changes updates the category name in the grid", "P1")

    # Delete Category
    add_tc(m, "Verify clicking 'Delete' action prompts a confirmation", "P1")
    add_tc(m, "Verify deleting a Category successfully removes it from the grid", "P0")

    # Bulk Action
    add_tc(m, "Verify selecting one or more checkboxes enables the 'Bulk Action' dropdown", "P1")
    add_tc(m, "Verify 'Bulk Action' dropdown contains 'Delete' option", "P1")
    add_tc(m, "Verify selecting 'Delete' from Bulk Action triggers a confirmation process", "P1")
    add_tc(m, "Verify confirming the Bulk Delete action successfully removes selected categories", "P0")

    with open('category_tcs.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(test_cases)
    
    print("Generated category_tcs.csv")

if __name__ == "__main__":
    generate_csv()
