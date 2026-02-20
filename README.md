# AI Resume Builder

An intelligent resume building application that analyzes job descriptions, extracts keywords, scores resumes against job requirements, and generates professional resume documents in PDF and DOCX formats.

## Features

- 📋 **Comprehensive Resume Form** - Collect personal info, education, skills, projects, experience, and certifications
- 🤖 **ATS Scoring** - Analyzes resume compatibility with job descriptions using machine learning
- 🔍 **Keyword Extraction** - Automatically extracts relevant keywords from job descriptions
- 📊 **Similarity Matching** - Computes similarity between resume and job requirements
- 📄 **Multi-Format Export** - Generate resumes in PDF and DOCX formats
- 💡 **Smart Feedback** - Provides actionable recommendations to improve ATS matching

## Tech Stack

- **Backend**: Flask (Python)
- **NLP**: spaCy
- **ML**: scikit-learn
- **Document Generation**: python-docx, reportlab
- **Server**: Gunicorn
- **Deployment**: Render

## Local Setup

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd ai_resume_builder

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The application will start at `http://localhost:10000`

## Deployment on Render

### Quick Deploy Steps

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Deploy to Render"
   git push origin main
   ```

2. **Connect to Render**
   - Go to [render.com](https://render.com)
   - Sign in with your GitHub account
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the `ai_resume_builder` repository

3. **Configure Deployment**
   - **Name**: `ai-resume-builder`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free (or upgrade as needed)

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete (2-3 minutes)

5. **Get Your Link**
   After deployment, Render will provide your URL:
   ```
   https://ai-resume-builder-xxxx.onrender.com
   ```

### Environment Variables (if needed)
- No required environment variables for basic deployment
- The app automatically uses Render's `PORT` environment variable

## Project Structure

```
ai_resume_builder/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── runtime.txt           # Python version
├── render.yaml           # Render deployment config
├── models/
│   └── ats_scorer.py     # ATS scoring logic
├── nlp/
│   ├── keyword_extractor.py  # Keyword extraction
│   └── similarity.py         # Similarity matching
├── resume/
│   ├── pdf_generator.py  # PDF generation
│   └── docx_generator.py # DOCX generation
├── static/
│   └── css/
│       └── styles.css    # Styling
└── templates/
    ├── index.html        # Main form
    └── result.html       # Results page
```

## Usage

1. Fill in your resume information in the form fields
2. Enter the job role or job description
3. Select resume template style
4. Click "Generate Resume"
5. Review your ATS score and feedback
6. Download your resume in PDF or DOCX format

## API Endpoints

- `GET /` - Main resume builder form
- `POST /` - Process resume form and generate documents

## Troubleshooting

**Deployment Failed?**
- Check that all dependencies are in `requirements.txt`
- Verify `render.yaml` has correct configuration
- Ensure `app.py` uses dynamic `PORT` environment variable

**File Generation Issues?**
- Ensure reportlab and python-docx are installed
- Check that template files exist in `templates/`

## Future Enhancements

- [ ] Multiple template designs
- [ ] Cover letter generation
- [ ] Resume parsing from uploaded files
- [ ] Custom color schemes
- [ ] Mobile-responsive design improvements
- [ ] Resume history/versions

## License

MIT License

## Support

For issues or questions, please create an issue in the repository.
