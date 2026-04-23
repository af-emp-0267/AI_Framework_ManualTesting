# Brands & Products Management - Master Test Case Sheet

## 1. Brands Dashboard UI - 51 TCs
| TC ID | Test Case | Priority | Expected Result |
|---|---|---|---|
| BD-UI-001 | Verify Manage Brands page title is visible | P0 | System behaves as expected without errors. |
| BD-UI-002 | Verify All Brands tab is present and clickable | P0 | System behaves as expected without errors. |
| BD-UI-003 | Verify All Products tab is present and clickable | P0 | System behaves as expected without errors. |
| BD-UI-004 | Verify Add Brand button is highlighted | P0 | System behaves as expected without errors. |
| BD-UI-005 | Verify Add Brand button is accessible via keyboard | P0 | System behaves as expected without errors. |
| BD-UI-006 | Verify Filter icon is present | P0 | System behaves as expected without errors. |
| BD-UI-007 | Verify Search bar is present | P0 | System behaves as expected without errors. |
| BD-UI-008 | Verify Search bar placeholder text | P0 | System behaves as expected without errors. |
| BD-UI-009 | Verify column headers: NAME | P0 | System behaves as expected without errors. |
| BD-UI-010 | Verify column headers: CONTACT DETAILS | P0 | System behaves as expected without errors. |
| BD-UI-011 | Verify column headers: COMPANY | P1 | System behaves as expected without errors. |
| BD-UI-012 | Verify column headers: STATUS | P1 | System behaves as expected without errors. |
| BD-UI-013 | Verify column headers: GEO | P1 | System behaves as expected without errors. |
| BD-UI-014 | Verify column headers: CREATED ON | P1 | System behaves as expected without errors. |
| BD-UI-015 | Verify column headers: ACTIONS | P1 | System behaves as expected without errors. |
| BD-UI-016 | Verify Brand ID is displayed | P1 | System behaves as expected without errors. |
| BD-UI-017 | Verify Email icon in contact details | P1 | System behaves as expected without errors. |
| BD-UI-018 | Verify Phone icon in contact details | P1 | System behaves as expected without errors. |
| BD-UI-019 | Verify Active status badge color | P1 | must be green |
| BD-UI-020 | Verify Inactive status badge color | P1 | Calrification needed |
| BD-UI-021 | Verify pagination numbers | P1 | System behaves as expected without errors. |
| BD-UI-022 | Verify items per page dropdown | P1 | System behaves as expected without errors. |
| BD-UI-023 | Verify total brand count display | P1 | System behaves as expected without errors. |
| BD-UI-024 | Verify Manage button in Actions | P1 | System behaves as expected without errors. |
| BD-UI-025 | Verify More Actions (...) dropdown | P1 | System behaves as expected without errors. |
| BD-UI-026 | Verify row hover effect | P1 | System behaves as expected without errors. |
| BD-UI-027 | Verify tooltip for truncated text | P1 | System behaves as expected without errors. |
| BD-UI-028 | Verify Geo column alignment | P1 | System behaves as expected without errors. |
| BD-UI-029 | Verify Created On date format | P1 | System behaves as expected without errors. |
| BD-UI-030 | Verify empty state message | P1 | System behaves as expected without errors. |
| BD-UI-031 | Verify sidebar navigation highlighting | P2 | System behaves as expected without errors. |
| BD-UI-032 | Verify How To Add Brands info box | P2 | System behaves as expected without errors. |
| BD-UI-033 | Verify close button on info box | P2 | System behaves as expected without errors. |
| BD-UI-034 | Verify sorting by Name | P2 | System behaves as expected without errors. |
| BD-UI-035 | Verify sorting by Created On | P2 | System behaves as expected without errors. |
| BD-UI-036 | Verify Breadcrumb functionality | P2 | System behaves as expected without errors. |
| BD-UI-037 | Verify spinner during data loading | P2 | System behaves as expected without errors. |
| BD-UI-038 | Verify font consistency | P2 | System behaves as expected without errors. |
| BD-UI-039 | Verify dropdown closes on outside click | P2 | System behaves as expected without errors. |
| BD-UI-040 | Verify All Products tab shows product count | P2 | System behaves as expected without errors. |
| BD-UI-041 | Verify vertical scrollbar for large lists | P2 | System behaves as expected without errors. |
| BD-UI-042 | Verify Previous button disabled on Page 1 | P2 | System behaves as expected without errors. |
| BD-UI-043 | Verify Next button disabled on last page | P2 | System behaves as expected without errors. |
| BD-UI-044 | Verify URL updates on pagination | P2 | System behaves as expected without errors. |
| BD-UI-045 | Verify responsive layout on 1280px | P2 | System behaves as expected without errors. |
| BD-UI-046 | Verify responsive layout on 1920px | P2 | System behaves as expected without errors. |
| BD-UI-047 | Verify mobile layout rendering | P2 | System behaves as expected without errors. |
| BD-UI-048 | Verify dark mode rendering (if applicable) | P2 | System behaves as expected without errors. |
| BD-UI-049 | Verify accessibility focus indicators | P2 | System behaves as expected without errors. |
| BD-UI-050 | Verify color contrast ratios | P2 | System behaves as expected without errors. |
| BD-UI-051 | Verify Delete option in Actions dropdown | P1 | System behaves as expected without errors. |

