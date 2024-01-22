import os
import aspose.words as aw

doc = aw.Document("sample.pdf")

for page in range(0, doc.page_count):
    extractedPage = doc.extract_pages(page, 1)
    extractedPage.save(f"Output_{page + 1}.pdf")