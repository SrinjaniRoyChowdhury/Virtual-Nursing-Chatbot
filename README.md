# 🩺 NurseBot - Virtual Nursing Assistant

**NurseBot** is an AI-powered virtual nursing assistant built with [Streamlit](https://streamlit.io/) and Google's [Gemini](https://ai.google.dev/) Generative AI model. It can help users with basic health questions, nursing-related guidance, and preliminary understanding of medical conditions in a compassionate and professional manner.

---

## 🚀 Features

- 🤖 Conversational chatbot for health and nursing queries
- 💬 Chat-style UI with message bubbles and avatars
- 🧠 Context-aware responses tailored to the medical domain
- 🔐 Secure API key management via `.env`
- 🖥️ Simple to run locally using Streamlit

---

## 🛠️ Tech Stack

- [Python 3.9+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google.dev/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/nursebot-chatbot.git
cd nursebot-chatbot
````

### 2. Create a `.env` File

Create a `.env` file in the root directory and add your [Google AI API key](https://aistudio.google.com/app/apikey):

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Usage

### Run the Streamlit App

```bash
streamlit run app.py
```

Then open the browser at [http://localhost:8501](http://localhost:8501)

---

## 🧪 Example Queries

* "I have pile"
* "Can you tell me symptoms of UTI?"
* "What should I eat if I have anemia?"
* "How to care for a diabetic patient?"

---

## 📁 Project Structure

```
nursebot-chatbot/
│
├── app.py               # Main Streamlit app
├── .env                 # API key (not included in GitHub)
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
```

---

## 📌 Notes

* This is not a replacement for professional medical advice.
* Always consult with a healthcare provider for serious or emergency issues.

---

## 📃 License

MIT License © [Srinjani Roy Chowdhury](https://github.com/SrinjaniRoyChowdhury)

---

## 💡 Future Improvements

* ✅ Add voice input / TTS
* ✅ Deploy on Streamlit Cloud
* ✅ Export chat history
* ✅ Support for multilingual responses

---

## 🙋‍♀️ Contributing

Pull requests and issues are welcome! If you find a bug or want to contribute a feature, feel free to open a PR.

```