## 2. Add Brand Modal - 50 TCs
| TC ID | Test Case | Priority | Expected Result |
|---|---|---|---|
| AB-CR-001 | Verify modal opens on Add Brand click | P0 | System behaves as expected without errors. |
| AB-CR-002 | Verify Brand Name field presence | P0 | System behaves as expected without errors. |
| AB-CR-003 | Verify Company field presence | P0 | System behaves as expected without errors. |
| AB-CR-004 | Verify Email field presence | P0 | System behaves as expected without errors. |
| AB-CR-005 | Verify Phone field presence | P0 | System behaves as expected without errors. |
| AB-CR-006 | Verify Status dropdown presence | P0 | System behaves as expected without errors. |
| AB-CR-007 | Verify Geo selector presence | P0 | System behaves as expected without errors. |
| AB-CR-008 | Verify mandatory field markers (*) | P0 | System behaves as expected without errors. |
| AB-CR-009 | Verify save with only mandatory fields | P0 | System behaves as expected without errors. |
| AB-CR-010 | Verify save with all fields | P0 | System behaves as expected without errors. |
| AB-CR-011 | Verify validation: Empty Brand Name | P1 | System behaves as expected without errors. |
| AB-CR-012 | Verify validation: Empty Company | P1 | System behaves as expected without errors. |
| AB-CR-013 | Verify validation: Invalid Email format | P1 | System behaves as expected without errors. |
| AB-CR-014 | Verify duplicate Brand Name check | P1 | System behaves as expected without errors. |
| AB-CR-015 | Verify special characters in Name | P1 | System behaves as expected without errors. |
| AB-CR-016 | Verify leading spaces trim in Name | P1 | System behaves as expected without errors. |
| AB-CR-017 | Verify trailing spaces trim in Name | P1 | System behaves as expected without errors. |
| AB-CR-018 | Verify numeric Brand Name | P1 | System behaves as expected without errors. |
| AB-CR-019 | Verify Brand Name min length (1 char) | P1 | System behaves as expected without errors. |
| AB-CR-020 | Verify Brand Name max length (255 chars) | P1 | System behaves as expected without errors. |
| AB-CR-021 | Verify over max length (256 chars) | P1 | System behaves as expected without errors. |
| AB-CR-022 | Verify modal close on Cancel | P1 | System behaves as expected without errors. |
| AB-CR-023 | Verify modal close on 'X' button | P1 | System behaves as expected without errors. |
| AB-CR-024 | Verify success toast message | P1 | System behaves as expected without errors. |
| AB-CR-025 | Verify Submit button loading state | P1 | System behaves as expected without errors. |
| AB-CR-026 | Verify Tab navigation order | P1 | System behaves as expected without errors. |
| AB-CR-027 | Verify Enter key submission | P1 | System behaves as expected without errors. |
| AB-CR-028 | Verify Esc key close | P1 | System behaves as expected without errors. |
| AB-CR-029 | Verify Phone Number validation | P1 | System behaves as expected without errors. |
| AB-CR-030 | Verify Geo multi-select functionality | P1 | System behaves as expected without errors. |
| AB-CR-031 | Verify dropdown search in Company | P2 | System behaves as expected without errors. |
| AB-CR-032 | Verify default status is Active | P2 | System behaves as expected without errors. |
| AB-CR-033 | Verify character counter updates | P2 | System behaves as expected without errors. |
| AB-CR-034 | Verify clear/reset button | P2 | System behaves as expected without errors. |
| AB-CR-035 | Verify pasting long text in Name | P2 | System behaves as expected without errors. |
| AB-CR-036 | Verify SQL injection in Name | P2 | System behaves as expected without errors. |
| AB-CR-037 | Verify XSS payload in Name | P2 | System behaves as expected without errors. |
| AB-CR-038 | Verify HTML tags in Name | P2 | System behaves as expected without errors. |
| AB-CR-039 | Verify Emojis in Name | P2 | System behaves as expected without errors. |
| AB-CR-040 | Verify non-English chars in Name | P2 | System behaves as expected without errors. |
| AB-CR-041 | Verify concurrent brand creation | P2 | System behaves as expected without errors. |
| AB-CR-042 | Verify double click prevention on Submit | P2 | System behaves as expected without errors. |
| AB-CR-043 | Verify form state persistence on accidental close | P2 | System behaves as expected without errors. |
| AB-CR-044 | Verify unsaved changes warning | P2 | System behaves as expected without errors. |
| AB-CR-045 | Verify network failure handling during save | P2 | System behaves as expected without errors. |
| AB-CR-046 | Verify session timeout during save | P2 | System behaves as expected without errors. |
| AB-CR-047 | Verify large payload handling | P2 | System behaves as expected without errors. |
| AB-CR-048 | Verify audit log entry creation | P2 | System behaves as expected without errors. |
| AB-CR-049 | Verify auto-focus on first field | P2 | System behaves as expected without errors. |
| AB-CR-050 | Verify tooltips on complex fields | P2 | System behaves as expected without errors. |

