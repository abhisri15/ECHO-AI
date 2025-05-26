# 🤖 ECHO AI – Your Personal Voice Assistant Powered by GPT

**ECHO AI** is an interactive voice-based assistant built using Python, OpenAI’s GPT model, and speech technologies. It listens to your commands, chats intelligently, opens websites, tells the time, plays music, and more — all through your voice.

> 🗓️ **Originally built in July 2023. Uploaded later because... well, better late than never! 😉**

---

## 🧠 Features

* 🎤 **Voice Command Recognition**
  Understands and executes spoken commands using `speechrecognition`.

* 🗣️ **Text-to-Speech Output**
  Responds with lifelike speech using `pyttsx3`.

* 🌐 **Smart Browsing**
  Opens websites like YouTube, Google, Wikipedia, Gmail, OpenAI, and more via voice.

* 🎶 **Play Music Locally**
  Triggers local music playback with a single command.

* 🕒 **Tell the Time**
  Speaks out the current time on request.

* 💬 **Chat with GPT (text-davinci-003)**
  Natural and continuous conversations using OpenAI's GPT model with context memory.

* 🧠 **Custom GPT Fine-Tuning (Implemented)**
  Integrated a fine-tuned GPT model for more personalized responses.

* 📁 **Prompt Logging**
  Automatically saves prompt-response logs for future reference.

* 🔧 **Modular & Extendable Design**
  Future-ready with TODOs for app launching, weather API, news API, and more.

---

## 🛠️ Installation

```bash
pip install speechrecognition
pip install wikipedia
pip install openai
pip install pyttsx3
```

Make sure to also:

* Install `PyAudio` (required for microphone input).
* Set up your OpenAI API key in a `config.py` file:

```python
# config.py
apiKey = "your_openai_api_key"
```

---

## 🚀 How to Use

Run the assistant:

```bash
python echo_ai.py
```

Then simply **speak into your microphone** and say things like:

* "Open YouTube"
* "What is artificial intelligence?"
* "Play music"
* "What time is it?"
* "Exit"

---

## 📁 File Structure

```
.
├── echo_ai.py          # Main assistant script
├── config.py           # API key file
├── OpenAI/             # Auto-generated prompt logs
├── requirements.txt    # (optional) dependency list
```

---

## 💡 Future Plans

* 🌤️ Integrate Weather API (weatherapi.com)
* 📰 Add News Support (newsapi.com)
* 📱 Launch Desktop Apps with Voice
* 🎙️ Improve Wake Word Detection
* 🧠 Switch to GPT-4 or LLM with better efficiency

---

## 📅 Timeline

* **Project Started**: July 2023
* **Fine-tuning & Feature Modifications**: August–September 2023
* **GitHub Upload**: May 2025 (yes, really 😅)

---

## 📢 Note

This project was a fun and experimental attempt at combining **voice AI**, **custom GPT fine-tuning**, and **practical automation**. Posting it late because life happened — but the code is battle-tested and works like a charm!

---

## 🤝 Contributing

Want to improve ECHO AI? Feel free to fork, raise issues, or open pull requests.

---

## 📜 License

This project is for educational purposes. Reach out for extended commercial use or collaborations.

---
