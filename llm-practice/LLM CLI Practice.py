from google import genai
from google.genai import types, errors

client = genai.Client()

system_prompt = """
你是病理檢驗部研究助理的 AI 文件整理助手。
請用清楚、簡短、專業但不艱深的方式回答。

規則：
1. 只能根據使用者提供的內容整理。
2. 不要自行補充使用者沒有提到的事實。
3. 如果需要推測，請明確標示「可能方向」。
4. 回答時請盡量條列，方便閱讀。
"""

while True:
    try:
        user_prompt = input("請輸入要詢問的問題：（輸入 q 可以離開程式）").strip()

        if user_prompt == "":
            print("你沒有輸入內容，請重新輸入。")
            continue

        if user_prompt == "q":
            print("結束工具")
            break

        response = client.models.generate_content(    #請 API 操作員，去使用模型功能，產生內容。
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(       #從type裡面找 產生要給Gemini內容的設定表
                system_instruction=system_prompt
            ),
            contents=user_prompt                      # 最終會把model、contents、config包裝成API request送給AI
        )          

        print("\nAI 答案:")
        print(response.text)

    except errors.APIError as e:
        print("\nAPI 呼叫失敗。")
        print("錯誤代碼:", e.code)
        print("錯誤訊息:", e.message)
        print("請檢查 API key、模型名稱、網路連線或使用額度。")

    except KeyboardInterrupt:
        print("\n偵測到 Ctrl + C，中止程式。")
        break

    except Exception as e:
        print("\n發生未預期的錯誤。")
        print("錯誤內容:", e)