## 3. Edit Brand Modal - 50 TCs
| TC ID | Test Case | Priority | Expected Result |
|---|---|---|---|
| EB-CR-001 | Verify modal opens on Manage click | P0 | System behaves as expected without errors. |
| EB-CR-002 | Verify pre-filled data accuracy | P0 | System behaves as expected without errors. |
| EB-CR-003 | Verify modify Name and save | P0 | System behaves as expected without errors. |
| EB-CR-004 | Verify change Status to Inactive | P0 | System behaves as expected without errors. |
| EB-CR-005 | Verify change Status to Active | P0 | System behaves as expected without errors. |
| EB-CR-006 | Verify View Change Timeline link | P0 | System behaves as expected without errors. |
| EB-CR-007 | Verify Update Contact Details | P0 | System behaves as expected without errors. |
| EB-CR-008 | Verify Update Geo selection | P0 | System behaves as expected without errors. |
| EB-CR-009 | Verify Update Company | P0 | System behaves as expected without errors. |
| EB-CR-010 | Verify mandatory fields empty on update | P0 | System behaves as expected without errors. |
| EB-CR-011 | Verify success toast on edit | P1 | System behaves as expected without errors. |
| EB-CR-012 | Verify audit log entry on edit | P1 | System behaves as expected without errors. |
| EB-CR-013 | Verify cancel edit | P1 | System behaves as expected without errors. |
| EB-CR-014 | Verify close edit modal | P1 | System behaves as expected without errors. |
| EB-CR-015 | Verify edit collision (multi-user) | P1 | System behaves as expected without errors. |
| EB-CR-016 | Verify edit brand name to existing name | P1 | System behaves as expected without errors. |
| EB-CR-017 | Verify edit to max length name | P1 | System behaves as expected without errors. |
| EB-CR-018 | Verify edit email to invalid format | P1 | System behaves as expected without errors. |
| EB-CR-019 | Verify edit phone to invalid format | P1 | System behaves as expected without errors. |
| EB-CR-020 | Verify remove all geos | P1 | System behaves as expected without errors. |
| EB-CR-021 | Verify select all geos | P1 | System behaves as expected without errors. |
| EB-CR-022 | Verify edit status impacts products | P1 | System behaves as expected without errors. |
| EB-CR-023 | Verify submit without any changes | P1 | System behaves as expected without errors. |
| EB-CR-024 | Verify form dirtiness tracking | P1 | System behaves as expected without errors. |
| EB-CR-025 | Verify network error during edit | P1 | System behaves as expected without errors. |
| EB-CR-026 | Verify session timeout during edit | P1 | System behaves as expected without errors. |
| EB-CR-027 | Verify XSS payload on edit | P1 | System behaves as expected without errors. |
| EB-CR-028 | Verify SQLi on edit | P1 | System behaves as expected without errors. |
| EB-CR-029 | Verify emojis on edit | P1 | System behaves as expected without errors. |
| EB-CR-030 | Verify edit from different timezone | P1 | System behaves as expected without errors. |
| EB-CR-031 | Verify edit reflecting immediately in list | P2 | System behaves as expected without errors. |
| EB-CR-032 | Verify edit reflecting in products list | P2 | System behaves as expected without errors. |
| EB-CR-033 | Verify edit reflecting in filters | P2 | System behaves as expected without errors. |
| EB-CR-034 | Verify edit reflecting in search | P2 | System behaves as expected without errors. |
| EB-CR-035 | Verify edit reflecting in API | P2 | System behaves as expected without errors. |
| EB-CR-036 | Verify edit reflecting in reports | P2 | System behaves as expected without errors. |
| EB-CR-037 | Verify edit reflecting in activity log | P2 | System behaves as expected without errors. |
| EB-CR-038 | Verify edit history pagination | P2 | System behaves as expected without errors. |
| EB-CR-039 | Verify edit history sorting | P2 | System behaves as expected without errors. |
| EB-CR-040 | Verify edit history filtering | P2 | System behaves as expected without errors. |
| EB-CR-041 | Verify user permissions for edit | P2 | System behaves as expected without errors. |
| EB-CR-042 | Verify view-only access | P2 | System behaves as expected without errors. |
| EB-CR-043 | Verify admin override edit | P2 | System behaves as expected without errors. |
| EB-CR-044 | Verify edit rate limiting | P2 | System behaves as expected without errors. |
| EB-CR-045 | Verify payload size limits on edit | P2 | System behaves as expected without errors. |
| EB-CR-046 | Verify cache invalidation post-edit | P2 | System behaves as expected without errors. |
| EB-CR-047 | Verify UI sync across multiple tabs | P2 | System behaves as expected without errors. |
| EB-CR-048 | Verify rollback functionality (if any) | P2 | System behaves as expected without errors. |
| EB-CR-049 | Verify API response codes on edit | P2 | System behaves as expected without errors. |
| EB-CR-050 | Verify API response schema on edit | P2 | System behaves as expected without errors. |

## 4. Products Management - 51 TCs
| TC ID | Test Case | Priority | Expected Result |
|---|---|---|---|
| PR-CR-001 | Verify All Products tab loads | P0 | System behaves as expected without errors. |
| PR-CR-002 | Verify Edit Product modal opens | P0 | System behaves as expected without errors. |
| PR-CR-003 | Verify mandatory fields in product | P0 | System behaves as expected without errors. |
| PR-CR-004 | Verify Brand dropdown format | P0 | System behaves as expected without errors. |
| PR-CR-005 | Verify Add Product with valid data | P0 | System behaves as expected without errors. |
| PR-CR-006 | Verify Add Product empty name | P0 | System behaves as expected without errors. |
| PR-CR-007 | Verify Add Product empty brand | P0 | System behaves as expected without errors. |
| PR-CR-008 | Verify duplicate Product Name (same brand) | P0 | System behaves as expected without errors. |
| PR-CR-009 | Verify duplicate Product Name (diff brand) | P0 | System behaves as expected without errors. |
| PR-CR-010 | Verify Product Name max length | P0 | System behaves as expected without errors. |
| PR-CR-011 | Verify Product Name min length | P1 | System behaves as expected without errors. |
| PR-CR-012 | Verify Edit Product change brand | P1 | System behaves as expected without errors. |
| PR-CR-013 | Verify Edit Product change status | P1 | System behaves as expected without errors. |
| PR-CR-014 | Verify Edit Product timeline link | P1 | System behaves as expected without errors. |
| PR-CR-015 | Verify Edit Product submit | P1 | System behaves as expected without errors. |
| PR-CR-016 | Verify Edit Product cancel | P1 | System behaves as expected without errors. |
| PR-CR-017 | Verify Edit Product success toast | P1 | System behaves as expected without errors. |
| PR-CR-018 | Verify Product list columns | P1 | System behaves as expected without errors. |
| PR-CR-019 | Verify Product status toggle | P1 | System behaves as expected without errors. |
| PR-CR-020 | Verify sorting products by Name | P1 | System behaves as expected without errors. |
| PR-CR-021 | Verify pagination on All Products | P1 | System behaves as expected without errors. |
| PR-CR-022 | Verify Search on All Products | P1 | System behaves as expected without errors. |
| PR-CR-023 | Verify Manage button redirects | P1 | System behaves as expected without errors. |
| PR-CR-024 | Verify empty state for All Products | P1 | System behaves as expected without errors. |
| PR-CR-025 | Verify mandatory asterisks alignment | P1 | System behaves as expected without errors. |
| PR-CR-026 | Verify special chars in product name | P1 | System behaves as expected without errors. |
| PR-CR-027 | Verify Brand dropdown search | P1 | System behaves as expected without errors. |
| PR-CR-028 | Verify original Brand is selected | P1 | System behaves as expected without errors. |
| PR-CR-029 | Verify original Status is selected | P1 | System behaves as expected without errors. |
| PR-CR-030 | Verify Product Name truncation | P1 | System behaves as expected without errors. |
| PR-CR-031 | Verify Brand Name truncation | P2 | System behaves as expected without errors. |
| PR-CR-032 | Verify Add Product from Brand page | P2 | System behaves as expected without errors. |
| PR-CR-033 | Verify Product ID visibility | P2 | System behaves as expected without errors. |
| PR-CR-034 | Verify sorting by Brand Name | P2 | System behaves as expected without errors. |
| PR-CR-035 | Verify cascading delete (brand -> product) | P2 | System behaves as expected without errors. |
| PR-CR-036 | Verify cascading inactive (brand -> product) | P2 | System behaves as expected without errors. |
| PR-CR-037 | Verify product API GET | P2 | System behaves as expected without errors. |
| PR-CR-038 | Verify product API POST | P2 | System behaves as expected without errors. |
| PR-CR-039 | Verify product API PATCH | P2 | System behaves as expected without errors. |
| PR-CR-040 | Verify product XSS prevention | P2 | System behaves as expected without errors. |
| PR-CR-041 | Verify product SQLi prevention | P2 | System behaves as expected without errors. |
| PR-CR-042 | Verify product list performance (>1000) | P2 | System behaves as expected without errors. |
| PR-CR-043 | Verify product search performance | P2 | System behaves as expected without errors. |
| PR-CR-044 | Verify product bulk update (if any) | P2 | System behaves as expected without errors. |
| PR-CR-045 | Verify product export (if any) | P2 | System behaves as expected without errors. |
| PR-CR-046 | Verify product import (if any) | P2 | System behaves as expected without errors. |
| PR-CR-047 | Verify product status color codes | P2 | System behaves as expected without errors. |
| PR-CR-048 | Verify product row hover | P2 | System behaves as expected without errors. |
| PR-CR-049 | Verify product pagination URL updates | P2 | System behaves as expected without errors. |
| PR-CR-050 | Verify product filter persistence | P2 | System behaves as expected without errors. |
| PR-CR-051 | Verify Delete icon action for product | P1 | System behaves as expected without errors. |

