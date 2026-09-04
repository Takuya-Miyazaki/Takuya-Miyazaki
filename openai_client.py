import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# 1. 安全な環境変数の読み込み
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
org_id = os.getenv("OPENAI_ORG_ID")
project_id = os.getenv("OPENAI_PROJECT_ID")

# ガバナンス：必須チェック（キーが無い場合は即座に安全に停止させる）
if not api_key or api_key == "sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx":
    print("[ERROR] 有効な OPENAI_API_KEY が設定されていません。.env ファイルを確認してください。", file=sys.stderr)
    sys.exit(1)

# 2. クライアントの初期化（タイムアウトと自動再試行の設定）
# 技術：通信エラー時に最大2回まで自動でリトライし、15秒でタイムアウトさせます
openai_client = OpenAI(
    api_key=api_key,
    organization=org_id,
    project_id=project_id,
    timeout=15.0,
    max_retries=2
)

# 3. ガバナンス：安全なデータ送信関数の定義
def safe_chat_completion(messages, model="gpt-4o-mini", max_tokens=1024):
    """
    セキュリティと予算管理（トークン制限）を考慮した、安全なテキスト生成関数。
    個人情報や機密データ（PII）の送信を事前に検知するフィルタをここに挟むことも可能です。
    """
    try:
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.2, # 技術：出力のブレを抑え、ガバナンス（再現性）を高めるため低めに設定
        )
        return response
    except Exception as e:
        print(f"[API ERROR] 接続または処理中にエラーが発生しました: {e}", file=sys.stderr)
        return None
