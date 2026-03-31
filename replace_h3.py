import os
import re

dir_path = r"c:\Users\user\Desktop\THINK-IN\IYRP_2026\WEB IYRP2026"

replace_es = """<h3 style="font-weight: normal; line-height: 1.5; margin-bottom: 20px;">Te damos la bienvenida a Celebrating The International Year Of Rangelands<br>
And Pastoralists 2026 :<br>
Madrid International Meeting<br>
Young Pastoralists & New Technologies</h3>"""

replace_en = """<h3 style="font-weight: normal; line-height: 1.5; margin-bottom: 20px;">Welcome to Celebrating The International Year Of Rangelands<br>
And Pastoralists 2026 :<br>
Madrid International Meeting<br>
Young Pastoralists & New Technologies</h3>"""

replace_fr = """<h3 style="font-weight: normal; line-height: 1.5; margin-bottom: 20px;">Bienvenue au Celebrating The International Year Of Rangelands<br>
And Pastoralists 2026 :<br>
Madrid International Meeting<br>
Young Pastoralists & New Technologies</h3>"""

for filename in os.listdir(dir_path):
    if filename.endswith(".html"):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if filename.endswith("_en.html"):
            new_content = re.sub(r"<h3>\s*Welcome to Celebrating.*?</h3>", replace_en, content, flags=re.IGNORECASE|re.DOTALL)
        elif filename.endswith("_fr.html"):
            new_content = re.sub(r"<h3>\s*Bienvenue au Celebrating.*?</h3>", replace_fr, content, flags=re.IGNORECASE|re.DOTALL)
        else:
            new_content = re.sub(r"<h3>\s*Te damos la bienvenida a Celebrating.*?</h3>", replace_es, content, flags=re.IGNORECASE|re.DOTALL)

        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filename}")
