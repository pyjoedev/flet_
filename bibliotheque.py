import flet as ft
from flet import *
def main (page:ft.Page):
    #page.theme_mode=ThemeMode.LIGHT

# FONCTIONS DE ROUTAGE QUI CONTIENT TOUTES LES OAGERS DE NOTRE APPLICATION
    def routage_page (e):
        page.views.clear()
        page.views.append(
            View(
                #PAGE D'ACCEUIL
                "/",
                [
                  logo_uob,block_login,
                ]
                ,bgcolor="#BAB9AF",
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            )
        )

        page.update()

    def retour (e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    #MODIFICATIONS DES INFORMATIONS D4AUTHENTIFICATION

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
    ancien_uti = TextField(
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
    nouveau_uti = TextField(
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
        )
    #2104C
    config_uti = TextField(
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
        )
    text_change = Text(
        "Entrer un nouveau mot de passe ",
        font_family="Rockwell",
        size=20
        )
    
    text_confirm = Text(
        "\nConfirmer vos informations ",
        font_family="Rockwell",
        size=20
        )
    block_change = Column(
        controls=[
            text_confirm,ancien_utilisateur,ancien_uti, text_change, nouveau_uti, config_uti
        ]
    )
    #0803
    modifier = AlertDialog(
        title="Modifier les informations d'authentification",
        content=block_change,
        modal=True,
        actions=[
            ElevatedButton("Modifier" ),
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
        margin=margin.only(top=20),
        content=change_info
    )
    #0507
    login_block= Container(
        margin=margin.only(left=90,top=20),
        content=(login)
    )
    #3105
    logo_uob = Image(
        src="memoire/image2.png",
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


    




    page.on_route_change = routage_page
    page.on_view_pop = retour
    page.go(page.route)

ft.app(target=main)