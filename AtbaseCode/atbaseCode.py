def atbashCipher(text: str) -> str:
	def translate(char):
		if char.isalpha():
			offset = 65 if char.isupper() else 97
			return chr(offset + (25 - (ord(char) - offset)))
		return char
	return ''.join(translate(c) for c in text)