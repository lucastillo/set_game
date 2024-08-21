# FastAPI Set Game Service

This FastAPI service finds all valid sets from a given list of cards, based on the rules of the Set card game. The service allows you to send a list of cards and returns all possible valid sets.

## Requirements

- Python 3.8 or higher
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/lucastillo/set_game.git
   cd fastapi-set-game
   ```

2. **Create a Virtual Environment**
   It is recommended to create a virtual environment for your project:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required dependencies using pip:

   ```bash
   pip install fastapi uvicorn pydantic
   ```

## Running the Service

To run the FastAPI service, use the following command:

```bash
   uvicorn main:app --reload
```

This will start the service at http://127.0.0.1:8000.

## Usage

You can test the API using curl, Postman, or any other HTTP client.

### Example Request

To find valid sets, send a POST request to the /find_sets/ endpoint with the list of cards in JSON format:

```bash
   curl -X POST "http://127.0.0.1:8000/find_sets/" -H "Content-Type: application/json" -d '{
    "cards": ["1111", "2222", "3333", "1122", "2211"]
}'
```

### Example Response

The response will be a JSON object containing all the valid sets:

```json
{
  "valid_sets": [["1111", "2222", "3333"]]
}
```
