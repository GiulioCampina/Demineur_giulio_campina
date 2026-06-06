#bon bha ici ca va jouer, c'est la page de jeu quoi
import streamlit as st
from random import randint







class Demineur:

    def __init__(self, taille, diff):

        if 'usnm' not in st.session_state:
            st.session_state["usnm"] = "Pas de nom"

        if "diff" not in st.session_state:
            st.session_state["diff"] = 8

        if "etat_jeu" not in st.session_state:
            st.session_state["etat_jeu"] = "menu"
        
        if "fin_jeu" not in st.session_state:
            st.session_state["fin_jeu"] = False
        
        if "nb_bombes" not in st.session_state:
            st.session_state["nb_bombes"] = 0
        
        if "score" not in st.session_state:
            st.session_state["score"] = 0
        
        if "taille" not in st.session_state:
            st.session_state["taille"] = 5


        self.score = 0
        self.size = st.session_state["taille"]
        self.nom = st.session_state["usnm"] 
        self.diff = diff
        self.nb_bombes = st.session_state["nb_bombes"]
        self.score = st.session_state["score"]
        
        
        

    def affichage_graphique_initial(self):
        entt = st.container(border=True)
        entt.title(f"Bienvenue sur le Démineur.: {self.nom}")
        entt.subheader("Choisi ta difficulté de jeu")
        taille = st.number_input("Quelle taille de grille (de 3 a 9)", min_value=3, max_value=9, step=1)
        st.session_state["taille"] = taille

        entt.button(label="difficulté 1",
                    key="1",
                    on_click=self.change_diff_et_lancer,
                    args=(9,)                
                    )
        
        entt.button(label="difficulté 2",
                    key="2",
                    on_click=self.change_diff_et_lancer,
                    args=(8,)  
                    )
        
        entt.button(label="difficulté 3",
                    key="3",
                    on_click=self.change_diff_et_lancer,
                    args=(7,)  
                    )
    
    def affichage_graphique_enjeux(self):
        entt = st.container(border=True)
        entt.title(f"Ca joue!{self.nom}")
        dmineur.afficher_grille()


        
    def afficher_grille(self):

        if (
                "img_grid" not in st.session_state
                or "data_grid" not in st.session_state
                or len(st.session_state["img_grid"]) != self.size
            ):
            self.create_grid_base_values()

        if "img_grid" not in st.session_state or "data_grid" not in st.session_state:
            
            self.img_grid =  []
            self.data_grid = []
            self.create_grid_base_values()

        else :
            self.img_grid  = st.session_state["img_grid"]
            self.data_grid = st.session_state["data_grid"]

        for i in range(self.size):
            col = st.columns(self.size)

            for e in range(self.size):
                with col[e]:
                    st.button(label=self.img_grid[i][e],
                    key=f"{i}_{e}",
                    on_click=self.click,
                    args=(i, e),
                    use_container_width=True
                )


    def click(self, x, y):
        self.score += 15
        st.session_state["score"] = self.score

        if self.data_grid[x][y] == -1:
            print("perdu")
            st.session_state["etat_jeu"] = "perdu"
        
        if self.data_grid[x][y] == 0:
            #si c'est sur la premièere ligne

            if x == 0:

                #si c'est la première collone 

                if y == 0:

                    if self.data_grid[x][y+1] == 0:
                        self.img_grid[x][y+1] = str(self.data_grid[x][y+1])
             
                    
                    if self.data_grid[x+1][y] == 0:
                        self.img_grid[x+1][y] = str(self.data_grid[x+1][y])
                

                    if self.data_grid[x+1][y+1] == 0:
                        self.img_grid[x+1][y+1] = str(self.data_grid[x+1][y+1])
         

                    #si c'est la dernière

                elif y == (self.size - 1):
                     
                    if self.data_grid[x][y-1] == 0:
                        self.img_grid[x][y-1] = str(self.data_grid[x][y-1])
            
                    
                    if self.data_grid[x+1][y] == 0:
                        self.img_grid[x+1][y] = str(self.data_grid[x+1][y])
                  

                    if self.data_grid[x+1][y-1] == 0:
                        self.img_grid[x+1][y-1] = str(self.data_grid[x+1][y-1])
                  
                
                else:
                    if self.data_grid[x][y-1] == 0:
                        self.img_grid[x][y-1] = str(self.data_grid[x][y-1])
                  
                    
                    if self.data_grid[x+1][y] == 0:
                        self.img_grid[x+1][y] = str(self.data_grid[x+1][y])
               

                    if self.data_grid[x+1][y-1] == 0:
                        self.img_grid[x+1][y-1] = str(self.data_grid[x+1][y-1])
           

                    if self.data_grid[x+1][y+1] == 0:
                        self.img_grid[x+1][y+1] = str(self.data_grid[x+1][y+1])
          
                    
                    if self.data_grid[x][y+1] == 0:
                        self.img_grid[x][y+1] = str(self.data_grid[x][y+1])
                
