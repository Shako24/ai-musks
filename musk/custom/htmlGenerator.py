from airium import Airium

a = Airium()
# Generating HTML file
with a.h1():
    a("HTML Generated")
# Casting the file to a string to extract the value
outputTemplate = str(a)