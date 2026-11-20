
import io
import streamlit as st
from pypdf import PdfReader, PdfWriter

st.set_page_config(
    page_title="PDF Tools",
    page_icon="📄"
)

st.title("📄 PDF Tools")
st.write("Объединяйте PDF-файлы бесплатно и просто.")

files = st.file_uploader(
    "Выберите PDF-файлы",
    type=["pdf"],
    accept_multiple_files=True
)

if files:
    st.success(f"Выбрано файлов: {len(files)}")

    if st.button("Объединить PDF"):
        try:
            writer = PdfWriter()

            for file in files:
                reader = PdfReader(file)
                writer.append(reader)

            output = io.BytesIO()
            writer.write(output)
            writer.close()
            output.seek(0)

            st.download_button(
                "📥 Скачать объединённый PDF",
                data=output.getvalue(),
                file_name="merged.pdf",
                mime="application/pdf"
            )

        except Exception as error:
            st.error(f"Ошибка: {error}")
