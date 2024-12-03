# Talking Assistant with Groq-AI for Diabetes Management 🩺

## 1. **Project Overview**
This project creates an AI-powered Talking Assistant designed specifically for diabetes patients. It listens to user speech, processes the input using the Groq-AI model, and generates health-related advice about diabetes management. The assistant converts its responses into speech using the Deepgram TTS API. This entire process is seamlessly integrated into a Streamlit interface, enabling real-time, spoken interactions.

### **Key Features**
- **Speech-to-Text (STT)**: Converts user speech to text using the **webkitSpeechRecognition** API.
- **AI Response Generation**: Utilizes the **Groq-AI** model to generate text responses based on the user's speech.
- **Text-to-Speech (TTS)**: Converts the generated text responses into audio using **Deepgram**'s TTS API.
- **Streamlit Interface**: A user-friendly interface where users can speak into the microphone, and the assistant responds through both text and audio.

### **Technologies Used**
- **Streamlit**: For building the interactive web app.
- **Bokeh**: For integrating custom widgets like the "Speak" button.
- **Groq-AI**: For generating responses based on user input.
- **Deepgram TTS**: For converting the AI-generated text responses into speech.
- **webkitSpeechRecognition**: For real-time speech-to-text transcription.

---
### **Project Video**
The project video is available in the `project_video.mp4` file, showcasing the full functionality of the Talking Assistant in action.

---

## 2. **Deepgram TTS Integration**

### **Description**
The **Deepgram** API is used to convert the AI-generated text into natural-sounding speech. This step enables the assistant to "speak" the generated response to the user. The **Deepgram TTS** system synthesizes high-quality speech in MP3 format and streams it back to the user via the **Streamlit** interface.

### **Features**
- Uses **Deepgram’s Aura-Asteria-en** model for high-quality, natural voice synthesis.
- Converts any AI-generated text into an audio file in MP3 format.
- Allows real-time playback of the audio file within the **Streamlit** interface.

### **Process Flow**
1. The AI generates a response based on user input.
2. The text response is sent to **Deepgram** for conversion into speech.
3. The MP3 file is returned and played back to the user through the **Streamlit** interface.

---

## 3. **Groq-AI Integration**

### **Description**
**Groq-AI** powers the assistant's response generation, utilizing a trained AI model to process and understand the user's speech. The assistant generates responses to health-related queries, particularly focusing on metabolic and endocrine disorders such as diabetes, obesity, and thyroid issues.

### **Features**
- The assistant uses a **predefined prompt** to generate medical and health-related advice in an empathetic and easy-to-understand manner.
- Integrates seamlessly with the **Streamlit** interface to provide real-time responses.
- The model used for generating responses is based on **Groq**'s Llama 3, tailored for tool use and conversational understanding.

### **Process Flow**
1. The user speaks into the microphone, and the speech is converted to text.
2. The text is sent to **Groq-AI** for generating a response.
3. The generated response is then converted into speech by **Deepgram TTS** and played back to the user.

---

## 4. **Speech-to-Text (STT) Integration**

### **Description**
The **Speech-to-Text (STT)** component of the application uses the **webkitSpeechRecognition** API, a web-based speech recognition tool, to transcribe the user's speech in real-time. This allows the assistant to understand and process natural language input for generating appropriate responses.

### **Features**
- Continuous speech recognition with real-time transcription.
- Handles interim results to display the user’s speech as it’s being processed.
- Supports **browser-based speech recognition**, meaning users can interact directly through their browser without needing additional software.

### **Process Flow**
1. When the user clicks the "Speak" button, the **webkitSpeechRecognition** API is triggered to start listening to the user’s speech.
2. The speech is transcribed into text and sent to **Groq-AI** for response generation.
3. The transcribed text is processed by **Groq-AI**, and the response is returned.

---

## 5. **Streamlit User Interface**

### **Description**
The application’s user interface is built using **Streamlit**, which allows for a clean, interactive design. The main interaction point for the user is the "Speak" button, which activates the speech recognition system. Once the user speaks, the assistant listens, processes the speech, generates a response, and plays it back via audio.

### **Features**
- Simple, intuitive UI with a button that triggers speech recognition.
- Displays AI-generated responses and plays them back as audio.
- Responsive design that allows real-time interactions.

### **User Interaction Flow**
1. The user accesses the **Streamlit** interface and clicks the "Speak" button.
2. The application starts recording the user’s speech.
3. Once the speech is detected, it is transcribed and sent to **Groq-AI** for a response.
4. The response is then converted into speech by **Deepgram TTS** and played to the user.

---

## 6. **Environment Setup**

### **Prerequisites**
To run this application, the following tools and dependencies need to be installed:

- **Python 3.x**
- **Streamlit**: To create the web application.
- **Bokeh**: For interactive widgets.
- **Groq**: For AI response generation.
- **Deepgram TTS**: For text-to-speech functionality.
- **dotenv**: For environment variable management.

### **Installation Steps**
1. Clone the repository and navigate to the project directory.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
## 6. **Environment Setup**

### **Installation Steps**
1. Clone the repository and navigate to the project directory.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt


## 7. API Keys and Configuration

### Deepgram API
- Sign up at [Deepgram](https://www.deepgram.com/) and obtain an API key to enable the Text-to-Speech (TTS) functionality.
- Add the API key to the `.env` file as `DG_API_KEY`.

### Groq-AI API
- Sign up at [Groq-AI](https://www.groq.com/) and obtain an API key to enable AI responses.
- Add the API key to the `.env` file as `GROQ_API_KEY`.

### Example `.env` File
Create a `.env` file in the project directory and add the following lines:

```env
DG_API_KEY=your_deepgram_api_key_here
GROQ_API_KEY=your_groq_api_key_here

```
## 8. Future Improvements

### Planned Features
- Integration with additional AI models to broaden the scope of conversations.
- Enhanced voice customization options for Deepgram TTS.
- Multi-language support for global users.

### Bug Fixes
- Address any speech recognition issues related to browser compatibility.
- Improve the response generation time and accuracy.

## 9. Conclusion

The Talking Assistant with Groq-AI provides an interactive way to communicate with an AI system through speech. By integrating Groq-AI for generating responses and Deepgram TTS for voice synthesis, the system offers a seamless conversational experience. This project demonstrates the potential of combining speech recognition, AI models, and text-to-speech systems to create user-friendly interactive assistants.

For more information or support, feel free to reach out via email a [hayatadil300@gmail.com](mailto:hayatadil300@gmail.com).