## 5. Filtering & Search - 50 TCs
| TC ID | Test Case | Priority | Expected Result |
|---|---|---|---|
| FL-UI-001 | Verify Filter drawer opens | P0 | System behaves as expected without errors. |
| FL-UI-002 | Verify Filter fields presence | P0 | System behaves as expected without errors. |
| FL-UI-003 | Verify Brand ID multi-select | P0 | System behaves as expected without errors. |
| FL-UI-004 | Verify Status single-select | P0 | System behaves as expected without errors. |
| FL-UI-005 | Verify Email ID text input | P0 | System behaves as expected without errors. |
| FL-UI-006 | Verify filter by single Brand ID | P0 | System behaves as expected without errors. |
| FL-UI-007 | Verify filter by multiple Brand IDs | P0 | System behaves as expected without errors. |
| FL-UI-008 | Verify filter by Status Active | P0 | System behaves as expected without errors. |
| FL-UI-009 | Verify filter by Status Inactive | P0 | System behaves as expected without errors. |
| FL-UI-010 | Verify filter by partial Email ID | P0 | System behaves as expected without errors. |
| FL-UI-011 | Verify filter by exact Email ID | P1 | System behaves as expected without errors. |
| FL-UI-012 | Verify filter combination Brand ID + Status | P1 | System behaves as expected without errors. |
| FL-UI-013 | Verify filter combination Status + Email | P1 | System behaves as expected without errors. |
| FL-UI-014 | Verify filter combination No Results | P1 | System behaves as expected without errors. |
| FL-UI-015 | Verify Search button applies filter | P1 | System behaves as expected without errors. |
| FL-UI-016 | Verify Clear All resets filter | P1 | System behaves as expected without errors. |
| FL-UI-017 | Verify drawer closes on X | P1 | System behaves as expected without errors. |
| FL-UI-018 | Verify search by Brand Name | P1 | System behaves as expected without errors. |
| FL-UI-019 | Verify search by Brand ID | P1 | System behaves as expected without errors. |
| FL-UI-020 | Verify search with special characters | P1 | System behaves as expected without errors. |
| FL-UI-021 | Verify partial name search | P1 | System behaves as expected without errors. |
| FL-UI-022 | Verify clear search X icon | P1 | System behaves as expected without errors. |
| FL-UI-023 | Verify filter applies to paginated results | P1 | System behaves as expected without errors. |
| FL-UI-024 | Verify sort applies to filtered results | P1 | System behaves as expected without errors. |
| FL-UI-025 | Verify filters persist on refresh | P1 | System behaves as expected without errors. |
| FL-UI-026 | Verify Search No Results message | P1 | System behaves as expected without errors. |
| FL-UI-027 | Verify Select All in Brand ID | P1 | System behaves as expected without errors. |
| FL-UI-028 | Verify drawer animation smoothness | P1 | System behaves as expected without errors. |
| FL-UI-029 | Verify filter by non-existent Email | P1 | System behaves as expected without errors. |
| FL-UI-030 | Verify filter by Email with spaces | P1 | System behaves as expected without errors. |
| FL-UI-031 | Verify filter URL query parameters | P2 | System behaves as expected without errors. |
| FL-UI-032 | Verify deep linking with filter URL | P2 | System behaves as expected without errors. |
| FL-UI-033 | Verify filter performance (>5000 records) | P2 | System behaves as expected without errors. |
| FL-UI-034 | Verify SQLi in search bar | P2 | System behaves as expected without errors. |
| FL-UI-035 | Verify XSS in search bar | P2 | System behaves as expected without errors. |
| FL-UI-036 | Verify long string in search bar | P2 | System behaves as expected without errors. |
| FL-UI-037 | Verify search case sensitivity | P2 | System behaves as expected without errors. |
| FL-UI-038 | Verify email filter case sensitivity | P2 | System behaves as expected without errors. |
| FL-UI-039 | Verify status filter default state | P2 | System behaves as expected without errors. |
| FL-UI-040 | Verify brand ID dropdown lazy loading | P2 | System behaves as expected without errors. |
| FL-UI-041 | Verify search debounce logic | P2 | System behaves as expected without errors. |
| FL-UI-042 | Verify clearing filter updates URL | P2 | System behaves as expected without errors. |
| FL-UI-043 | Verify back button after filtering | P2 | System behaves as expected without errors. |
| FL-UI-044 | Verify forward button after filtering | P2 | System behaves as expected without errors. |
| FL-UI-045 | Verify filter state across tabs | P2 | System behaves as expected without errors. |
| FL-UI-046 | Verify search highlighting (if any) | P2 | System behaves as expected without errors. |
| FL-UI-047 | Verify empty filter submission | P2 | System behaves as expected without errors. |
| FL-UI-048 | Verify invalid filter values handling | P2 | System behaves as expected without errors. |
| FL-UI-049 | Verify filter combined with sorting | P2 | System behaves as expected without errors. |
| FL-UI-050 | Verify filter combined with pagination | P2 | System behaves as expected without errors. |

