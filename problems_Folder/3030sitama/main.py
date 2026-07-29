"""sitama"""

witpuen = int(input())
situp = int(input())
luknang = int(input())
run = int(input())

witpuen_inday = int(input())
situp_inday = int(input())
run_inday = int(input())
luknang_inday = int(input())

solu_witpuen = witpuen // witpuen_inday
solu_situp = situp // situp_inday
solu_luknang = luknang // luknang_inday
solu_run = run // run_inday

day_max = max(solu_witpuen,solu_situp,solu_luknang,solu_run)

print(day_max)
