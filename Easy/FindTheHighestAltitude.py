class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altura = 0
        i = 0
        maior = 0
        while i <  len(gain):
            altura = altura + gain[i]
            if altura > maior:
                maior = altura
                i = i+1
            else:
                i = i+1 
        print(maior)
        return (maior)