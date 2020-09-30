from PIL import Image
import os


def mskf():
	print('                       _')
	print('  /\\    /\\    /  | /  |_')
	print(' /  \\  /  \\   \\  ||   | ')
	print('/    \\/    \\  /  | \\  | ')
	print('\n@mskf1383 - A programmer\nfrom the Depths of Mars!')
	print('========================\n')


def clean_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
	

def app():
	clean_screen()
	mskf()
	
	try:
		file_old = input('Enter the image adress: ')
		file_new = file_old.replace('.', '-new.')
		img = Image.open(file_old)
		
		try:
			img.save(file_new, quality = 50, optimize = True)
			
			input('Your image compressed successfully :)')
			app()

		except:
			input('Failed to compress :(')
			app()
		
	except:
		input('Failed to import image :(')
		app()
		

app()