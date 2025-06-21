#Projet de bibliotheque
import flet as ft
from flet import *
import sqlite3
connexion=sqlite3.connect("bibliotheque.db")
cur=connexion.cursor()
cur.execute("SELECT nom , pass FROM utilisateur WHERE Id_utilisateur = 1 ")
recupere = cur.fetchall()
recupere_tuple = tuple(recupere[0])
uti = str(recupere_tuple[0])
pss = str(recupere_tuple[1])
def main (page:ft.Page):

# TOUTES LES FONCTIONS SE METTRONS ICI EN HAUT
    def close_page(e):
        page.update()
        page.window.destroy()
  
    def verify_login(e) :
        if not utilisateur.value == uti:
            page.open(box_login)
        elif not passeword.value == pss:
            page.open(box_login)
        else:
            utilisateur.value =""
            passeword.value=""
            page.update()
            page.go("/Acceuil")

    def verify_change(e):
        if not ancien_utilisateur.value == uti:
            page.open(box_change)
        elif not ancien_password.value == pss:
            page.open(box_change)
        else:
            text_change.visible=True
            nouveau_password.visible=True
            config_password.visible= True
            ancien_utilisateur.value=""
            ancien_password.value=""
            ancien_utilisateur.disabled=True
            ancien_password.disabled=True
            login_continue.disabled=True

        page.update()
    #2104c
    def change_login(e):
        new=nouveau_password.value
        confirm=config_password.value
       
        if not confirm == new:
            nouveau_password.value=""
            config_password.value=""
            text_error.visible=True
            page.update()
        else:
            connexion=sqlite3.connect("bibliotheque.db")
            cur=connexion.cursor()
            requete = ("UPDATE utilisateur SET pass = ? WHERE Id_utilisateur = 1 ")
            valeurs = (confirm,)
            cur.execute(requete,valeurs)
            connexion.commit()
            nouveau_password.value=""
            config_password.value=""
            page.update()
            page.close(modifier)
            page.open(box_exit)

    
