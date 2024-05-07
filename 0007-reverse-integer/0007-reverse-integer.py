class Solution:
    
    def reverse(self, x: int) -> int:

        numb = abs(x);
        count = 0
        while numb>0:
            numb=numb//10;
            count = count+1;

        numb=abs(x);
        rev =0
        while count>0:
            count = count-1;
            rev = rev*10+numb%10;
            numb = numb//10
        if (-(2**31)<rev and rev<(2**31)):
            if x<0:return rev*(-1)
            else:return rev
        else:
            return 0
