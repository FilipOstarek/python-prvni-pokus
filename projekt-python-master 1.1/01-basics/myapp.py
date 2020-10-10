"""
Cvičení 3:

Vytvořte originální aplikaci v Pythonu, v níž požádáte uživatele o různé vstupní údaje a
využijete na maximum možností výstupů do konzole. Může to být vtipný dotazník, jednoduchý znalostní test (např.
z matematiky...), průvodce fiktivní instalací atd. Fantazii se meze nekladou a vtipnější vyhrává :-)
Aplikaci uložte do samostatného souboru myapp.py.
"""
#"----------------------------------------------------------------------------------------------------------------------------\n"\
print("Tato minihra se hraje pomocí zadávání číslic podle nabídky (něco na způsob starých komiksů kdy jste mohli přetáčet stránky podle toho jak jste \n"
      "postupovali příběhově), např\n"
      "1)....\n"
      "2)....\n"
      "3)....\n"
      ",pozor ve hře je ale i tzvn. neviditelná nabídka xd \n"
      "jde o to pokud zadáte jiné číslo než je v nabídce tak se stane něco, prostě něco :D, takže pozor na situace kdy toto použijete \n"
      "a písmena nefungují(až na jednu možnost), ale na to už přijdete sami :)")
print("----------------------------------------------------------------------------------------------------------------------------")
hra = input("Jsi Dobrodruh a kdysi sis řekl/a že jednou prozkoumáš jednu jeskyňku blízkosti tvého domova, která není ani moc známá i přes\n"
            "svou velikost a rozsháhlost, avšak nejsi si o tom moc jistý/á, jelikož není moc prouzkoumána. Vydaš se na cestu ? \n"
            "---\n"
            "1)Už jsem o tom tolikrát přemýšlel/a\n"
            "2)I když možná by to nebylo špatné, ještě k tomu, když je to tak blízko\n"
            ":")
