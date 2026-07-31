"""sitama"""

witpuen = int(input())
situp = int(input())
luknang = int(input())
run = int(input())

witpuen_inday = int(input())
situp_inday = int(input())
run_inday = int(input())
luknang_inday = int(input())

#สูตรคืออออ(เป้าหมาย + ทำได้ต่อวัน - 1) // ทำได้ต่อวัน ลบหนึ่งเพื่อกันเลขหารลงตัว
solu_witpuen = (witpuen + witpuen_inday - 1) // witpuen_inday
solu_situp = (situp + situp_inday - 1) // situp_inday
solu_luknang = (luknang + luknang_inday - 1) // luknang_inday
solu_run = (run + run_inday - 1) // run_inday

day_max = max(solu_witpuen,solu_situp,solu_luknang,solu_run)

print(day_max)
