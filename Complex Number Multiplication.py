class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_r, num1_im = num1.split("+")
        num2_r, num2_im = num2.split("+")

        product1 = int(num1_r) * int(num2_r)
        product2 = int(num1_r) * int(num2_im[:-1])
        product3 = int(num1_im[:-1]) * int(num2_r)
        product4 = -1 * int(num1_im[:-1]) * int(num2_im[:-1])

        sum_r = product1 + product4
        sum_im = product2 + product3

        result = str(sum_r)+"+"+str(sum_im)+"i"

        return result
