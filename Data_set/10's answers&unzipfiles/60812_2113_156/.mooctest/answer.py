class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        d1 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
              'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
        d2 = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        if num == 0: return 'Zero'
        if num <= 20: return d1[num]
        if num < 100:
            t, d = num // 10, num % 10
            return d2[t] + ' ' + d1[d] if d > 0 else d2[t]

        if num < 1000:
            h = num // 100
            if num % 100 == 0: return d1[h] + ' Hundred'
            return d1[h] + ' Hundred ' + self.numberToWords(num % 100)

        if num < 10 ** 6:
            th = num // 10 ** 3
            if num % 10 ** 3 == 0:
                return self.numberToWords(th) + ' Thousand'
            return self.numberToWords(th) + ' Thousand ' + self.numberToWords(num % 10 ** 3)

        if num < 10 ** 9:
            mi = num // 10 ** 6
            if num % 10 ** 6 == 0:
                return self.numberToWords(mi) + ' Million'
            return self.numberToWords(mi) + ' Million ' + self.numberToWords(num % 10 ** 6)

        if num < 10 ** 12:
            bi = num // 10 ** 9
            if num % 10 ** 9 == 0:
                return d1[num // 10 ** 9] + ' Billion'
            return self.numberToWords(bi) + ' Billion ' + self.numberToWords(num % 10 ** 9)
a = input()
s = Solution()
print(s.numberToWords(int(a)))