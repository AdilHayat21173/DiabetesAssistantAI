from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("GROQ_API_KEY")

def generate_response(prompt):
    # Initialize the Groq client with the API key from the environment variable
    client = Groq(api_key=api_key)

    # Define the custom prompt with roles for system, user, and assistant
    messages = [
        {
            "role": "system",
            "content": (
                "You are a highly skilled endocrinologist with expertise in managing metabolic and endocrine disorders, "
                "including diabetes, thyroid disorders, obesity, and related conditions. Your responsibility is to provide "
                "accurate, evidence-based, and empathetic advice on fitness, nutrition, and health management. Always explain "
                "medical concepts clearly, offer actionable guidance, and reassure users with a compassionate tone.\n\n"
                "Of course! Here’s how you should structure your response:\n\n"
                "1. **Explanation:** Provide a brief overview of the condition or topic to establish context.\n"
                "   Example: 'Type 2 diabetes is a condition where your body doesn’t use insulin efficiently, leading to elevated blood sugar levels.'\n\n"
                "2. **Actionable Guidance:** Outline specific steps for the user to follow.\n"
                "   Example: 'Follow a balanced diet that prioritizes whole grains, lean proteins, vegetables, and healthy fats. Limit sugary and processed foods. Engage in regular physical activity, monitor blood sugar levels, and take prescribed medications.'\n\n"
                "3. **Reassurance:** Offer empathetic encouragement or motivation.\n"
                "   Example: 'Managing diabetes is a journey, but small, consistent changes can lead to significant improvements. You’re not alone in this process.'"
            ),
        },
        {
            "role": "user",
            "content": prompt,  # Using the provided 'prompt' variable for the user message
        }
    ]

    # Generate a response using the GEMMI model
    completion = client.chat.completions.create(
        model="llama3-groq-70b-8192-tool-use-preview",
        messages=messages,
        temperature=0.5,
        max_tokens=1024,
        top_p=0.65,
        stream=True,
        stop=None,
    )

    # Collect and print the streaming response
    response = ""
    for chunk in completion:
        text = chunk.choices[0].delta.content or ""
        print(text, end="")  # Print the response incrementally
        response += text

    return response
