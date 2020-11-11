from PIL import Image
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
		file_new = file_old.replace('.', '-new.')
		img = Image.open(file_old)

		try:
			# Save the compressed image
			img.save(file_new, quality = 50, optimize = True)
			input('Your image compressed successfully :)')

		except:
			# If unable to save compressed image
			input('Failed to compress :(')

	except:
		# If unable to import image
		input('Failed to import image :(')

	finally:
		app() # Run the app again


# Run the app
app()
