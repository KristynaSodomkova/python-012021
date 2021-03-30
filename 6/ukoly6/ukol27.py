import pandas
import wget

# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")
vykazy = pandas.read_csv("vykazy.csv")
# proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty
info_pro_zakaznika = vykazy.groupby("project")["hours"].sum()
print(info_pro_zakaznika)

# dobrovolný doplněk
# propoj tab s výkazy a zaměstnanci
zamestnanci = pandas.read_csv("zamestnanci.csv")
vykazy = vykazy.rename(columns={"emloyee_id": "cislo_zamestnance"})
zamestnanci_vykazy = pandas.merge(zamestnanci, vykazy, on=["cislo_zamestnance"], how="outer")
# proveď statistiku vykázaných hodin za jednotlivé kanceláře = spočítej počet hodin vykázaný jednotlivých kanceláří
# na projekty daného zákazníka
info_o_projektech = zamestnanci_vykazy.groupby("mesto")["hours"].sum()
print(info_o_projektech)
# nerozumím zadání, jestli to mělo být i rozdělené na počet hodin za každý projekt zvlášt v každém městě, tak:
info_o_projektech2 = zamestnanci_vykazy.groupby(["mesto", "project"])["hours"].sum()
print(info_o_projektech2)

