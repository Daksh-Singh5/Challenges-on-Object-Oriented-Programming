class Number:
    def __init__(self, num):
        self.num = int(num)

    def makeroman(self):
        if self.num > 3000:
            return "Too Big"
        
        roman_numerals = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV",
            1: "I"
        }

        roman = ""
        number = self.num
        
        for value, symbol in roman_numerals.items():
            while number >= value:
                roman += symbol
                number -= value
        
        return roman


num = Number(3125)
print(num.makeroman())

num2 = Number(1987)
print(num2.makeroman())
