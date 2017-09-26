#!flask/bin/python
import json, urllib

han = 0
hon = 0
den = 0
det = 0
denna = 0
denne = 0
hen = 0


data = []


with open("test.json") as j:
	for line in j:
		try:
			line2 = json.loads(line)
			print("*****")
			text = line2['text']
			print(text)
			data.append(text)
			print("****")

			line == "\n"

			if ('han' in text):
				print("han is there")
				han = han + 1

			if ('hon' in text):
				print("hon is there")
				hon = hon + 1

			if ('den' in text):
				print("den is there")
				den = den + 1

			if ('det' in text):
				print("det is there")
				det = det + 1

			if ('denna' in text):
				print("denna is there")
				denna = denna + 1

			if ('denne' in text):
				print("denne is there")
				denne = denne + 1

			if ('hen' in text):
				print("hen is there")
				hen = hen + 1




		except Exception as e:
			print("")


print(data)


wordsArray = [han, hon, den, det, denna, denne, hen]

for word in wordsArray:
	print(word)
