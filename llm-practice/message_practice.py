from google import genai    #genai 負責建立 client、呼叫模型；types 負責提供設定用的資料結構。
from google.genai import types  #從 Gemini SDK 裡拿出「設定用的工具」

client = genai.Client()   

system_prompt = """
你是已在醫院的病理檢驗部成功導入AI應用的工程師。
請用清楚、簡短、專業但不艱深的方式回答。
規則：
1. 只能根據使用者提供的內容整理。
2. 不要自行補充使用者沒有提到的效果、優點或結論。
3. 如果需要推測，請明確標示「可能方向」。
4. 請用三個重點回答，每點包含「流程」和「可練習的AI應用方向」。
"""

user_prompt = """
請把以下內容整理成三個可以練習AI導入的小方向：
我目前在病理檢驗部，可能接觸到紙本文件整理、掃片影像資料、實驗室紀錄、會議紀錄。
我希望先從不涉及病人個資、風險較低、可以用假資料練習的方向開始。
請幫我整理出三個適合初學AI工程師練習的題目。
"""

response = client.models.generate_content(    
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(    #模型產生內容時要遵守的規則
        system_instruction=system_prompt
    ),
    contents=user_prompt   #使用者輸入的任務
)

print(response.text)


