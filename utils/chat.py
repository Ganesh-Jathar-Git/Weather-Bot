import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
load_dotenv()

# Use of environment variables
API_KEY=os.getenv("IBM_API_KEY")
PROJECT_ID=os.getenv("IBM_PROJECT_ID")
MODEL_ID=os.getenv("MODEL_ID")
URL=os.getenv("URL")

# Set up IBM watsonx credentials
credentials = Credentials(
    url=URL,
    api_key=API_KEY,
)

#Function to generatate the suggestion on the basis of weather condition.
def generate_suggestion(text, weather):
    prompt = f"""
            ユーザーの発言:「{text}」
            現在の天気情報: {weather}

        この情報に基づいて、以下の中から最大3つ、100文字以内で親しみやすく実用的な提案をMarkdown形式で返してください。

        【視点の例】
        ・旅行やおでかけのおすすめ
        ・今日のファッション
        ・気分に合う音楽
        ・屋外作業や運動のヒント

        【条件】
        - 出力はMarkdown形式で、**箇条書きのみ**（*や・）を使ってください。
        - セクションタイトルや天気情報は**出力しないでください**。
        - 内容に応じて適切な絵文字（🌂👕☀️など）を入れてください。
        - 丁寧でポジティブな日本語を使ってください。
        """

    params = TextChatParameters(temperature=0.7)
    model = ModelInference(
        model_id=MODEL_ID,
        credentials=credentials,
        project_id=PROJECT_ID,
        params=params,
    )

    messages = [
        {
            "role": "system",
            "content": "あなたは日本語で丁寧に対応する天気チャットボットです。天気とユーザーの言葉から、役立つアイデアや提案をします。旅行、音楽、農業、ファッション、スポーツなど、自由に発想してください.",
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]

    try:
        response = model.chat(messages=messages)
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"


#Function to extract the City from transcript.
def extract_city(transcript: str) -> str:
    prompt = f"""
以下の日本語の発話から、話し手が言及している都市または地域名を一つだけ抽出してください。
発話に複数の地名が含まれている場合は、最も関連性が高いものを選んでください。
存在しない場合は「不明」と返してください。

発話: 「{transcript}」
出力（都市名のみ）:
"""
    params = TextChatParameters(temperature=0.0)
    model = ModelInference(
        model_id=MODEL_ID,
        credentials=credentials,
        project_id=PROJECT_ID,
        params=params,
    )

    messages = [
        {
            "role": "system",
            "content": (
                "あなたは日本語の発話から都市または地域名を正確に抽出するAIです。"
                "必ず1つだけ、日本語で都市名または地域名のみを出力してください。"
                "都市が存在しない場合は「不明」と返してください。"
            ),
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]

    try:
        response = model.chat(messages=messages)
        city = response["choices"][0]["message"]["content"].strip()

        # Checking the ambigious values
        if city in ["不明", "", "なし", "無し"]:
            return "東京"  # fallback city
        return city

    except Exception as e:
        return city if city != "不明" and city != "" else "東京"  # fallback on failure



