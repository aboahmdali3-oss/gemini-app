import google.generativeai as genai

# 1. إعداد المفتاح
genai.configure(api_key="AIzaSyC...") # مفتاحك موجود بالفعل في الملف

# 2. اختيار النموذج (جربنا gemini-pro لضمان التوافق)
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # 3. إرسال السؤال
    print("جاري الاتصال بالذكاء الاصطناعي...")
    response = model.generate_content("أهلاً جيمناي، أنا علي مبرمج وتاجر، هل تسمعني؟")
    
    print("-" * 20)
    print("رد الذكاء الاصطناعي:")
    print(response.text)
    print("-" * 20)

except Exception as e:
    print(f"حدث خطأ تقني: {e}")
    print("نصيحة: تأكد من تحديث المكتبة أو تجربة نموذج 'gemini-pro'")