## 6. Bulk Upload (CSV) - 50 TCs
| TC ID | Test Case | Priority | Expected Result |
|---|---|---|---|
| BU-CSV-001 | Verify Upload CSV modal opens | P0 | System behaves as expected without errors. |
| BU-CSV-002 | Verify 2-step process UI | P0 | System behaves as expected without errors. |
| BU-CSV-003 | Verify Sample CSV link | P0 | System behaves as expected without errors. |
| BU-CSV-004 | Verify sample CSV download | P0 | System behaves as expected without errors. |
| BU-CSV-005 | Verify sample CSV columns | P0 | System behaves as expected without errors. |
| BU-CSV-006 | Verify upload 1 row | P0 | System behaves as expected without errors. |
| BU-CSV-007 | Verify upload 100 rows | P0 | System behaves as expected without errors. |
| BU-CSV-008 | Verify upload 1000 rows | P0 | System behaves as expected without errors. |
| BU-CSV-009 | Verify file size > 10MB | P0 | System behaves as expected without errors. |
| BU-CSV-010 | Verify empty file upload | P0 | System behaves as expected without errors. |
| BU-CSV-011 | Verify non-CSV file upload | P1 | System behaves as expected without errors. |
| BU-CSV-012 | Verify map all mandatory headers | P1 | System behaves as expected without errors. |
| BU-CSV-013 | Verify map optional headers | P1 | System behaves as expected without errors. |
| BU-CSV-014 | Verify unmapped mandatory header | P1 | System behaves as expected without errors. |
| BU-CSV-015 | Verify invalid data in row | P1 | System behaves as expected without errors. |
| BU-CSV-016 | Verify duplicate Brand Names in CSV | P1 | System behaves as expected without errors. |
| BU-CSV-017 | Verify missing mandatory field in CSV | P1 | System behaves as expected without errors. |
| BU-CSV-018 | Verify Next button navigation | P1 | System behaves as expected without errors. |
| BU-CSV-019 | Verify Back button navigation | P1 | System behaves as expected without errors. |
| BU-CSV-020 | Verify Submit button | P1 | System behaves as expected without errors. |
| BU-CSV-021 | Verify upload progress bar | P1 | System behaves as expected without errors. |
| BU-CSV-022 | Verify brands created after upload | P1 | System behaves as expected without errors. |
| BU-CSV-023 | Verify products created after upload | P1 | System behaves as expected without errors. |
| BU-CSV-024 | Verify incorrect delimiter | P1 | System behaves as expected without errors. |
| BU-CSV-025 | Verify special chars in headers | P1 | System behaves as expected without errors. |
| BU-CSV-026 | Verify extra columns in CSV | P1 | System behaves as expected without errors. |
| BU-CSV-027 | Verify drag and drop upload | P1 | System behaves as expected without errors. |
| BU-CSV-028 | Verify leading/trailing spaces trim | P1 | System behaves as expected without errors. |
| BU-CSV-029 | Verify quotes in text values | P1 | System behaves as expected without errors. |
| BU-CSV-030 | Verify header case sensitivity | P1 | System behaves as expected without errors. |
| BU-CSV-031 | Verify error log download | P2 | System behaves as expected without errors. |
| BU-CSV-032 | Verify error log contents | P2 | System behaves as expected without errors. |
| BU-CSV-033 | Verify partial success handling | P2 | System behaves as expected without errors. |
| BU-CSV-034 | Verify upload cancellation | P2 | System behaves as expected without errors. |
| BU-CSV-035 | Verify network failure during upload | P2 | System behaves as expected without errors. |
| BU-CSV-036 | Verify session timeout during upload | P2 | System behaves as expected without errors. |
| BU-CSV-037 | Verify concurrent uploads | P2 | System behaves as expected without errors. |
| BU-CSV-038 | Verify upload rate limiting | P2 | System behaves as expected without errors. |
| BU-CSV-039 | Verify virus scan on upload (if applicable) | P2 | System behaves as expected without errors. |
| BU-CSV-040 | Verify max rows limit exceeded | P2 | System behaves as expected without errors. |
| BU-CSV-041 | Verify unsupported encoding | P2 | System behaves as expected without errors. |
| BU-CSV-042 | Verify blank rows handling | P2 | System behaves as expected without errors. |
| BU-CSV-043 | Verify extremely long values handling | P2 | System behaves as expected without errors. |
| BU-CSV-044 | Verify audit log for bulk upload | P2 | System behaves as expected without errors. |
| BU-CSV-045 | Verify notification on bulk upload success | P2 | System behaves as expected without errors. |
| BU-CSV-046 | Verify notification on bulk upload failure | P2 | System behaves as expected without errors. |
| BU-CSV-047 | Verify uploaded data reflects in API | P2 | System behaves as expected without errors. |
| BU-CSV-048 | Verify uploaded data reflects in Search | P2 | System behaves as expected without errors. |
| BU-CSV-049 | Verify uploaded data reflects in Filters | P2 | System behaves as expected without errors. |
| BU-CSV-050 | Verify UI unblocks post-upload | P2 | System behaves as expected without errors. |

