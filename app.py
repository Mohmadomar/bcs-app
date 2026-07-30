bcs-app
Repository navigation
Code
Issues
Pull requests
bcs-app
/app.py
Mohmadomar
Mohmadomar
23 minutes ago
77 lines (62 loc) · 3.76 KB

Code

Blame
import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. إعداد الصفحة
st.set_page_config(
    page_title="نظام تقييم BCS للأبقار",
    page_icon="🐄",
    layout="wide"
)

# 2. إدخال مفتاح API الخاص بـ Gemini
st.sidebar.header("⚙️ الإعدادات")
api_key = st.sidebar.text_input("أدخل API Key لـ Gemini:", type="password")

# 3. عرض المرجع البصري في الشريط الجانبي
st.sidebar.markdown("---")
st.sidebar.header("📚 مرجع تقييم الـ BCS")
st.sidebar.info("""
**مقياس التقييم (1 - 5):**
* **BCS 2.0 (نحيفة):** عظام الورك والدبوس بارزة جداً وشكل V حاد عند الذيل.
* **BCS 3.0 (مثالية):** غطاء دهني متوازن، شكل U ناعم عند الذيل، العظام غير حادة.
* **BCS 4.0 (سمينة):** غطاء دهني سميك، منطقة الذيل ممتلئة تماماً.
""")

# 4. الواجهة الرئيسية
st.title("🐄 نظام التقييم الآلي لحالة الجسم (BCS Analyzer)")
st.write("قم برفع صورة جانبية وصورة خلفية للبقرة للحصول على تقييم دقيق ومُصنف.")

col1, col2 = st.columns(2)

with col1:
    side_img_file = st.file_uploader("📸 صورة الجانب (Side View)", type=["jpg", "jpeg", "png"])
    if side_img_file:
        side_img = Image.open(side_img_file)
        st.image(side_img, caption="صورة الجانب", use_column_width=True)

with col2:
    back_img_file = st.file_uploader("📸 صورة الخلف (Rear View)", type=["jpg", "jpeg", "png"])
    if back_img_file:
        back_img = Image.open(back_img_file)
        st.image(back_img, caption="صورة الخلف", use_column_width=True)

st.markdown("---")

# 5. زر التحليل والتقييم
if st.button("🔍 تحليل وبدء التقييم", type="primary"):
    if not api_key:
        st.error("⚠️ يرجى إدخال API Key في الشريط الجانبي أولاً.")
    elif not side_img_file or not back_img_file:
        st.warning("⚠️ يرجى رفع الصورتين (الجانب والخلف) لإتمام التقييم بشكل دقيق.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')

            with st.spinner("جاري تحليل الصور والتقييم..."):
                prompt = """
                أنت خبير متقدم في تقييم حالة الجسم لأبقار الحليب (Body Condition Scoring - BCS).
                أمامك صورتان لنفس البقرة: الأولى من الجانب والثانية من الخلف.

                المطلوب منك:
                1. تقديم تقييم BCS دقيق (برقم محدد أو نطاق ضيق مثل 2.75 - 3.00) بناءً على مقياس 1-5.
                2. توضيح الأسباب والمعالم التشريحية التي بنيت عليها هذا التقييم بالتفصيل (شكل زاوية الحوض V أم U، امتلاء منطقة الذيل، وضوح الضلوع والعمود الفقري).
                3. تقديم توصية تغذية سريعة بناءً على النتيجة.

                اصغ التقرير باللغة العربية بطريقة منظمة باستخدام النقاط والعناوين.
                """

                response = model.generate_content([prompt, side_img, back_img])

                st.success("تم التحليل بنجاح!")
                st.markdown("### 📊 تقرير التقييم:")
                st.markdown(response.text)

        except Exception as e:
            st.error(f"حدث خطأ أثناء التحليل: {e}"
                اصغ التقرير باللغة العربية بطريقة منظمة باستخدام النقاط والعناوين.
                """

                response = model.generate_content([prompt, side_img, back_img])

                st.success("تم التحليل بنجاح!")
                st.markdown("### 📊 تقرير التقييم:")
                st.markdown(response.text)

        except Exception as e:
            st.error(f"حدث خطأ أثناء التحليل: {e}")
