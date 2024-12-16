# Sentiment Analysis API

A FastAPI-based web service that performs sentiment analysis on text input using NLTK (Natural Language Toolkit). This service provides sentiment scores indicating whether the input text expresses positive, negative, or neutral sentiment.

## Features

- RESTful API endpoints for sentiment analysis
- Text preprocessing including tokenization and cleaning
- Sentiment scoring using NLTK's VADER sentiment analyzer
- Async request handling for better performance
- Comprehensive error handling and input validation

## Prerequisites

- Python 3.8+
- FastAPI
- NLTK
- uvicorn (ASGI server)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sentiment-analysis-api.git
cd sentiment-analysis-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Download required NLTK data:
```python
python -c "import nltk; nltk.download('vader_lexicon')"
```

## Usage

### Running the API Server

1. Start the server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. Access the API documentation at `http://localhost:8000/docs`

### API Endpoints

#### POST /analyze
Analyzes the sentiment of provided text.

Request body:
```json
{
    "text": "Your text to analyze"
}
```

Response:
```json
{
    "text": "Your text to analyze",
    "sentiment": {
        "compound": 0.556,
        "pos": 0.437,
        "neu": 0.563,
        "neg": 0.0
    }
}
```

## Project Structure

```
sentiment-analysis-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── analyzer.py
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py
├── requirements.txt
└── README.md
```

## Configuration

The application can be configured using environment variables:

- `HOST`: Server host (default: "0.0.0.0")
- `PORT`: Server port (default: 8000)
- `LOG_LEVEL`: Logging level (default: "info")

## Testing

Run the test suite:
```bash
pytest tests/
```

## Error Handling

The API includes comprehensive error handling for:
- Invalid input text
- Missing required fields
- Server processing errors
- Rate limiting exceeded

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions and support, please open an issue in the GitHub repository or contact [your-email@example.com].
