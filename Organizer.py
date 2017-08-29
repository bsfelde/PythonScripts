import os, shutil

path = 'C:/Users/bsfelde/Desktop/'
dest = 'C:/Users/bsfelde/OneDrive for Business'

for f in os.listdir(path):
	f_name, f_ext = os.path.splitext(f)
	if 'm-' in f_name.lower():
		shutil.move((path+f), ( dest + '/UPS/' + f))
	elif f_ext in ('.txt','.FEDS','.EDI','.dat','.edi','.xml'):
		if any(x.isdigit() for x in f_name):
			shutil.move((path+f), (dest + '/RawData/' + f))
	elif f_ext in ('.csv','.xls','.xlsx'):
		shutil.move((path+f), (dest + '/ExcelFiles/' + f))
	elif f_ext in ('.pdf','.txt','.jpg','.htm','.html','.doc','.docx'):
		shutil.move((path+f), (dest + '/Attachments/' + f))
	elif f_ext in ('.cer','.crt'):
		shutil.move((path+f), (dest + '/AS2/' + f))
	elif f_ext == '.msg':
		shutil.move((path+f), ('C:/Users/bsfelde/Desktop/Email Chains/' + f))
	elif f_ext == '.png':
		shutil.move((path+f), ('C:/Users/bsfelde/Desktop/Screenshots/' + f))
