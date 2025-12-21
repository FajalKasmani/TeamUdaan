import os
from dotenv import load_dotenv
from google import genai # Nayi library

# 1. Environment Load karo
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

print("------------------------------------------------")
print("🔍 DIAGNOSTIC TEST STARTED")
print("------------------------------------------------")

# 2. Check karo Key mili ya nahi
if not api_key:
    print("❌ ERROR: API Key NOT FOUND!")
    print("👉 Check kariye ki '.env' file 'app.py' ke bagal mein hai ya nahi.")
    print("👉 Check kariye ki file ka naam sirf '.env' hai (koi .txt nahi).")
else:
    print(f"✅ API Key Found: {api_key[:5]}...*******")
    
    # 3. Agar Key hai, to Call try karo
    try:
        print("🚀 Sending request to Google Gemini...")
        client = genai.Client(api_key=api_key)
        
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents="Write a funny haiku about coding."
        )
        print("\n🎉 SUCCESS! REPLY FROM GOOGLE:")
        print(response.text)
        print("------------------------------------------------")
        print("✅ Conclusion: API mast chal rahi hai. App restart karo.")
        
    except Exception as e:
        print("\n❌ API CONNECTION FAILED!")
        print(f"Error Details: {e}")
        print("------------------------------------------------")
        print("👉 Agar error '404' hai -> Model name galat hai.")
        print("👉 Agar error '401' hai -> API Key galat hai.")