#1411 
# FONCTIONS DE ROUTAGE QUI CONTIENT TOUTES LES OAGERS DE NOTRE APPLICATION
    def routage_page (e):
        page.views.clear()
        page.views.append(
            View(
                #PAGE D'AUTHENTIFICATION
                "/",
                [
                  logo_uob,block_login,
                ]
                ,bgcolor="#BAB9AF",
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            )
        )
        #2712
        if page.route == "/Acceuil":
               page.views.append(
            View(
                #PAGE D'ACCEUIL
                "/Acceuil",
                [
                 #AppBar(title=Text("Acceuil", font_family="Rockwell"), bgcolor="#BAB9AF",color="#000000", ),
                 block_menu,block_gauche
                ]
                ,bgcolor="#BAB9AF",
              
            )
        )

        page.update()

    def retour (e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # TOUTES LES BOITES DE DIALOGUES ET MESSAGE D'ERREUR SERONT ICI
    #1509
    box_login = AlertDialog(
            title="Erreur de saisie",
            content=Text("Informations d'authentifications incorrects"),
            actions=[ElevatedButton("Retour", on_click=lambda e : page.close(box_login))],
            modal=True
        )
    box_change = AlertDialog(
        title="Erreur de saisie",
        content=Text(
            """Informations d'authentifications incorrects """ ),
        actions=[ElevatedButton("Retour", on_click=lambda e:page.close(box_change))],
        modal=True
    )
    box_exit = AlertDialog(
       title="Fermeture de l'application" ,
       content=Text("L'application va fermer pour enregistrer les modifications"),
       actions=[ElevatedButton("OK", on_click=close_page )]
    )
    #MODIFICATIONS DES INFORMATIONS D'AUTHENTIFICATION
    #2712
    ancien_utilisateur = TextField(
        label="Nom d'utilisateurs",
        border_radius=7,
        color="#FFFFFF",
        width=380,
        height=40,
        text_style=ft.TextStyle(
            font_family="Rockwell"),
        label_style=ft.TextStyle(
            color="#FFFFFF",
            font_family="Rockwell"),
        )
    #1205
    ancien_password = TextField(
        label="Ancien mot de passe",
        password=True,
        border_radius=7,
        color="#FFFFFF",
        width=380,
        height=40,
        text_style=ft.TextStyle(
            font_family="Rockwell"),
        label_style=ft.TextStyle(
            color="#FFFFFF",
            font_family="Rockwell"),
        )
     #1205
    login_continue = ElevatedButton(
        "CONTINUER",
        bgcolor="#27445A",
        color="#FFFFFF", 
        width=150 ,
        height=30, 
        on_click=verify_change
             
    )
    #2104
    nouveau_password = TextField(
        label="configurer un nouveau mot de pass",
        password=True,
        border_radius=7,
        color="#FFFFFF",
        width=380,
        height=40,
        text_style=ft.TextStyle(
            font_family="Rockwell"),
        label_style=ft.TextStyle(
            color="#FFFFFF",
            font_family="Rockwell"),
            visible=False,
            max_length=40
        )
    #2104C
    config_password = TextField(
        label="Confirmer votre mot de passe",
        password=True,
        border_radius=7,
        color="#FFFFFF",
        width=380,
        height=40,
        text_style=ft.TextStyle(
            font_family="Rockwell"),
        label_style=ft.TextStyle(
            color="#FFFFFF",
            font_family="Rockwell"),
            visible=False,
             max_length=40
        )
    #2712
    text_change = Text(
        "Entrer un nouveau mot de passe ",
        font_family="Rockwell",
        size=20,
        visible=False
        )
    #0407
    text_confirm = Text(
        "\nConfirmer vos informations ",
        font_family="Rockwell",
        size=20
        )
    #2707
    text_error = Text(
        "\n les informations entrées ne sont pas identitique ",
        font_family="Rockwell",
        size=13,
        color="red",
        visible=False)
    
    block_change = Column(
        controls=[
            text_confirm,ancien_utilisateur,ancien_password,login_continue , text_change, nouveau_password, config_password,text_error
        ], horizontal_alignment=CrossAxisAlignment.CENTER
    )
    #0803
    modifier = AlertDialog(
        title="Modifier les informations d'authentification",
        content=block_change,
        modal=True,
        actions=[
            ElevatedButton("Modifier", on_click=change_login ),
            ElevatedButton("Annuler", on_click=lambda e: page.close(modifier))
        ]
    )
    #PAGE DAUTHENTIFICATION
    #1509
    utilisateur = TextField(
        label="Nom d'utilisateur",
        border_radius=7,
        color="#000000",
        width=350,
        height=40,
        text_style=ft.TextStyle(
            font_family="Rockwell"),
        label_style=ft.TextStyle(
            color="#000000",
            font_family="Rockwell"),
        
        )
    #3003
    passeword= TextField(
        label="Mot de pass",
        color="#000000",
        border_radius=7,
        width=350,
        height=40,
        password=True,
         text_style=ft.TextStyle(
            font_family="Rockwell"),
        label_style=ft.TextStyle(
            color="#000000",
            font_family="Rockwell"),           
       
    )
    #1411
    login = ElevatedButton(
        "SE CONNECTER",
        bgcolor="#27445A",
        color="#FFFFFF", 
        width=150 ,
        height=30, 
        on_click=verify_login
             
    )
    #2309
    change_info= TextButton(
        "Modifier le mot de passe ",
        style=ft.ButtonStyle(
        color="#0D65E9",
        text_style=ft.TextStyle(font_family="Britannic",
        size=18)),
        on_click=lambda e: page.open(modifier)
        
    )
    # 0409
    block_bouton = Container(
        margin=margin.only(top=20,left=60),
        content=change_info
    )
    #0507
    login_block= Container(
        margin=margin.only(left=90,top=20),
        content=(login)
    )
    #3105
    logo_uob = Image(
        src="image2.png",
        width=300,
        height=300
    )
    #0407
    ligne_login = Column(
        controls=[
            Row(
                controls=[utilisateur]
            ),
            Row(
                controls=[ passeword]
            ),
            Row(
                controls=[login_block]
            ),
            Row(
                controls=[block_bouton]
            )
        ],
       
    )
    #2707
    block_login = Container(
        width=400,
        height=300,
        content=ligne_login,
         padding=padding.only(left=30,)
         #margin=margin.only(top=90)
        
    )
#PAGE SUIVANTE 0
    titre=Text(
        "UNIVERSITE OFFICIELLE DE BUKAVU",
        font_family="Rockwell",
        size=30,
        color="#00023D",
        
        )
    #MENUS 1302A
    but_lecteur= ElevatedButton(
        "LECTEURS",
        bgcolor="#FFFFFF",
        width=130,
        color="#000000"
        
    )
    but_livre= ElevatedButton(
        "LIVRES",
        bgcolor="#ADB9CA",
         width=130,
         color="#000000"
    )
    but_emprunt= ElevatedButton(
        "EMPRUNT",
        bgcolor="#ADB9CA",
        width=130,
        color="#000000"
    )
    but_remise= ElevatedButton(
        "REMISE",
        bgcolor="#ADB9CA",
        width=130,
        color="#000000"
    )
    #LIGNE MENU 0407 P
    row_boutons= Row(
        controls=[
            but_lecteur,but_livre,but_emprunt,but_remise
        ]
    )
    #CONT LIGNE 2707 F
    block_menu = ResponsiveRow(
        controls=[
            Stack(
                controls=[
                    Container(
                        height=100,
                        bgcolor="#C3C3C3",
                        col={"xs":12,"sm":12,"md":12,"lg":12},
                        
                    ),
                    Container (
                        height=70,
                        width=600,
                        bgcolor="#E4E2D7",
                        margin=margin.only(top=15,left=12),
                        padding=padding.only(left=30, top=15),
                        border_radius=15,
                        content=titre   
                    ),
                        Container(
                        content=row_boutons,
                        margin=margin.only(left=780,top=50)
                    )
                    
                ],
                 col={"xs":12,"sm":12,"md":12,"lg":12},
            ) 
        ]
    )
    block_gauche = ResponsiveRow(
        controls=[
            Stack(
                controls=[
                    Container(
                        height=570,
                        bgcolor="#808080",
                        border_radius=7
                        
                    )
                ],
                col={"xs":12,"sm":12,"md":3,"lg":2},
            ),
            Stack(
                controls=[
                    Container(
                         height=570,
                        bgcolor="#E4E2D7",
                        border_radius=7
                        
                    )
                ],
                col={"xs":12,"sm":12,"md":6,"lg":7},
            ),
            Stack(
                controls=[
                    Container(
                        height=570,
                        bgcolor="#E4E2D7",
                        border_radius=7
                        
                    )
                ],
                col={"xs":12,"sm":12,"md":3,"lg":3},
                
            )
        ]
    )



    




    page.on_route_change = routage_page
    page.on_view_pop = retour
    page.go(page.route)

ft.app(target=main)