if (int(hra) == 2):
    print("----------------------------------------------------------------------------------------------------------------------------\n")
    print("Po obědě s plnou hlavou myšlenek nashromáždíš to co jsi se dozvěděl/a z internetu a od tvých známých o tomto místě. Další \n"
          "týden se vydáváš na cestu")
    volba =input("Dále po sehnání vybavení a naplánování cesty si jedeš za dalším svým snem a to i přesto že víš, že vstup do jeskyně je\n"
                 "zataresen prkny,to ale nedělá problém se přes ně dostat páčidlem, narazíš však i na další tentokrát i s cedulí o \n"
                 "pokusech lidí před tebou. Jsi si jistý\á že tohle je přesně to, co chceš ?\n"
                 "---\n"
                 "1)Jasně vole, proč jsem tu asi taky šel\n"
                 "2)Možná jsem měl ty recenze asi fakt brát vážně... ale když už tu jsem\n"
                 "3)V hlavě se ti točí, co se může ale za to nemusí stát a tak pro jistotu radši přestaneš\n"
                 "4)*Otočíš se k přípravě odjezdu, zatímco přemýšlíš co za blbost sis to zase vymyslel/a*\n"
                 ":")
    if (int(volba) == 1 or int(volba) == 2):
        print("----------------------------------------------------------------------------------------------------------------------------\n")
        print("Shazuješ poslední prkno a vcházíš do obří chodby prokláté různými jeskynními útvary, vidíš 3 cesty, slyšíš sumění křídel")
        chodba = input("Rozhlížíš se kolem sebe a pozoruješ, opravdu pouze 3 cesty, tak která se ti zamlouvá jako první ?\n"
                       "1)Vlevo\n"
                       "2)Uprostřed\n"
                       "3)Vpravo\n"
                       ":")
        if (int(chodba) == 1):
            print("----------------------------------------------------------------------------------------------------------------------------\n")
            print("Vstupuješ do menší průrvy v levo, vypadá že pokračuje dál")
            plyn = input("Po chvíli chození se všimneš, že tě začíná bolet hlava a dělá se ti trošku špatně \n"
                         "1)*Jdeš dále*\n"
                         "2)*Nezdá se ti to a tak se radši procpeš zpátky*\n"
                         ":")
            if(int (plyn)==1):
                print("----------------------------------------------------------------------------------------------------------------------------\n")
                kviti = input("Uvědomíš si, že je v této části jeskyně vysoké ticho, pomalu jak šlapeš dále, začínáš lapat po dechu, vidíš dvě cesty\n"
                              "1)První cesta\n"
                              "2)Druhá cesta... tady už končí všechna sranda\n"
                              ":")
                if(int(kviti) == 1):
                    print("Slepá chodba, tohle není dobré, podlamují se ti nohy, potřebuješ si spočnout.....")
                if (int(kviti) == 2):
                    print("Jdeš dál po chodbě, vidíš světlo, přijdeš blíž a spatříš uprostřed jeskyně palouček modrého svítivého kvítí, cesta za tímto paloukem,\n"
                          "ale pokračuje dál, po chvíli bloudění v jeskyním systému vidíš další světlo, stoupáš nahoru, vidíš další prkna,\n"
                          "po tolika hodinách je slunce požehnáním, přejdeš na druhou stranu hory, najdeš auto a jedeš domů s pocitem štěstí a novým zážitkem")
                if ((int(kviti) <= 0)or(int(kviti) >= 3)):
                    print("Samým zděšením nevíš co máš dělat,bojíš se a je ti stále čím dál více hůře, proběhneš chodbou zpátky a ihned odjíždíš s tím že\n"
                          "tohle už nikdy neuděláš")
            if (int(plyn) == 2):
                print("----------------------------------------------------------------------------------------------------------------------------\n")
                chodba = input("Vylezeš rychle zpátky na začátek, je ti o dost lépe, jsi si jistý že chceš jít pryč ?\n"
                    "1)Jít pryč a zabalit to\n"
                    "2)Jít místo toho prostřední chodbou\n"
                    "3)Anebo vpravo\n"
                    ":")
                if(int(chodba) == 1):
                    print("Vylezeš ven a i přesto co jsi všechno zažil, víš že tahle jeskyně opravdu nestojí za to")
            if (int(plyn) >= 3)or(int(plyn) <= 0):
                print("Opravdu ti není dobře, padáš na zem, to poslední co vidíš je mírně blikající světlo baterky....")
        if (int(chodba) == 2):
            netopirek = True
            print("----------------------------------------------------------------------------------------------------------------------------\n")
            print("Jdeš ke prostřední komoře a začínáš se slaňovat přímo dolů po srázi, šumění jde slyšet více, ")
            jmeno = input("najednou vidíš malé netopýrky, jen tak ze srandy si jednoho pojmenuješ\n"
                         ":")
            print("Jak slanuješ dolů, všímáš si že " + jmeno + " se probouzí")
        if (int(chodba) == 3):
            print("Pomalu slézáš po úpatí skály dolů, cesta je bez problémů")
        if (int(chodba) == 3) or (int(chodba) == 2):
            print("----------------------------------------------------------------------------------------------------------------------------\n")
            rimsa = input("Najednou však spatříš trámy ???, rozhlídneš se a vidíš že pokračují přímo do skály nad propastí, štestí je ale na tvojí\n"
                         "straně a trámy jsou blízko u tebe, je třeba jenom přelést římsu, avšak máš z toho špatný pocit \n"
                          "1)Přelést římsu\n"
                          "2)Slaňovat dál\n"
                          "3)HALOOOOO ?!\n"
                          "4)Okamžitě vylézt zpátky a odjet než tě někdo uvidí\n"
                          ":")
            if (int(rimsa) <= 0)or(int(rimsa) >=5 ):
                print("----------------------------------------------------------------------------------------------------------------------------\n")
                lano = input("UKLOUZNUL JSI ale naštěstí tě stihlo zachytit záchranné lano\n"
                             "1)*UKAMŽITE SE TOHO ZÁCHRANÉHO LANA CHYTNEŠ*\n"
                             "2)*UKAMŽITE SE TOHO ZÁCHRANÉHO LANA CHYTNEŠ*\n"
                             ":")
                if ((int(lano) == 1) or (int(lano) == 2)):
                    print("A LANO RUPNE....")
                if ((int(lano) <= 0) or (int(lano) >= 3)):
                    print("RYCHLE SE LANA CHYTNES A vyšplháš se rychle zpátky vyškrábeš")
                    print("----------------------------------------------------------------------------------------------------------------------------\n")
                rimsa = input("Okay to by možná bylo dneska adrenalinu dost ne ?\n"
                              "1)I tak bych mohl/a přelézt tu římsu a nachvilu se porozlédnout \n"
                              "2)Slaňovat dál ???\n"
                              "3)Možná pokud tu někdo je, můžu zavolat, možná proto jsou tyhle jeskyně normálně nedostupné\n"
                              "4)anebo bude lepší když odsud rychle zmizím...\n"
                              ":")
                if (int(rimsa) <= 0) or (int(rimsa) >= 5):
                    print("Snažíš se pobrat, co se tu vlastně děje, proč tu jsou ty trámy atd...\n"
                          "a pro jistotu šplháš zpátky, s tím že tohle UŽ NIKDY")
            if (int(rimsa) == 1):
                print("Už je ti vše jasné, nepoužívané doly ze starých dob, otázkou však je proč přestali těžit i když vidíš něco co připomíná rudu")
            if (int(rimsa) == 3):
                print("HALOOOOO... haloooo...halo___ ozývá se ze všech stran poblíž a nasloucháš pro nějakou odpověď\n"
                      "....žádná krom tvého hlasu nepřichází, je ti jasné, že tu jsi sám/sama ")
            if (int(rimsa) == 4):
                print("Odjíždíš pomalu se pocitem že některé věci by měly zůstat neodkryté")
            if (int(rimsa) == 2):
                print("Slaňuješ dál a dostáváš se na dno, jediné co však vidíš jsou roztříštěné koleje, trámy a dokonce i jeden vozík přetočený na stranu \n"
                      "dozvídáš se že nejspíše tam kde jsi před chvíli byl se nejspíše stavěl most na druhou stanu, nebo se aspoň pokusili.... ")
            if ((int(rimsa) == 1) or (int(rimsa) == 2) or (int(rimsa) == 3)):
                print("----------------------------------------------------------------------------------------------------------------------------\n")
                prozkoumani =input("Co takhle se jít tam podívat ?\n"
                                   "1) Už jsem tak daleko, tak proč ne\n"
                                   "2) Co když je tohle jenom nepoužívaná část, co když se to zhroutí ??\n"
                                   ":")
                if(int(prozkoumani) == 1):
                    print("Jdeš prozkoumat dál hlouběji do dolů, nic nenacházíš i když tvá baterka svítí silně, pouze nevykopanou rudu. Rozhodneš se tady svůj\n"
                          "výlet ukončit s novými zážitky, kdo ví, možná slaňování jeskyň bude tvůj koníček")
                if (int(prozkoumani) == 2):
                    print("Nakonec se rozhodneš tohle zabalit, viděl jsi dost, přeci jenom musel být nějaký důvod proč to tu zavřeli nebo zablokovali... jo určitě\n"
                          ".... Po chvíli přemýšlení radši vylezeš zpátky napovrch a odjíždíš s novými plány a pocitem že musíš zjistit víc i když se tam nechceš \n"
                          "vracet");
                if ((int(prozkoumani) <= 0 or int(prozkoumani) >= 3)and (netopirek == True)):
                    print("Z ničehonic vidíš jak ze shora sletí " + jmeno + "a přímo před tebou si sedne na trám, vypadá mnohem více roztomileji než jsi ho viděl \n"
                          "předtím, zvláštní jak je přítulný že doletěl k tobě až tak blízko.")
        if (int(chodba) >= 4) or (int(chodba) <= 0):
            print("Na poslední chvíli se ti vštípí do hlavy příběh známého, co kdysi byl v podobné situaci jako ty, ale narozdíl og něj nehodláš \n"
                  "získat to, co se stalo jemu....")
    if ((int(volba) == 3 or int(volba) == 4)or(int(volba) <= 0 or int(volba) >= 5)):
        print("A jedeš domů všímající si svého okolí, jop tu výstroj budeš muset vrátit")
if (int(hra) == 1):
    print("Nakonec tě tato tvá myšlenka rychle přešla, jelikož jsi zapomněl/a o palačinkách na plotně\n")
if (int(hra) != 1 and int(hra) != 2):
    print("Ze svojí nerozhodnosti tě mezitím vytrhla vůně něčeho spáleného...\n")