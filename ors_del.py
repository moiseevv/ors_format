# coding: utf8

import pandas as pd
import numpy as np
import csv
from datetime import datetime as dt
c = 0

print("Загрузка csv для удалнея полей")
s1_path = 'ORS_202209_БЕЗЕПДLOAD_633665BFD15BF_out.csv'
print (s1_path)


print("Время запуска: ", dt.now())
s1 = pd.read_csv(s1_path, sep=';', engine='python', encoding="ISO-8859-1", dtype={'BIK':str})


fin_s1 = s1.drop(['INN_COMPANY', 'District','FIAS','CHARGES_Ob','RECALC_Ob','COUNT_JIL','COUNT_SOBST','COUNT_REG'], axis = 1)

fin_s1.rename(columns = {'RASCH_ED':'FULLAREA', 'OLD_CNUM':'ACC'}, inplace = True)
fin_s1['FIO1'] = fin_s1['FIO1'] +' '+ fin_s1['FIO2'] +' '+ fin_s1['FIO3'] 
fin_s1 = fin_s1.drop(['FIO2','FIO3'], axis =1)

fin_s1.loc[(np.isnan(fin_s1.SALDO_IN_PENI)),'SALDO_IN_PENI'] = "0"
fin_s1.loc[(np.isnan(fin_s1.CHARGES_PENI)),'CHARGES_PENI'] = "0"
fin_s1.loc[(np.isnan(fin_s1.RECALC_PENI)),'RECALC_PENI'] = "0"
fin_s1.loc[(np.isnan(fin_s1.PAYMENT_PENI)),'PAYMENT_PENI'] = "0"
fin_s1.loc[(np.isnan(fin_s1.SALDO_OUT_PENI)),'SALDO_OUT_PENI'] = "0"

fin_s1.ID_COMPANY= fin_s1.ID_COMPANY.str.replace('"','')

fin_s1.rename(columns = {'FIO1':'FIO'}, inplace = True)

print(' в итоге',fin_s1)


jj = str(f"ORS_{s1_path}")
fin_s1.to_csv(jj, sep=";", index=False, quoting=csv.QUOTE_NONE, header=True, encoding="ISO-8859-1")
print("Время завершения: ", dt.now())
