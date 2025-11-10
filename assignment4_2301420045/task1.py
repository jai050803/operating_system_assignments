import subprocess
scripts = ['1.py', '2.py', '3.py']

for s in scripts:
	print(f"executinng {s}....")
	subprocess.call(['python3', s])

