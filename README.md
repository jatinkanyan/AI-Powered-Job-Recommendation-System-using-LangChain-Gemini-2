# AI-Powered Job Recommendation System (LangChain + Groq + Streamlit)

A complete working demo app that matches a student's skills or resume text to job postings and generates personalized recommendations using Groq LLM — built only with the provided files.

--------------------------------------------------------------------------------
OBJECTIVE
--------------------------------------------------------------------------------
- Help students discover job/internship opportunities that match their skills, experience, and preferences.
- Use modern LLM-based RAG techniques for personalized recommendations.

--------------------------------------------------------------------------------
FEATURES
--------------------------------------------------------------------------------
1. Upload your resume (PDF) or type skills/preferences manually.
2. Embed and compare against locally stored job postings using sentence-transformers.
3. Rank jobs using cosine similarity.
4. Generate short, tailored explanations using Groq API.
5. Display results in a simple, dark-themed Streamlit web interface.

--------------------------------------------------------------------------------
TECH STACK
--------------------------------------------------------------------------------
Language         : Python  
Embeddings       : sentence-transformers (all-MiniLM-L6-v2)  
Similarity       : scikit-learn cosine similarity  
LLM              : Groq API (llama-3.3-70b-versatile)  
UI               : Streamlit  
Data Source      : Local JSON file (data/jobs.json)  

--------------------------------------------------------------------------------
FOLDER STRUCTURE
--------------------------------------------------------------------------------
project/
├── app.py
├── requirements.txt
├── .gitignore
├── .env                   # contains GROQ_API_KEY
├── data/
│   └── jobs.json
└── src/
    ├── utils.py
    ├── embed_utils.py
    ├── groq_utils.py
    ├── recommendation.py   # legacy OpenAI example, not used in app.py
    └── vector_store.py     # optional Chroma example, not used in app.py

--------------------------------------------------------------------------------
ENVIRONMENT VARIABLES
--------------------------------------------------------------------------------
Create a file `.env` in the project root:

GROQ_API_KEY=your_groq_api_key_here

--------------------------------------------------------------------------------
INSTALLATION & SETUP
--------------------------------------------------------------------------------
1) Clone or open the project folder.

2) Create and activate virtual environment:
   Windows (PowerShell):
       python -m venv venv
       .\venv\Scripts\Activate.ps1

   macOS/Linux (bash/zsh):
       python3 -m venv venv
       source venv/bin/activate

3) Upgrade pip and install dependencies:
       python -m pip install --upgrade pip
       pip install -r requirements.txt

4) Add your `.env` file with the Groq API key.

5) Prepare jobs data in `data/jobs.json`:
   Each job should have at least:
       {
         "id": "job_001",
         "title": "Data Analyst Intern",
         "companyName": "Acme Corp",
         "description": "Work with SQL, Python, and dashboards."
       }

6) Run the application:
       streamlit run app.py

--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------
- Upload a resume PDF or enter skills/preferences.
- Click "Get Recommendations".
- View top 5 matched jobs based on similarity.
- If Groq API key is active, see a personalized recommendation explanation.

--------------------------------------------------------------------------------
HOW IT WORKS
--------------------------------------------------------------------------------
1. Load jobs from `data/jobs.json` using `utils.py`.
2. Embed user input and job descriptions with `embed_utils.py`.
3. Compute cosine similarity to rank jobs.
4. Call `groq_utils.py` for a personalized explanation.
5. Display results in Streamlit UI with custom CSS dark theme.

--------------------------------------------------------------------------------
VS CODE QUICK GUIDE
--------------------------------------------------------------------------------
1. Install VS Code and open the project folder.
2. Open terminal in VS Code (View -> Terminal).
3. Create & activate venv inside terminal.
4. Install requirements.
5. Press Ctrl+Shift+P -> "Python: Select Interpreter" -> choose venv interpreter.
6. Run:
       streamlit run app.py

--------------------------------------------------------------------------------
TROUBLESHOOTING
--------------------------------------------------------------------------------
- Groq API error: Check `.env` and key validity.
- Jobs not loading: Ensure `data/jobs.json` exists and is valid JSON.
- Empty PDF extraction: Try a different resume file or manual input.
- Slow first run: Model downloads on first use; wait until complete.

--------------------------------------------------------------------------------
QUICK START (COMMANDS)
--------------------------------------------------------------------------------
python -m venv venv
.\venv\Scripts\Activate.ps1         # Windows
# source venv/bin/activate          # macOS/Linux
pip install --upgrade pip
pip install -r requirements.txt
echo GROQ_API_KEY=your_groq_api_key_here > .env
streamlit run app.py

--------------------------------------------------------------------------------
NOTES
--------------------------------------------------------------------------------
- Jobs are from local file, no live scraping in app.py.
- UI displays "No Title"/"Unknown" if jobs.json lacks title/company keys.
- For richer display, modify utils.py to preserve more metadata.
