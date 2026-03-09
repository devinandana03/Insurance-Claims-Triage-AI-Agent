# Insurance Claims Triage AI

An AI-powered insurance claims triage system that analyzes claim details, detects fraud risk using machine learning, retrieves policy rules using Retrieval-Augmented Generation (RAG), and generates grounded insights using an LLM.

The system helps insurers prioritize claims, detect suspicious patterns, and understand potential financial implications.

---

## Features

- Fraud risk prediction using a trained ML model
- Policy and regulatory grounding using RAG
- AI-generated claim analysis
- Streamlit web interface
- LLM reasoning using Groq (LLaMA model)
- Synthetic dataset generation for testing

---

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- Sentence Transformers
- FAISS
- Groq LLM API
- Pandas / NumPy

---

## Project Structure

```
insurance_AI_agent/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
│   ├── generate_data.py
│   └── claims_dataset.csv
│
├── fraud/
│   ├── train_model.py
│   └── fraud_model.pkl
│
├── rag/
│   ├── rag_engine.py
│   └── knowledge_base.txt
│
├── utils/
│   ├── __init__.py
│   ├── claim_parser.py
│   └── groq_llm.py
│
└── prompts/
    └── system_prompt.txt
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/insurance-ai-claims-triage.git
cd insurance-ai-claims-triage
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Groq SDK

```bash
pip install groq
```

---

## Environment Variables

Create a `.env` file in the root directory.

```
GROQ_API_KEY=your_api_key_here
```

You can generate an API key from the Groq console.

---

## Generate Dataset

Run the dataset generator:

```bash
python data/generate_data.py
```

This creates a synthetic insurance claims dataset used to train the fraud detection model.

---

## Train Fraud Detection Model

```bash
python fraud/train_model.py
```

This will generate:

```
fraud_model.pkl
```

---

## Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Open the browser:

```
http://localhost:8501
```

---

## Example Input

```
Claim Amount: 42000
Delay Days: 25
Previous Claims: 4
```

Example Output:

- Fraud risk score
- Claims triage summary
- Policy-based reasoning
- Financial impact insight

---

## How It Works

1. User enters claim details in Streamlit.
2. Fraud model predicts fraud probability.
3. RAG retrieves relevant insurance policy rules.
4. Prompt is sent to Groq LLM.
5. AI generates a grounded claims analysis.

---

## Future Improvements

- Claim document upload
- Fraud explanation charts
- ACORD-compliant claim schema
- Vector database (ChromaDB)
- Dashboard analytics

---

## License

MIT License