from groq import Groq


class LLM:

    def __init__(self):
        self.client = Groq()

    def generate(self, prompt):

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content