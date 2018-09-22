import re

print('')
print('')

# Read File:
with open('/Users/martin/Haushaltsbuch/Konto/2018_05.csv','r',errors='replace') as fileKontoCsv:
    content = fileKontoCsv.readlines()

    content = [x.strip() for x in content] #remove whitespace and line breaks


#print(content)


# Find and remove Header
lineNumber = 0
lineHeaderEnd = 0
for line in content:
	result = re.match('\"Buchungstag.*', line)
	if result:
		lineHeaderEnd=lineNumber
	lineNumber+=1

content=content[lineHeaderEnd+1:lineNumber]


class KontoEintrag():
	def __init__(self,buchungstag, auftraggeber, verwendungszweck, betrag):
		self.buchungstag=buchungstag
		self.auftraggeber=auftraggeber
		self.verwendungszweck = verwendungszweck
		betrag = betrag.replace('.','')
		betrag = betrag.replace(',','.')
		betrag = betrag.replace('\"','')
		self.betrag = float(betrag)

		if self.betrag > 0:
			self.art = 'Einnahme'
		else:
			self.art = 'Ausgabe'

	def __str__(self):
		return  'Buchungstag: '+ self.buchungstag +' Auftraggeber: '+ self.auftraggeber + ' Verwendungszweck: '+ self.verwendungszweck + ' Betrag: '+ str(self.betrag)

kontoeintraege=[]

for line in content:
	entries = line.split(';')
	#print('Buchungstag: '+ entries[0] +' Auftraggeber: '+ entries[3])
	#print('Verwendungszweck: '+entries[4] + ' Betrag: '+entries[7])

	kontoeintraege.append(KontoEintrag(entries[0], entries[3],entries[4],entries[7]))


print('')
print('Einnahmen:')
summeEinnahmen = 0
for entry in kontoeintraege:
	if entry.art == 'Einnahme':
		#print(entry)
		summeEinnahmen += entry.betrag

print('Summe Einnahmen: ' + str(summeEinnahmen))


print('')
print('Ausgaben:')
summeAusgaben = 0
for entry in kontoeintraege:
	if entry.art == 'Ausgabe':
		#print(entry)
		summeAusgaben += entry.betrag

print('Summe Ausgaben: ' + str(summeAusgaben))


