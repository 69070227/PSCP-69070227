"""กระดาษห่อของขวัญ"""
def main():
    """main"""
    r,h,glue = map(float,(input().split()))

    solu_Yao = (2 * 3.14 * r) + glue #บวกหนึ่งไว้ทากาว
    solu_Guang = h + r + r
    print(f"{solu_Guang:.2f} {solu_Yao:.2f}")

main()
