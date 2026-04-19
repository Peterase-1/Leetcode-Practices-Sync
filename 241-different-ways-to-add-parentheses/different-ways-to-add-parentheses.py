class Solution(object):
    def diffWaysToCompute(self, expression):
        memo = {}
        
        def solve(expr):
            if expr in memo:
                return memo[expr]
            
            res = []
            
            for i, ch in enumerate(expr):
                if ch in '+-*':
                    left = solve(expr[:i])
                    right = solve(expr[i+1:])
                    
                    for l in left:
                        for r in right:
                            if ch == '+':
                                res.append(l + r)
                            elif ch == '-':
                                res.append(l - r)
                            else:  # '*'
                                res.append(l * r)
            
            if not res:
                res.append(int(expr))
            
            memo[expr] = res
            return res
        
        return solve(expression)