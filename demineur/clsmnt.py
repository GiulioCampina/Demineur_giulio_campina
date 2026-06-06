import supabase as sb



url = "https://jhftbycjyhyvcgotxjqr.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpoZnRieWNqeWh5dmNnb3R4anFyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MDc2NTEzMywiZXhwIjoyMDk2MzQxMTMzfQ.sNxs3Cf_KxQBlIm_rdXixiZ0_ss0IjHEJ56rH0Z0MBo"
Client = sb.create_client(url, key)

def  get_tabl():
    dta = Client.table("rank").select("*").execute()
    lst_tot = []
    lst_nom = []
    lst_scores = []

    for e in dta:
        for s in e:
            if isinstance(s, list):
                for element in s:
                    lst_nom.append(element["nom"])
                    lst_scores.append(element["result"])
                    

    lst_tot.append(lst_scores)
    lst_tot.append(lst_nom)
    return lst_tot

def insert_new_score(nom, rslt):
    Client.table("rank").insert({"nom": nom, "result": rslt}).execute()


get_tabl()