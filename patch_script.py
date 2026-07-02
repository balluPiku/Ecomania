with open('rewrite.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'subprocess.run("git add .", shell=True, env=env)' in line:
        lines.insert(i, '    for file in ["README.md", "rewrite.py"]:\n')
        lines.insert(i+1, '        if os.path.exists(file):\n')
        lines.insert(i+2, '            with open(file, "r", encoding="utf-8") as f_in:\n')
        lines.insert(i+3, '                content = f_in.read()\n')
        lines.insert(i+4, '            content = content.replace("balluPiku", "npmPiku")\n')
        lines.insert(i+5, '            content = content.replace("1DGs1FJkQv92l0KSO9_2AL2ErFeUzG7azgun6IxEi2Mo/edit?resourcekey=&gid=102589315#gid=102589315", "19s8gVCqncAzV8rcIwnVstIrMQqYzoFJ5i2p4W_nkFHM/edit?resourcekey=&gid=5844705#gid=5844705")\n')
        lines.insert(i+6, '            content = content.replace("FxmR3DPuoe9BL16H9", "pHLXcMchAnkkSvTp8")\n')
        lines.insert(i+7, '            content = content.replace("1-HqwHpPZG6L2Mtc5MLacA-vG5XbyGpbN", "1FMNFB31QNM97Mooi18i8DbcesmzMgpkw")\n')
        lines.insert(i+8, '            with open(file, "w", encoding="utf-8") as f_out:\n')
        lines.insert(i+9, '                f_out.write(content)\n')
        break

with open('rewrite.py', 'w') as f:
    f.writelines(lines)
