# Postman Configuration Reference – All Panels

## Collections Structure
Each panel has its own Postman Collection under "COLLECTIONS":
```
COLLECTIONS
├── AB Net
│   ├── POST Create Customer  → https://api.affnook.io/api/admin/v2/customers
│   └── POST create activity  → https://api.trackierigaming.io/api/admin/v2/activities
├── AB op
│   ├── POST Create Customer
│   └── POST create activity
├── BiAffiliation
│   ├── POST Create Customer
│   └── POST create activity
├── KtAccount
│   ├── POST Create Customer
│   ├── POST create activity
│   └── GET New Request
└── tmtpanel
    └── (various requests)
```

---

## Headers for EVERY Request (12 headers total, 4 visible key ones)

| Header Key | Value | Notes |
|------------|-------|-------|
| Accept | application/json | Same across ALL panels |
| Authorization | Bearer 123 | Same across ALL panels |
| Content-Type | application/json | Same across ALL panels |
| x-api-key | (copy from platform) | **DIFFERENT per panel** |

### How to get x-api-key:
1. Open the panel website (e.g., oscorp7.affnookqa1.online for AB Network)
2. Go to **Configuration → Automation → API tab**
3. Copy the API Key shown
4. Paste as x-api-key value in Postman for that panel's collection

---

## API Endpoints

### Customers
- **Create Customer**: `POST https://api.affnook.io/api/admin/v2/customers`

### Activities
- **Create Activity**: `POST https://api.trackierigaming.io/api/admin/v2/activities`

### Geo APIs (New with City & Region feature)
- **Get Regions**: `GET /web/admin/v2/regions/filter?country_code=US&name=Cal&page=1&limit=10`
- **Get Cities**: `GET /web/admin/v2/cities/filter?region_name=California&name=Los&page=1&limit=10`

---

## Create Customer – Full Request Body (with Geo fields)
```json
{
  "customerId": "CnR_Cus_001",
  "customerName": "CnR_Cus_001",
  "timestamp": "{{$timestamp}}",
  "currency": "usd",
  "trackingToken": "69e681d0b6e25fc69a199a49",
  "country": "US",
  "region": "California",
  "city": "Los Angeles"
}
```

## Create Customer – Geo Rejection Scenario
```json
{
  "customerId": "CnR_Cus_002",
  "customerName": "CnR_Cus_002",
  "timestamp": "{{$timestamp}}",
  "currency": "usd",
  "trackingToken": "69e681d0b6e25fc69a199a49",
  "country": "US",
  "region": "Texas",
  "city": "Houston"
}
```
*(Use this when campaign is set to Exclude Texas – expect Rejection: Geo Not Allowed)*

## Create Activity – Request Body
```json
{
  "customerId": "CnR_Cus_001",
  "activityType": "deposit",
  "amount": 100,
  "timestamp": "{{$timestamp}}",
  "currency": "usd"
}
```

---

## Response Examples

### Successful Customer Creation (200 OK)
```json
{
  "success": true,
  "message": "Customer created with id: 69e6087c79efa9a9bc87dd7f",
  "data": {
    "hash_id": "69e6087c79efa9a9bc87dd7f",
    "customer_id": "CnR_Cus_001"
  }
}
```

### Geo Rejected Activity (Check in Activity Report after ~2 min)
- Status: **Rejected**
- Rejection Reason: **Geo Not Allowed**
