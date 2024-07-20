# Adjective, noun, verb, place

adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
verb = input("Enter a verb: ")
problem = input("Enter a problem, something that goes wrong: ")

# print('------------------------------')
# print("Hariet was a " + adjective + " young girl. She lived in " + place + " and found life beatiful and enjoyable. But one day " + problem + " and her life was never the same again. To fix this terrible situation she " + verb + ", which solved all her issues and she lived happily ever after.")
# print('------------------------------')

# String interpolation
print('------------------------------')
print(f'Hariet was a {adjective} young girl. She lived in {place} and found life beautiful and enjoyable. But one day {problem} and her life was never the same again. To fix this terrible situation she {verb} which solved all her issues and she lived happily ever after.')
print('------------------------------')