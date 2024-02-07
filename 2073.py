class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        while tickets[k]!=0:
            for i in range(len(tickets)):
                if tickets[k]==0:
                    break
                if(tickets[i]!=0):
                    tickets[i]-=1
                    count+=1
            print(tickets)
        return count