# cvicenie na konverziu z eur do czk

def main():
    try:
        eur = float(input("Zadajte sumu v EUR: "))
    except:
        print("Zadajte prosím číslo!")
        return
    
    czk = 25 * eur

    print(f"{eur} EUR je {czk} CZK")

if __name__ == "__main__":
    main()