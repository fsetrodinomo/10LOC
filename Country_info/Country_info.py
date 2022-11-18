from countryinfo import CountryInfo
count = input ("Enter your country : ")
country = CountryInfo(count)
print("Capital is : ", country.capital())
print("Currencies is : ", country.currencies())
print("Languages is : ", country.languages())
print("Borders is : ", country.borders())
print("Other names is : ", country.alt_spellings())