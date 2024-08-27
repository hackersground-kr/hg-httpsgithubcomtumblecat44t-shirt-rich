import os
from flask import Flask, request, jsonify
from openai import AzureOpenAI
from flask_cors import CORS

# 환경 변수 로드
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# CORS 설정
CORS(app)  # 모든 도메인에 대해 CORS 허용

# Azure OpenAI API 설정
ENDPOINT = "https://polite-ground-030dc3103.4.azurestaticapps.net/api/v1"
API_KEY = os.getenv("API_KEY")
API_VERSION = "2024-02-01"
MODEL_NAME = "model-gpt4o-20240513"

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

# 설정을 저장할 변수
setting = ""

def get_openai_chat(setting, question):
    MESSAGES = [
        {"role": "system", "content": f"""당신은 '{setting}'라는 정서를 가진 사람입니다. 그 정서와 말투를 카피하여 대답하시오."""},
        {"role": "user", "content": question},
    ]
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=MESSAGES,
    )
    return completion.choices[0].message.content

def get_openai_response(question, context):
    MESSAGES = [
        {"role": "system", "content": "다음 일기를 읽는 사람과 일기를 쓴사람과의 관계를 예측하고 일기 속 사람의 나이나 생각, 정서를 추론 하시오 ."},
        {"role": "user", "content": f"""
        다음 일기를 읽는 사람과 일기를 쓴사람과의 관계를 예측하고 일기 속 사람의 나이나 생각, 정서를 추론 하시오 또한 GPT 가 말 대답할때 꼭 설명의 말투까지도 따라 해서 일기속 사람과 함께 같이 있다는 느낌이 들도록 만들어줘 절대로 GPT 특유의 말투가 나와선 안되고 일기속 말투를 따라해야해 특유의 말투까지 GPT 가 이해하도록 잘설명해야해 그리고 또한 답변에 이스케이프 문자를 절대로 포함 시켜서는 안돼 말투를 학습하고 실제 일기를 쓴사람으로 빙의를 하는것을 첫번째 목표로 해야해.
        ===
        {question}
        ===
        """},
    ]
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=MESSAGES,
    )
    return completion.choices[0].message.content

@app.route('/', methods=['GET'])
def index():
    return "djfkdajdfjkafjkda"

@app.route('/chat', methods=['POST'])
def chat():
    global setting
    if request.is_json:
        data = request.get_json()
        question = data.get("question", "")

        if not question:
            return jsonify({"error": "No question provided"}), 400

        # OpenAI API를 사용해 답변을 얻기
        answer = get_openai_chat(setting, question)
        setting = answer  # Update setting with the new response

        return jsonify({"question": question, "answer": answer})
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/ask', methods=['POST'])
def ask():
    global setting
    if request.is_json:
        data = request.get_json()
        question = data.get("question", "")

        if not question:
            return jsonify({"error": "No question provided"}), 400

        # OpenAI API를 사용해 답변을 얻기
        answer = get_openai_response(question, setting)
        setting = answer  # Update setting with the new response

        return jsonify({"question": question, "answer": answer})
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
