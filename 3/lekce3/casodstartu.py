from datetime import datetime, timedelta

apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start.strftime("%m/%d/%Y"))

orbiter_start = datetime(2020, 2, 10, 5, 3)
print(orbiter_start.isoweekday())
cas_od_startu = datetime.now() - orbiter_start
print(cas_od_startu)
print(type(cas_od_startu))

cas_objednavky = datetime(2020,11,13,19,47)
prevzeti = timedelta(minutes=8, seconds=35)
priprava = timedelta(minutes=30)
doprava = timedelta(minutes=25, seconds=30)

print(cas_objednavky + prevzeti + priprava + doprava)

