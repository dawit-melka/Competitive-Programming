class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        res = []

        for domain in cpdomains:
            [rep, dom] = domain.split()
            while dom:
                if dom in count:
                    count[dom] += int(rep)
                else:
                    count[dom] = int(rep)
                idx = dom.find(".")
                if idx == -1:
                    break
                dom = dom[idx+1:]
        
        for key in count:
            temp = str(count[key])+" "+key
            res.append(temp) 
        
        return res
