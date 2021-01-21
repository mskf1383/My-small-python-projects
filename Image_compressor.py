"""by MSKF"""


from PIL import Image, UnidentifiedImageError
import os


def mskf():
	print('                       _')
	print('  /\\    /\\    /  | /  |_')
	print(' /  \\  /  \\   \\  ||   |')
	print('/    \\/    \\  /  | \\  |')
	print('\n@mskf1383 - A programmer\nfrom the Depths of Mars!')
	print('========================\n')


def clean_screen():
	os.system('cls' if os.name == 'nt' else 'clear')


# The app
def app():
	clean_screen()
	mskf()

	try:
		# Get the image
		file_old = input('Enter the image adress: ')
		file_new = file_old.replace('.', '-compressed.')
		img = Image.open(file_old)

		# Save the compressed image
		img.save(file_new, quality=50, optimize=True)
		input('Your image compressed successfully :)')

	# If unable to import image
	except FileNotFoundError:
		input('Failed to import image :(')

	# If unable to save compressed image
	except UnidentifiedImageError:
		input('Failed to compress :(')

	finally:
		app() # Run the app again


# Run the app
app()