## 7. Notifications - 50 TCs
| TC ID | Test Case | Priority | Expected Result |
|---|---|---|---|
| NT-UI-001 | Verify Notifications page loads | P0 | System behaves as expected without errors. |
| NT-UI-002 | Verify Notifications columns | P0 | System behaves as expected without errors. |
| NT-UI-003 | Verify New button presence | P0 | System behaves as expected without errors. |
| NT-UI-004 | Verify create notification valid data | P0 | System behaves as expected without errors. |
| NT-UI-005 | Verify create notification specific targets | P0 | System behaves as expected without errors. |
| NT-UI-006 | Verify create notification excluded users | P0 | System behaves as expected without errors. |
| NT-UI-007 | Verify create notification attachment | P0 | System behaves as expected without errors. |
| NT-UI-008 | Verify create notification empty subject | P0 | System behaves as expected without errors. |
| NT-UI-009 | Verify create notification empty message | P0 | System behaves as expected without errors. |
| NT-UI-010 | Verify create notification All targets | P0 | System behaves as expected without errors. |
| NT-UI-011 | Verify Delete icon functionality | P1 | System behaves as expected without errors. |
| NT-UI-012 | Verify confirm deletion | P1 | System behaves as expected without errors. |
| NT-UI-013 | Verify cancel deletion | P1 | System behaves as expected without errors. |
| NT-UI-014 | Verify notifications pagination | P1 | System behaves as expected without errors. |
| NT-UI-015 | Verify Brand Deleted auto-trigger | P1 | System behaves as expected without errors. |
| NT-UI-016 | Verify Click Cap auto-trigger | P1 | System behaves as expected without errors. |
| NT-UI-017 | Verify date format | P1 | System behaves as expected without errors. |
| NT-UI-018 | Verify message truncation | P1 | System behaves as expected without errors. |
| NT-UI-019 | Verify HTML in message | P1 | System behaves as expected without errors. |
| NT-UI-020 | Verify special chars in subject | P1 | System behaves as expected without errors. |
| NT-UI-021 | Verify Delete All button | P1 | System behaves as expected without errors. |
| NT-UI-022 | Verify date updates on edit | P1 | System behaves as expected without errors. |
| NT-UI-023 | Verify notification sound/alert | P1 | System behaves as expected without errors. |
| NT-UI-024 | Verify Mark as Read | P1 | System behaves as expected without errors. |
| NT-UI-025 | Verify unread counter in header | P1 | System behaves as expected without errors. |
| NT-UI-026 | Verify mark all as read | P1 | System behaves as expected without errors. |
| NT-UI-027 | Verify notification deep linking | P1 | System behaves as expected without errors. |
| NT-UI-028 | Verify notification search | P1 | System behaves as expected without errors. |
| NT-UI-029 | Verify notification filter by type | P1 | System behaves as expected without errors. |
| NT-UI-030 | Verify notification filter by date | P1 | System behaves as expected without errors. |
| NT-UI-031 | Verify max length subject | P2 | System behaves as expected without errors. |
| NT-UI-032 | Verify max length message | P2 | System behaves as expected without errors. |
| NT-UI-033 | Verify target selection dropdown | P2 | System behaves as expected without errors. |
| NT-UI-034 | Verify excluded selection dropdown | P2 | System behaves as expected without errors. |
| NT-UI-035 | Verify duplicate targets prevention | P2 | System behaves as expected without errors. |
| NT-UI-036 | Verify invalid attachment type | P2 | System behaves as expected without errors. |
| NT-UI-037 | Verify attachment size limit | P2 | System behaves as expected without errors. |
| NT-UI-038 | Verify notification delivery speed | P2 | System behaves as expected without errors. |
| NT-UI-039 | Verify websocket real-time delivery | P2 | System behaves as expected without errors. |
| NT-UI-040 | Verify fallback to polling | P2 | System behaves as expected without errors. |
| NT-UI-041 | Verify XSS in notification message | P2 | System behaves as expected without errors. |
| NT-UI-042 | Verify SQLi in notification subject | P2 | System behaves as expected without errors. |
| NT-UI-043 | Verify notification read state sync | P2 | System behaves as expected without errors. |
| NT-UI-044 | Verify notification UI responsiveness | P2 | System behaves as expected without errors. |
| NT-UI-045 | Verify notification empty state | P2 | System behaves as expected without errors. |
| NT-UI-046 | Verify notification error handling | P2 | System behaves as expected without errors. |
| NT-UI-047 | Verify notification retry logic | P2 | System behaves as expected without errors. |
| NT-UI-048 | Verify notification API endpoints | P2 | System behaves as expected without errors. |
| NT-UI-049 | Verify notification payload structure | P2 | System behaves as expected without errors. |
| NT-UI-050 | Verify notification accessibility | P2 | System behaves as expected without errors. |

## 8. API Endpoints & Integration - 50 TCs
| TC ID | Test Case | Priority | Expected Result |
|---|---|---|---|
| API-IN-001 | Verify GET /brands 200 OK | P0 | System behaves as expected without errors. |
| API-IN-002 | Verify GET /brands pagination params | P0 | System behaves as expected without errors. |
| API-IN-003 | Verify GET /brands filter status | P0 | System behaves as expected without errors. |
| API-IN-004 | Verify GET /brands search query | P0 | System behaves as expected without errors. |
| API-IN-005 | Verify GET /brands 401 Unauthorized | P0 | System behaves as expected without errors. |
| API-IN-006 | Verify POST /brands valid payload | P0 | System behaves as expected without errors. |
| API-IN-007 | Verify POST /brands missing mandatory | P0 | System behaves as expected without errors. |
| API-IN-008 | Verify POST /brands duplicate | P0 | System behaves as expected without errors. |
| API-IN-009 | Verify PATCH /brands/{id} valid | P0 | System behaves as expected without errors. |
| API-IN-010 | Verify PATCH /brands/{id} invalid ID | P0 | System behaves as expected without errors. |
| API-IN-011 | Verify GET /products 200 OK | P1 | System behaves as expected without errors. |
| API-IN-012 | Verify GET /products filter brand | P1 | System behaves as expected without errors. |
| API-IN-013 | Verify POST /products valid payload | P1 | System behaves as expected without errors. |
| API-IN-014 | Verify POST /products invalid brand | P1 | System behaves as expected without errors. |
| API-IN-015 | Verify API response time < 500ms | P1 | System behaves as expected without errors. |
| API-IN-016 | Verify API JSON schema validation | P1 | System behaves as expected without errors. |
| API-IN-017 | Verify API XSS sanitization | P1 | System behaves as expected without errors. |
| API-IN-018 | Verify API SQLi sanitization | P1 | System behaves as expected without errors. |
| API-IN-019 | Verify API rate limiting | P1 | System behaves as expected without errors. |
| API-IN-020 | Verify API CORS headers | P1 | System behaves as expected without errors. |
| API-IN-021 | Verify API Content-Type headers | P1 | System behaves as expected without errors. |
| API-IN-022 | Verify API pagination metadata | P1 | System behaves as expected without errors. |
| API-IN-023 | Verify API error message format | P1 | System behaves as expected without errors. |
| API-IN-024 | Verify API caching headers | P1 | System behaves as expected without errors. |
| API-IN-025 | Verify DELETE /brands (if supported) | P1 | System behaves as expected without errors. |
| API-IN-026 | Verify DELETE /products (if supported) | P1 | System behaves as expected without errors. |
| API-IN-027 | Verify GET /brands/{id} 200 OK | P1 | System behaves as expected without errors. |
| API-IN-028 | Verify GET /brands/{id} 404 | P1 | System behaves as expected without errors. |
| API-IN-029 | Verify API auth token expiration | P1 | System behaves as expected without errors. |
| API-IN-030 | Verify API refresh token logic | P1 | System behaves as expected without errors. |
| API-IN-031 | Verify API bulk endpoints | P2 | System behaves as expected without errors. |
| API-IN-032 | Verify API payload size limits | P2 | System behaves as expected without errors. |
| API-IN-033 | Verify API response compression (gzip) | P2 | System behaves as expected without errors. |
| API-IN-034 | Verify API versioning (/v1, /v2) | P2 | System behaves as expected without errors. |
| API-IN-035 | Verify API deprecated fields handling | P2 | System behaves as expected without errors. |
| API-IN-036 | Verify API unknown fields handling | P2 | System behaves as expected without errors. |
| API-IN-037 | Verify API idempotency on POST | P2 | System behaves as expected without errors. |
| API-IN-038 | Verify API concurrency control | P2 | System behaves as expected without errors. |
| API-IN-039 | Verify API audit logging | P2 | System behaves as expected without errors. |
| API-IN-040 | Verify API webhook triggers | P2 | System behaves as expected without errors. |
| API-IN-041 | Verify API GraphQL query (if applicable) | P2 | System behaves as expected without errors. |
| API-IN-042 | Verify API WebSocket connection | P2 | System behaves as expected without errors. |
| API-IN-043 | Verify API trace IDs in headers | P2 | System behaves as expected without errors. |
| API-IN-044 | Verify API health check endpoint | P2 | System behaves as expected without errors. |
| API-IN-045 | Verify API metrics endpoint | P2 | System behaves as expected without errors. |
| API-IN-046 | Verify API documentation accuracy | P2 | System behaves as expected without errors. |
| API-IN-047 | Verify API SDK compatibility | P2 | System behaves as expected without errors. |
| API-IN-048 | Verify API CLI compatibility | P2 | System behaves as expected without errors. |
| API-IN-049 | Verify API mock server responses | P2 | System behaves as expected without errors. |
| API-IN-050 | Verify API load testing | P2 | System behaves as expected without errors. |

