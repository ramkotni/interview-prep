from docx import Document
import os

def fix_all_issues(file_path):
    """Fix years and any remaining issues"""
    try:
        doc = Document(file_path)

        replacements = [
            ('13+ years', '18 years'),
            ('13 years', '18 years'),
            ('16 years', '18 years'),
            ('17 years', '18 years'),
            ('over 13+ years', '18 years of'),
        ]

        updated = False
        for para in doc.paragraphs:
            for old_text, new_text in replacements:
                if old_text in para.text:
                    for run in para.runs:
                        if old_text in run.text:
                            run.text = run.text.replace(old_text, new_text)
                            updated = True

        if updated:
            doc.save(file_path)
            print(f"✓ Fixed: {os.path.basename(file_path)}")
        else:
            print(f"✓ Already correct: {os.path.basename(file_path)}")

        return True

    except Exception as e:
        print(f"✗ Error: {os.path.basename(file_path)} - {str(e)}")
        return False

# All files
files = [
    r"C:\RamKotni\Personal\interview-prep\resumework\Ram Mohan Kotni-Java-FullStack Lead.docx",
    r"C:\RamKotni\Personal\interview-prep\Resume\Ram Mohan Kotni-Java-FullStack Lead.docx",
    r"C:\RamKotni\Personal\interview-prep\resumework\Mohan Kotni-Python-FullStack Lead.docx",
    r"C:\RamKotni\Personal\interview-prep\Resume\Mohan Kotni-Python-FullStack Lead.docx",
    r"C:\RamKotni\Personal\interview-prep\resumework\Ram-Kotni-AgilePLM.docx",
    r"C:\RamKotni\Personal\interview-prep\Resume\Ram-Kotni-AgilePLM.docx"
]

print("Fixing all years to 18 years...\n")

for file_path in files:
    if os.path.exists(file_path):
        fix_all_issues(file_path)

print("\n✓ All issues fixed!")

