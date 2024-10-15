from AtbaseCode import atbashCipher


def encode(text):
	return atbashCipher(text)


def decode(text):
	return atbashCipher(text)


def main():
	process = input("Choose encode/ decode: ")
	if process == 'encode':
		plainText = input("Enter a plain text: ")
		print(encode(plainText))
	if process == 'decode':
		plainText = input("Enter a encoded text: ")
		print(decode(plainText))


if __name__ == "__main__":
	main()
