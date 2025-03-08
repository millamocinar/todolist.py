def main():
    gorevler = []  # 'gorev' yerine 'gorevler' kullanmalıyız

    while True:
        print("\n---= TO-DO LIST =---", end="\n--")
        print("1. Gorev Ekle", end="\n--")
        print("2. Gorevleri Goster", end="\n--")
        print("3. Tamamlanmis Gorevleri Isaretle", end="\n--")
        print("4. Iyı Gunler :)", end="\n--")

        secim = int(input("Secimini yap: "))

        if secim == 1:
            print()
            s_gorevler = int(input("\n--Kac gorev eklemek istersin: "))

            for i in range(s_gorevler):
                gorev = input("\n--Gorev gir: \n--0rnek olarak: - Eve git: ")
                gorevler.append({"gorev": gorev, "Oldu bil": False})
                print("\n🌺Yapmaya basla!💪")

        elif secim == 2:
            print("\n--Gorevler:")
            for index, gorev in enumerate(gorevler):  # 'numaralandır' yerine 'enumerate'
                statu = "Damn adamım çok azimli!" if gorev["Oldu bil"] else "Hadi ama🙁"
                print(f"{index + 1}. {gorev['gorev']} - {statu}")

        elif secim == 3:
            gorev_index = int(input("\n--Isaretlenicek gorev sayisini soyle: ")) - 1
            if 0 <= gorev_index < len(gorevler):  # 'gorev' yerine 'gorevler'
                gorevler[gorev_index]["Oldu bil"] = True  # 'tasks' yerine 'gorevler' ve 'Tamamdır!' yerine 'Oldu bil'
                print("Gorev tamamdır rahatla!")
            else:
                print("\n--Girilmemis gorev.")

        elif secim == 4:  # 'choice' yerine 'secim'
            print("Iyi gunler🤚🏻")
            break

        else:
            print("Yapma bana numara.")

if __name__ == "__main__":
    main()
