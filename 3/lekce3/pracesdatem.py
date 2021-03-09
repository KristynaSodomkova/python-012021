from datetime import datetime, timedelta

apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start)
print(apollo_start.weekday())
print(apollo_start.strftime("%d. %m. %Y, %H:%M"))
print(apollo_start.isoweekday())
print(apollo_start.isoformat())
print(apollo_start.strftime("%d. %m. %Y, %H:%M"))
apollo_pristani = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M")
delka_mise = apollo_pristani - apollo_start
print(apollo_pristani)
print(delka_mise)