#si c'est la dernière ligne
            elif x == (self.size - 1):
                #si c'est la premièere casse de la dernière ligne
                if y == 0:
                    if self.data_grid[x][y+1] == 0:
                        self.img_grid[x][y+1] = str(self.data_grid[x][y+1])
                      
                    if self.data_grid[x-1][y+1] == 0:
                        self.img_grid[x-1][y+1] = str(self.data_grid[x-1][y+1])
                    
                    if self.data_grid[x-1][y] == 0:
                        self.img_grid[x-1][y] = str(self.data_grid[x-1][y])
                  

                    
                    #si c'est la der case de la der
                elif y == (self.size -1):
                    if self.data_grid[x][y-1] == 0:
                        self.img_grid[x][y-1] = str(self.data_grid[x][y-1])
                   
                    if self.data_grid[x-1][y-1] == 0:
                        self.img_grid[x-1][y-1] = str(self.data_grid[x-1][y-1])
                    
                    if self.data_grid[x-1][y] == 0:
                        self.img_grid[x-1][y] = str(self.data_grid[x-1][y])
                     

                    #les autres 
                else:
                    if self.data_grid[x-1][y+1] == 0:
                        self.img_grid[x-1][y+1] = str(self.data_grid[x-1][y+1])
                     
                    if self.data_grid[x-1][y-1] == 0:
                        self.img_grid[x-1][y-1] = str(self.data_grid[x-1][y-1])
                
                    if self.data_grid[x-1][y] == 0:
                        self.img_grid[x-1][y] = str(self.data_grid[x-1][y])
          
                    if self.data_grid[x][y+1] == 0:
                        self.img_grid[x][y+1] = str(self.data_grid[x][y+1])
             

                    if self.data_grid[x][y-1] == 0:
                        self.img_grid[x][y-1] = str(self.data_grid[x][y-1])
             

            #si c'est les autres lignes :
            else:
                #si c'est la première colonne
                if y == 0:
                    if self.data_grid[x][y+1] == 0:
                        self.img_grid[x][y+1] = str(self.data_grid[x][y+1])
               

                    if self.data_grid[x-1][y+1] == 0:
                        self.img_grid[x-1][y+1] = str(self.data_grid[x-1][y+1])
                  

                    if self.data_grid[x-1][y] == 0:
                        self.img_grid[x-1][y] = str(self.data_grid[x-1][y])
           
                    if self.data_grid[x+1][y+1] == 0:
                        self.img_grid[x+1][y+1] = str(self.data_grid[x+1][y+1])
               

                    if self.data_grid[x+1][y+1] == 0:
                        self.img_grid[x+1][y+1] = str(self.data_grid[x+1][y+1])
        
                #si c'est la der
                elif y == (self.size -1):
                    if self.data_grid[x][y-1] == 0:
                        self.img_grid[x][y-1] = str(self.data_grid[x][y-1])
            
                    
                    if self.data_grid[x-1][y-1] == 0:
                        self.img_grid[x-1][y-1] = str(self.data_grid[x-1][y-1])
                  

                    if self.data_grid[x-1][y] == 0:
                        self.img_grid[x-1][y] = str(self.data_grid[x-1][y])
                       
                    
                    if self.data_grid[x+1][y-1] == 0:
                        self.img_grid[x+1][y-1] = str(self.data_grid[x+1][y-1])
            

                    if self.data_grid[x+1][y-1] == 0:
                        self.img_grid[x+1][y-1] = str(self.data_grid[x+1][y-1])
                        
                #les autres
                
                else:
                    if self.data_grid[x][y-1] == 0:
                        self.img_grid[x][y-1] = str(self.data_grid[x][y-1])
                        
                    if self.data_grid[x][y+1] == 0:
                        self.img_grid[x][y+1] = str(self.data_grid[x][y+1])
                        
                        
                    if self.data_grid[x-1][y+1] == 0:
                        self.img_grid[x-1][y+1] = str(self.data_grid[x-1][y+1])
                        

                    if self.data_grid[x-1][y] == 0:
                        self.img_grid[x-1][y] = str(self.data_grid[x-1][y])
                        
                    
                    if self.data_grid[x-1][y-1] == 0:
                        self.img_grid[x-1][y-1] = str(self.data_grid[x-1][y-1])
                        
                    
                    if self.data_grid[x+1][y-1] == 0:
                        self.img_grid[x+1][y-1] = str(self.data_grid[x+1][y-1])
                        

                    if self.data_grid[x+1][y] == 0:
                        self.img_grid[x+1][y] = str(self.data_grid[x+1][y])
                        
                    
                    if self.data_grid[x+1][y+1] == 0:
                        self.img_grid[x+1][y+1] = str(self.data_grid[x+1][y+1])
                        
        
        compte = (self.size **2) - self.nb_bombes


        for i in self.img_grid:
            for e in i:
                if e != " ":
                    compte -= 1
                    
                if compte == 1:
                    st.session_state["etat_jeu"] = "V"



        self.img_grid[x][y] = str(self.data_grid[x][y])
        



        
        

    def create_grid_base_values(self):

        self.img_grid = []
        self.data_grid = []
        

        for colonnes in range(self.size):
            lst = []
            for lignes in range(self.size):
                lst.append(" ")
            self.img_grid.append(lst)
        


        for colonnes in range(self.size):
            lst = []
            for lignes in range(self.size):
                rng = randint(0, 100)

                if rng >= self.diff * 10:
                    lst.append(-1)
                else:
                    lst.append(0)


                
            self.data_grid.append(lst)
        
        print(self.data_grid)

        #c'est lheure de sortir le gros cerveau

        for ligne in range(self.size):
        #ligne1
            if ligne == 0:
                #les cases de la ligne 1
                for collone in range(self.size):
                    #si on est a la case 1 de la ligne 1
                    if collone ==0:
                        
                        if self.data_grid[ligne][collone] == 0:
                            if self.data_grid[ligne][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne+1][collone] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne+1][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1
                        
                        # si on est a la dernière case de la ligne 1
                    elif collone == (self.size -1):

                        if self.data_grid[ligne][collone] == 0:
                            if self.data_grid[ligne][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne+1][collone] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne+1][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1
                        
                        #et les autres cases 

                    else:
                        if self.data_grid[ligne][collone] == 0:
                            if self.data_grid[ligne][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne+1][collone] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne+1][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne+1][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1

                #si c'est la dernièere ligne
            if ligne == (self.size - 1) :

                for collone in range(self.size):
                    #si on est a la case 1 de la ligne size-1
                    if collone ==0:
                        
                        if self.data_grid[ligne][collone] == 0:
                            if self.data_grid[ligne][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1
                        
                        # si on est a la dernière case de la ligne size - 1
                    elif collone == (self.size -1):

                        if self.data_grid[ligne][collone] == 0:
                            if self.data_grid[ligne][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1
                        
                        #et les autres cases 

                    else:
                        if self.data_grid[ligne][collone] == 0:
                            if self.data_grid[ligne][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1
                
            #et si c'est une autre ligne : 

            if ligne != 0 and ligne != (self.size -1):
                for collone in range(self.size):
                    #si on est a la case 1 de la ligne 
                    if collone ==0:
                        
                        if self.data_grid[ligne][collone] == 0:
                            if self.data_grid[ligne][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1

                            if self.data_grid[ligne+1][collone] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne+1][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1
                        
                        # si on est a la dernière case de la ligne 
                    elif collone == (self.size -1):
                        if self.data_grid[ligne][collone] == 0:
                            if self.data_grid[ligne][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1

                            if self.data_grid[ligne+1][collone] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne+1][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1

                        
                        
                        #et les autres cases 

                    else:
                        if self.data_grid[ligne][collone] == 0:
                            if self.data_grid[ligne][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1

                            if self.data_grid[ligne+1][collone] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne+1][collone-1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne-1][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1

                            if self.data_grid[ligne][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1
                            
                            if self.data_grid[ligne+1][collone+1] == -1:
                                self.data_grid[ligne][collone] += 1



        st.session_state["img_grid"] = self.img_grid
        st.session_state["data_grid"] = self.data_grid
        
        self.nb_bombes = 0
        for i in self.data_grid:
            for e in i:
                if e == -1:
                    self.nb_bombes += 1
        

        
            
        st.session_state["nb_bombes"] = self.nb_bombes

        print(self.data_grid)


    def change_diff_et_lancer(self, n):
        st.session_state["diff"] = n
        st.session_state["etat_jeu"] = "en_jeu"
        self.create_grid_base_values()
        
    def relancer(self):
        st.session_state["etat_jeu"] = "menu"
        st.session_state["nb_bombes"] = 0
        st.session_state["score"] = 0
        
    
    

   

dmineur = Demineur(
    st.session_state.get("taille", 5),
    st.session_state.get("diff", 8)
)

if st.session_state["etat_jeu"] == "menu":
    dmineur.affichage_graphique_initial()

if st.session_state["etat_jeu"] == "en_jeu":
    dmineur.affichage_graphique_enjeux()

if st.session_state["etat_jeu"] == "perdu":
    st.header("Perdu, tu peux relancer une partie en cliquant sur le bouton ci-joint ")
    st.subheader(f"Sore: {dmineur.score}")
    st.button("relancer", on_click=dmineur.relancer)

if st.session_state["etat_jeu"] == "V":
    
    st.header("Félicitations, tu as fini le démineur.")
    st.subheader(f"Sore: {dmineur.score}")
    st.button("relancer", on_click=dmineur.relancer)
