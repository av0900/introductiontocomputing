# to compute the income tax

income=float(input("enter your gross ioncome in dollar: "))
dependents=int(input("enter the total dependents: "))


income_tax=(income-10000-(dependents*3000))




final_tax=income_tax*0.2

final_tax=round(final_tax,2)


if final_tax<0:

    final_tax=0



else:
    final_tax=final_tax


    print("your income tax is: ",final_tax)

    
