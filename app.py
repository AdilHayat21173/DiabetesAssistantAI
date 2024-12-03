import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from TTS import *
from groq_ai import *
import base64


def autoplay_audio(file_path: str):
    # Check if the file_path is valid
    if not file_path:
        st.error("Invalid file path.")
        return
    
    try:
        # Read the audio file in binary mode
        with open(file_path, "rb") as f:
            data = f.read()
        
        # Encode the audio file to base64
        b64 = base64.b64encode(data).decode()

        # Create an HTML audio tag with autoplay enabled
        md = f"""
        <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """

        # Render the audio player in Streamlit
        st.markdown(md, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("Talking Assistant with Groq-AI 🗣️")
    st.write("Please click the button below to start recording your speech:")

    # Create a Bokeh Button
    stt_button = Button(label="Speak", width=100)
    
    st.bokeh_chart(stt_button)
     
    # Custom JavaScript for speech recognition using webkitSpeechRecognition
    stt_button.js_on_event("button_click", CustomJS(code="""
        var recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;

        recognition.onresult = function (e) {
            var value = "";
            for (var i = e.resultIndex; i < e.results.length; ++i) {
                if (e.results[i].isFinal) {
                    value += e.results[i][0].transcript;
                }
            }
            if (value != "") {
                document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
            }
        };
        recognition.start();
    """))

    

    # Handle the event triggered by the custom JS and get the result
    result = streamlit_bokeh_events(stt_button, key="listen",events="GET_TEXT", refresh_on_update=False,override_height=75,debounce_time=0)

    if result:
        if "GET_TEXT" in result:
            # st.write("You said: ", result.get("GET_TEXT"))
            response=generate_response(result.get("GET_TEXT"))
            file=TTS(response)
            autoplay_audio(file)
            

if __name__ == "__main__":
    main()