## 9. Reporting & Activity Logs - 50 TCs
| TC ID | Test Case | Priority | Expected Result |
|---|---|---|---|
| RP-AC-001 | Verify Brand Report page loads | P0 | System behaves as expected without errors. |
| RP-AC-002 | Verify Brand Report columns | P0 | System behaves as expected without errors. |
| RP-AC-003 | Verify Brand Report filter specific brand | P0 | System behaves as expected without errors. |
| RP-AC-004 | Verify Brand Report filter date today | P0 | System behaves as expected without errors. |
| RP-AC-005 | Verify Brand Report filter date 7 days | P0 | System behaves as expected without errors. |
| RP-AC-006 | Verify Brand Report export CSV | P0 | System behaves as expected without errors. |
| RP-AC-007 | Verify Brand Report export Excel | P0 | System behaves as expected without errors. |
| RP-AC-008 | Verify Brand Report clicks accuracy | P0 | System behaves as expected without errors. |
| RP-AC-009 | Verify Brand Report conversions accuracy | P0 | System behaves as expected without errors. |
| RP-AC-010 | Verify Brand Report sorting | P0 | System behaves as expected without errors. |
| RP-AC-011 | Verify Activity Log brand created | P1 | System behaves as expected without errors. |
| RP-AC-012 | Verify Activity Log brand updated | P1 | System behaves as expected without errors. |
| RP-AC-013 | Verify Activity Log product added | P1 | System behaves as expected without errors. |
| RP-AC-014 | Verify Activity Log filter brand | P1 | System behaves as expected without errors. |
| RP-AC-015 | Verify Activity Log timestamp accuracy | P1 | System behaves as expected without errors. |
| RP-AC-016 | Verify Activity Log user mapping | P1 | System behaves as expected without errors. |
| RP-AC-017 | Verify Activity Log IP address | P1 | System behaves as expected without errors. |
| RP-AC-018 | Verify Activity Log action type filter | P1 | System behaves as expected without errors. |
| RP-AC-019 | Verify Activity Log export | P1 | System behaves as expected without errors. |
| RP-AC-020 | Verify Activity Log pagination | P1 | System behaves as expected without errors. |
| RP-AC-021 | Verify Activity Log real-time updates | P1 | System behaves as expected without errors. |
| RP-AC-022 | Verify Activity Log data retention | P1 | System behaves as expected without errors. |
| RP-AC-023 | Verify Activity Log search | P1 | System behaves as expected without errors. |
| RP-AC-024 | Verify Activity Log sorting | P1 | System behaves as expected without errors. |
| RP-AC-025 | Verify Activity Log details view | P1 | System behaves as expected without errors. |
| RP-AC-026 | Verify Brand Report UI responsiveness | P1 | System behaves as expected without errors. |
| RP-AC-027 | Verify Brand Report chart rendering | P1 | System behaves as expected without errors. |
| RP-AC-028 | Verify Brand Report drill-down | P1 | System behaves as expected without errors. |
| RP-AC-029 | Verify Brand Report timezone handling | P1 | System behaves as expected without errors. |
| RP-AC-030 | Verify Brand Report currency conversion | P1 | System behaves as expected without errors. |
| RP-AC-031 | Verify Brand Report empty state | P2 | System behaves as expected without errors. |
| RP-AC-032 | Verify Brand Report large date range | P2 | System behaves as expected without errors. |
| RP-AC-033 | Verify Brand Report custom date range | P2 | System behaves as expected without errors. |
| RP-AC-034 | Verify Brand Report scheduled exports | P2 | System behaves as expected without errors. |
| RP-AC-035 | Verify Brand Report API endpoints | P2 | System behaves as expected without errors. |
| RP-AC-036 | Verify Brand Report print view | P2 | System behaves as expected without errors. |
| RP-AC-037 | Verify Brand Report share link | P2 | System behaves as expected without errors. |
| RP-AC-038 | Verify Brand Report access control | P2 | System behaves as expected without errors. |
| RP-AC-039 | Verify Brand Report caching | P2 | System behaves as expected without errors. |
| RP-AC-040 | Verify Brand Report auto-refresh | P2 | System behaves as expected without errors. |
| RP-AC-041 | Verify Activity Log audit compliance | P2 | System behaves as expected without errors. |
| RP-AC-042 | Verify Activity Log tamper evidence | P2 | System behaves as expected without errors. |
| RP-AC-043 | Verify Activity Log system events | P2 | System behaves as expected without errors. |
| RP-AC-044 | Verify Activity Log API errors | P2 | System behaves as expected without errors. |
| RP-AC-045 | Verify Activity Log login events | P2 | System behaves as expected without errors. |
| RP-AC-046 | Verify Activity Log bulk action logging | P2 | System behaves as expected without errors. |
| RP-AC-047 | Verify Activity Log detail JSON format | P2 | System behaves as expected without errors. |
| RP-AC-048 | Verify Activity Log mask sensitive data | P2 | System behaves as expected without errors. |
| RP-AC-049 | Verify Activity Log performance | P2 | System behaves as expected without errors. |
| RP-AC-050 | Verify Activity Log archive process | P2 | System behaves as expected without errors. |

