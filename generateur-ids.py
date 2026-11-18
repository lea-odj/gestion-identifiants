def create_id(domaine = '@univ.com'):
    prenom = input("prénom : ").replace(" ", "").lower()
    nom = input("nom : ").replace(" ","").lower()
    mail = prenom + '.' + nom  

    if len(mail) > 20:
        mail = prenom[:1]+ '.' + nom[:18]

    full_mail = mail + domaine
    return full_mail, mail, domaine 

def verif_doublon(full_mail, domaine, mail, file):
    x = 1 
    mail_base = mail 
    while full_mail in file: 
        full_mail = mail_base + str(x) + domaine
        x += 1 
    return full_mail


if __name__ == "__main__" : 

    user = []

    try: 
        with open ("user.txt", 'r') as file:
            for line in file: 
                user.append(line.strip())

    except FileNotFoundError:
        with open ("user.txt", 'a') as file:
            pass 

    full_mail, mail, domaine = create_id()

    if full_mail in user: 
        ask = input('avez vous déjà un compte ? (oui / non)')
        if ask.lower().strip() == "non":
            final_mail = verif_doublon(full_mail, domaine, mail, user)

        else: 
            print("appuyez sur \"se connecter\"") 
            final_mail = None 

    else : 
        final_mail = full_mail 

    if final_mail : 
        with open('user.txt', 'a') as file: 
            file.write(final_mail + '\n')

        print('votre mail est désormais : ', final_mail)
