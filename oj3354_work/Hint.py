"""Hint"""

def check_symbol(symbol, val , target):
    """checkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"""
    if symbol == "==":
        return val == target
    if symbol == ">":
        return val > target
    if symbol == "<":
        return val < target
    if symbol == "<=":
        return val <= target
    if symbol == ">=":
        return val >= target
    if symbol == "!=":
        return val != target
    return False


symbol_nuai,nuai = input().split()
symbol_sib,sib = input().split()
symbol_roi,roi = input().split()
nuai = int(nuai)
sib = int(sib)
roi = int(roi)
for rakroi  in range(10):
    if check_symbol(symbol_roi, rakroi, roi):
        for raksib in range(10):
            if check_symbol(symbol_sib,raksib,sib):
                for raknuai in range(10):
                    if check_symbol(symbol_nuai,raknuai,nuai):
                        print(f"{rakroi}{raksib}{raknuai}")
