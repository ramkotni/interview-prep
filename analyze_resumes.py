from docx import Document

files = [
    (r'C:\RamKotni\Personal\interview-prep\resumework\Ram Mohan Kotni-Java-FullStack Lead.docx', 'JAVA RESUME'),
    (r'C:\RamKotni\Personal\interview-prep\resumework\Mohan Kotni-Python-FullStack Lead.docx', 'PYTHON RESUME'),
    (r'C:\RamKotni\Personal\interview-prep\resumework\Ram-Kotni-AgilePLM.docx', 'AGILE PLM RESUME'),
]

print("\n" + "="*90)
print("CURRENT RESUME TITLES AND ROLES ANALYSIS")
print("="*90)

for file_path, label in files:
    try:
        doc = Document(file_path)
        print(f"\n{label}:")
        print("-" * 90)

        for i, para in enumerate(doc.paragraphs[:20]):
            if para.text.strip():
                text = para.text.strip()
                # Show title and role lines
                if any(x in text.lower() for x in ['senior', 'full stack', 'java', 'python', 'engineer', 'developer', 'architect', 'lead']):
                    print(f"  {text[:100]}")
    except Exception as e:
        print(f"  Error: {e}")

print("\n" + "="*90)
print("RECOMMENDATION")
print("="*90)
print("""
For ATS systems and broad applicability:
✓ "Senior Full Stack Engineer" - MORE RECOMMENDED
  - Broader appeal to recruiters
  - Works for Java, Python, .NET, or any stack
  - Professional and modern terminology
  - Matches ATS keyword search patterns
  - Not tool-specific (Java/Python/etc)

vs

✗ "Senior Java Full Stack Engineer" - LESS RECOMMENDED
  - Limits you to Java-focused roles
  - Python resume would conflict with Java title
  - May get filtered out for non-Java positions
  - More niche positioning

RECOMMENDATION: Use "Senior Full Stack Engineer" for all resumes for maximum reach
""")

