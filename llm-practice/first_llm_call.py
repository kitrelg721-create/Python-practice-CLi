from google import genai

client = genai.Client() #透過操作員和gemini溝通

response = client.models.generate_content(
    model="gemini-2.5-flash",#用哪個模型
    contents="請用三句話解釋：什麼是大型語言模型？"#送給模型的任務
)

print(response.text)#把答案印到終端機
#之後在終端機上叫python執行我的py檔
