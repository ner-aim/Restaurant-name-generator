# 🧠 LLM-Powered Analytics Automation

This project demonstrates how **Large Language Models (LLMs)** can automate retail media analytics workflows — generating insights, campaign summaries, and interactive Q&A from unstructured inputs.  

Built with **LangChain**, **OpenAI**, and **Streamlit**, the app simulates how retailers or advertisers can leverage AI for **faster decision-making and campaign optimization**.

---

## ✨ Features
- 🔍 **Insight Generation** – Automatically produce campaign highlights and optimization suggestions.  
- 📝 **Summarization** – Condense verbose reports into concise, actionable takeaways.  
- 💬 **Q&A System** – Ask natural-language questions about your campaigns and get structured answers.  
- 🔗 **LangChain SequentialChain** – Demonstrates chaining prompts for complex workflows.  
- ⚡ **Interactive UI** – Built with Streamlit for quick experimentation and demos.  

---

## 📊 Demo

| Campaign Input | Generated Insights |
|----------------|--------------------|
<!-- | ![input](assets/campaign_input.png) | ![output](assets/campaign_output.png) | -->

🔹 Example: The model takes in raw campaign data (spend, impressions, CTR, conversions) and outputs **clear recommendations** on ROI and optimizations.  

---

## 🚀 Tech Stack
- **Python 3.9+**  
- [LangChain](https://www.langchain.com/) – LLM pipelines & orchestration  
- [OpenAI API](https://platform.openai.com/) – GPT-based language models  
- [Streamlit](https://streamlit.io/) – Interactive UI  
- [pandas / SQLAlchemy] – Data handling & querying  

---

## 📦 Installation
```bash
# Clone the repo
git clone https://github.com/your-username/llm-analytics-automation.git
cd llm-analytics-automation

# Create virtual environment
python -m venv venv
source venv/bin/activate   # (or venv\Scripts\activate on Windows)

# Install dependencies
pip install -r requirements.txt
```

Set your **OpenAI API Key**:
```bash
export OPENAI_API_KEY="your_key_here"
```

---

## ▶️ Usage
Run the Streamlit app:
```bash
streamlit run main.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser to interact.  

---

## 🖼️ Screenshots

### Campaign Q&A
![QA Demo](assets/qa_demo.gif)

### Insight Summarization
![Summarization Demo](assets/summarization.png)

---

## 📈 Potential Applications
- Retail media performance reporting  
- Supplier campaign optimization (CPG, eCommerce)  
- Automated BI report generation  
- Customer-facing analytics dashboards  

---

## 🤝 Contributing
Contributions are welcome!  
1. Fork the repo  
2. Create a branch (`feature/my-feature`)  
3. Commit changes  
4. Open a PR 🚀  

---

## 📜 License
MIT License © 2025
