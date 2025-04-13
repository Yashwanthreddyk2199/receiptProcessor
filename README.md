# Receipt Processor

## Step 1: Clone the Repository

Clone the repository to your local machine using `git`:

```bash
git clone https://github.com/Yashwanthreddyk2199/receiptProcessor.git
```
Navigate to Cloned Directory 

```bash 
cd receiptProcessor
```
## Step 2: Build the Docker Image

Build the Docker image from the `Dockerfile` in the repository:

```bash
docker build -t receipt-processor .
```

## Step 3: Run the Docker Container

Run the Docker container from the image you just built:

```bash
docker run -p 8000:8000 receipt-processor
```

Now, the server should be running at `http://localhost:8000`.

---

## API Endpoints

### `POST /receipts/process`

- **Description**: Submits a receipt for processing.
- **Request Body**: JSON with receipt details.
- **Response**: Receipt ID.

#### Example Request

```json
{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },
    {
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    }
  ],
  "total": "18.74"
}
```

#### Example Response

```json
{
  "id": "e35f8b22-4dbd-4372-85fc-4bfb32d3cd20"
}
```

---

### `GET /receipts/<id>/points`

- **Description**: Retrieves the points awarded for a specific receipt.
- **Path Parameter**: `id` – the unique ID of the receipt.
- **Response**: JSON with the points.

#### Example Response

```json
{
  "points": 28
}

