class Solution:
    def helper(self, num: int) -> str:
        print(num)
        if num >= 1000000000:
            if (num%1000000000==0):
                return self.process3digits(num//1000000000) + ' Billion'
            return self.process3digits(num//1000000000) + ' Billion ' + self.helper(num%1000000000)
        elif num >= 1000000:
            if (num%1000000==0):
                return self.process3digits(num//1000000) + ' Million'
            return self.process3digits(num//1000000) + ' Million ' + self.helper(num%1000000)
        elif num >= 1000:
            if (num%1000==0):
                return self.process3digits(num//1000) + ' Thousand'
            return self.process3digits(num//1000) + ' Thousand ' + self.helper(num%1000)
        return self.process3digits(num)
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        return self.helper(num)
    def process3digits(self, num):
        one_digit = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        
        tens = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        if num <= 19:
            return one_digit[num]
        elif num <= 99:
            if num%10==0:
                return tens[num // 10]
            return tens[num // 10] + ' ' + one_digit[num % 10]
        return one_digit[num//100] + ' Hundred' if (num%100==0) else one_digit[num//100] + ' Hundred ' + self.process3digits(num % 100)
        