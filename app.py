import openai
from flask import Flask, render_template, request

app = Flask(teste_GPT)

# Insira aqui a sua chave secreta da API OpenAI
openai.api_key = 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

# Defina aqui o modelo do OpenAI que você quer usar
model_engine = "davinci"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    user_message = request.args.get('msg')
    response = openai.Completion.create(
        engine=model_engine,
        prompt=f"Me: {user_message}\nChatbot:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )
    bot_message = response.choices[0].text.strip()
    return str(bot_message)

if __name__ == '__main__':
    app.run()
