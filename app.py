import zipfile, os, py7zr

targetDir = input('Target Directory: ')
outputDir = input('Output Directory: ')

extensions = ['tar', 'zip', '7z']
files = []

for f in os.listdir(targetDir):
    if not os.path.isdir(f):
        if f.split('.')[-1] in extensions:
            files.append(f)

for i in files:
    print(f'Extracting file "{i}" to "{outputDir}\{i.split(".")[0]}"...')
    os.mkdir(f'{outputDir}\{i.split(".")[0]}')
    if i.split('.')[-1] == '7z':
        archive = py7zr.SevenZipFile(f'{targetDir}/{i}', mode='r')
        archive.extractall(path=f'{outputDir}\{i.split(".")[0]}')
        archive.close()
    else:
        with zipfile.ZipFile(f'{targetDir}\{i}', 'r') as zip_ref:
            zip_ref.extractall(f'{outputDir}\{i.split(".")[0]}')

print('\n[+] Complete')