# AI-Powered Job Application Assistant

A Python-based application that helps job seekers find relevant job postings from LinkedIn and analyze their resume compatibility using AI.

## Features

- Fetch job postings from LinkedIn using Apify
- Analyze resume compatibility with job descriptions
- Streamlit-based web interface for easy interaction
- Environment variable configuration for API keys

## Prerequisites

- Python 3.7+
- Apify account and API token
- OpenAI API key (for resume analysis)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd job
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API keys:
   ```
   APIFY_API_TOKEN=your_apify_token_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run src/job_api.py
   ```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Use the interface to:
   - Search for jobs by keywords and location
   - Upload your resume (PDF format)
   - Get AI-powered analysis of job matches

## Project Structure

```
job/
├── src/
│   ├── __init__.py
│   ├── helper.py        # Helper functions
│   └── job_api.py       # Main API and job fetching logic
├── image/               # Directory for storing images
├── pdf/                 # Directory for storing PDF files
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Dependencies

- `streamlit` - Web application framework
- `openai` - For AI-powered resume analysis
- `pymupdf` - For PDF processing
- `python-dotenv` - For managing environment variables
- `apify-client` - For fetching job listings from LinkedIn

## Configuration

All configuration is done through environment variables in the `.env` file. Make sure to never commit this file to version control.

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Apify](https://apify.com/) for the LinkedIn job scraping service
- [OpenAI](https://openai.com/) for the AI analysis capabilities
- [Streamlit](https://streamlit.io/) for the web interface framework