## 10. Advanced Edge & Security - 50 TCs
| TC ID | Test Case | Priority | Expected Result |
|---|---|---|---|
| ES-SE-001 | Verify XSS in Brand Name | P0 | System behaves as expected without errors. |
| ES-SE-002 | Verify SQLi in Brand Name | P0 | System behaves as expected without errors. |
| ES-SE-003 | Verify Session Timeout on save | P0 | System behaves as expected without errors. |
| ES-SE-004 | Verify Unauthorized direct URL access | P0 | System behaves as expected without errors. |
| ES-SE-005 | Verify Concurrent edit collision | P0 | System behaves as expected without errors. |
| ES-SE-006 | Verify Network disconnect on save | P0 | System behaves as expected without errors. |
| ES-SE-007 | Verify Browser Back after submit | P0 | System behaves as expected without errors. |
| ES-SE-008 | Verify Rapid Double Click on submit | P0 | System behaves as expected without errors. |
| ES-SE-009 | Verify numeric value in Email field | P0 | System behaves as expected without errors. |
| ES-SE-010 | Verify large int in Brand ID filter | P0 | System behaves as expected without errors. |
| ES-SE-011 | Verify 1M rows CSV upload | P1 | System behaves as expected without errors. |
| ES-SE-012 | Verify UTF-16 encoded CSV | P1 | System behaves as expected without errors. |
| ES-SE-013 | Verify window resize to 300px | P1 | System behaves as expected without errors. |
| ES-SE-014 | Verify direct API POST missing fields | P1 | System behaves as expected without errors. |
| ES-SE-015 | Verify direct API POST invalid key | P1 | System behaves as expected without errors. |
| ES-SE-016 | Verify emojis in Brand Name | P1 | System behaves as expected without errors. |
| ES-SE-017 | Verify non-English chars in Brand Name | P1 | System behaves as expected without errors. |
| ES-SE-018 | Verify manage deleted brand | P1 | System behaves as expected without errors. |
| ES-SE-019 | Verify negative items per page | P1 | System behaves as expected without errors. |
| ES-SE-020 | Verify empty mandatory fields CSV steps | P1 | System behaves as expected without errors. |
| ES-SE-021 | Verify rapid tab switching | P1 | System behaves as expected without errors. |
| ES-SE-022 | Verify 500+ chars in Email filter | P1 | System behaves as expected without errors. |
| ES-SE-023 | Verify non-numeric in Brand ID filter | P1 | System behaves as expected without errors. |
| ES-SE-024 | Verify 0 rows CSV upload | P1 | System behaves as expected without errors. |
| ES-SE-025 | Verify multiple Add Brand modals | P1 | System behaves as expected without errors. |
| ES-SE-026 | Verify CSRF token validation | P1 | System behaves as expected without errors. |
| ES-SE-027 | Verify Clickjacking protection | P1 | System behaves as expected without errors. |
| ES-SE-028 | Verify Content Security Policy | P1 | System behaves as expected without errors. |
| ES-SE-029 | Verify HTTP Strict Transport Security | P1 | System behaves as expected without errors. |
| ES-SE-030 | Verify cookie secure flag | P1 | System behaves as expected without errors. |
| ES-SE-031 | Verify cookie HttpOnly flag | P2 | System behaves as expected without errors. |
| ES-SE-032 | Verify brute force API protection | P2 | System behaves as expected without errors. |
| ES-SE-033 | Verify mass assignment vulnerability | P2 | System behaves as expected without errors. |
| ES-SE-034 | Verify parameter tampering | P2 | System behaves as expected without errors. |
| ES-SE-035 | Verify directory traversal on CSV upload | P2 | System behaves as expected without errors. |
| ES-SE-036 | Verify XML External Entity on CSV | P2 | System behaves as expected without errors. |
| ES-SE-037 | Verify Server Side Request Forgery | P2 | System behaves as expected without errors. |
| ES-SE-038 | Verify open redirect vulnerability | P2 | System behaves as expected without errors. |
| ES-SE-039 | Verify broken access control | P2 | System behaves as expected without errors. |
| ES-SE-040 | Verify insecure direct object reference | P2 | System behaves as expected without errors. |
| ES-SE-041 | Verify security misconfiguration | P2 | System behaves as expected without errors. |
| ES-SE-042 | Verify cross-origin resource sharing | P2 | System behaves as expected without errors. |
| ES-SE-043 | Verify sensitive data exposure | P2 | System behaves as expected without errors. |
| ES-SE-044 | Verify broken authentication | P2 | System behaves as expected without errors. |
| ES-SE-045 | Verify insufficient logging | P2 | System behaves as expected without errors. |
| ES-SE-046 | Verify unvalidated redirects | P2 | System behaves as expected without errors. |
| ES-SE-047 | Verify components with known vulnerabilities | P2 | System behaves as expected without errors. |
| ES-SE-048 | Verify API rate limit bypass | P2 | System behaves as expected without errors. |
| ES-SE-049 | Verify session fixation | P2 | System behaves as expected without errors. |
| ES-SE-050 | Verify account takeover attempts | P2 | System behaves as expected without errors. |

