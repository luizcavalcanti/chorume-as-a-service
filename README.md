# chorume-as-a-service

O Twitter dificulta a exportação e importação de lista de contas bloqueadas, então eu fiz um script safadinho em python para gerar essa tabela abaixo.

Por enquanto ainda é muito trabalhoso bloquear um a um, mas vale muito a pena se livrar de gente desgraçada no Twitter :)

### Como rodar na minha máquina?

Você precisa configurar as seguintes variáveis de ambiente (é preciso gerar seus próprios valores em developer.twitter.com):

```bash
export TWITTER_CONSUMER_KEY=blablabla
export TWITTER_CONSUMER_SECRET=blebleble
export TWITTER_ACCESS_TOKEN=bliblibli
export TWITTER_TOKEN_SECRET=blobloblo
```

Depois basta mandar um make:

```bash
make deps # instala as dependências
make export # para criar um csv com seus blocks, além de atualizar este README.md
make block # lê o blocks.csv e bloqueia os mesmos desgraçados na sua conta
```

### Lista de gente desgraçada e robôs do twitter




(1444 contas bloqueadas em 30/01/2021 17:12:59)

| Usuário | Criado em | Razão (Seguidores/Seguindo) | Tweets |
| --- | --- | --- | --- |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Maria Barros](https://twitter.com/MariaCr29588223) | 07/11/2018 | 0.073 (14/191) | 2306 |
| ![alt text](http://pbs.twimg.com/profile_images/1293661375244402748/inIaZn3S_normal.png "foto do usuário") [Felipe](https://twitter.com/Flifrds) | 09/12/2018 | 3.919 (16343/4170) | 53042 |
| ![alt text](http://pbs.twimg.com/profile_images/1282882833443323904/1wWs8mWx_normal.jpg "foto do usuário") [OSMAR ANGELO](https://twitter.com/OSMARANGELO) | 21/01/2012 | 0.183 (228/1243) | 17254 |
| ![alt text](http://pbs.twimg.com/profile_images/1290019934064586754/oHd8OOkK_normal.jpg "foto do usuário") [Jaelson Azevedo Carmo](https://twitter.com/CarmoJaelson) | 23/10/2019 | 0.412 (7/17) | 11280 |
| ![alt text](http://pbs.twimg.com/profile_images/1323523707252473858/lWk8S2cZ_normal.jpg "foto do usuário") [Felipe C. Rodrigues](https://twitter.com/Lipevia) | 22/06/2010 | 0.898 (53/59) | 1459 |
| ![alt text](http://pbs.twimg.com/profile_images/1274506311120703488/AGh5qBP__normal.jpg "foto do usuário") [Ailton Santos 🤜🤛🙌🙏🇧🇷💍 SOU DE DIREITA.](https://twitter.com/AiltonS55157435) | 27/06/2019 | 0.623 (1746/2803) | 12157 |
| ![alt text](http://pbs.twimg.com/profile_images/1278123963248500736/Q6gfjZCg_normal.jpg "foto do usuário") [luis gonzaga](https://twitter.com/luisgon49622608) | 01/07/2020 | 0.029 (1/35) | 167 |
| ![alt text](http://pbs.twimg.com/profile_images/1353427548043177985/uh8o6nAD_normal.jpg "foto do usuário") [Maria Aspasia](https://twitter.com/aspasia_maria) | 08/11/2019 | 0.976 (1097/1124) | 138614 |
| ![alt text](http://pbs.twimg.com/profile_images/1353032820717973504/RvvJKAa1_normal.jpg "foto do usuário") [Raphael](https://twitter.com/Eu_o_Rapha) | 08/04/2019 | 0.292 (64/219) | 599 |
| ![alt text](http://pbs.twimg.com/profile_images/1248725472420278272/Ei6ktl9V_normal.jpg "foto do usuário") [Eleva - VOTO IMPRESSO JÁ!](https://twitter.com/ElevaBrasilES) | 10/04/2020 | 1.05 (1648/1570) | 3773 |
| ![alt text](http://pbs.twimg.com/profile_images/1238570078649683968/Llzng0gM_normal.jpg "foto do usuário") [Rosicler Cantarelli](https://twitter.com/RosiclerCantar1) | 06/11/2018 | 0.899 (3790/4215) | 126065 |
| ![alt text](http://pbs.twimg.com/profile_images/682124039683502080/K0PICQS5_normal.jpg "foto do usuário") [Sergio NeviereCoimbra](https://twitter.com/SCoimb) | 29/12/2015 | 4.262 (439/103) | 84413 |
| ![alt text](http://pbs.twimg.com/profile_images/1345587075786145792/gg7YLgCi_normal.jpg "foto do usuário") [Fátima Lugato](https://twitter.com/FtimaLugato4) | 14/11/2019 | 0.335 (55/164) | 5029 |
| ![alt text](http://pbs.twimg.com/profile_images/1347844828860719106/m7xbsWrM_normal.jpg "foto do usuário") [O_Autentico](https://twitter.com/Motta1O) | 18/05/2014 | 0.649 (316/487) | 4113 |
| ![alt text](http://pbs.twimg.com/profile_images/623190910730305536/jcwPKLwo_normal.png "foto do usuário") [Saab do Brasil](https://twitter.com/saabdobrasil) | 17/07/2015 | 1302.037 (35155/27) | 780 |
| ![alt text](http://pbs.twimg.com/profile_images/1251230166136827913/1mONTuMZ_normal.jpg "foto do usuário") [MD Neuman](https://twitter.com/MDNeuman01) | 16/02/2010 | 0.512 (154/301) | 6718 |
| ![alt text](http://pbs.twimg.com/profile_images/1313886380498595840/FI2VITQW_normal.jpg "foto do usuário") [Ramonᶜʳᶠ](https://twitter.com/RamonLR_Oficial) | 03/11/2015 | 0.141 (38/270) | 445 |
| ![alt text](http://pbs.twimg.com/profile_images/993211235654041600/UVwZVdFe_normal.jpg "foto do usuário") [Alvaro Garnero](https://twitter.com/AlvaroGarnero) | 21/03/2009 | 405.049 (583271/1440) | 34453 |
| ![alt text](http://pbs.twimg.com/profile_images/378800000244936111/895394e423009a17c0d0ec09622dcab1_normal.jpeg "foto do usuário") [Max Almeida🇧🇷🇮🇱](https://twitter.com/maxwilliam_max) | 02/01/2013 | 0.621 (744/1199) | 11987 |
| ![alt text](http://pbs.twimg.com/profile_images/1329770835968667648/C9ccqggT_normal.jpg "foto do usuário") [andre gomes](https://twitter.com/andrego96010482) | 10/11/2020 | 0.333 (657/1971) | 14952 |
| ![alt text](http://pbs.twimg.com/profile_images/1283164294968942593/1GleCIDx_normal.jpg "foto do usuário") [Sr Pumão](https://twitter.com/pugplud) | 12/12/2016 | 0.21 (38/181) | 380 |
| ![alt text](http://pbs.twimg.com/profile_images/1234330249485221889/Ayd4dj7J_normal.jpg "foto do usuário") [Brayan Lopes](https://twitter.com/BrayanL19589859) | 13/04/2017 | 0.156 (5/32) | 276 |
| ![alt text](http://pbs.twimg.com/profile_images/1349487096352935938/4UKJKtzz_normal.jpg "foto do usuário") [Mandy](https://twitter.com/Lets_38) | 03/10/2011 | 0.612 (221/361) | 2805 |
| ![alt text](http://pbs.twimg.com/profile_images/1349246791401820163/vu1URN52_normal.jpg "foto do usuário") [FoX McCloud](https://twitter.com/_Fire_x_FoX_) | 27/06/2019 | 0.325 (50/154) | 2909 |
| ![alt text](http://pbs.twimg.com/profile_images/1342848708057194498/nB1QE3Ne_normal.jpg "foto do usuário") [ālyson™](https://twitter.com/empadao_) | 04/10/2018 | 1.442 (385/267) | 24623 |
| ![alt text](http://pbs.twimg.com/profile_images/1348982121923289089/cA4dwUsg_normal.jpg "foto do usuário") [carlos jose andrade](https://twitter.com/carlostaiti) | 30/10/2009 | 0.239 (38/159) | 809 |
| ![alt text](http://pbs.twimg.com/profile_images/1330897073995198465/IX2LPa5z_normal.jpg "foto do usuário") [MariaJuliaFernandes Bolsonaro](https://twitter.com/baxulas) | 25/12/2012 | 2.9 (986/340) | 47109 |
| ![alt text](http://pbs.twimg.com/profile_images/1002238407152754691/RoZHEZsv_normal.jpg "foto do usuário") [ana monello](https://twitter.com/anamonello) | 10/11/2009 | 0.663 (724/1092) | 22153 |
| ![alt text](http://pbs.twimg.com/profile_images/1350631005988806658/LClmph-V_normal.jpg "foto do usuário") [@marcia779011](https://twitter.com/marcia779011) | 12/10/2020 | 0.775 (275/355) | 4797 |
| ![alt text](http://pbs.twimg.com/profile_images/1347723752927338501/Xqz1reZb_normal.jpg "foto do usuário") [kitana](https://twitter.com/kitanadestra) | 17/06/2018 | 0.302 (84/278) | 1075 |
| ![alt text](http://pbs.twimg.com/profile_images/1237571881818976256/kCSl03iN_normal.jpg "foto do usuário") [-](https://twitter.com/SauloMineiro) | 11/07/2009 | 0.01 (1562/0) | 5798 |
| ![alt text](http://pbs.twimg.com/profile_images/1287719179957743616/PSUqaY9O_normal.jpg "foto do usuário") [¦§@ 🧂👌🏻 🐸](https://twitter.com/BasedMatrix) | 17/12/2018 | 0.961 (2463/2564) | 21142 |
| ![alt text](http://pbs.twimg.com/profile_images/1333597089113247745/M-EJDtUB_normal.jpg "foto do usuário") [Faby Gonçalves](https://twitter.com/labiolafasantos) | 26/10/2010 | 1.056 (1332/1261) | 8878 |
| ![alt text](http://pbs.twimg.com/profile_images/1344955616410923011/CgieLKVH_normal.jpg "foto do usuário") [Marcelo Silva direita BRASIL🇧🇷🇮🇱38😎👉👉](https://twitter.com/marcelosilva_ti) | 12/09/2016 | 0.646 (1120/1734) | 10117 |
| ![alt text](http://pbs.twimg.com/profile_images/1275076838843277315/UOewvV4O_normal.jpg "foto do usuário") [maria auxiladora](https://twitter.com/marrafellows) | 01/08/2013 | 0.15 (39/260) | 1229 |
| ![alt text](http://pbs.twimg.com/profile_images/1264687862848598016/sRI5B8on_normal.jpg "foto do usuário") [Sérgio Camargo](https://twitter.com/sergiodireita1) | 08/01/2020 | 853.585 (234736/275) | 6743 |
| ![alt text](http://pbs.twimg.com/profile_images/1355163103349133313/qy3zYpMy_normal.jpg "foto do usuário") [Marco, a favor da governabilidade](https://twitter.com/marcoaurelio969) | 19/12/2017 | 0.996 (10228/10269) | 29095 |
| ![alt text](http://pbs.twimg.com/profile_images/1313566728585187329/icvf-5VR_normal.jpg "foto do usuário") [Fernando](https://twitter.com/bolsomito_2) | 06/10/2020 | 1.029 (7245/7038) | 14033 |
| ![alt text](http://pbs.twimg.com/profile_images/1350405179812753409/yygs7sv-_normal.jpg "foto do usuário") [Fábio JMB 2022 🇧🇷](https://twitter.com/Jmb_newage) | 12/03/2014 | 0.933 (3404/3650) | 9517 |
| ![alt text](http://pbs.twimg.com/profile_images/1342462981045706752/3h-qtixS_normal.jpg "foto do usuário") [⚔️🇧🇷 William Walace 🇧🇷⚔️](https://twitter.com/willwalacebr) | 20/05/2020 | 1.145 (12591/10996) | 16748 |
| ![alt text](http://pbs.twimg.com/profile_images/1355276474773856260/juSu4c-L_normal.jpg "foto do usuário") [AG.Martins](https://twitter.com/AGMartins3) | 30/07/2018 | 0.955 (4575/4792) | 38197 |
| ![alt text](http://pbs.twimg.com/profile_images/1251283253417390084/2NFuw9Y6_normal.jpg "foto do usuário") [Claudinha França](https://twitter.com/claudinha_jp) | 10/04/2011 | 2.783 (8917/3204) | 5614 |
| ![alt text](http://pbs.twimg.com/profile_images/1304201064179265541/NoE_4OaH_normal.jpg "foto do usuário") [Eduardo B Miraflores 💯%🇧🇷](https://twitter.com/EduBM1979) | 01/07/2009 | 0.772 (3833/4965) | 57563 |
| ![alt text](http://pbs.twimg.com/profile_images/1352691351507316736/BqRJouyR_normal.jpg "foto do usuário") [Vieira65🇧🇷🇺🇸🇮🇱](https://twitter.com/Vieira651) | 26/05/2019 | 1.014 (1290/1272) | 3719 |
| ![alt text](http://pbs.twimg.com/profile_images/809448679362985984/XCvGtF2g_normal.jpg "foto do usuário") [Rosangellasm😷 🐊⚖️🏖️](https://twitter.com/Rosangellasm) | 01/03/2013 | 0.922 (540/586) | 12050 |
| ![alt text](http://pbs.twimg.com/profile_images/1350476707019567104/r37YoPCM_normal.jpg "foto do usuário") [🇧🇷Cleverson Ribeiro🇧🇷](https://twitter.com/cleverzone) | 19/04/2011 | 0.435 (81/186) | 2290 |
| ![alt text](http://pbs.twimg.com/profile_images/1266725172255395840/ykJ8fZaB_normal.jpg "foto do usuário") [Rob Smith](https://twitter.com/rcssmedasmith) | 28/03/2012 | 0.198 (790/3991) | 46467 |
| ![alt text](http://pbs.twimg.com/profile_images/1242191276096786433/tlU6LZxw_normal.jpg "foto do usuário") [Lange](https://twitter.com/LangeGV) | 25/05/2016 | 0.193 (21/109) | 2405 |
| ![alt text](http://pbs.twimg.com/profile_images/1297534264804868097/WZJbtxf7_normal.jpg "foto do usuário") [Paulo C Pavan](https://twitter.com/PauloCPavan) | 10/02/2014 | 0.147 (88/598) | 4882 |
| ![alt text](http://pbs.twimg.com/profile_images/1220808726749138944/YKfLA6lA_normal.jpg "foto do usuário") [Colony Siege](https://twitter.com/FinifugalGames) | 06/10/2019 | 2.14 (1175/549) | 462 |
| ![alt text](http://pbs.twimg.com/profile_images/1348421323085721602/ocx4M2MH_normal.jpg "foto do usuário") [Pruda-CWB 🤡](https://twitter.com/pruda1268) | 01/09/2009 | 0.957 (4154/4340) | 36729 |
| ![alt text](http://pbs.twimg.com/profile_images/1280570280168099840/sJzGBsJz_normal.jpg "foto do usuário") [👉🇧🇷 David 🇧🇷👈](https://twitter.com/David73692593) | 06/08/2019 | 0.521 (1844/3542) | 16533 |
| ![alt text](http://pbs.twimg.com/profile_images/1351670415761010688/KWmkR7z7_normal.jpg "foto do usuário") [Ranieri](https://twitter.com/ranieriqueiroz) | 22/06/2009 | 0.522 (713/1366) | 10046 |
| ![alt text](http://pbs.twimg.com/profile_images/1350423858181005313/pyiUkwic_normal.jpg "foto do usuário") [L.V.Mises](https://twitter.com/v_mises) | 08/10/2019 | 0.325 (101/311) | 5024 |
| ![alt text](http://pbs.twimg.com/profile_images/1349165193792794629/-WVWnKHG_normal.jpg "foto do usuário") [HAROLDECIO ROMEU LINDO](https://twitter.com/HRomeu_Lindo) | 04/01/2015 | 0.837 (3966/4741) | 17665 |
| ![alt text](http://pbs.twimg.com/profile_images/1057407738572144640/cix8aZOr_normal.jpg "foto do usuário") [maria_julinha](https://twitter.com/maria_julinha) | 20/07/2009 | 0.654 (380/581) | 10022 |
| ![alt text](http://pbs.twimg.com/profile_images/1342043294889598976/6YuEVAsH_normal.jpg "foto do usuário") [dunder mifflin this is 𝓫𝓮𝓬𝓴𝓼 🗿](https://twitter.com/oppressionbecks) | 02/09/2020 | 0.072 (13/180) | 404 |
| ![alt text](http://pbs.twimg.com/profile_images/1334905555064905732/puYPjGkD_normal.jpg "foto do usuário") [PROFESSOR NA DIREITA](https://twitter.com/PROFESSORORUS) | 28/05/2019 | 1.394 (16375/11747) | 67180 |
| ![alt text](http://pbs.twimg.com/profile_images/1349536362215714817/yEtkoQXz_normal.jpg "foto do usuário") [Carlos RIOS](https://twitter.com/CarlosRios2013) | 25/01/2014 | 1.075 (958/891) | 103248 |
| ![alt text](http://pbs.twimg.com/profile_images/1247665466283298818/4x3kR9sL_normal.jpg "foto do usuário") [Dimitri Portugal](https://twitter.com/_PatriotaBR_) | 28/02/2020 | 0.807 (1139/1411) | 22414 |
| ![alt text](http://pbs.twimg.com/profile_images/1296903000187953154/d2HvrkqT_normal.jpg "foto do usuário") [Ivan Boesky](https://twitter.com/boesky_ivan) | 21/08/2020 | 0.049 (11/224) | 57 |
| ![alt text](http://pbs.twimg.com/profile_images/1114932730796572672/1KXwvMrT_normal.jpg "foto do usuário") [André Rojas](https://twitter.com/Andre26Rojas) | 05/04/2019 | 0.484 (46/95) | 1093 |
| ![alt text](http://pbs.twimg.com/profile_images/1350207292545912839/Ab5ygq1d_normal.jpg "foto do usuário") [Pinto](https://twitter.com/pinto_rogrio) | 08/02/2013 | 0.902 (2140/2372) | 11902 |
| ![alt text](http://pbs.twimg.com/profile_images/1249899769616613376/Jroa2xxx_normal.jpg "foto do usuário") [Angeli](https://twitter.com/Angeli20756515) | 10/04/2020 | 0.73 (756/1035) | 7269 |
| ![alt text](http://pbs.twimg.com/profile_images/1348021099771154432/kNJCneqo_normal.png "foto do usuário") [Jade Brasil](https://twitter.com/BrasilJade) | 29/09/2019 | 0.555 (402/724) | 11960 |
| ![alt text](http://pbs.twimg.com/profile_images/1348357339154362370/OPsIiKgN_normal.jpg "foto do usuário") [RP](https://twitter.com/eaipartiuu) | 09/04/2019 | 0.514 (169/329) | 1287 |
| ![alt text](http://pbs.twimg.com/profile_images/1250255507727753219/vRpIsd9k_normal.jpg "foto do usuário") [Bud](https://twitter.com/ronaldcontador) | 03/05/2011 | 0.091 (36/394) | 3164 |
| ![alt text](http://pbs.twimg.com/profile_images/1318372288593612802/G6kPA1Dt_normal.jpg "foto do usuário") [Nilson](https://twitter.com/NilsonR56) | 19/06/2013 | 0.356 (202/568) | 8948 |
| ![alt text](http://pbs.twimg.com/profile_images/1275172883157958663/Uq0T7zNq_normal.jpg "foto do usuário") [Tonn Carvalho](https://twitter.com/carvalho_tonn) | 15/05/2020 | 0.35 (55/157) | 7499 |
| ![alt text](http://pbs.twimg.com/profile_images/1256985363291275264/d4o7Itjw_normal.jpg "foto do usuário") [Rosely](https://twitter.com/RoselyViveiros) | 09/07/2010 | 2.027 (298/147) | 22707 |
| ![alt text](http://pbs.twimg.com/profile_images/1326654060611723265/B5r99LUS_normal.jpg "foto do usuário") [Patricia Bolsonaro](https://twitter.com/PatriciaBolson5) | 11/11/2020 | 0.474 (55/116) | 178 |
| ![alt text](http://pbs.twimg.com/profile_images/1351241579646906368/Cmk1VjMF_normal.jpg "foto do usuário") [tomás marabo](https://twitter.com/MaraboTomas) | 08/11/2019 | 0.237 (171/720) | 15543 |
| ![alt text](http://pbs.twimg.com/profile_images/1345027136139255808/eSahX192_normal.jpg "foto do usuário") [Sócio Colorado](https://twitter.com/_SocioColorado) | 29/11/2016 | 1.245 (681/547) | 19881 |
| ![alt text](http://pbs.twimg.com/profile_images/1214549763720388608/29UIqVxj_normal.jpg "foto do usuário") [Dougla Anselmo👉👌](https://twitter.com/AnselmoDougla) | 05/01/2020 | 0.091 (19/209) | 3811 |
| ![alt text](http://pbs.twimg.com/profile_images/1355218092410941440/uRZv61te_normal.jpg "foto do usuário") [Eduardo](https://twitter.com/Odraude_1980) | 06/11/2020 | 0.855 (744/870) | 837 |
| ![alt text](http://pbs.twimg.com/profile_images/1317148608114950146/QFhggKzE_normal.jpg "foto do usuário") [M. Toscano 🇧🇷🇧🇷🇧🇷](https://twitter.com/MTJumper) | 04/05/2009 | 0.575 (1154/2008) | 4290 |
| ![alt text](http://pbs.twimg.com/profile_images/1328736568811597829/YjyiEF7K_normal.jpg "foto do usuário") [Michelangelo](https://twitter.com/sem_estressee) | 02/10/2019 | 0.559 (19/34) | 622 |
| ![alt text](http://pbs.twimg.com/profile_images/1254572938206105611/xQ2WJvYA_normal.jpg "foto do usuário") [Luciano Mendes](https://twitter.com/Luciano07466549) | 19/09/2018 | 0.373 (88/236) | 3063 |
| ![alt text](http://pbs.twimg.com/profile_images/1352370265179762688/txiDM5vh_normal.jpg "foto do usuário") [Ogge Santos 🇧🇷🇺🇦](https://twitter.com/ogge_san) | 12/12/2018 | 0.43 (446/1038) | 10322 |
| ![alt text](http://pbs.twimg.com/profile_images/1279199652051632128/YAr7piW8_normal.jpg "foto do usuário") [Bruno Oss🇧🇷🇺🇸🇮🇱](https://twitter.com/yossefoss) | 23/06/2013 | 1.052 (1130/1074) | 14113 |
| ![alt text](http://pbs.twimg.com/profile_images/1141063179897909249/BtA_eMHl_normal.jpg "foto do usuário") [Daniel Lara de Souza](https://twitter.com/DanielLaraBass) | 18/06/2019 | 0.377 (114/302) | 2462 |
| ![alt text](http://pbs.twimg.com/profile_images/1342417999928688643/fZI4-BEl_normal.jpg "foto do usuário") [jo santi](https://twitter.com/josanti15) | 21/10/2019 | 1.022 (1252/1225) | 27621 |
| ![alt text](http://pbs.twimg.com/profile_images/1351117540546785281/3R3Np-Sj_normal.jpg "foto do usuário") [eliana braga 🇧🇷](https://twitter.com/elianabragam) | 06/06/2009 | 0.896 (4406/4916) | 44561 |
| ![alt text](http://pbs.twimg.com/profile_images/1347855028967628801/gbK1AIv9_normal.jpg "foto do usuário") [Walter Rodrigues🤡](https://twitter.com/WalterRDgues) | 09/09/2020 | 0.642 (990/1541) | 6752 |
| ![alt text](http://pbs.twimg.com/profile_images/1347940914694664192/ER_g6XuF_normal.jpg "foto do usuário") [Canal da Cultura](https://twitter.com/CulturaDa) | 18/02/2016 | 0.08 (7/87) | 1402 |
| ![alt text](http://pbs.twimg.com/profile_images/1283735623229210625/o80JgmHM_normal.jpg "foto do usuário") [Luiz Miguel Balbuena 🇧🇷](https://twitter.com/lumiba12) | 28/01/2012 | 0.361 (366/1015) | 10935 |
| ![alt text](http://pbs.twimg.com/profile_images/1234912516901396481/AOKIrneo_normal.jpg "foto do usuário") [Y](https://twitter.com/Nemesiskk) | 17/10/2017 | 0.108 (13/120) | 1359 |
| ![alt text](http://pbs.twimg.com/profile_images/1233816369206087680/sZAREguV_normal.jpg "foto do usuário") [Eric](https://twitter.com/Eric18394463) | 29/02/2020 | 0.056 (8/144) | 547 |
| ![alt text](http://pbs.twimg.com/profile_images/1273680894805585924/iFAapm1C_normal.jpg "foto do usuário") [Vigilante da Ciência](https://twitter.com/Vigilante3757) | 27/12/2015 | 2.429 (17/7) | 2599 |
| ![alt text](http://pbs.twimg.com/profile_images/1348802570454790150/VtE8bxYJ_normal.jpg "foto do usuário") [Joseane🇧🇷🇺🇸🇳🇮](https://twitter.com/CleideJoseane) | 02/03/2019 | 0.809 (3430/4241) | 3816 |
| ![alt text](http://pbs.twimg.com/profile_images/1335183725345247232/UWP66IeE_normal.jpg "foto do usuário") [Alex S.ᵉᶜᵇ 🇱🇺 | (32/45) | 🚜 CALOTEIRIZADO 🤠](https://twitter.com/swaglex19) | 13/12/2009 | 11.191 (2753/246) | 9061 |
| ![alt text](http://pbs.twimg.com/profile_images/1044676340534964224/FV_lxZBo_normal.jpg "foto do usuário") [MDegani- 🇧🇷🇧🇷🇧🇷](https://twitter.com/degani_m) | 27/08/2018 | 0.779 (2336/3000) | 95204 |
| ![alt text](http://pbs.twimg.com/profile_images/1340440639570370562/BxMklHNj_normal.jpg "foto do usuário") [Adriano](https://twitter.com/Adriano34071239) | 13/09/2020 | 0.633 (361/570) | 15531 |
| ![alt text](http://pbs.twimg.com/profile_images/1334698094366236673/KRWd0diW_normal.jpg "foto do usuário") [Júlia🇧🇷 🦋🎱🥣](https://twitter.com/julia_rafaelad) | 29/07/2016 | 0.76 (787/1036) | 34882 |
| ![alt text](http://pbs.twimg.com/profile_images/1133762492491026432/qo9izI-Y_normal.jpg "foto do usuário") [Elizabete Maria Gomes Gomes](https://twitter.com/Elizabe74882200) | 29/05/2019 | 0.132 (5/38) | 560 |
| ![alt text](http://pbs.twimg.com/profile_images/1080166096932667394/0GNaGmLl_normal.jpg "foto do usuário") [Angelina Maria](https://twitter.com/Angelinadosul) | 20/02/2017 | 0.775 (879/1134) | 3011 |
| ![alt text](http://pbs.twimg.com/profile_images/1283915324128100353/znUYecnj_normal.jpg "foto do usuário") [AMIR](https://twitter.com/AMIR61297855) | 17/07/2020 | 0.966 (5241/5424) | 7387 |
| ![alt text](http://pbs.twimg.com/profile_images/1352448254332559361/-Cgs5uAc_normal.jpg "foto do usuário") [Vilma Thomas Costa](https://twitter.com/VilmaThomasCos1) | 26/02/2020 | 1.001 (5247/5244) | 25385 |
| ![alt text](http://pbs.twimg.com/profile_images/1287224782640033793/7lp22b7u_normal.jpg "foto do usuário") [Leandro 🔰Brasil acima de todos,incluso o governo](https://twitter.com/Sergio64029292) | 21/07/2019 | 1.0 (245/245) | 12282 |
| ![alt text](http://pbs.twimg.com/profile_images/1176674930802475008/-nAGxO5H_normal.jpg "foto do usuário") [sem ideologia](https://twitter.com/pixoty100) | 15/11/2009 | 0.682 (15/22) | 2684 |
| ![alt text](http://pbs.twimg.com/profile_images/1263919702725865473/ZgPvNHYj_normal.jpg "foto do usuário") [Liana Santa Ritta](https://twitter.com/RittaLiana) | 02/03/2019 | 0.975 (2516/2580) | 30392 |
| ![alt text](http://pbs.twimg.com/profile_images/1299727173465632770/wC5Omq9__normal.jpg "foto do usuário") [Luc Az- 🇧🇷🇧🇷](https://twitter.com/DrLuc_Azevedo) | 12/12/2011 | 6.902 (6170/894) | 3035 |
| ![alt text](http://pbs.twimg.com/profile_images/1257462705096740866/VYXNrbz9_normal.jpg "foto do usuário") [Maria Brasil](https://twitter.com/MariaFPatriota1) | 22/06/2019 | 2.22 (131/59) | 6194 |
| ![alt text](http://pbs.twimg.com/profile_images/1347380254034243592/HJNFgg8V_normal.jpg "foto do usuário") [Eduardo](https://twitter.com/educardinal) | 29/05/2013 | 17.313 (19997/1155) | 109528 |
| ![alt text](http://pbs.twimg.com/profile_images/1240637351132647430/Z1LmDQBd_normal.jpg "foto do usuário") [ClauGoetten 🇧🇷](https://twitter.com/ClauSkywalker1) | 23/09/2017 | 0.939 (1148/1222) | 2275 |
| ![alt text](http://pbs.twimg.com/profile_images/1354275567944802306/hOkWSHiu_normal.jpg "foto do usuário") [LukaumSK8X2](https://twitter.com/LukaumSk8x22) | 26/08/2020 | 0.589 (123/209) | 8031 |
| ![alt text](http://pbs.twimg.com/profile_images/1344122631528849409/x9Ywy9qq_normal.jpg "foto do usuário") [Ancap Chopper 🐒#SVG](https://twitter.com/AncapChopper) | 17/06/2020 | 1.905 (362/190) | 8299 |
| ![alt text](http://pbs.twimg.com/profile_images/1348234016131084288/TyfJvcQm_normal.jpg "foto do usuário") [wagner](https://twitter.com/conservador2022) | 16/04/2020 | 0.91 (6856/7535) | 25223 |
| ![alt text](http://pbs.twimg.com/profile_images/1346149020964691972/lpY3yqK0_normal.jpg "foto do usuário") [Dayvson Fernandes 🇧🇷](https://twitter.com/DayvsonFernands) | 18/08/2009 | 1.044 (143/137) | 1527 |
| ![alt text](http://pbs.twimg.com/profile_images/1351195001783537670/juenGodz_normal.jpg "foto do usuário") [Figueiredo Jorge](https://twitter.com/FigueiredoJor) | 08/12/2012 | 1446.0 (2892/2) | 54716 |
| ![alt text](http://pbs.twimg.com/profile_images/1254524539800899585/5QsoFa9f_normal.jpg "foto do usuário") [Mauro Cesar Severino](https://twitter.com/MauroCesarSeve1) | 26/04/2020 | 0.164 (35/213) | 1221 |
| ![alt text](http://pbs.twimg.com/profile_images/1279802934373605377/YIWgvUkZ_normal.jpg "foto do usuário") [everaluz🇧🇷💚💛💚🇧🇷🇮🇱🇺🇸🇧🇷](https://twitter.com/everaluz) | 19/08/2009 | 0.52 (521/1002) | 3113 |
| ![alt text](http://pbs.twimg.com/profile_images/1349410947597742080/Q9veU-ZX_normal.jpg "foto do usuário") [Politicamente Sincero](https://twitter.com/PoliticamenteS7) | 10/07/2019 | 0.092 (11/119) | 4381 |
| ![alt text](http://pbs.twimg.com/profile_images/1239254317024055298/hOdeXxfV_normal.jpg "foto do usuário") [Ronaldo Schork Jr](https://twitter.com/ronaldoschorkjr) | 18/04/2009 | 0.386 (186/482) | 1340 |
| ![alt text](http://pbs.twimg.com/profile_images/1350105587112157186/Rr1f5na0_normal.jpg "foto do usuário") [SR RAMOS.🇧🇷🇧🇷🇧🇷](https://twitter.com/ROMEORA12323981) | 30/01/2020 | 0.734 (1109/1510) | 14011 |
| ![alt text](http://pbs.twimg.com/profile_images/1350280025485008897/Lfgoc-yK_normal.jpg "foto do usuário") [Cristiane](https://twitter.com/Crisfarias38) | 15/04/2019 | 0.915 (1610/1760) | 29510 |
| ![alt text](http://pbs.twimg.com/profile_images/1112137574963920897/lXljZdsP_normal.png "foto do usuário") [Sylberman](https://twitter.com/Sylberman1) | 20/06/2018 | 0.335 (116/346) | 21732 |
| ![alt text](http://pbs.twimg.com/profile_images/1266884278350237696/Pd8klBOp_normal.jpg "foto do usuário") [CharlesReis](https://twitter.com/Charles84165492) | 05/01/2019 | 0.66 (198/300) | 626 |
| ![alt text](http://pbs.twimg.com/profile_images/1353499762545340416/HC1Q4FsA_normal.jpg "foto do usuário") [Cássia: Nossa máscara virou mordaça 😶](https://twitter.com/CassiaBolso38) | 02/11/2018 | 0.989 (4332/4382) | 71430 |
| ![alt text](http://pbs.twimg.com/profile_images/1238276978228318209/XHpZ2eca_normal.jpg "foto do usuário") [João 8:32🇧🇷](https://twitter.com/joao_jb38) | 03/09/2009 | 1.149 (4284/3728) | 21047 |
| ![alt text](http://pbs.twimg.com/profile_images/1295797297935196163/PKkxIJjp_normal.jpg "foto do usuário") [DEFU DESENVOLVENDO FUTUROS](https://twitter.com/DeFu22) | 15/09/2017 | 0.354 (1626/4592) | 671 |
| ![alt text](http://pbs.twimg.com/profile_images/1114117464714035201/_XWMbtMX_normal.jpg "foto do usuário") [ricardo k s](https://twitter.com/rkucerasulzbach) | 16/04/2009 | 1.847 (2759/1494) | 102919 |
| ![alt text](http://pbs.twimg.com/profile_images/983068452884746240/lhwSxHwN_normal.jpg "foto do usuário") [Renata ARAUJO](https://twitter.com/RenataBressan73) | 03/08/2017 | 0.582 (325/558) | 4733 |
| ![alt text](http://pbs.twimg.com/profile_images/1288890536565313537/pkijDm8I_normal.jpg "foto do usuário") [Dayse BB DIA #CENSURASTF(BarelaBolsonaro 🇧🇷👉)](https://twitter.com/DayseBarela) | 26/01/2015 | 1.011 (8954/8860) | 386348 |
| ![alt text](http://pbs.twimg.com/profile_images/1340070811391111171/KOpGaphV_normal.jpg "foto do usuário") [JcWolf, o Rei Solitário](https://twitter.com/JcWolf09) | 22/01/2018 | 0.563 (209/371) | 10343 |
| ![alt text](http://pbs.twimg.com/profile_images/1336550162815180802/Fw0MMXAR_normal.jpg "foto do usuário") [Sapu](https://twitter.com/EhSapu) | 29/03/2019 | 0.367 (175/477) | 3367 |
| ![alt text](http://pbs.twimg.com/profile_images/1234827328263421952/ZOisrpBw_normal.jpg "foto do usuário") [Paulo Soares](https://twitter.com/paulinhonarede) | 09/04/2011 | 0.073 (31/423) | 1884 |
| ![alt text](http://pbs.twimg.com/profile_images/988932698260561922/PnRMjsTL_normal.jpg "foto do usuário") [Caio Zanette](https://twitter.com/zannacaio) | 16/07/2009 | 0.363 (49/135) | 4405 |
| ![alt text](http://pbs.twimg.com/profile_images/1348770636865413120/tvb3-ZSl_normal.jpg "foto do usuário") [Luciano Bat-Caverna 🌀](https://twitter.com/lucianobcaverna) | 27/05/2018 | 0.247 (156/631) | 23471 |
| ![alt text](http://pbs.twimg.com/profile_images/1353858148298326017/v5j2krTm_normal.jpg "foto do usuário") [Sr. DIREITO](https://twitter.com/carloslegori) | 10/02/2011 | 0.907 (734/809) | 36779 |
| ![alt text](http://pbs.twimg.com/profile_images/1352459243408994305/JHbiRtJG_normal.jpg "foto do usuário") [André Bicho Solto 🇧🇷⚒️](https://twitter.com/andrebichosolto) | 23/10/2019 | 0.756 (1314/1737) | 3593 |
| ![alt text](http://pbs.twimg.com/profile_images/1059316620840067082/iixtW1C1_normal.jpg "foto do usuário") [Flávio Augusto](https://twitter.com/GeracaodeValor) | 18/12/2010 | 597.469 (515018/862) | 10695 |
| ![alt text](http://pbs.twimg.com/profile_images/1310619154790207495/gESPbM1D_normal.jpg "foto do usuário") [Pedrão](https://twitter.com/Pedro78528451) | 28/09/2020 | 0.094 (5/53) | 1203 |
| ![alt text](http://pbs.twimg.com/profile_images/1350088784080220163/Tw6jykWz_normal.jpg "foto do usuário") [Tiago Bolsonaro 2022](https://twitter.com/TiagoDe49232105) | 21/04/2020 | 0.973 (1499/1541) | 7331 |
| ![alt text](http://pbs.twimg.com/profile_images/1308976818301685761/m90BZShl_normal.jpg "foto do usuário") [REINNER CARLOS](https://twitter.com/REINNERCARLOS3) | 23/09/2020 | 0.014 (7/490) | 192 |
| ![alt text](http://pbs.twimg.com/profile_images/1349501948504977409/8N5qT3pe_normal.jpg "foto do usuário") [Dikastro](https://twitter.com/dikastro1) | 18/10/2020 | 0.309 (195/632) | 1429 |
| ![alt text](http://pbs.twimg.com/profile_images/1033854206774599680/LQdodrGU_normal.jpg "foto do usuário") [Gustavo Moura](https://twitter.com/Gustavo_Moura7) | 21/09/2014 | 0.288 (151/524) | 2208 |
| ![alt text](http://pbs.twimg.com/profile_images/1350130658664980487/f_Iv-N67_normal.jpg "foto do usuário") [Bia Kicis](https://twitter.com/Biakicis) | 17/08/2011 | 738.306 (761193/1031) | 26198 |
| ![alt text](http://pbs.twimg.com/profile_images/1350932963056357376/Y1IDHuvF_normal.jpg "foto do usuário") [Osvaldo](https://twitter.com/tedeschijr) | 18/06/2009 | 0.559 (81/145) | 6761 |
| ![alt text](http://pbs.twimg.com/profile_images/1312375061609959424/nQ4VTtzv_normal.jpg "foto do usuário") [Amanda Bueno](https://twitter.com/Blueblu45188082) | 05/07/2020 | 0.033 (18/542) | 642 |
| ![alt text](http://pbs.twimg.com/profile_images/1247688870520598528/8W-rzYjJ_normal.jpg "foto do usuário") [Oliveira](https://twitter.com/oliveira060284) | 08/04/2020 | 0.039 (6/152) | 260 |
| ![alt text](http://pbs.twimg.com/profile_images/1325932917768466432/HOFGdMoy_normal.jpg "foto do usuário") [L](https://twitter.com/LawlietLxx) | 01/06/2019 | 4.889 (132/27) | 3167 |
| ![alt text](http://pbs.twimg.com/profile_images/1348959331912450049/-V9_kO2A_normal.jpg "foto do usuário") [Fernando Maciel 🇧🇷🇮🇱🇺🇸](https://twitter.com/Feemaciel) | 07/01/2011 | 1.096 (583/532) | 1261 |
| ![alt text](http://pbs.twimg.com/profile_images/1354636714824892417/IbQRFVu5_normal.jpg "foto do usuário") [Zolbec](https://twitter.com/zolbec) | 15/06/2020 | 3.691 (358/97) | 6492 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Paulo Rogerio](https://twitter.com/PauloRo17083734) | 06/10/2020 | 0.034 (6/177) | 496 |
| ![alt text](http://pbs.twimg.com/profile_images/1350895222918676482/ErBvtMT0_normal.jpg "foto do usuário") [Rosmary 🇧🇷🇧🇷🇧🇷🇧🇷🇧🇷🇧🇷](https://twitter.com/Rosmary79076573) | 31/10/2018 | 0.676 (855/1265) | 4337 |
| ![alt text](http://pbs.twimg.com/profile_images/1255007024695390210/EUjdCFkC_normal.jpg "foto do usuário") [Brasileiro](https://twitter.com/ThiagooterrorNE) | 19/07/2017 | 1.421 (1056/743) | 108503 |
| ![alt text](http://pbs.twimg.com/profile_images/1251224406682107906/iSITHPw__normal.jpg "foto do usuário") [Marcos Farias](https://twitter.com/Mpafarias3) | 18/06/2017 | 0.545 (157/288) | 13233 |
| ![alt text](http://pbs.twimg.com/profile_images/1330974564747194368/Bkg2ZdXe_normal.jpg "foto do usuário") [Sylvia 🇧🇷](https://twitter.com/SylviaMinion2) | 09/11/2019 | 0.686 (1314/1916) | 15858 |
| ![alt text](http://pbs.twimg.com/profile_images/1267328235542585350/W8Z4Kdu8_normal.jpg "foto do usuário") [Josué Gomes](https://twitter.com/eujosuegomes) | 22/10/2009 | 2.92 (3898/1335) | 5359 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [gualdino campos](https://twitter.com/CamposGualdino) | 21/09/2020 | 0.326 (30/92) | 839 |
| ![alt text](http://pbs.twimg.com/profile_images/1257371194283773952/cKLZIQAI_normal.jpg "foto do usuário") [#vida](https://twitter.com/nivalzinhoooo) | 15/03/2014 | 0.417 (396/950) | 12108 |
| ![alt text](http://pbs.twimg.com/profile_images/1330892724363517954/5avi6pl2_normal.jpg "foto do usuário") [Elisa 🇧🇷](https://twitter.com/lyzaa_) | 23/07/2011 | 1.875 (707/377) | 8343 |
| ![alt text](http://pbs.twimg.com/profile_images/1348372051283894279/D9on-ee4_normal.jpg "foto do usuário") [Henrique Silva](https://twitter.com/Henriqu53465330) | 27/09/2020 | 0.174 (8/46) | 896 |
| ![alt text](http://pbs.twimg.com/profile_images/1255975652982915080/8p8fZ3uC_normal.jpg "foto do usuário") [@suelioliveirarp](https://twitter.com/Suelioliveirarp) | 02/03/2020 | 1.115 (5038/4520) | 5054 |
| ![alt text](http://pbs.twimg.com/profile_images/1266347452640174081/v4dOEBhx_normal.jpg "foto do usuário") [Eng Leonardo](https://twitter.com/EngLeoOficial) | 19/05/2020 | 25.608 (5096/199) | 4180 |
| ![alt text](http://pbs.twimg.com/profile_images/1302381140695830529/mYqcAJnO_normal.jpg "foto do usuário") [Emperor Soros](https://twitter.com/brunohesc) | 20/04/2014 | 0.183 (120/655) | 3377 |
| ![alt text](http://pbs.twimg.com/profile_images/1333907381873414146/iMBP5LNp_normal.jpg "foto do usuário") [isto mesmo.](https://twitter.com/Diogvs) | 07/12/2011 | 0.339 (130/383) | 2791 |
| ![alt text](http://pbs.twimg.com/profile_images/1350894178641833986/bXbOiIdL_normal.jpg "foto do usuário") [Heitor Kombeteiro x2](https://twitter.com/Hei1999) | 13/05/2011 | 0.684 (256/374) | 13257 |
| ![alt text](http://pbs.twimg.com/profile_images/1243299826919407616/1puOlnYt_normal.jpg "foto do usuário") [Dougllas Pierre](https://twitter.com/dougllaspierre) | 21/09/2009 | 0.267 (355/1328) | 8174 |
| ![alt text](http://pbs.twimg.com/profile_images/1351797161839755265/D8gm4A9u_normal.jpg "foto do usuário") [Isuannon - #NaçãoVerde💚](https://twitter.com/Aourus_) | 27/04/2018 | 0.655 (148/226) | 4537 |
| ![alt text](http://pbs.twimg.com/profile_images/1338104297037443074/V8udosLR_normal.jpg "foto do usuário") [Kelly](https://twitter.com/KelinhaAssis) | 09/02/2010 | 1.138 (16276/14302) | 15282 |
| ![alt text](http://pbs.twimg.com/profile_images/1319683610425831425/81erPQ-S_normal.jpg "foto do usuário") [Xbot YXBA](https://twitter.com/XXBBOOXX11) | 18/03/2020 | 0.4 (14/35) | 1572 |
| ![alt text](http://pbs.twimg.com/profile_images/1348427633839771649/fmvDaWUR_normal.jpg "foto do usuário") [Luiz Reimann ❎](https://twitter.com/LuizReimann) | 22/10/2016 | 4.463 (299/67) | 2783 |
| ![alt text](http://pbs.twimg.com/profile_images/1340684408467185664/usl8G7o7_normal.jpg "foto do usuário") [L05💲](https://twitter.com/leoaugusto05) | 07/05/2019 | 0.622 (239/384) | 5886 |
| ![alt text](http://pbs.twimg.com/profile_images/1299180084822192129/v0Y8Q-5V_normal.jpg "foto do usuário") [Will ✠](https://twitter.com/WilliamHalfhand) | 12/07/2016 | 1.981 (210/106) | 7556 |
| ![alt text](http://pbs.twimg.com/profile_images/1246899174907486210/WS52SZjY_normal.jpg "foto do usuário") [Marlene](https://twitter.com/Marlene37486699) | 07/01/2020 | 0.414 (67/162) | 5670 |
| ![alt text](http://pbs.twimg.com/profile_images/1254919742894284800/THyZjfl-_normal.png "foto do usuário") [David Ágape 🕵️‍♂️](https://twitter.com/david_agape_) | 19/10/2018 | 1.211 (367/303) | 2777 |
| ![alt text](http://pbs.twimg.com/profile_images/1354176127720423424/tc9eFLrS_normal.jpg "foto do usuário") [Embelleze Oficial](https://twitter.com/Embelleze) | 09/04/2009 | 9.252 (18652/2016) | 5961 |
| ![alt text](http://pbs.twimg.com/profile_images/1347210304778891264/Qb0Ao-L3_normal.jpg "foto do usuário") [MarcoJr013](https://twitter.com/Jr013Marco) | 26/08/2018 | 0.373 (60/161) | 1177 |
| ![alt text](http://pbs.twimg.com/profile_images/1300904513344339976/cBdI6NO7_normal.jpg "foto do usuário") [Kleber SCCP](https://twitter.com/krebito) | 27/12/2018 | 0.429 (297/692) | 11220 |
| ![alt text](http://pbs.twimg.com/profile_images/1254577821671919616/GLiaFff-_normal.jpg "foto do usuário") [🔰A.R.M.S. 📢〰〰️〰〰️ 🛡️⚔️](https://twitter.com/AUSTRALIANO1980) | 29/06/2009 | 1.015 (2658/2619) | 83584 |
| ![alt text](http://pbs.twimg.com/profile_images/1291080192929259520/S8znWC4K_normal.jpg "foto do usuário") [Brasil Sem Medo](https://twitter.com/JornalBSM) | 03/12/2019 | 1572.484 (298772/190) | 5221 |
| ![alt text](http://pbs.twimg.com/profile_images/1229955848941842432/Sf5d2kOV_normal.jpg "foto do usuário") [Carreta Furacao](https://twitter.com/CaarretaFuracao) | 19/05/2016 | 4.0 (4/1) | 331 |
| ![alt text](http://pbs.twimg.com/profile_images/1122811578796130305/YPHrPvQ5_normal.png "foto do usuário") [FreiTas](https://twitter.com/FreiTas39495616) | 16/10/2018 | 1.93 (1330/689) | 28983 |
| ![alt text](http://pbs.twimg.com/profile_images/1338842376689901571/V6MU2rnF_normal.jpg "foto do usuário") [4% É MTU !! #RUMOAOTETRA](https://twitter.com/outroplaneta20) | 21/12/2017 | 0.075 (61/810) | 691 |
| ![alt text](http://pbs.twimg.com/profile_images/1274919632659456005/L5D4HI79_normal.jpg "foto do usuário") [André Vicente](https://twitter.com/AndreVicente9) | 28/01/2012 | 1.231 (655/532) | 19326 |
| ![alt text](http://pbs.twimg.com/profile_images/1298055083389788163/pXrgd1ZN_normal.jpg "foto do usuário") [🇪🇪 Alemão 🇪🇪](https://twitter.com/Alemao_839517) | 12/02/2011 | 0.272 (77/283) | 2317 |
| ![alt text](http://pbs.twimg.com/profile_images/1342659847448383489/CgcuSPHO_normal.jpg "foto do usuário") [gummo #vaifiuk](https://twitter.com/_gvmmos) | 17/02/2019 | 28.364 (6694/236) | 21475 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Eduardo](https://twitter.com/Eduardoadv19) | 24/10/2019 | 0.022 (9/410) | 246 |
| ![alt text](http://pbs.twimg.com/profile_images/726618346402242560/8Hg9IU72_normal.jpg "foto do usuário") [Profiles Police](https://twitter.com/profilespolice) | 25/04/2016 | 0.188 (9/48) | 149 |
| ![alt text](http://pbs.twimg.com/profile_images/1299722550751170560/HP2SyZux_normal.jpg "foto do usuário") [Robson Pinto](https://twitter.com/RobsonP94564295) | 19/05/2020 | 0.872 (1952/2238) | 5961 |
| ![alt text](http://pbs.twimg.com/profile_images/1308862180692037633/sYGr95zb_normal.jpg "foto do usuário") [MrDarkness868™ #TeamKong](https://twitter.com/MrDarkness868) | 03/11/2014 | 0.608 (115/189) | 1899 |
| ![alt text](http://pbs.twimg.com/profile_images/1252289600615219201/vQosZ6sN_normal.jpg "foto do usuário") [T-800](https://twitter.com/Skinet20517523) | 23/01/2020 | 0.818 (604/738) | 7648 |
| ![alt text](http://pbs.twimg.com/profile_images/625910485863546880/koz6wx60_normal.jpg "foto do usuário") [Ursinho Embuste ✌](https://twitter.com/DJ_luisao) | 17/08/2009 | 0.487 (635/1305) | 36451 |
| ![alt text](http://pbs.twimg.com/profile_images/1272339035667730432/WFLIqHKE_normal.jpg "foto do usuário") [Isaque 🇧🇷](https://twitter.com/Isaque45153048) | 05/02/2019 | 0.935 (5177/5539) | 8911 |
| ![alt text](http://pbs.twimg.com/profile_images/1300969854485303297/7sztnYwc_normal.jpg "foto do usuário") [Aprendiz_Do_Zap](https://twitter.com/mia_sandro) | 21/08/2020 | 0.205 (41/200) | 1193 |
| ![alt text](http://pbs.twimg.com/profile_images/1314591452626915328/3VxYKqFD_normal.jpg "foto do usuário") [Jowandowski 7° conta](https://twitter.com/Josu69542733) | 30/04/2020 | 0.074 (16/217) | 1726 |
| ![alt text](http://pbs.twimg.com/profile_images/1350129350444802052/jhmeyE8d_normal.jpg "foto do usuário") [𝙰𝚗𝚍 𝙼𝚛𝚜 ¯\_(ツ)_/¯](https://twitter.com/AndrMrs2) | 28/07/2020 | 0.09 (30/332) | 1020 |
| ![alt text](http://pbs.twimg.com/profile_images/1351697671745056768/_0C0v_ST_normal.jpg "foto do usuário") [Dan H.](https://twitter.com/DanHashima) | 05/10/2010 | 0.672 (119/177) | 2991 |
| ![alt text](http://pbs.twimg.com/profile_images/3117591989/97d398ef43a4308dd57aa4f8634fc2c3_normal.jpeg "foto do usuário") [Mauricio Finotti](https://twitter.com/maufinotti) | 01/09/2010 | 0.375 (249/664) | 3449 |
| ![alt text](http://pbs.twimg.com/profile_images/1346285731690512384/d4-p4kbg_normal.jpg "foto do usuário") [🅴🆃 🆂🅸🅽🅲🅴🆁🅾 €Ø₦₮₳ ɌɆ$ɆɌ⩔₳](https://twitter.com/ETcontroverso) | 27/06/2019 | 0.912 (10700/11732) | 25050 |
| ![alt text](http://pbs.twimg.com/profile_images/1275306683573641224/5KNIpib1_normal.jpg "foto do usuário") [CARLOS DAMASCENO](https://twitter.com/_CARLOSDAM) | 05/04/2013 | 0.217 (26/120) | 2776 |
| ![alt text](http://pbs.twimg.com/profile_images/1260721676834258945/85Xi0wMp_normal.jpg "foto do usuário") [daniel machado](https://twitter.com/danielm01261009) | 13/05/2020 | 0.591 (97/164) | 1010 |
| ![alt text](http://pbs.twimg.com/profile_images/1280121610322808834/O2fjM5mQ_normal.jpg "foto do usuário") [memóriacurta](https://twitter.com/TomLiz3) | 03/11/2018 | 0.163 (27/166) | 2484 |
| ![alt text](http://pbs.twimg.com/profile_images/1092377953336549377/caK1xi65_normal.jpg "foto do usuário") [Guilherme Salomão](https://twitter.com/GLCSalomao) | 23/07/2017 | 0.085 (33/388) | 8557 |
| ![alt text](http://pbs.twimg.com/profile_images/1187176975066120192/_nTROd8A_normal.jpg "foto do usuário") [Davis](https://twitter.com/davissp1) | 12/10/2018 | 0.563 (853/1515) | 2612 |
| ![alt text](http://pbs.twimg.com/profile_images/1284169620824498176/O-ghmQdz_normal.jpg "foto do usuário") [Kelly](https://twitter.com/Kelly30br) | 31/07/2009 | 0.803 (3838/4777) | 46284 |
| ![alt text](http://pbs.twimg.com/profile_images/1354070609974550529/zmLvVw3Q_normal.jpg "foto do usuário") [Daniel Paul](https://twitter.com/DanielP58009529) | 25/08/2020 | 0.458 (1331/2909) | 11152 |
| ![alt text](http://pbs.twimg.com/profile_images/1354122141827006466/6t8OKmfQ_normal.jpg "foto do usuário") [Dumpzz ∆](https://twitter.com/Dumpzz5) | 28/09/2020 | 0.597 (142/238) | 4556 |
| ![alt text](http://pbs.twimg.com/profile_images/1354122141827006466/6t8OKmfQ_normal.jpg "foto do usuário") [Dumpzz ∆](https://twitter.com/Dumpzz5) | 28/09/2020 | 0.598 (143/239) | 4556 |
| ![alt text](http://pbs.twimg.com/profile_images/1339539759555899394/ROgpKn1e_normal.jpg "foto do usuário") [⚡Yuna Lightning⚡🎮△◯X▢](https://twitter.com/Yuna_br21) | 19/10/2019 | 14.589 (1313/90) | 11603 |
| ![alt text](http://pbs.twimg.com/profile_images/778733727568371713/oqxSZ6Mg_normal.jpg "foto do usuário") [Patrícia Vaz](https://twitter.com/patygarciavaz) | 21/09/2016 | 0.378 (74/196) | 841 |
| ![alt text](http://pbs.twimg.com/profile_images/1347785548270854145/XiipHYuP_normal.jpg "foto do usuário") [Son Gohan](https://twitter.com/son_gohan25) | 04/02/2018 | 0.213 (201/944) | 1316 |
| ![alt text](http://pbs.twimg.com/profile_images/1329434280125140997/d9x-bCLx_normal.jpg "foto do usuário") [Ivan Silva 🇧🇷 Direita Burra!](https://twitter.com/IvanSilvaNavi) | 06/07/2018 | 0.834 (825/989) | 35432 |
| ![alt text](http://pbs.twimg.com/profile_images/1326859315496562693/EKlKzfoW_normal.jpg "foto do usuário") [Al Leong Blockchain DeFi Fintech CEO CMO Advisor](https://twitter.com/iDesignStrategy) | 18/10/2011 | 165.838 (124876/753) | 3267 |
| ![alt text](http://pbs.twimg.com/profile_images/1224821501846749184/uMijsZ_D_normal.jpg "foto do usuário") [jonhson salles 🤡](https://twitter.com/jonhrecife) | 28/11/2014 | 0.424 (235/554) | 10331 |
| ![alt text](http://pbs.twimg.com/profile_images/1194569347550908418/xkG58XQm_normal.jpg "foto do usuário") [Claus](https://twitter.com/claus_2019) | 15/08/2019 | 0.0 (0/38) | 6896 |
| ![alt text](http://pbs.twimg.com/profile_images/1238871631352791041/ZGCbLiU1_normal.jpg "foto do usuário") [Americo Guazzelli 🇮🇱🇮🇹🇪🇺🇦🇷🇺🇸](https://twitter.com/uagg1982) | 11/06/2015 | 0.56 (256/457) | 5787 |
| ![alt text](http://pbs.twimg.com/profile_images/1244687373511909376/yTo9uc9T_normal.jpg "foto do usuário") [Bolsotroopers](https://twitter.com/bolsotroopers) | 30/03/2020 | 2.199 (16932/7699) | 26665 |
| ![alt text](http://pbs.twimg.com/profile_images/1298748600932065280/5Yq3wAGm_normal.jpg "foto do usuário") [Renato I.H.C.](https://twitter.com/RenatoIHC2) | 25/05/2020 | 0.716 (1917/2679) | 26730 |
| ![alt text](http://pbs.twimg.com/profile_images/1301325002185347072/07IGQy7g_normal.jpg "foto do usuário") [Humberto Sampaio](https://twitter.com/HumbertoSampai8) | 17/01/2019 | 0.159 (44/277) | 1620 |
| ![alt text](http://pbs.twimg.com/profile_images/1280195129781809157/wQMOk9dY_normal.png "foto do usuário") [Teresa](https://twitter.com/Teresa0741) | 05/10/2017 | 0.581 (147/253) | 2134 |
| ![alt text](http://pbs.twimg.com/profile_images/1290506394135928833/QcXeDndM_normal.jpg "foto do usuário") [Anderson](https://twitter.com/Anderso56252231) | 19/04/2020 | 0.45 (326/725) | 4936 |
| ![alt text](http://pbs.twimg.com/profile_images/811010789771542528/L3gswaYD_normal.jpg "foto do usuário") [Alvaro](https://twitter.com/AlvaroTemporim) | 11/12/2015 | 0.717 (3577/4989) | 5734 |
| ![alt text](http://pbs.twimg.com/profile_images/1051818386525687808/fyhLzrsL_normal.jpg "foto do usuário") [PandaDemocrático](https://twitter.com/PandaDemocrtic1) | 08/10/2018 | 0.19 (47/247) | 1941 |
| ![alt text](http://pbs.twimg.com/profile_images/1163985676406329344/UvYtA9Tg_normal.jpg "foto do usuário") [Eduardo o. 😎🇧🇷](https://twitter.com/edu_sdo) | 26/06/2010 | 0.078 (38/486) | 394 |
| ![alt text](http://pbs.twimg.com/profile_images/2158803375/pai_ogum_normal.jpg "foto do usuário") [Marcelo Gonzaga Sampaio](https://twitter.com/margonsam) | 02/07/2009 | 0.273 (265/969) | 5440 |
| ![alt text](http://pbs.twimg.com/profile_images/1216389612467257346/occ2qVWi_normal.jpg "foto do usuário") [Magnun Coutinho](https://twitter.com/mcesar25) | 15/06/2010 | 0.468 (102/218) | 4016 |
| ![alt text](http://pbs.twimg.com/profile_images/681236274263552000/wsnDXzqr_normal.jpg "foto do usuário") [Fernando Crivoi](https://twitter.com/fcrivoi) | 15/08/2015 | 0.056 (8/144) | 322 |
| ![alt text](http://pbs.twimg.com/profile_images/1174849196/Grand_Canyon_USA_05-4_normal.JPG "foto do usuário") [Ronaldo Tomé](https://twitter.com/ronaldotome) | 10/03/2009 | 0.856 (368/430) | 16970 |
| ![alt text](http://pbs.twimg.com/profile_images/1069279064932913153/Uz-VZQeP_normal.jpg "foto do usuário") [Alceu Garcia🇦🇹🇧🇷🇬🇧](https://twitter.com/GarciaAlceu) | 29/05/2013 | 0.382 (47/123) | 10802 |
| ![alt text](http://pbs.twimg.com/profile_images/1018841110515474432/mHVL1tIR_normal.jpg "foto do usuário") [Rafael Menin](https://twitter.com/rafaelmeninsouz) | 29/09/2010 | 268.128 (96258/359) | 1671 |
| ![alt text](http://pbs.twimg.com/profile_images/872191039603343360/YrzayaYI_normal.jpg "foto do usuário") [Regnon Molina](https://twitter.com/regnonmolina) | 02/04/2009 | 0.478 (163/341) | 4136 |
| ![alt text](http://pbs.twimg.com/profile_images/1350735151442120704/jw52TLFS_normal.jpg "foto do usuário") [🇧🇷 GUINA .🇧🇷 🇧🇷 🇧🇷 🇧🇷](https://twitter.com/AgnaldoPontara) | 12/03/2013 | 0.408 (665/1630) | 26813 |
| ![alt text](http://pbs.twimg.com/profile_images/1355216750284042245/-39Xop8r_normal.jpg "foto do usuário") [ohohoho](https://twitter.com/tellmeaac1) | 14/04/2017 | 0.097 (31/321) | 307 |
| ![alt text](http://pbs.twimg.com/profile_images/1195255868540907520/IT6Cc5zW_normal.jpg "foto do usuário") [Faustino Oliver](https://twitter.com/faustsoli) | 23/10/2019 | 0.156 (30/192) | 402 |
| ![alt text](http://pbs.twimg.com/profile_images/1268107337925001216/-3rmXm1K_normal.jpg "foto do usuário") [Eletricista Bad ⚡🇧🇷](https://twitter.com/GeoquimicaE) | 11/12/2019 | 0.086 (77/893) | 1695 |
| ![alt text](http://pbs.twimg.com/profile_images/1176570301678792713/YKvA_cU6_normal.jpg "foto do usuário") [India Capitalista](https://twitter.com/IndiaCapitalist) | 22/06/2016 | 22.016 (9533/433) | 48409 |
| ![alt text](http://pbs.twimg.com/profile_images/621859861232529408/lCu05Z0E_normal.jpg "foto do usuário") [Eussauro](https://twitter.com/Azdandandan) | 17/07/2015 | 0.145 (66/455) | 2433 |
| ![alt text](http://pbs.twimg.com/profile_images/1320719377424175104/F9KyIP49_normal.jpg "foto do usuário") [メイピュー](https://twitter.com/Maypew_) | 06/10/2018 | 0.533 (368/691) | 18823 |
| ![alt text](http://pbs.twimg.com/profile_images/1308604405944647688/ydDwYbSv_normal.jpg "foto do usuário") [Sedex](https://twitter.com/Sedexmilgrau) | 22/09/2020 | 0.145 (67/462) | 329 |
| ![alt text](http://pbs.twimg.com/profile_images/1347875977842618368/fA1K1uSF_normal.jpg "foto do usuário") [N](https://twitter.com/nclhdd) | 03/01/2019 | 22.408 (5714/255) | 24498 |
| ![alt text](http://pbs.twimg.com/profile_images/1311419679609622528/YwZQ9Whr_normal.jpg "foto do usuário") [Honrar a bandeira, não queimar](https://twitter.com/avfdf) | 05/03/2012 | 0.453 (395/872) | 1485 |
| ![alt text](http://pbs.twimg.com/profile_images/1249731366754963458/G7CD3KKN_normal.jpg "foto do usuário") [Brazilian Lacroeconomic Review](https://twitter.com/lacroeconomic) | 12/04/2020 | 252.955 (11130/44) | 123 |
| ![alt text](http://pbs.twimg.com/profile_images/1285524327669157888/MZySpdnA_normal.jpg "foto do usuário") [Os Sonystas 🕶](https://twitter.com/OsSonystass) | 12/05/2020 | 0.815 (88/108) | 3536 |
| ![alt text](http://pbs.twimg.com/profile_images/493993581712252928/Buv8bzhI_normal.jpeg "foto do usuário") [Heros de Moraes](https://twitter.com/HerosMoraes) | 14/03/2009 | 0.995 (3873/3892) | 342498 |
| ![alt text](http://pbs.twimg.com/profile_images/1309845702097408000/bxd56WjE_normal.jpg "foto do usuário") [Dardo](https://twitter.com/Coringaemoringa) | 02/10/2010 | 0.334 (133/398) | 1561 |
| ![alt text](http://pbs.twimg.com/profile_images/1211342778350915584/072gF-oc_normal.jpg "foto do usuário") [@douglascri Parler 🇧🇷🇾🇪](https://twitter.com/Douglas20832354) | 29/12/2019 | 0.497 (1412/2841) | 37431 |
| ![alt text](http://pbs.twimg.com/profile_images/1328037633025511424/ezf1oLnt_normal.jpg "foto do usuário") [Marcio Andrade](https://twitter.com/marc_architect) | 04/12/2017 | 0.804 (41/51) | 633 |
| ![alt text](http://pbs.twimg.com/profile_images/1227686487099088896/vk3Cat5N_normal.jpg "foto do usuário") [Neto](https://twitter.com/Neto95523351) | 12/02/2020 | 0.229 (8/35) | 1957 |
| ![alt text](http://pbs.twimg.com/profile_images/1351678480770019330/qnVh4wwp_normal.jpg "foto do usuário") [Ticalacatica](https://twitter.com/BFFAL1) | 01/04/2015 | 0.544 (409/752) | 6686 |
| ![alt text](http://pbs.twimg.com/profile_images/1010354884158386176/a11H4igU_normal.jpg "foto do usuário") [Bruno Sousa 🤡](https://twitter.com/BrunoSousa_88) | 23/06/2018 | 0.213 (185/869) | 8240 |
| ![alt text](http://pbs.twimg.com/profile_images/1347983895933890560/M1GPtNel_normal.jpg "foto do usuário") [:)))))))))))))))))](https://twitter.com/lolwutson) | 04/02/2020 | 0.02 (17/864) | 152 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Kaue Lopes](https://twitter.com/KaueLopes2020) | 18/04/2020 | 0.062 (1/16) | 14 |
| ![alt text](http://pbs.twimg.com/profile_images/1317289418064072706/jvTzl8Es_normal.jpg "foto do usuário") [Angelo Vilchez](https://twitter.com/AngeloVilchez5) | 11/11/2019 | 0.857 (60/70) | 1351 |
| ![alt text](http://pbs.twimg.com/profile_images/1352559959767134215/_rtmHETJ_normal.jpg "foto do usuário") [PLANETA TERRA](https://twitter.com/mineirotchotcho) | 08/05/2019 | 1.012 (1877/1855) | 31093 |
| ![alt text](http://pbs.twimg.com/profile_images/1282262502756225024/bO9KEgIi_normal.jpg "foto do usuário") [Everton Filho 3️⃣8️⃣ 🇧🇷🇧🇷](https://twitter.com/Everton37073034) | 12/07/2020 | 0.628 (2593/4130) | 4675 |
| ![alt text](http://pbs.twimg.com/profile_images/1351995980107931649/0NkzeRR__normal.jpg "foto do usuário") [Darth Ërïcksøn](https://twitter.com/TheRagnarok77) | 23/02/2015 | 0.154 (22/143) | 1121 |
| ![alt text](http://pbs.twimg.com/profile_images/1213138313881833473/7Ki7X11M_normal.jpg "foto do usuário") [Pequena🇧🇷🇧🇷🇧🇷](https://twitter.com/Pequena05246490) | 03/01/2020 | 0.917 (2791/3042) | 15721 |
| ![alt text](http://pbs.twimg.com/profile_images/1354144952398344195/82V7gw5Y_normal.jpg "foto do usuário") [zeitgeist](https://twitter.com/tiraolanister) | 26/06/2020 | 0.712 (1324/1859) | 10017 |
| ![alt text](http://pbs.twimg.com/profile_images/1343344544969064448/YZbiZ5Gu_normal.jpg "foto do usuário") [Juh❤️🇧🇷](https://twitter.com/JuhZanca) | 16/10/2015 | 13.948 (29137/2089) | 37037 |
| ![alt text](http://pbs.twimg.com/profile_images/1294059194186964993/9EyGOCBD_normal.jpg "foto do usuário") [Terezinha Dias de Araújo](https://twitter.com/TerezinhaDiasd8) | 13/08/2020 | 0.931 (2535/2722) | 18907 |
| ![alt text](http://pbs.twimg.com/profile_images/1353360139747790848/tx-yfRQn_normal.jpg "foto do usuário") [Maura Martins](https://twitter.com/MauraMarts) | 03/07/2020 | 0.958 (748/781) | 7800 |
| ![alt text](http://pbs.twimg.com/profile_images/1241150290486800384/DgcPN-7j_normal.jpg "foto do usuário") [JhowJhow ✪](https://twitter.com/JhowWaifulJhow) | 08/01/2013 | 1.081 (414/383) | 10228 |
| ![alt text](http://pbs.twimg.com/profile_images/1249064370023411714/ECKZgN9a_normal.jpg "foto do usuário") [Demagogia do Oprimido 🔥](https://twitter.com/DOprimido) | 11/04/2020 | 99.541 (13239/133) | 10812 |
| ![alt text](http://pbs.twimg.com/profile_images/1323095126206521345/z8j37t74_normal.jpg "foto do usuário") [Bruno Nunes](https://twitter.com/Bruno2012) | 10/04/2009 | 0.461 (317/688) | 3538 |
| ![alt text](http://pbs.twimg.com/profile_images/1273461867151753216/IBeoTGcL_normal.jpg "foto do usuário") [Astro SpaceX](https://twitter.com/AstroSpaceXXX) | 07/07/2019 | 0.318 (232/729) | 21754 |
| ![alt text](http://pbs.twimg.com/profile_images/1289973569825525762/F5pvd6R0_normal.jpg "foto do usuário") [José Antonio](https://twitter.com/Jos65983040) | 13/04/2019 | 0.628 (766/1219) | 29083 |
| ![alt text](http://pbs.twimg.com/profile_images/1295218592829538304/7AowUr6K_normal.jpg "foto do usuário") [Ito 🇧🇷❤️](https://twitter.com/itopamito) | 25/03/2020 | 1.182 (10610/8977) | 11554 |
| ![alt text](http://pbs.twimg.com/profile_images/1348820478564179973/iqOsSW8c_normal.jpg "foto do usuário") [João Mendes 🇧🇷](https://twitter.com/joaomagmendes) | 11/01/2016 | 0.255 (178/698) | 18797 |
| ![alt text](http://pbs.twimg.com/profile_images/1353517336142217216/6LLQssqU_normal.jpg "foto do usuário") [Das Klein](https://twitter.com/daskleinfelipe) | 31/01/2011 | 0.53 (238/449) | 2540 |
| ![alt text](http://pbs.twimg.com/profile_images/1353533428960997378/3OP5o2g2_normal.jpg "foto do usuário") [💚 Nilda💛 Patriota 🇧🇷 Pernambucana🏜️](https://twitter.com/NildaPatriota) | 05/04/2019 | 1.057 (25077/23720) | 10004 |
| ![alt text](http://pbs.twimg.com/profile_images/1348194141612756992/5hBOrejX_normal.jpg "foto do usuário") [George S Patton 🇧🇷🇮🇱🇵🇱🇭🇺🇯🇵](https://twitter.com/Jambock67) | 24/08/2018 | 1.276 (16707/13089) | 96761 |
| ![alt text](http://pbs.twimg.com/profile_images/1349084933457903620/0bos_CKC_normal.jpg "foto do usuário") [Marcia 💪💪🇧🇷](https://twitter.com/ForaComunaJa) | 20/03/2018 | 1.095 (40554/37051) | 37560 |
| ![alt text](http://pbs.twimg.com/profile_images/1349216629691965440/56NdpcTS_normal.jpg "foto do usuário") [Ian Maldonado](https://twitter.com/ianmdo) | 14/09/2012 | 14.341 (14183/989) | 12059 |
| ![alt text](http://pbs.twimg.com/profile_images/1354818737912696841/II9oUeWf_normal.jpg "foto do usuário") [Zé Pistola](https://twitter.com/ZehPistola) | 23/07/2019 | 1.034 (17465/16885) | 12130 |
| ![alt text](http://pbs.twimg.com/profile_images/1329921039338442754/lF1zZLO0_normal.jpg "foto do usuário") [🌄TUTU-BARÃO #FechadosComBolsonaro](https://twitter.com/TutuBarao2106) | 25/06/2019 | 0.978 (20275/20738) | 32911 |
| ![alt text](http://pbs.twimg.com/profile_images/1353165431180300290/ZADNymvM_normal.jpg "foto do usuário") [Fabio Alexander](https://twitter.com/FabioAlexander_) | 03/03/2019 | 0.966 (2795/2894) | 13449 |
| ![alt text](http://pbs.twimg.com/profile_images/1303317897176113152/C3zyxRMU_normal.jpg "foto do usuário") [Zeca 3️⃣8️⃣](https://twitter.com/Zecauru57340622) | 12/08/2020 | 0.941 (16/17) | 329 |
| ![alt text](http://pbs.twimg.com/profile_images/1283561588931334144/9taw0PD6_normal.jpg "foto do usuário") [Erlete Ribeiro](https://twitter.com/ErleteRibeiro) | 24/06/2020 | 0.861 (4161/4835) | 5991 |
| ![alt text](http://pbs.twimg.com/profile_images/1239374373905195009/hP01Xm73_normal.jpg "foto do usuário") [Junio Amaral](https://twitter.com/cabojunioamaral) | 10/10/2017 | 257.112 (94360/367) | 1388 |
| ![alt text](http://pbs.twimg.com/profile_images/1270853462327205889/EgPdX1J4_normal.jpg "foto do usuário") [Apartments near me](https://twitter.com/ApartmentNearMe) | 07/11/2019 | 0.108 (21/194) | 1101 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Jorge Almeida](https://twitter.com/JorgeAl38550618) | 20/12/2019 | 0.037 (11/301) | 3264 |
| ![alt text](http://pbs.twimg.com/profile_images/1353741924235173889/Er37-P2I_normal.jpg "foto do usuário") [ReginaAlmeida](https://twitter.com/Regina47270842) | 30/04/2020 | 0.815 (2153/2642) | 4244 |
| ![alt text](http://pbs.twimg.com/profile_images/1309290293737422851/R_QwOJJJ_normal.jpg "foto do usuário") [renato 🇧🇷](https://twitter.com/renatofranca191) | 14/04/2020 | 0.322 (141/438) | 2638 |
| ![alt text](http://pbs.twimg.com/profile_images/1340261960886210560/Mh28rMQw_normal.jpg "foto do usuário") [Mônica Fraga](https://twitter.com/Monica_Fraga2) | 08/04/2019 | 1.477 (65946/44655) | 27310 |
| ![alt text](http://pbs.twimg.com/profile_images/1057573957422014464/Tx4_OlHG_normal.jpg "foto do usuário") [Paulo Pires](https://twitter.com/PauloPi23011918) | 31/10/2018 | 0.809 (309/382) | 3538 |
| ![alt text](http://pbs.twimg.com/profile_images/1295544304904151040/klJ6yMmD_normal.jpg "foto do usuário") [Bolsonarista 🇧🇷](https://twitter.com/Apto965) | 14/06/2020 | 1.795 (578/322) | 12184 |
| ![alt text](http://pbs.twimg.com/profile_images/1342472743074324480/5LF6FbLE_normal.jpg "foto do usuário") [XCapimBR](https://twitter.com/xcapimBr) | 18/04/2010 | 17.242 (9121/529) | 7830 |
| ![alt text](http://pbs.twimg.com/profile_images/972660089453793281/ACkUCM-6_normal.jpg "foto do usuário") [Patriotas](https://twitter.com/PATRlOTAS) | 22/01/2018 | 97.146 (219356/2258) | 27655 |
| ![alt text](http://pbs.twimg.com/profile_images/1341369243514925057/yjSLIo1l_normal.jpg "foto do usuário") [Lobotomav](https://twitter.com/lobotosasha) | 13/05/2019 | 6.584 (31075/4720) | 10486 |
| ![alt text](http://pbs.twimg.com/profile_images/1353864667375017985/m8kLyX4J_normal.jpg "foto do usuário") [Vitória](https://twitter.com/mareclausum__) | 06/05/2020 | 34.279 (12272/358) | 19820 |
| ![alt text](http://pbs.twimg.com/profile_images/1354284713389797376/4IrMoARQ_normal.jpg "foto do usuário") [#BOLSORINGA CONDENSADO](https://twitter.com/TPGOMES1) | 23/03/2020 | 0.67 (1549/2312) | 6462 |
| ![alt text](http://pbs.twimg.com/profile_images/1082422871601876992/fH_Rdz96_normal.jpg "foto do usuário") [Daniel Vieira](https://twitter.com/dv1oliveira) | 04/05/2011 | 0.271 (432/1596) | 12232 |
| ![alt text](http://pbs.twimg.com/profile_images/1309547485535375360/7M1EGI8z_normal.jpg "foto do usuário") [Daniel](https://twitter.com/DanielCarv) | 16/11/2009 | 0.094 (343/3661) | 14723 |
| ![alt text](http://pbs.twimg.com/profile_images/885722133044891649/qc932DqH_normal.jpg "foto do usuário") [Foco de Luz](https://twitter.com/focodeluz_) | 28/07/2011 | 366159.0 (732318/2) | 13059 |
| ![alt text](http://pbs.twimg.com/profile_images/1352358627546460160/b1JH_ufU_normal.jpg "foto do usuário") [Márcio Ventura 🇧🇷](https://twitter.com/MrcioVentura7) | 18/02/2020 | 0.548 (1168/2133) | 2598 |
| ![alt text](http://pbs.twimg.com/profile_images/1289533178949128192/lbgq60hC_normal.jpg "foto do usuário") [Chico](https://twitter.com/chico12527859) | 17/07/2020 | 0.0 (0/1) | 76 |
| ![alt text](http://pbs.twimg.com/profile_images/1237671434224308224/YqJoeK4__normal.jpg "foto do usuário") [formiga](https://twitter.com/Alessan50086602) | 11/03/2020 | 0.446 (103/231) | 1040 |
| ![alt text](http://pbs.twimg.com/profile_images/1136967575009726467/nkNgiiSo_normal.jpg "foto do usuário") [Leone Madureira](https://twitter.com/LeoneMadureira) | 07/06/2019 | 0.089 (18/202) | 414 |
| ![alt text](http://pbs.twimg.com/profile_images/1268172531091091462/HhH7BWPI_normal.jpg "foto do usuário") [MarioFrias](https://twitter.com/mfriasoficial) | 05/01/2020 | 753.867 (158312/210) | 1863 |
| ![alt text](http://pbs.twimg.com/profile_images/1341886058842238976/U3JFJ4Hz_normal.jpg "foto do usuário") [seydous](https://twitter.com/seydoussss) | 30/08/2015 | 0.925 (136/147) | 6303 |
| ![alt text](http://pbs.twimg.com/profile_images/1344075779471269889/ZtGvclKS_normal.jpg "foto do usuário") [pedro paulo ](https://twitter.com/pedrosebasti) | 08/11/2012 | 0.751 (3531/4701) | 20084 |
| ![alt text](http://pbs.twimg.com/profile_images/1125223994192539648/vzcqmOKV_normal.jpg "foto do usuário") [Otávio Lacerda](https://twitter.com/OtavioLacerda84) | 26/03/2018 | 0.208 (350/1684) | 8325 |
| ![alt text](http://pbs.twimg.com/profile_images/1340439435658334209/2PY1rfnO_normal.jpg "foto do usuário") [Gilmar](https://twitter.com/Gilmar10391290) | 06/03/2019 | 0.658 (273/415) | 44442 |
| ![alt text](http://pbs.twimg.com/profile_images/1350400393298251777/1JShQyw7_normal.jpg "foto do usuário") [Tiago Mesquita](https://twitter.com/paidobernardo19) | 13/09/2019 | 0.151 (70/464) | 2522 |
| ![alt text](http://pbs.twimg.com/profile_images/1345149647476690946/LRiaH2CC_normal.jpg "foto do usuário") [マテウス](https://twitter.com/Matheus22331) | 04/01/2019 | 0.538 (716/1331) | 48721 |
| ![alt text](http://pbs.twimg.com/profile_images/1196200723521982470/uQBgcH4X_normal.jpg "foto do usuário") [Shimei Takezo](https://twitter.com/musashinii) | 11/08/2013 | 0.302 (104/344) | 3687 |
| ![alt text](http://pbs.twimg.com/profile_images/1319098953074429952/MVcJ0zjE_normal.jpg "foto do usuário") [eder junior](https://twitter.com/ederjuniors97) | 10/04/2011 | 0.483 (143/296) | 2134 |
| ![alt text](http://pbs.twimg.com/profile_images/1319098953074429952/MVcJ0zjE_normal.jpg "foto do usuário") [eder junior](https://twitter.com/ederjuniors97) | 10/04/2011 | 0.483 (143/296) | 2134 |
| ![alt text](http://pbs.twimg.com/profile_images/895079491784945665/ZgT9yuTi_normal.jpg "foto do usuário") [REGINA DINIZ OUTEIRO](https://twitter.com/REGINAOUTEIRO) | 23/11/2009 | 0.844 (1177/1394) | 108932 |
| ![alt text](http://pbs.twimg.com/profile_images/1355353411462561795/cdVbjZ-X_normal.jpg "foto do usuário") [Iracema Da Costa 🇧🇷🇺🇦🗽](https://twitter.com/IracemaDCS) | 30/03/2016 | 1.302 (6936/5326) | 79944 |
| ![alt text](http://pbs.twimg.com/profile_images/1347733964308492290/qESeDAsg_normal.jpg "foto do usuário") [Ana Vasques](https://twitter.com/AVasquesv) | 20/04/2013 | 0.923 (5262/5703) | 155438 |
| ![alt text](http://pbs.twimg.com/profile_images/1344025380290748416/YA2VkOA-_normal.jpg "foto do usuário") [Gan-Ganowicz](https://twitter.com/7Lagoano) | 21/05/2019 | 1.728 (178/103) | 5947 |
| ![alt text](http://pbs.twimg.com/profile_images/1183855346126864384/f-lNo08x_normal.jpg "foto do usuário") [K.Doug.](https://twitter.com/kbentes06) | 31/01/2011 | 0.25 (712/2847) | 7247 |
| ![alt text](http://pbs.twimg.com/profile_images/1199107716767199234/yVOOhy7A_normal.jpg "foto do usuário") [Justiceiro de Direita 🇧🇷🇧🇷](https://twitter.com/justiceidireita) | 05/02/2019 | 0.929 (2645/2846) | 9783 |
| ![alt text](http://pbs.twimg.com/profile_images/1352398056583520258/e1EgiB-R_normal.jpg "foto do usuário") [Reinaldo Gois 🇧🇷 💻🔬🔍](https://twitter.com/reinaldogois) | 09/09/2010 | 0.509 (1647/3238) | 7288 |
| ![alt text](http://pbs.twimg.com/profile_images/1194635987348946945/2Nx7Jitb_normal.jpg "foto do usuário") [Luiz Otavio Robô Weintraub de Almeida 🇧🇷](https://twitter.com/LuizOtavioAlme1) | 12/01/2014 | 0.741 (1282/1729) | 55497 |
| ![alt text](http://pbs.twimg.com/profile_images/1300199423981613058/1eovlquq_normal.jpg "foto do usuário") [Lucas](https://twitter.com/lucas_pser) | 15/06/2016 | 0.208 (49/236) | 2142 |
| ![alt text](http://pbs.twimg.com/profile_images/1340170237707169792/IINFycwF_normal.jpg "foto do usuário") [Mari](https://twitter.com/maribsbecherer) | 16/11/2016 | 7.393 (1656/224) | 12443 |
| ![alt text](http://pbs.twimg.com/profile_images/1144418177817939968/DNzg-0Kd_normal.png "foto do usuário") [Fabiano](https://twitter.com/fpshello2u) | 25/08/2009 | 0.682 (438/642) | 61824 |
| ![alt text](http://pbs.twimg.com/profile_images/1352053142364499972/yZF32cJH_normal.jpg "foto do usuário") [Vivi...👻](https://twitter.com/eumesmavivi0) | 01/07/2010 | 9.54 (17133/1796) | 78517 |
| ![alt text](http://pbs.twimg.com/profile_images/1349123893525680131/8SFwsIxo_normal.jpg "foto do usuário") [Lobotosasha](https://twitter.com/lobotomav) | 15/04/2014 | 14.44 (10512/728) | 64925 |
| ![alt text](http://pbs.twimg.com/profile_images/1341813112459194368/ycwhvW3h_normal.jpg "foto do usuário") [Gaby Samedhi 🇺🇲🦅#GodWins](https://twitter.com/Tumultuous_G) | 28/12/2019 | 1.123 (228/203) | 3563 |
| ![alt text](http://pbs.twimg.com/profile_images/1347725917255315456/LLEHF_Jn_normal.jpg "foto do usuário") [Célia 🇺🇲❤🇧🇷](https://twitter.com/Clia53846846) | 21/06/2019 | 0.247 (169/685) | 1457 |
| ![alt text](http://pbs.twimg.com/profile_images/1350442267757174784/Zzp-uKkF_normal.jpg "foto do usuário") [rDomotor JB3⃣8⃣ 🇧🇷🇮🇱🇺🇸🇭🇺🇵🇱🇺🇦](https://twitter.com/rDomotor3) | 07/08/2018 | 1.185 (846/714) | 15341 |
| ![alt text](http://pbs.twimg.com/profile_images/1353056232869793793/191CCEt3_normal.jpg "foto do usuário") [Thiago Matheus Câmara de Araújo🇧🇷🇮🇱🥋](https://twitter.com/ThiagoMatheusC6) | 13/02/2020 | 0.618 (260/421) | 2813 |
| ![alt text](http://pbs.twimg.com/profile_images/1298007627302043648/eMYfQhTE_normal.jpg "foto do usuário") [MÁRCIO APARECIDO ](https://twitter.com/mca_74) | 11/12/2013 | 0.492 (398/809) | 974 |
| ![alt text](http://pbs.twimg.com/profile_images/1352098019865473026/C3VhfpAt_normal.jpg "foto do usuário") [Isa GP 🙌🏻🇧🇷🇺🇸🙌🏻](https://twitter.com/IsaNCC1701) | 05/07/2019 | 0.348 (295/848) | 5616 |
| ![alt text](http://pbs.twimg.com/profile_images/1160262692986335234/eUdrf2ld_normal.jpg "foto do usuário") [ricardosarmento](https://twitter.com/ricardosarmento) | 06/10/2008 | 0.228 (86/377) | 4649 |
| ![alt text](http://pbs.twimg.com/profile_images/1337788317442650113/JYvDt8kc_normal.jpg "foto do usuário") [Lucy🍼🥣](https://twitter.com/luccyy_lucy) | 23/08/2010 | 0.255 (344/1351) | 14168 |
| ![alt text](http://pbs.twimg.com/profile_images/1228821670636343296/d_MGcjfi_normal.jpg "foto do usuário") [Advogado do Diabo,conservador.](https://twitter.com/Insulano171) | 03/12/2015 | 0.187 (366/1954) | 34431 |
| ![alt text](http://pbs.twimg.com/profile_images/1297840353320546304/XhDO1Vq2_normal.jpg "foto do usuário") [FLAMENGO MALVADAO](https://twitter.com/luckasserrate) | 30/04/2015 | 0.103 (192/1867) | 11953 |
| ![alt text](http://pbs.twimg.com/profile_images/1142796983754788870/tMjJKScQ_normal.jpg "foto do usuário") [Natália 🌻](https://twitter.com/marla_ms0) | 07/04/2014 | 8.688 (2502/288) | 8438 |
| ![alt text](http://pbs.twimg.com/profile_images/1326485076448845826/zmyexEOO_normal.jpg "foto do usuário") [Marcelo santos](https://twitter.com/celosantos71) | 19/09/2012 | 0.131 (160/1223) | 25082 |
| ![alt text](http://pbs.twimg.com/profile_images/1242278813742096385/TT8YB-Sx_normal.jpg "foto do usuário") [Pensador](https://twitter.com/pensador_fil) | 22/12/2009 | 0.728 (1747/2399) | 29730 |
| ![alt text](http://pbs.twimg.com/profile_images/1353429760991522817/0QfQqXj2_normal.jpg "foto do usuário") [Fraitag 💲☕🍺🇧🇷🍽️🚗🎸](https://twitter.com/shitlikler1) | 30/04/2011 | 0.732 (1110/1516) | 7574 |
| ![alt text](http://pbs.twimg.com/profile_images/593091455322890242/_PUUgBy9_normal.jpg "foto do usuário") [ɱα૨૮εℓℓµร รαɳƭσร ® 🇧🇷](https://twitter.com/Sr_Marcellus) | 05/08/2011 | 0.802 (637/794) | 37451 |
| ![alt text](http://pbs.twimg.com/profile_images/1314017372911677440/r8r7aIP0_normal.jpg "foto do usuário") [Vincent_ᶜʳᶠ](https://twitter.com/lwyzvincent) | 02/08/2011 | 0.231 (124/537) | 6087 |
| ![alt text](http://pbs.twimg.com/profile_images/1076043754342154241/4ZlDNes3_normal.jpg "foto do usuário") [Diego](https://twitter.com/diegoreis05) | 15/07/2010 | 0.079 (25/315) | 1065 |
| ![alt text](http://pbs.twimg.com/profile_images/1351386584776642560/SlbcC_zb_normal.jpg "foto do usuário") [coments 🧙](https://twitter.com/angeskay) | 17/02/2013 | 1.443 (306/212) | 15742 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Pedro](https://twitter.com/Pedro70046278) | 26/04/2020 | 0.999 (1356/1357) | 14616 |
| ![alt text](http://pbs.twimg.com/profile_images/1350129102783737858/8p0eo0Zo_normal.jpg "foto do usuário") [A Brasiliense](https://twitter.com/brasiliense_a) | 30/09/2018 | 0.475 (502/1056) | 14979 |
| ![alt text](http://pbs.twimg.com/profile_images/1312515124058640384/iFC6VPzZ_normal.jpg "foto do usuário") [Eduardo Pereira](https://twitter.com/EduardoVet) | 01/05/2009 | 0.487 (347/713) | 15775 |
| ![alt text](http://pbs.twimg.com/profile_images/1097137213165527040/RukVYcpF_normal.jpg "foto do usuário") [🆘️ Cristina A. 🔊🕹](https://twitter.com/achefedagoma) | 11/04/2017 | 0.069 (31/451) | 2072 |
| ![alt text](http://pbs.twimg.com/profile_images/1313941300601925637/oZTXiI07_normal.jpg "foto do usuário") [Joel Filho](https://twitter.com/joel_fi) | 04/06/2011 | 1.016 (2797/2753) | 11788 |
| ![alt text](http://pbs.twimg.com/profile_images/1347140029357973505/ImUFiFQZ_normal.jpg "foto do usuário") [Vanderlei Nunes](https://twitter.com/VanderleiANune5) | 17/04/2016 | 0.281 (129/459) | 5016 |
| ![alt text](http://pbs.twimg.com/profile_images/1338809576561455105/6nRv2kFa_normal.jpg "foto do usuário") [Rafael Ferreira](https://twitter.com/RAFAELSimpatia) | 12/09/2011 | 0.153 (124/812) | 2371 |
| ![alt text](http://pbs.twimg.com/profile_images/1057296212263686144/NbOJdmmy_normal.jpg "foto do usuário") [Lyverton](https://twitter.com/Lyverton01) | 28/10/2018 | 0.043 (12/278) | 149 |
| ![alt text](http://pbs.twimg.com/profile_images/585907442669772800/dMBGbTM1_normal.jpg "foto do usuário") [Vitor Santos](https://twitter.com/VitorSantos290) | 21/01/2013 | 0.109 (89/813) | 2673 |
| ![alt text](http://pbs.twimg.com/profile_images/1278150246678355969/a4ysrlYZ_normal.jpg "foto do usuário") [PHLO](https://twitter.com/PHLO50334299) | 06/03/2020 | 0.74 (284/384) | 2279 |
| ![alt text](http://pbs.twimg.com/profile_images/1294259194154098695/u7_PeCut_normal.jpg "foto do usuário") [Fabio Silva 🇧🇷](https://twitter.com/CarloFabio1997) | 23/07/2020 | 0.566 (1282/2266) | 12185 |
| ![alt text](http://pbs.twimg.com/profile_images/1355607477119823873/2x5pAAJz_normal.jpg "foto do usuário") [moraes](https://twitter.com/RMora3s) | 18/08/2009 | 1.937 (1205/622) | 80052 |
| ![alt text](http://pbs.twimg.com/profile_images/1354639486802669568/KlV6AXsW_normal.jpg "foto do usuário") [João Ortiz](https://twitter.com/J0A0JR) | 05/07/2018 | 0.222 (197/888) | 30437 |
| ![alt text](http://pbs.twimg.com/profile_images/1339935864596672518/akCauZ10_normal.jpg "foto do usuário") [AM.Baroni](https://twitter.com/BaroAM20) | 24/06/2020 | 0.047 (12/255) | 926 |
| ![alt text](http://pbs.twimg.com/profile_images/1334221834846416897/FaRqzAJK_normal.jpg "foto do usuário") [Angel Oliver 🇵🇹🇬🇧🇺🇲](https://twitter.com/RosangelaAdv11) | 19/01/2020 | 0.508 (219/431) | 5379 |
| ![alt text](http://pbs.twimg.com/profile_images/1103438049298518023/pHG1k5yh_normal.jpg "foto do usuário") [Agente de Polícia Penal . Laba](https://twitter.com/LabaLeandro) | 06/03/2019 | 0.079 (394/4979) | 392 |
| ![alt text](http://pbs.twimg.com/profile_images/1347762258697465857/ZQBk837B_normal.jpg "foto do usuário") [DoraFelip](https://twitter.com/Sonja10860334) | 01/08/2020 | 0.819 (1845/2254) | 1285 |
| ![alt text](http://pbs.twimg.com/profile_images/1350797388877803520/siUuaRqa_normal.jpg "foto do usuário") [Ana Reloaded](https://twitter.com/AnaPaul62668239) | 02/09/2019 | 0.802 (4012/5001) | 33260 |
| ![alt text](http://pbs.twimg.com/profile_images/1303458487855452165/EZH7qjBr_normal.jpg "foto do usuário") [F Carvalho 🇧🇷🤜🏼⚓🤛🏼🇺🇸](https://twitter.com/FRAS_OR_EW) | 11/02/2019 | 0.943 (1281/1358) | 4342 |
| ![alt text](http://pbs.twimg.com/profile_images/1298737686308585473/DXbIJNQ6_normal.jpg "foto do usuário") [marina Santos Carvalho🇧🇷🇧🇷🇧🇷🇧🇷🇧🇷🇧🇷🇧🇷](https://twitter.com/Ca2Santos) | 26/08/2020 | 0.925 (7157/7741) | 1897 |
| ![alt text](http://pbs.twimg.com/profile_images/1347959587627016193/oAHJK1Wi_normal.jpg "foto do usuário") [Pedrop_cl](https://twitter.com/ClPedrop) | 03/05/2020 | 0.838 (1097/1309) | 3403 |
| ![alt text](http://pbs.twimg.com/profile_images/1350356109824028674/D_mX3rBG_normal.jpg "foto do usuário") [Bolsomeiry](https://twitter.com/rossimeiry) | 21/01/2019 | 0.706 (2797/3962) | 11525 |
| ![alt text](http://pbs.twimg.com/profile_images/1347960624224022529/daxARNWU_normal.jpg "foto do usuário") [🇧🇷 Paulo 🇧🇷](https://twitter.com/pflora09) | 01/02/2013 | 0.727 (348/479) | 45529 |
| ![alt text](http://pbs.twimg.com/profile_images/1289224738846511104/X1ib9xTX_normal.jpg "foto do usuário") [Winner](https://twitter.com/jsmlmec) | 20/01/2010 | 0.589 (1958/3323) | 40483 |
| ![alt text](http://pbs.twimg.com/profile_images/1283365957470228481/PPWft03t_normal.jpg "foto do usuário") [Cris](https://twitter.com/Cris83499431) | 15/07/2020 | 0.434 (242/558) | 5532 |
| ![alt text](http://pbs.twimg.com/profile_images/1349238399001976836/9IjX90sm_normal.jpg "foto do usuário") [-=|Î¢ëრäñß®ä§¡£|=-❁🇧🇷🇯🇵](https://twitter.com/IceManBrazil) | 08/01/2019 | 0.973 (3248/3339) | 13342 |
| ![alt text](http://pbs.twimg.com/profile_images/1348069283524468737/1C4lCylZ_normal.jpg "foto do usuário") [CrisAgain&Again](https://twitter.com/CrisagainA) | 18/04/2020 | 0.733 (1164/1587) | 12405 |
| ![alt text](http://pbs.twimg.com/profile_images/1331073687613812736/ERGGB7tc_normal.jpg "foto do usuário") [Mauricio M](https://twitter.com/MauricioxMar) | 27/06/2012 | 0.26 (110/423) | 3380 |
| ![alt text](http://pbs.twimg.com/profile_images/1351868865689640963/9zVlqfop_normal.jpg "foto do usuário") [Lu Sapori🇧🇷🌎](https://twitter.com/ALLuSapore) | 24/07/2013 | 8.919 (26301/2949) | 49753 |
| ![alt text](http://pbs.twimg.com/profile_images/1741209230/2_normal.jpg "foto do usuário") [Paola P.](https://twitter.com/paolapfau) | 02/07/2009 | 1.429 (423/296) | 3427 |
| ![alt text](http://pbs.twimg.com/profile_images/1253294053938147328/eFPCdUmm_normal.jpg "foto do usuário") [Ezequiel Alves🇧🇷🇮🇱](https://twitter.com/Ezequiel_alv1) | 20/04/2020 | 0.979 (7612/7773) | 14256 |
| ![alt text](http://pbs.twimg.com/profile_images/1240456980822732803/CLFiG1Jr_normal.jpg "foto do usuário") [tec_miguel_es](https://twitter.com/tecmigueles1) | 06/11/2019 | 0.704 (88/125) | 4567 |
| ![alt text](http://pbs.twimg.com/profile_images/1246525270380740609/FNrywupR_normal.jpg "foto do usuário") [herbert newton moreira](https://twitter.com/herbertnewtonm1) | 08/04/2018 | 0.926 (2332/2519) | 59037 |
| ![alt text](http://pbs.twimg.com/profile_images/1348078006586245122/fLRNWnxy_normal.jpg "foto do usuário") [souLuizPaulo](https://twitter.com/souLuizPaulo) | 14/02/2008 | 0.706 (1602/2270) | 40523 |
| ![alt text](http://pbs.twimg.com/profile_images/1346775724359880704/ZJbDK5pn_normal.jpg "foto do usuário") [Valéria Taliatti](https://twitter.com/TaliattiValeria) | 06/07/2020 | 0.69 (2430/3522) | 8635 |
| ![alt text](http://pbs.twimg.com/profile_images/1301691631326855169/D2FgSSfe_normal.jpg "foto do usuário") [Pererinha 🇧🇷🇮🇱🇺🇸](https://twitter.com/Olverpera) | 28/09/2010 | 0.774 (838/1083) | 628 |
| ![alt text](http://pbs.twimg.com/profile_images/1308192426784362497/ciQN5WZK_normal.jpg "foto do usuário") [𝓜𝓪𝓻𝓬𝓲𝓸 𝓜𝓪𝓬𝓲𝓮𝓵🇧🇷 🇧🇷🇾🇪🇧🇷🇧🇷](https://twitter.com/MarcioM61326104) | 11/12/2019 | 0.01 (16221/0) | 19055 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [alberto gomez](https://twitter.com/alberto45129151) | 15/03/2019 | 0.682 (90/132) | 2508 |
| ![alt text](http://pbs.twimg.com/profile_images/1271697722001756165/AmiWqZi8_normal.jpg "foto do usuário") [FilhodoGrilo](https://twitter.com/rubensvaz) | 09/09/2010 | 0.985 (14891/15118) | 112102 |
| ![alt text](http://pbs.twimg.com/profile_images/344513261579119658/9c641bf746282723866265dc0f1c63e3_normal.jpeg "foto do usuário") [J.](https://twitter.com/juliofilho231) | 14/06/2013 | 0.611 (11/18) | 1182 |
| ![alt text](http://pbs.twimg.com/profile_images/1278849812222394374/q4DDzGlH_normal.jpg "foto do usuário") [Marcos Penteado](https://twitter.com/MarcosPenteado9) | 03/07/2020 | 0.425 (453/1067) | 18871 |
| ![alt text](http://pbs.twimg.com/profile_images/1294697553095806977/OmXT2x-k_normal.jpg "foto do usuário") [Daniel de Brito](https://twitter.com/DanieldeBrito19) | 15/08/2020 | 0.024 (1/42) | 80 |
| ![alt text](http://pbs.twimg.com/profile_images/1198371675441684481/fppz1j3p_normal.jpg "foto do usuário") [Augusto Nunes](https://twitter.com/augustosnunes) | 24/06/2009 | 1485.994 (1056542/711) | 24737 |
| ![alt text](http://pbs.twimg.com/profile_images/1339751802061934592/xoO7PQv__normal.jpg "foto do usuário") [Medeiros](https://twitter.com/Azzidea) | 20/03/2013 | 1.395 (4339/3111) | 10484 |
| ![alt text](http://pbs.twimg.com/profile_images/1280643672342761472/Z_pmmGSr_normal.jpg "foto do usuário") [Universidade Libertária 📚](https://twitter.com/UniversidadeLi3) | 13/05/2019 | 43.58 (7583/174) | 3318 |
| ![alt text](http://pbs.twimg.com/profile_images/1344751956749905929/DO7f7p5b_normal.jpg "foto do usuário") [Jurista Libertário](https://twitter.com/JurisLibertario) | 13/01/2019 | 4.429 (8531/1926) | 14350 |
| ![alt text](http://pbs.twimg.com/profile_images/1129857965245259776/qNQ0u0gi_normal.jpg "foto do usuário") [Renata Brandt](https://twitter.com/Rebrandtsants) | 13/07/2009 | 0.529 (659/1245) | 11351 |
| ![alt text](http://pbs.twimg.com/profile_images/1308113197933748233/svjjpg4c_normal.jpg "foto do usuário") [#Bolsonaro2022 🇧🇷](https://twitter.com/fdcalbuquerque7) | 09/08/2010 | 0.614 (1043/1700) | 13358 |
| ![alt text](http://pbs.twimg.com/profile_images/1347654885249081344/fA6FTgw7_normal.jpg "foto do usuário") [davi](https://twitter.com/littlecoutodavi) | 18/01/2017 | 0.364 (187/514) | 11962 |
| ![alt text](http://pbs.twimg.com/profile_images/1344105733709824000/AORO5arD_normal.jpg "foto do usuário") [RAFAEL GL4U](https://twitter.com/RGL4U) | 13/10/2016 | 59.158 (22421/379) | 17890 |
| ![alt text](http://pbs.twimg.com/profile_images/1343303089743228928/y5Am13JM_normal.jpg "foto do usuário") [Tsuki - 🥂 2021 Energiza🥂](https://twitter.com/Fa1ryNight) | 10/02/2019 | 23.244 (9902/426) | 44243 |
| ![alt text](http://pbs.twimg.com/profile_images/1208245456129667073/D1aMhtJ0_normal.jpg "foto do usuário") [Iverson Moura 🇧🇷](https://twitter.com/Iversonmouras) | 13/01/2017 | 0.363 (186/513) | 13371 |
| ![alt text](http://pbs.twimg.com/profile_images/1294633463954518018/6h7qJNRX_normal.jpg "foto do usuário") [opropriorafael](https://twitter.com/opropriorafael) | 03/03/2020 | 4.738 (488/103) | 7520 |
| ![alt text](http://pbs.twimg.com/profile_images/1347988379917545477/ZOcalKJu_normal.jpg "foto do usuário") [LUIZ CAMARGO vlog](https://twitter.com/LuizCamargoVlog) | 06/11/2019 | 314.524 (97188/309) | 2508 |
| ![alt text](http://pbs.twimg.com/profile_images/1328318373785112576/ZmIPLsx5_normal.jpg "foto do usuário") [Paula Marisa](https://twitter.com/profpaulamarisa) | 17/09/2009 | 340.554 (274827/807) | 17494 |
| ![alt text](http://pbs.twimg.com/profile_images/1282758320982503424/FT32oKP2_normal.jpg "foto do usuário") [Lilo](https://twitter.com/LiloVLOG) | 02/06/2009 | 170.005 (145694/857) | 45192 |
| ![alt text](http://pbs.twimg.com/profile_images/917799068595867648/j4rM72Nn_normal.jpg "foto do usuário") [Cris Bolsonaro 2022](https://twitter.com/ciancaglini_15) | 27/10/2009 | 12.965 (9594/740) | 181703 |
| ![alt text](http://pbs.twimg.com/profile_images/1355287409605402624/deMYxfbu_normal.jpg "foto do usuário") [𝐅𝐥𝐚𝐮𝐛𝐞𝐫𝐭 𝟏𝟗𝟏𝟒 🟢⚪🔴](https://twitter.com/flaubertbinho) | 24/11/2009 | 0.442 (253/573) | 10439 |
| ![alt text](http://pbs.twimg.com/profile_images/1148915249610928128/KGtwUa6O_normal.jpg "foto do usuário") [Tacílio Benedito de Araújo](https://twitter.com/DeTacilio) | 10/07/2019 | 0.407 (22/54) | 12509 |
| ![alt text](http://pbs.twimg.com/profile_images/1171389275650351104/cRrGtLC7_normal.jpg "foto do usuário") [Vitor Gomes](https://twitter.com/Darwinista_) | 01/12/2018 | 0.287 (151/527) | 11090 |
| ![alt text](http://pbs.twimg.com/profile_images/1310611933700272128/iF52f-BZ_normal.jpg "foto do usuário") [Júnior Reis](https://twitter.com/juniorreisfla) | 06/07/2019 | 0.076 (63/825) | 2404 |
| ![alt text](http://pbs.twimg.com/profile_images/1342676850967982081/6qbiiJnk_normal.jpg "foto do usuário") [Crimes Reais](https://twitter.com/CrimesReais) | 11/09/2019 | 211965.333 (635896/3) | 8886 |
| ![alt text](http://pbs.twimg.com/profile_images/1343347102999576577/TgDK3QjN_normal.jpg "foto do usuário") [Alberto Ainstain](https://twitter.com/RY0ASUKA__) | 17/04/2019 | 3.698 (13421/3629) | 131363 |
| ![alt text](http://pbs.twimg.com/profile_images/1276665475339030530/bmUv-xxw_normal.jpg "foto do usuário") [Maria Rita LOPES](https://twitter.com/MariaRi33071719) | 23/06/2020 | 1.819 (14616/8035) | 1711 |
| ![alt text](http://pbs.twimg.com/profile_images/1342833092508217351/GHErCqbV_normal.jpg "foto do usuário") [®️Marcello Neves 🇧🇷](https://twitter.com/marcelloneves72) | 19/04/2016 | 1.305 (48184/36924) | 15640 |
| ![alt text](http://pbs.twimg.com/profile_images/1230887995785588739/x1LH_olB_normal.jpg "foto do usuário") [BetoSilvaBR 🇧🇷🇧🇷](https://twitter.com/BetoSilvaBR) | 14/09/2014 | 1.961 (10675/5444) | 83278 |
| ![alt text](http://pbs.twimg.com/profile_images/1351607987937435648/X7vldeBA_normal.jpg "foto do usuário") [Douglas Gomes](https://twitter.com/verdouglasgomes) | 22/06/2016 | 12.576 (15594/1240) | 9286 |
| ![alt text](http://pbs.twimg.com/profile_images/1341941704350453760/QeWATd15_normal.jpg "foto do usuário") [Alexandre 🇧🇷🇧🇷🇧🇷](https://twitter.com/AleGZahra38) | 27/02/2019 | 3.436 (72156/21000) | 86333 |
| ![alt text](http://pbs.twimg.com/profile_images/1335739124540727299/1hUD_pzq_normal.jpg "foto do usuário") [Deise Severo](https://twitter.com/Deise62377862) | 29/04/2020 | 0.672 (160/238) | 843 |
| ![alt text](http://pbs.twimg.com/profile_images/1348446545579024385/GZ1-KrDk_normal.jpg "foto do usuário") [Andréa Bolsonaro](https://twitter.com/AndreaBonoro) | 04/08/2020 | 1.323 (8058/6089) | 1428 |
| ![alt text](http://pbs.twimg.com/profile_images/1346313530040078336/DFHTw9MF_normal.jpg "foto do usuário") [Deise Peres. oficial 🇧🇷](https://twitter.com/DeisePeres4) | 22/05/2019 | 1.137 (26927/23679) | 17008 |
| ![alt text](http://pbs.twimg.com/profile_images/1354499048250748932/pZyiBbzu_normal.jpg "foto do usuário") [Alê Lopes Brasil 2022 🇧🇷](https://twitter.com/Alelopes81Lopes) | 22/10/2011 | 1.001 (14188/14173) | 91661 |
| ![alt text](http://pbs.twimg.com/profile_images/1348164769740705792/hfjKcNac_normal.jpg "foto do usuário") [dire(i)to no ponto - César Soares](https://twitter.com/direitonoponto) | 11/04/2013 | 1.035 (30146/29131) | 35548 |
| ![alt text](http://pbs.twimg.com/profile_images/1257361643530485760/_quO3Qv7_normal.jpg "foto do usuário") [Carlos Jordy](https://twitter.com/carlosjordy) | 14/10/2009 | 452.337 (415698/919) | 7889 |
| ![alt text](http://pbs.twimg.com/profile_images/1343335923413635073/K_9D2NDK_normal.jpg "foto do usuário") [Soraia](https://twitter.com/sisbresolin) | 19/02/2017 | 1.02 (1448/1420) | 13706 |
| ![alt text](http://pbs.twimg.com/profile_images/1043666945940365312/5NkNT_JV_normal.jpg "foto do usuário") [Anderson Jefferson](https://twitter.com/CacaFittipald) | 30/10/2011 | 2.622 (97/37) | 3669 |
| ![alt text](http://pbs.twimg.com/profile_images/1108382212792168449/IIlKEEMw_normal.jpg "foto do usuário") [Pedro Melo](https://twitter.com/pedropimelo) | 06/11/2018 | 5.639 (547/97) | 36599 |
| ![alt text](http://pbs.twimg.com/profile_images/1326579650835996673/2nmI1rAR_normal.jpg "foto do usuário") [Roberto Jefferson](https://twitter.com/BobjeffHD) | 03/08/2020 | 103.145 (115729/1122) | 3170 |
| ![alt text](http://pbs.twimg.com/profile_images/1349031725461102597/SrncaP_H_normal.jpg "foto do usuário") [Marcelo Q Jacob 🇧🇷🇺🇲🇮🇱](https://twitter.com/saoapenasmil) | 19/11/2017 | 0.582 (397/682) | 10379 |
| ![alt text](http://pbs.twimg.com/profile_images/1264459880334843904/4QEt9ZYc_normal.jpg "foto do usuário") [Luma Rodrigues2](https://twitter.com/Rodrigues2Luma) | 23/05/2020 | 0.9 (189/210) | 906 |
| ![alt text](http://pbs.twimg.com/profile_images/1280533988977893376/B_CHyy___normal.jpg "foto do usuário") [Juliana Gama](https://twitter.com/Jugamenes) | 03/06/2019 | 2.646 (13897/5253) | 3961 |
| ![alt text](http://pbs.twimg.com/profile_images/1171225938220204032/RtD1nLUY_normal.jpg "foto do usuário") [Jornal da Record](https://twitter.com/jornaldarecord) | 02/05/2011 | 6815.481 (354405/52) | 57179 |
| ![alt text](http://pbs.twimg.com/profile_images/1293916624311988224/Jt764eqN_normal.jpg "foto do usuário") [Alexandre Duarte](https://twitter.com/alexandrebie) | 13/05/2013 | 0.934 (7192/7703) | 5787 |
| ![alt text](http://pbs.twimg.com/profile_images/1283534581375918081/6DrZlQeC_normal.jpg "foto do usuário") [Alex 🇧🇷🇧🇷🇧🇷🇧🇷 💪](https://twitter.com/Alex76844340) | 15/02/2020 | 0.802 (2756/3437) | 384 |
| ![alt text](http://pbs.twimg.com/profile_images/1350533620516220933/6_xbcXab_normal.jpg "foto do usuário") [Floriano Barros](https://twitter.com/barros_floriano) | 23/12/2014 | 0.786 (3752/4776) | 9924 |
| ![alt text](http://pbs.twimg.com/profile_images/1334861526029783043/-ScGth5K_normal.jpg "foto do usuário") [ChuteiraTemQSerPreta🇧🇷⚫🔴](https://twitter.com/robsonsodre10) | 30/04/2013 | 0.718 (3592/5004) | 231836 |
| ![alt text](http://pbs.twimg.com/profile_images/953063375893917696/FiakBS6g_normal.jpg "foto do usuário") [Cocadinha de sal](https://twitter.com/DeCocadinha) | 16/01/2018 | 1.095 (7974/7280) | 23759 |
| ![alt text](http://pbs.twimg.com/profile_images/1179730636644454402/lEcDRpIC_normal.jpg "foto do usuário") [Portal R7.com](https://twitter.com/portalR7) | 13/08/2009 | 50087.237 (4858462/97) | 456428 |
| ![alt text](http://pbs.twimg.com/profile_images/479713820978712577/j7JKLwpn_normal.jpeg "foto do usuário") [José Rodrigues](https://twitter.com/Jrodrigues1954) | 15/10/2011 | 1.641 (37071/22592) | 395834 |
| ![alt text](http://pbs.twimg.com/profile_images/1165427240160702469/OwWQYQr1_normal.jpg "foto do usuário") [SANDRA VASCONCELOS CAVALCANTE](https://twitter.com/SANDRAV61852675) | 08/11/2017 | 0.352 (1392/3956) | 23964 |
| ![alt text](http://pbs.twimg.com/profile_images/1165937410225692672/v9SLlKyw_normal.jpg "foto do usuário") [Vinicius Carrion](https://twitter.com/viniciuscfp82) | 03/11/2009 | 161.897 (51969/321) | 9483 |
| ![alt text](http://pbs.twimg.com/profile_images/941265049926144000/dk9aqI2n_normal.jpg "foto do usuário") [Mengo Minha Loucura ᶜʳᶠ ¹⁸⁹⁵](https://twitter.com/MengoLoucura) | 07/08/2013 | 1.11 (8697/7833) | 16961 |
| ![alt text](http://pbs.twimg.com/profile_images/1150156348388196357/yV2kSzNc_normal.jpg "foto do usuário") [Marcelo Bechler](https://twitter.com/marcelobechler) | 10/08/2009 | 207.24 (233145/1125) | 76292 |
| ![alt text](http://pbs.twimg.com/profile_images/1293699048533352452/ZXHL9W3B_normal.jpg "foto do usuário") [Argos](https://twitter.com/OArgonauta) | 06/08/2020 | 0.353 (225/638) | 6318 |
| ![alt text](http://pbs.twimg.com/profile_images/1248848016724955137/x6MLOTxM_normal.jpg "foto do usuário") [ギルバー](https://twitter.com/PrinceOfFeels) | 30/11/2016 | 0.156 (57/365) | 4842 |
| ![alt text](http://pbs.twimg.com/profile_images/1227020263537172480/ibxailNS_normal.jpg "foto do usuário") [Curiosidades Premier League](https://twitter.com/CuriosidadesPRL) | 11/02/2020 | 2.647 (27920/10549) | 10395 |
| ![alt text](http://pbs.twimg.com/profile_images/1355594250709303302/S1OTaOuH_normal.jpg "foto do usuário") [guilherme](https://twitter.com/guilhermariae) | 17/01/2015 | 2.647 (30970/11700) | 53231 |
| ![alt text](http://pbs.twimg.com/profile_images/1321356952534921217/A71ScfpA_normal.jpg "foto do usuário") [Dama de Ferro](https://twitter.com/Damadeferroofic) | 22/09/2018 | 227.441 (157844/694) | 15274 |
| ![alt text](http://pbs.twimg.com/profile_images/1143549755324342272/bA-lWE_P_normal.jpg "foto do usuário") [Arthur Wrightman](https://twitter.com/WrightmanW) | 25/06/2019 | 0.378 (87/230) | 2521 |
| ![alt text](http://pbs.twimg.com/profile_images/1333087957058809858/RUjXPgmu_normal.jpg "foto do usuário") [Knight of the Atlantic ♱](https://twitter.com/knight_atlantic) | 12/09/2018 | 27.751 (8242/297) | 62875 |
| ![alt text](http://pbs.twimg.com/profile_images/1350815614521257984/aqvvtTXQ_normal.jpg "foto do usuário") [FUI PARA O CCORE @Gfrreis](https://twitter.com/GFRREIS) | 10/03/2011 | 1.222 (2506/2051) | 87869 |
| ![alt text](http://pbs.twimg.com/profile_images/1320091968479891461/QneLtKK9_normal.jpg "foto do usuário") [Márcia C Lima 🇧🇷 3️⃣8️⃣ 🇧🇷](https://twitter.com/McLima9) | 03/10/2019 | 3.813 (28787/7549) | 57027 |
| ![alt text](http://pbs.twimg.com/profile_images/1343596865955258368/Hp6ZCyph_normal.jpg "foto do usuário") [Agnes](https://twitter.com/bolosaurus) | 17/10/2018 | 1.554 (811/522) | 36210 |
| ![alt text](http://pbs.twimg.com/profile_images/1292786210692386816/C1YFsRUA_normal.jpg "foto do usuário") [Medeiros✨](https://twitter.com/viimedeiros0) | 21/01/2020 | 1.363 (124/91) | 204 |
| ![alt text](http://pbs.twimg.com/profile_images/1311439459041325056/tc8MrktB_normal.jpg "foto do usuário") [Carlos Silva 🇻🇦](https://twitter.com/carlosdemariae) | 30/08/2016 | 0.424 (187/441) | 2234 |
| ![alt text](http://pbs.twimg.com/profile_images/1343612451917615105/MPcI94LD_normal.jpg "foto do usuário") [Delegado M Quezado](https://twitter.com/MarcosQuezado1) | 08/07/2019 | 4.248 (70056/16491) | 77332 |
| ![alt text](http://pbs.twimg.com/profile_images/1294670673072324608/N1Jg0W1l_normal.jpg "foto do usuário") [Bruno](https://twitter.com/BrunoNice) | 17/08/2018 | 0.879 (210/239) | 7020 |
| ![alt text](http://pbs.twimg.com/profile_images/1236832422404280321/5huBV7ij_normal.jpg "foto do usuário") [Joana Lima 🇧🇷](https://twitter.com/mjmacul_lima) | 30/05/2017 | 1.456 (70192/48200) | 65518 |
| ![alt text](http://pbs.twimg.com/profile_images/1336651474894540801/KEo9sgTJ_normal.jpg "foto do usuário") [TyC Sports](https://twitter.com/TyCSports) | 24/07/2008 | 14361.154 (2326507/162) | 247935 |
| ![alt text](http://pbs.twimg.com/profile_images/1322854270971092995/sGGBteTK_normal.jpg "foto do usuário") [Vitor Acosta 🇻🇦](https://twitter.com/VitorLGA) | 09/07/2012 | 0.612 (219/358) | 22063 |
| ![alt text](http://pbs.twimg.com/profile_images/1270131295918702593/gxyWwLo7_normal.jpg "foto do usuário") [Syllabus](https://twitter.com/syllabus1917) | 08/06/2020 | 94.0 (752/8) | 151 |
| ![alt text](http://pbs.twimg.com/profile_images/1333582664155205633/zdMnHzyI_normal.jpg "foto do usuário") [Maria Teresa PROLIFE ☧](https://twitter.com/catholicgaby) | 13/04/2020 | 7.313 (1843/252) | 6089 |
| ![alt text](http://pbs.twimg.com/profile_images/1301128415173435392/sg0y3SxB_normal.jpg "foto do usuário") [Kim D. Paim](https://twitter.com/kimpaim) | 18/09/2009 | 554.725 (213569/385) | 19345 |
| ![alt text](http://pbs.twimg.com/profile_images/1135712344489771008/YUPqm95O_normal.jpg "foto do usuário") [Antonio Rocha](https://twitter.com/Antonio39784357) | 03/06/2019 | 0.09 (6/67) | 631 |
| ![alt text](http://pbs.twimg.com/profile_images/1338559371991715847/REkR_hdd_normal.jpg "foto do usuário") [Tenente josemir W. Silva](https://twitter.com/WillJosemir) | 19/02/2020 | 2.056 (5125/2493) | 27143 |
| ![alt text](http://pbs.twimg.com/profile_images/994303995467501568/lgtYfbKy_normal.jpg "foto do usuário") [Jornal da Cidade Online](https://twitter.com/JornalDaCidadeO) | 09/05/2018 | 1387.12 (184487/133) | 15166 |
| ![alt text](http://pbs.twimg.com/profile_images/998215310023901185/25SgMSmx_normal.jpg "foto do usuário") [🇧🇷Ailton Benedito](https://twitter.com/AiltonBenedito) | 25/07/2011 | 190.916 (227190/1190) | 72280 |
| ![alt text](http://pbs.twimg.com/profile_images/1290051615907553284/aF5CZq2B_normal.jpg "foto do usuário") [Bernardo P Küster LIVRE](https://twitter.com/bernardokuster2) | 02/08/2020 | 311.865 (101980/327) | 1184 |
| ![alt text](http://pbs.twimg.com/profile_images/1113594255958773761/i1cK8unW_normal.jpg "foto do usuário") [Teddy - VAMOS TE DERRUBAR MAIA!](https://twitter.com/Mr_TeddyBR) | 03/01/2017 | 1.238 (4132/3338) | 200069 |
| ![alt text](http://pbs.twimg.com/profile_images/1348940113426976768/9m9zYW2v_normal.jpg "foto do usuário") [francisconeto1](https://twitter.com/francisdear12) | 16/01/2010 | 1.118 (12902/11539) | 122676 |
| ![alt text](http://pbs.twimg.com/profile_images/1154373675178758144/ab0wH9RX_normal.jpg "foto do usuário") [Rodrigo Augusto Kayser](https://twitter.com/kayser_augusto) | 25/07/2019 | 0.418 (378/905) | 28455 |
| ![alt text](http://pbs.twimg.com/profile_images/1348611445462884357/kVdvyFTg_normal.jpg "foto do usuário") [Rodrigo Constantino](https://twitter.com/Rconstantino) | 20/04/2009 | 870.004 (663813/763) | 35044 |
| ![alt text](http://pbs.twimg.com/profile_images/1080512434635501569/kuYSZzx-_normal.jpg "foto do usuário") [Jornal Meia Hora](https://twitter.com/meiahora) | 13/02/2009 | 13.871 (80505/5804) | 115072 |
| ![alt text](http://pbs.twimg.com/profile_images/1095532385926631424/ODX2AmEZ_normal.jpg "foto do usuário") [Charlie Kirk](https://twitter.com/charliekirk11) | 04/05/2011 | 8.483 (1727660/203650) | 49670 |
| ![alt text](http://pbs.twimg.com/profile_images/1353656619666726912/sOy_6nXq_normal.jpg "foto do usuário") [JOSÉ MEDEIROS](https://twitter.com/JoseMedeirosMT) | 19/06/2010 | 76.545 (120023/1568) | 50306 |
| ![alt text](http://pbs.twimg.com/profile_images/1033726541442641920/s4fyfWuM_normal.jpg "foto do usuário") [Rafael Fontana](https://twitter.com/RafaelFontana) | 20/05/2009 | 235.615 (50186/213) | 50239 |
| ![alt text](http://pbs.twimg.com/profile_images/1350399662088450049/sTnvaHjZ_normal.jpg "foto do usuário") [Fabiana Santos](https://twitter.com/fabiss1072) | 14/04/2019 | 3.922 (1961/500) | 130766 |
| ![alt text](http://pbs.twimg.com/profile_images/1144086717839958016/uT_Ccb1y_normal.png "foto do usuário") [marquito](https://twitter.com/MarcoMarcodal) | 14/07/2016 | 1.311 (358/273) | 33383 |
| ![alt text](http://pbs.twimg.com/profile_images/1177897115411988481/3o2CIUyu_normal.jpg "foto do usuário") [Cão](https://twitter.com/Co19040320) | 27/09/2019 | 0.856 (2413/2818) | 21913 |
| ![alt text](http://pbs.twimg.com/profile_images/1104242634216914944/IKhYPqQ2_normal.jpg "foto do usuário") [Rodrigo Vieira](https://twitter.com/rvieira6005) | 20/11/2017 | 0.792 (3940/4975) | 12855 |
| ![alt text](http://pbs.twimg.com/profile_images/1349716262847467520/8SBb9ny3_normal.jpg "foto do usuário") [Nelson Carvalheira](https://twitter.com/N_Carvalheira) | 14/01/2013 | 2.056 (95191/46308) | 1245229 |
| ![alt text](http://pbs.twimg.com/profile_images/1346930321137217537/s2zfqxuS_normal.jpg "foto do usuário") [Phasma🇮🇹](https://twitter.com/GelPhasma) | 15/06/2019 | 2.033 (982/483) | 45305 |
| ![alt text](http://pbs.twimg.com/profile_images/1298398139376959500/xGApRWk__normal.jpg "foto do usuário") [Mili: Sai daqui jumento falador de bosta](https://twitter.com/milicianaaa) | 24/02/2020 | 5.93 (10300/1737) | 3234 |
| ![alt text](http://pbs.twimg.com/profile_images/1349036010563366917/s9owLdeO_normal.jpg "foto do usuário") [JC Denton católico](https://twitter.com/Felipe00_true) | 10/04/2018 | 1.018 (169/166) | 10224 |
| ![alt text](http://pbs.twimg.com/profile_images/1222585110719094787/fncUZzFw_normal.jpg "foto do usuário") [ALAN  CRN: 468468](https://twitter.com/alanjonnes) | 04/01/2011 | 0.617 (2501/4053) | 77401 |
| ![alt text](http://pbs.twimg.com/profile_images/796482667340382211/CoV8077b_normal.jpg "foto do usuário") [James Woods](https://twitter.com/RealJamesWoods) | 30/09/2009 | 539.557 (2433400/4510) | 36128 |
| ![alt text](http://pbs.twimg.com/profile_images/1299807716442075137/oR-xVxz8_normal.jpg "foto do usuário") [🃏🤡🔴Joker - CRF⚫🤡🃏](https://twitter.com/JokerRubroNegro) | 04/10/2014 | 1.061 (23452/22097) | 105400 |
| ![alt text](http://pbs.twimg.com/profile_images/1351701636222230529/DUa-PwGa_normal.jpg "foto do usuário") [Nelson Junior](https://twitter.com/nelson_skjr) | 01/10/2011 | 2.42 (1055/436) | 36025 |
| ![alt text](http://pbs.twimg.com/profile_images/1293196592779010050/7qYTYb2U_normal.jpg "foto do usuário") [marion](https://twitter.com/marion26823696) | 11/08/2020 | 0.23 (14/61) | 2 |
| ![alt text](http://pbs.twimg.com/profile_images/1295400023967113218/ycoxZ7-F_normal.jpg "foto do usuário") [Lgbts Passando Vergonha](https://twitter.com/LgbtsPassando) | 21/07/2020 | 111.937 (8843/79) | 784 |
| ![alt text](http://pbs.twimg.com/profile_images/1273665940622802946/vTlyP9dN_normal.jpg "foto do usuário") [Kubrick](https://twitter.com/stanley_kubr) | 08/05/2013 | 0.04 (90/2224) | 3763 |
| ![alt text](http://pbs.twimg.com/profile_images/504814454786502656/8mpKoSS9_normal.jpeg "foto do usuário") [Joao Victor](https://twitter.com/Jvictor09Joao) | 09/05/2013 | 0.339 (38/112) | 1793 |
| ![alt text](http://pbs.twimg.com/profile_images/1149090077412352000/XbfQBiaV_normal.jpg "foto do usuário") [alex felix brandine](https://twitter.com/FelixBrandine) | 05/01/2014 | 0.122 (12/98) | 492 |
| ![alt text](http://pbs.twimg.com/profile_images/1258962957268062211/aDpulWFM_normal.jpg "foto do usuário") [Russevel Crow💪😎👍](https://twitter.com/RussevelCrow) | 29/05/2009 | 0.776 (45/58) | 2672 |
| ![alt text](http://pbs.twimg.com/profile_images/1295673601908183040/BJW1r7vV_normal.jpg "foto do usuário") [Lu..Deus acima de TODOS](https://twitter.com/luzdosoltbcura) | 03/04/2010 | 0.899 (4223/4697) | 10538 |
| ![alt text](http://pbs.twimg.com/profile_images/1351849774316707841/WSlVj6mR_normal.jpg "foto do usuário") [Jardel](https://twitter.com/oliveira1208) | 28/07/2010 | 0.043 (18/415) | 2315 |
| ![alt text](http://pbs.twimg.com/profile_images/1348640622647926787/frsL9QXg_normal.jpg "foto do usuário") [Fernandes](https://twitter.com/Fernand32956519) | 15/03/2020 | 0.271 (49/181) | 5977 |
| ![alt text](http://pbs.twimg.com/profile_images/1348832830424547329/MkuMntfl_normal.jpg "foto do usuário") [Renata Pimenta](https://twitter.com/blogdarenatamg) | 09/08/2010 | 2.03 (1265/623) | 22339 |
| ![alt text](http://pbs.twimg.com/profile_images/1353802016204730368/vFloEal9_normal.jpg "foto do usuário") [Paulo Cenize](https://twitter.com/CenizePaulo) | 20/11/2017 | 0.224 (26/116) | 4470 |
| ![alt text](http://pbs.twimg.com/profile_images/1232474545992470528/QegpfxYT_normal.jpg "foto do usuário") [Sandro](https://twitter.com/Sandro43354227) | 26/02/2020 | 0.618 (558/903) | 970 |
| ![alt text](http://pbs.twimg.com/profile_images/1266526093693116416/SyRHke73_normal.jpg "foto do usuário") [Marcos Vidal](https://twitter.com/marcos_vvidal) | 03/04/2020 | 0.054 (21/392) | 879 |
| ![alt text](http://pbs.twimg.com/profile_images/1335358232307658752/vwhKlPgC_normal.jpg "foto do usuário") [Mika🍥](https://twitter.com/mikaehtudo) | 16/07/2015 | 0.923 (205/222) | 8266 |
| ![alt text](http://pbs.twimg.com/profile_images/309987237/IMAG0131__montagem__normal.jpg "foto do usuário") [Elton Pereira](https://twitter.com/elton_tp) | 09/07/2009 | 0.48 (82/171) | 266 |
| ![alt text](http://pbs.twimg.com/profile_images/1257373723365179393/9u-F5LIC_normal.jpg "foto do usuário") [Bety Alves](https://twitter.com/BetyAlves8) | 01/05/2020 | 0.1 (89/893) | 2235 |
| ![alt text](http://pbs.twimg.com/profile_images/1539496932/SDC12282_-_C_pia_normal.JPG "foto do usuário") [Adilson](https://twitter.com/Adilson_tigre) | 12/09/2011 | 0.976 (858/879) | 7562 |
| ![alt text](http://pbs.twimg.com/profile_images/1226980143060725760/SUWnzKQL_normal.jpg "foto do usuário") [Sidney ladeira cerqueira](https://twitter.com/LadeiraSidney) | 10/02/2020 | 0.527 (252/478) | 1262 |
| ![alt text](http://pbs.twimg.com/profile_images/1255559732313628674/s-Ms0UcH_normal.jpg "foto do usuário") [Moisés Constâncio](https://twitter.com/MoissConstncio1) | 29/04/2020 | 0.131 (11/84) | 2411 |
| ![alt text](http://pbs.twimg.com/profile_images/1341414066242412545/RNJMhco8_normal.jpg "foto do usuário") [Ricardo Casagrande](https://twitter.com/CasagrandeEqi) | 21/12/2018 | 7.595 (4899/645) | 3329 |
| ![alt text](http://pbs.twimg.com/profile_images/1326703561200332802/qcV7BqSK_normal.jpg "foto do usuário") [JÁ LEU MURRAY ROTHBARD?](https://twitter.com/Murray60850889) | 28/07/2020 | 0.81 (34/42) | 2232 |
| ![alt text](http://pbs.twimg.com/profile_images/1335347435716141056/L8GgyHwQ_normal.jpg "foto do usuário") [André Bogaerts🇧🇷🇧🇪🇮🇹](https://twitter.com/albogaerts) | 21/03/2012 | 0.633 (1491/2355) | 15169 |
| ![alt text](http://pbs.twimg.com/profile_images/1283355479612301312/NqNfoIPd_normal.jpg "foto do usuário") [JM](https://twitter.com/JM24238850) | 01/03/2020 | 0.139 (35/251) | 1840 |
| ![alt text](http://pbs.twimg.com/profile_images/1250883067868217349/FG1qDZeB_normal.jpg "foto do usuário") [Ana Costa](https://twitter.com/AnaPCCosta) | 01/10/2018 | 0.054 (14/260) | 6911 |
| ![alt text](http://pbs.twimg.com/profile_images/1282443456363794432/DCr4B2hO_normal.jpg "foto do usuário") [Cida & Frank](https://twitter.com/Frankdeluca1801) | 17/10/2009 | 0.749 (1681/2243) | 46803 |
| ![alt text](http://pbs.twimg.com/profile_images/1352936081453412353/V9eGfO-O_normal.jpg "foto do usuário") [Pagliaça](https://twitter.com/pagliacinha) | 24/02/2020 | 1.509 (403/267) | 19410 |
| ![alt text](http://pbs.twimg.com/profile_images/1314753506268581888/9TAiVTjB_normal.jpg "foto do usuário") [o vírus é chines](https://twitter.com/saudadedoBra) | 08/11/2018 | 0.266 (71/267) | 2229 |
| ![alt text](http://pbs.twimg.com/profile_images/1346845824110751746/9E7m4UaT_normal.jpg "foto do usuário") [Clsgf](https://twitter.com/Clsgf2) | 09/05/2020 | 0.708 (2482/3507) | 4554 |
| ![alt text](http://pbs.twimg.com/profile_images/1318705444312010754/g5c9PqYe_normal.jpg "foto do usuário") [VACINA JÁ💉💉💉](https://twitter.com/Jadyguedes1) | 29/01/2014 | 1.012 (1185/1171) | 10948 |
| ![alt text](http://pbs.twimg.com/profile_images/1293691295391768576/2m-n0uis_normal.jpg "foto do usuário") [Gabi](https://twitter.com/entropy_ss) | 12/05/2015 | 0.179 (26/145) | 311 |
| ![alt text](http://pbs.twimg.com/profile_images/1349779397511929857/9Y4Wn2w6_normal.jpg "foto do usuário") [Flavio 🇧🇷🇺🇲DM🚫](https://twitter.com/Flavio30131851) | 15/05/2019 | 0.956 (3272/3423) | 30135 |
| ![alt text](http://pbs.twimg.com/profile_images/1261790482184757250/gwyZ7gZM_normal.jpg "foto do usuário") [Silvia G Rodrigues](https://twitter.com/Silviagrr) | 12/10/2010 | 1.25 (110/88) | 14799 |
| ![alt text](http://pbs.twimg.com/profile_images/1193623285227016192/ZRrF742i_normal.jpg "foto do usuário") [Gerson Gabriéhl](https://twitter.com/GabriehlGerson) | 08/11/2019 | 1.972 (71/36) | 4544 |
| ![alt text](http://pbs.twimg.com/profile_images/1350124165454569478/7oDBpP85_normal.jpg "foto do usuário") [Marizete](https://twitter.com/Mary50680302) | 06/08/2019 | 0.701 (393/561) | 5368 |
| ![alt text](http://pbs.twimg.com/profile_images/1353022388263378945/zrvp4tbN_normal.jpg "foto do usuário") [Ângelo jr](https://twitter.com/ngelomarchioll1) | 18/04/2020 | 1.364 (45/33) | 8891 |
| ![alt text](http://pbs.twimg.com/profile_images/1239880143746842625/xBgNn6GS_normal.jpg "foto do usuário") [Sidnei](https://twitter.com/Sidnei08000613) | 01/03/2019 | 0.809 (224/277) | 9577 |
| ![alt text](http://pbs.twimg.com/profile_images/1345421492377542658/fSJm_YVQ_normal.jpg "foto do usuário") [🇧🇷🇺🇸Franci Müller 3️⃣8️⃣ 🌹❤](https://twitter.com/maemuller) | 21/07/2010 | 1.039 (5327/5127) | 100753 |
| ![alt text](http://pbs.twimg.com/profile_images/1312779017528004608/h63z5-PA_normal.jpg "foto do usuário") [Linda](https://twitter.com/Lindasod) | 26/04/2011 | 2.061 (12126/5884) | 43245 |
| ![alt text](http://pbs.twimg.com/profile_images/1260595298495324164/u_pgSnOQ_normal.jpg "foto do usuário") [Patricia Brito](https://twitter.com/patsbrito) | 29/03/2010 | 0.629 (149/237) | 12951 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [lucasleal](https://twitter.com/lucasle64163628) | 10/07/2020 | 0.01 (0/0) | 3 |
| ![alt text](http://pbs.twimg.com/profile_images/1315112442167517184/T4AzOAPX_normal.jpg "foto do usuário") [Angela](https://twitter.com/Angela40638513) | 05/04/2019 | 0.945 (432/457) | 83828 |
| ![alt text](http://pbs.twimg.com/profile_images/1309974237873082370/nVSqJO5L_normal.jpg "foto do usuário") [Cristiano](https://twitter.com/Crist__Barros) | 25/06/2019 | 0.87 (1135/1305) | 10297 |
| ![alt text](http://pbs.twimg.com/profile_images/1268545461247410178/41RWfM2w_normal.jpg "foto do usuário") [Mico Brasileiro](https://twitter.com/BrasileiroMico) | 04/06/2020 | 0.029 (18/624) | 468 |
| ![alt text](http://pbs.twimg.com/profile_images/1271140472824758272/GNQLYqxg_normal.jpg "foto do usuário") [Remus Jr. 🇧🇷 & 🇺🇲 #Bolsonaro2022 #Kalil2020](https://twitter.com/remusjr1) | 27/02/2020 | 0.492 (523/1063) | 3314 |
| ![alt text](http://pbs.twimg.com/profile_images/1352714747670638601/qNVTL_dL_normal.jpg "foto do usuário") [ﻝ](https://twitter.com/jaoooop) | 08/05/2014 | 0.291 (159/546) | 3956 |
| ![alt text](http://pbs.twimg.com/profile_images/782543305/Ange_normal.bmp "foto do usuário") [Angelina Wittmann](https://twitter.com/AngelWittmann) | 28/03/2010 | 0.9 (45/50) | 1165 |
| ![alt text](http://pbs.twimg.com/profile_images/1197192016800755713/ajutXX3L_normal.jpg "foto do usuário") [Fernando 🇧🇷](https://twitter.com/fernando_g_f_) | 20/11/2019 | 2.34 (37236/15914) | 43004 |
| ![alt text](http://pbs.twimg.com/profile_images/1349834187172442114/kyLQPoIY_normal.jpg "foto do usuário") [Humberto Gebrim](https://twitter.com/Gebrim_H) | 09/02/2010 | 1.1 (66392/60329) | 30665 |
| ![alt text](http://pbs.twimg.com/profile_images/1126289821289340928/f4EorfCy_normal.jpg "foto do usuário") [Leandro Nunes Siqueira](https://twitter.com/LeandroNunesSi6) | 09/05/2019 | 0.671 (279/416) | 9480 |
| ![alt text](http://pbs.twimg.com/profile_images/1279883974685396995/6J0vvKkI_normal.jpg "foto do usuário") [Vanderli](https://twitter.com/Vanderl57606727) | 23/11/2019 | 0.834 (1688/2023) | 12417 |
| ![alt text](http://pbs.twimg.com/profile_images/1273371402373083136/CD9qzzYT_normal.jpg "foto do usuário") [Ricardo Bolsonaro 2022](https://twitter.com/RicBols2022) | 01/07/2009 | 0.766 (36/47) | 2894 |
| ![alt text](http://pbs.twimg.com/profile_images/1284622837303697420/lrLggwTS_normal.jpg "foto do usuário") [A fia da Mae](https://twitter.com/AfiadaMae) | 08/11/2011 | 1.756 (2306/1313) | 49275 |
| ![alt text](http://pbs.twimg.com/profile_images/1293588405549506562/uawLDbCj_normal.jpg "foto do usuário") [Tarcísio 100% Bolsonaro 🇧🇷](https://twitter.com/FelixZuza) | 20/03/2020 | 0.77 (1202/1561) | 6298 |
| ![alt text](http://pbs.twimg.com/profile_images/1354094265715011585/ZduE7Eg9_normal.jpg "foto do usuário") [Alan Alves Ricardo](https://twitter.com/aaricardo) | 15/01/2010 | 0.268 (138/515) | 1120 |
| ![alt text](http://pbs.twimg.com/profile_images/1277165955/Mad_normal.jpg "foto do usuário") [Mauricio M Almeida](https://twitter.com/menegas67) | 04/03/2011 | 0.152 (52/343) | 2042 |
| ![alt text](http://pbs.twimg.com/profile_images/1273660292367634433/dv7tKhXc_normal.jpg "foto do usuário") [Claudia Pinho 🇧🇷🇧🇷🇧🇷 💛💚](https://twitter.com/Cacauprof1) | 26/10/2018 | 1.03 (24648/23927) | 35165 |
| ![alt text](http://pbs.twimg.com/profile_images/1254475585327370247/MpcadIaw_normal.jpg "foto do usuário") [SubeidaHexa🏆🦊💙](https://twitter.com/subeida1) | 03/01/2012 | 3.3 (59362/17990) | 320214 |
| ![alt text](http://pbs.twimg.com/profile_images/1352438839755866112/snTsJWRg_normal.jpg "foto do usuário") [A Esperança está em nós mesmos, no povo! 🇧🇷](https://twitter.com/MiriamTaokei100) | 10/01/2018 | 1.351 (24717/18295) | 172352 |
| ![alt text](http://pbs.twimg.com/profile_images/1333229483252396038/izlMM4ZL_normal.jpg "foto do usuário") [Liomar de Oliveira](https://twitter.com/PastorLiomar) | 19/09/2011 | 6.893 (39671/5755) | 250670 |
| ![alt text](http://pbs.twimg.com/profile_images/1289177331052040192/diRKG9HZ_normal.jpg "foto do usuário") [gдbЯiΞĿ gØmΞŞ](https://twitter.com/_GabrielBest) | 30/12/2010 | 1.289 (1753/1360) | 14615 |
| ![alt text](http://pbs.twimg.com/profile_images/943483867410960384/fpj6_U7B_normal.jpg "foto do usuário") [Samy Dana](https://twitter.com/samydana) | 23/04/2009 | 247.155 (187838/760) | 26016 |
| ![alt text](http://pbs.twimg.com/profile_images/1314969441894109185/nVi418T2_normal.jpg "foto do usuário") [Raphael Francelino](https://twitter.com/rsfran) | 15/10/2009 | 0.123 (141/1149) | 8021 |
| ![alt text](http://pbs.twimg.com/profile_images/1348235635149123590/2B7T_lfV_normal.jpg "foto do usuário") [Carlos Miguel Ferrara](https://twitter.com/CarlosCuequinha) | 04/06/2020 | 0.254 (173/680) | 7416 |
| ![alt text](http://pbs.twimg.com/profile_images/1135225370196811777/-Hr1fAF0_normal.jpg "foto do usuário") [🇧🇷 Patricia 🇧🇷](https://twitter.com/Pati_Medeiross) | 08/03/2018 | 5.821 (3958/680) | 27072 |
| ![alt text](http://pbs.twimg.com/profile_images/1348008813786521601/iFz2SLDZ_normal.jpg "foto do usuário") [EuSouLuz](https://twitter.com/EuSouLuz6) | 28/01/2019 | 0.551 (471/855) | 7834 |
| ![alt text](http://pbs.twimg.com/profile_images/1322918184903675905/MPWXf0eQ_normal.jpg "foto do usuário") [♔ Monark](https://twitter.com/monark) | 26/01/2011 | 124.661 (1093403/8771) | 16196 |
| ![alt text](http://pbs.twimg.com/profile_images/1320128673287163905/M7eK9p_O_normal.jpg "foto do usuário") [DOM WERNECK OFICIAL](https://twitter.com/Dom_Werneck) | 12/03/2015 | 7.068 (4036/571) | 4484 |
| ![alt text](http://pbs.twimg.com/profile_images/1239474108737470464/KGuNaxHU_normal.png "foto do usuário") [RENOVA](https://twitter.com/RenovaMidia) | 29/04/2013 | 138.98 (329938/2374) | 103348 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Elias G da Silva Jr](https://twitter.com/EliasGdaSilvaJ1) | 11/02/2016 | 0.0 (0/22) | 306 |
| ![alt text](http://pbs.twimg.com/profile_images/1326187265912082433/r3Ka_5Q7_normal.jpg "foto do usuário") [Luciano de Sá 🇧🇷 SDV](https://twitter.com/LUCIANOFELIPED9) | 29/01/2020 | 0.01 (3539/0) | 8126 |
| ![alt text](http://pbs.twimg.com/profile_images/1299084905192841216/Ofglm-Jt_normal.jpg "foto do usuário") [Theodore Roosevelt🇮🇱🇺🇸🇧🇷](https://twitter.com/CelsoSi70558592) | 20/03/2020 | 0.173 (66/382) | 3106 |
| ![alt text](http://pbs.twimg.com/profile_images/1271628865178349568/E51yp6nh_normal.jpg "foto do usuário") [Chad!](https://twitter.com/Thechad_guy) | 08/10/2018 | 0.146 (23/157) | 3201 |
| ![alt text](http://pbs.twimg.com/profile_images/1057008881552027649/8EM_OwQg_normal.jpg "foto do usuário") [Professor Igor 🇧🇷](https://twitter.com/professorigor) | 01/07/2009 | 120.133 (75924/632) | 28860 |
| ![alt text](http://pbs.twimg.com/profile_images/1295975423654977537/dHw9JcrK_normal.jpg "foto do usuário") [Elon Musk](https://twitter.com/elonmusk) | 02/06/2009 | 436009.373 (44472956/102) | 13456 |
| ![alt text](http://pbs.twimg.com/profile_images/1189724195434958848/aU8Qjg4M_normal.jpg "foto do usuário") [Fernanda Salles](https://twitter.com/reportersalles) | 10/08/2009 | 162.914 (182464/1120) | 7348 |
| ![alt text](http://pbs.twimg.com/profile_images/1272260257717325832/4I0cV2Hx_normal.jpg "foto do usuário") [Michelle Barros🇧🇷](https://twitter.com/MichelleBelo7) | 02/03/2020 | 2.484 (21221/8542) | 3662 |
| ![alt text](http://pbs.twimg.com/profile_images/1119710117782540288/FyeJVw3Y_normal.png "foto do usuário") [Cláudio Barizon](https://twitter.com/cbarizon) | 25/06/2010 | 0.203 (378/1859) | 9669 |
| ![alt text](http://pbs.twimg.com/profile_images/1287882800121753600/YDfSCGEo_normal.jpg "foto do usuário") [anderson gava](https://twitter.com/anderso_gava) | 20/01/2016 | 2.892 (940/325) | 1795 |
| ![alt text](http://pbs.twimg.com/profile_images/1250968868715204609/oLqtea0N_normal.jpg "foto do usuário") [Italiano dalla nostra casa di famiglia](https://twitter.com/DallaNostra) | 17/04/2020 | 0.099 (17/171) | 3936 |
| ![alt text](http://pbs.twimg.com/profile_images/1346508543256637440/9HNI__zK_normal.jpg "foto do usuário") [Rodrigo Santos](https://twitter.com/rodrigo03618840) | 18/07/2012 | 0.128 (50/391) | 578 |
| ![alt text](http://pbs.twimg.com/profile_images/1240351716039708672/ZwTMWEk0_normal.jpg "foto do usuário") [mauro Weber](https://twitter.com/mauroWeber3) | 30/01/2016 | 0.406 (73/180) | 4648 |
| ![alt text](http://pbs.twimg.com/profile_images/1355276039786737665/mo9EVcFh_normal.jpg "foto do usuário") [Marlon Reis](https://twitter.com/Marl0nreis) | 29/06/2011 | 1.454 (391/269) | 4732 |
| ![alt text](http://pbs.twimg.com/profile_images/1186443888220950529/34AgEdCE_normal.jpg "foto do usuário") [nill_san](https://twitter.com/san_nill) | 22/10/2019 | 0.026 (4/151) | 873 |
| ![alt text](http://pbs.twimg.com/profile_images/1346223920396070914/7onXNlC6_normal.jpg "foto do usuário") [Carmelo Neto](https://twitter.com/carmelonetobr) | 23/09/2015 | 886.61 (129445/146) | 14655 |
| ![alt text](http://pbs.twimg.com/profile_images/1263510971424944129/M15Ske78_normal.jpg "foto do usuário") [C. Clay 🎼🎙️🤘🚩](https://twitter.com/STARTOVERBRAZIL) | 18/05/2016 | 0.667 (310/465) | 19322 |
| ![alt text](http://pbs.twimg.com/profile_images/1326285896132554752/oJRXpXmz_normal.jpg "foto do usuário") [gi](https://twitter.com/aopgiovanna) | 09/01/2010 | 0.851 (251/295) | 27708 |
| ![alt text](http://pbs.twimg.com/profile_images/613710446315573248/XY0TuBmA_normal.jpg "foto do usuário") [Cassiano Brust](https://twitter.com/cassianobrust) | 01/12/2010 | 0.06 (22/364) | 1818 |
| ![alt text](http://pbs.twimg.com/profile_images/1347743237012918272/9SxmbzzX_normal.jpg "foto do usuário") [Nordestibolsominion](https://twitter.com/silviop05956501) | 21/07/2019 | 0.095 (41/430) | 1285 |
| ![alt text](http://pbs.twimg.com/profile_images/1320761022249140225/IjVEM6oB_normal.jpg "foto do usuário") [Paulo Alexandre](https://twitter.com/pauloalexandrev) | 18/10/2009 | 0.748 (110/147) | 73225 |
| ![alt text](http://pbs.twimg.com/profile_images/1064259712001163264/1YPzdNLl_normal.jpg "foto do usuário") [Roberto Stolt](https://twitter.com/RobertoStolt) | 25/05/2009 | 0.424 (219/516) | 1405 |
| ![alt text](http://pbs.twimg.com/profile_images/1351612322050142210/aIRsR_3I_normal.jpg "foto do usuário") [Médicos Pela Liberdade](https://twitter.com/liberdademedico) | 12/07/2020 | 204.718 (60187/294) | 5729 |
| ![alt text](http://pbs.twimg.com/profile_images/1348095797288697857/K_a4aNjK_normal.jpg "foto do usuário") [Zeuda Maria🇧🇷🇧🇷🇧🇷](https://twitter.com/zeeuda) | 13/02/2015 | 0.986 (3951/4006) | 43653 |
| ![alt text](http://pbs.twimg.com/profile_images/1260613492996005889/aPUJM4p8_normal.jpg "foto do usuário") [Rhayani Cordeiro](https://twitter.com/rhayanirfc) | 04/11/2010 | 0.274 (149/543) | 3051 |
| ![alt text](http://pbs.twimg.com/profile_images/1351131456266002439/zgQQEkvB_normal.jpg "foto do usuário") [Si vis pacem, para bellum](https://twitter.com/SunTzuPatriota) | 21/11/2019 | 0.982 (1393/1418) | 22941 |
| ![alt text](http://pbs.twimg.com/profile_images/1283250653134032897/nJO2atA-_normal.jpg "foto do usuário") [ju🇧🇷💚💛](https://twitter.com/jufmjules) | 19/10/2018 | 1.959 (1013/517) | 20353 |
| ![alt text](http://pbs.twimg.com/profile_images/1160650152706809858/yODWgfo3_normal.jpg "foto do usuário") [Raquel 👩🔰 Jesus salve o Brasil!](https://twitter.com/RaquelAcredita) | 24/03/2019 | 0.984 (6221/6325) | 35261 |
| ![alt text](http://pbs.twimg.com/profile_images/1225750369654931461/cZ1plrEw_normal.jpg "foto do usuário") [Leão da montanha...](https://twitter.com/odontvitor) | 16/07/2009 | 0.938 (1264/1347) | 6034 |
| ![alt text](http://pbs.twimg.com/profile_images/1264079900669067264/hYTLDAUK_normal.jpg "foto do usuário") [Lima](https://twitter.com/avanti_lima) | 17/06/2009 | 29.721 (1278/43) | 65091 |
| ![alt text](http://pbs.twimg.com/profile_images/1260029150179454976/AA5gyDcm_normal.jpg "foto do usuário") [Michele](https://twitter.com/Michele00304982) | 29/10/2018 | 0.349 (37/106) | 404 |
| ![alt text](http://pbs.twimg.com/profile_images/1283139152209481728/AoBEoDzr_normal.jpg "foto do usuário") [Direita Paraná](https://twitter.com/militaroperaci3) | 23/01/2020 | 0.084 (36/431) | 70 |
| ![alt text](http://pbs.twimg.com/profile_images/645609158117564416/hOaxP9Ul_normal.jpg "foto do usuário") [Marcos](https://twitter.com/marcostmartins) | 09/11/2009 | 0.137 (84/613) | 8361 |
| ![alt text](http://pbs.twimg.com/profile_images/1323054958820892672/LH38JtfG_normal.jpg "foto do usuário") [Brunokkkkkkkk](https://twitter.com/eitabichokkk) | 25/11/2018 | 0.094 (36/381) | 1675 |
| ![alt text](http://pbs.twimg.com/profile_images/1349570926430588931/3Vj8C6Hh_normal.jpg "foto do usuário") [Snowy ❄](https://twitter.com/SnowyNevado) | 23/04/2015 | 0.179 (37/207) | 473 |
| ![alt text](http://pbs.twimg.com/profile_images/1251687512139010051/GcJ2DTQp_normal.jpg "foto do usuário") [Jose lourenco neto](https://twitter.com/cysneiros_neto) | 30/05/2011 | 0.22 (9/41) | 204 |
| ![alt text](http://pbs.twimg.com/profile_images/1328451641754980358/f54_lLK0_normal.jpg "foto do usuário") [Carlos Bolsonaro](https://twitter.com/CarlosBolsonaro) | 25/08/2009 | 3249.915 (2066946/636) | 17298 |
| ![alt text](http://pbs.twimg.com/profile_images/1350261049589706753/Z0kMOc8i_normal.jpg "foto do usuário") [Antônio Inácio da Silva Júnior](https://twitter.com/AntnioInciodaS2) | 10/11/2019 | 0.036 (121/3396) | 5860 |
| ![alt text](http://pbs.twimg.com/profile_images/1347883144226222083/8T5Y8Wvg_normal.jpg "foto do usuário") [Raquel Blak](https://twitter.com/RaquelBlak) | 12/07/2009 | 1.508 (47650/31591) | 64195 |
| ![alt text](http://pbs.twimg.com/profile_images/1157824203141328897/6s-4Yuo3_normal.jpg "foto do usuário") [Churchill Sincerão](https://twitter.com/ChurchillSince1) | 04/08/2019 | 0.08 (18/225) | 261 |
| ![alt text](http://pbs.twimg.com/profile_images/1153823245625225217/XwWmVrFN_normal.jpg "foto do usuário") [Finipe Nuis](https://twitter.com/finipenuiscrf) | 27/05/2019 | 0.218 (22/101) | 287 |
| ![alt text](http://pbs.twimg.com/profile_images/1351915412812914688/DKfAjFbq_normal.jpg "foto do usuário") [Free To Choose](https://twitter.com/FreeToChooseNet) | 12/03/2009 | 5.422 (30855/5691) | 6841 |
| ![alt text](http://pbs.twimg.com/profile_images/3659320535/bc912a84f45aa0edf4e9e4af72815f7f_normal.jpeg "foto do usuário") [Jeremiah Boehner](https://twitter.com/sfboehner) | 14/10/2010 | 5.278 (3584/679) | 13991 |
| ![alt text](http://pbs.twimg.com/profile_images/1279464552111972358/Ss1uDb_7_normal.jpg "foto do usuário") [Chloé S. Valdary 📚](https://twitter.com/cvaldary) | 28/09/2011 | 28.862 (82661/2864) | 24408 |
| ![alt text](http://pbs.twimg.com/profile_images/1347942891453362178/PTIVdfXS_normal.jpg "foto do usuário") [matheusrj26](https://twitter.com/matheus26777) | 12/11/2009 | 0.595 (150/252) | 24708 |
| ![alt text](http://pbs.twimg.com/profile_images/792948932359884800/ukCGaFBy_normal.jpg "foto do usuário") [Breno Fernando 🇧🇷🇮🇱](https://twitter.com/brenofslopes) | 02/11/2009 | 0.861 (1609/1869) | 1324 |
| ![alt text](http://pbs.twimg.com/profile_images/1350437768976068608/EmLFEhYJ_normal.jpg "foto do usuário") [Rodolfo Rodrigues](https://twitter.com/rodrodri2020) | 21/05/2020 | 0.652 (796/1221) | 3208 |
| ![alt text](http://pbs.twimg.com/profile_images/1280615509378117640/HU6PbpDU_normal.jpg "foto do usuário") [Renato M Freire](https://twitter.com/renatomagnago) | 01/04/2011 | 0.63 (102/162) | 4413 |
| ![alt text](http://pbs.twimg.com/profile_images/1298393590742355975/WCLu7JSl_normal.jpg "foto do usuário") [Bolsonaro 2022/ STF Escritório do Crime](https://twitter.com/valter080396) | 25/03/2020 | 1.068 (472/442) | 27169 |
| ![alt text](http://pbs.twimg.com/profile_images/1301152532807454720/vtpradRl_normal.jpg "foto do usuário") [Alexandre Alcatraz 🇧🇷🏳️‍🌈](https://twitter.com/aleealcatraz) | 19/01/2020 | 13.243 (24129/1822) | 4823 |
| ![alt text](http://pbs.twimg.com/profile_images/1341189831561535490/C7RZ9Iz4_normal.jpg "foto do usuário") [Fernando kabulozo](https://twitter.com/FernandoCabulo3) | 24/10/2019 | 0.972 (13880/14286) | 23932 |
| ![alt text](http://pbs.twimg.com/profile_images/1313137582407024649/pVOQu3Mj_normal.jpg "foto do usuário") [Daniel (Dan) 🇧🇷🇨🇦 🔴⚪️⚫️](https://twitter.com/danfrancaca) | 20/03/2016 | 1.006 (5005/4975) | 25125 |
| ![alt text]( "foto do usuário") [](https://twitter.com/blogdojefferson) | 12/06/2019 | 444.023 (215351/485) | 4334 |
| ![alt text](http://pbs.twimg.com/profile_images/1353410600030892033/O9h2h8Uu_normal.jpg "foto do usuário") [LAURICIO 🇧🇷🇮🇹🇺🇸 🚜🍀🍃🌻🌴🌍](https://twitter.com/LauricioBiasi) | 09/02/2010 | 0.782 (1200/1535) | 10831 |
| ![alt text](http://pbs.twimg.com/profile_images/1331668753696890882/R3bkGvrk_normal.jpg "foto do usuário") [Douglas Garcia](https://twitter.com/DouglasGarcia) | 14/09/2018 | 949.346 (271513/286) | 7730 |
| ![alt text](http://pbs.twimg.com/profile_images/1150493763460050950/pY97yqoX_normal.jpg "foto do usuário") [Virgílio Marques](https://twitter.com/virgiliormneto) | 14/07/2019 | 0.114 (119/1042) | 3502 |
| ![alt text](http://pbs.twimg.com/profile_images/1297203614050668552/N-PlxfdY_normal.jpg "foto do usuário") [J C](https://twitter.com/juniorenanda2) | 14/06/2014 | 0.143 (158/1106) | 11352 |
| ![alt text](http://pbs.twimg.com/profile_images/1288670345034072064/eR9os4eY_normal.jpg "foto do usuário") [thiago guilherme 🇧🇷🇧🇷🇧🇷](https://twitter.com/thiagopmpe2012) | 22/01/2014 | 0.019 (3/154) | 721 |
| ![alt text](http://pbs.twimg.com/profile_images/1347911135098511360/Jlb2oDWe_normal.jpg "foto do usuário") [Neo](https://twitter.com/Neo_Ancap) | 23/02/2019 | 0.526 (1160/2204) | 8179 |
| ![alt text](http://pbs.twimg.com/profile_images/1343620643728863235/_3n-HSPB_normal.jpg "foto do usuário") [Arthur Bellato](https://twitter.com/ArthurBellato1) | 10/08/2019 | 0.072 (33/456) | 714 |
| ![alt text](http://pbs.twimg.com/profile_images/1331568215655403523/HA1c6sZZ_normal.jpg "foto do usuário") [Leonardo Dias](https://twitter.com/tocomleonardo) | 04/08/2018 | 3.046 (1118/367) | 3219 |
| ![alt text](http://pbs.twimg.com/profile_images/1267822312360837123/ICh8yqif_normal.jpg "foto do usuário") [Erica Oliveira](https://twitter.com/EricaOlvsantos) | 12/03/2015 | 0.882 (3590/4072) | 18219 |
| ![alt text](http://pbs.twimg.com/profile_images/1183511942129950721/auYIcXkF_normal.jpg "foto do usuário") [🇧🇷VℹVℹ🇧🇷](https://twitter.com/Vinascy7) | 23/09/2013 | 0.57 (147/258) | 2923 |
| ![alt text](http://pbs.twimg.com/profile_images/1267930819206828034/gjMt1UJW_normal.jpg "foto do usuário") [Lori](https://twitter.com/emma_swan17) | 12/04/2015 | 0.309 (51/165) | 5750 |
| ![alt text](http://pbs.twimg.com/profile_images/1347352136884092929/3AOaWIHL_normal.jpg "foto do usuário") [Robson 🇧🇷](https://twitter.com/robsondlz) | 12/07/2009 | 0.275 (142/516) | 3112 |
| ![alt text](http://pbs.twimg.com/profile_images/1247917609586249730/hYdfib-0_normal.jpg "foto do usuário") [Gabriela G.](https://twitter.com/Gabriel12125273) | 29/11/2019 | 0.191 (27/141) | 434 |
| ![alt text](http://pbs.twimg.com/profile_images/1182860711074189313/esgG3Q8s_normal.jpg "foto do usuário") [RODRIGO MOLLER](https://twitter.com/Ro_Moller) | 15/05/2014 | 308.492 (119695/388) | 66096 |
| ![alt text](http://pbs.twimg.com/profile_images/1308206408626835458/UAvqEhUR_normal.jpg "foto do usuário") [André Fernandes 🇧🇷](https://twitter.com/andrefernm) | 22/08/2011 | 664.746 (167516/252) | 15327 |
| ![alt text](http://pbs.twimg.com/profile_images/1283762343202172930/yKYVbk6I_normal.jpg "foto do usuário") [Juliana Vilarta](https://twitter.com/JulianaVilarta) | 05/05/2020 | 1.014 (12880/12703) | 5693 |
| ![alt text](http://pbs.twimg.com/profile_images/1348626046145466375/qe0e2pLr_normal.jpg "foto do usuário") [Fabio Pedrosa Weintraub🇧🇷 🇺🇸 🇮🇱 🤖](https://twitter.com/FabioPedrosa16) | 03/08/2018 | 0.583 (1212/2079) | 16785 |
| ![alt text](http://pbs.twimg.com/profile_images/1267836669669105665/jr2MqCv__normal.jpg "foto do usuário") [Abraham Weintraub](https://twitter.com/AbrahamWeint) | 22/04/2019 | 5641.808 (998600/177) | 8121 |
| ![alt text](http://pbs.twimg.com/profile_images/1328494979325505536/WH8kqCVC_normal.jpg "foto do usuário") [Gabriel Monteiro](https://twitter.com/GMonteiroRJ) | 13/12/2018 | 622.081 (300465/483) | 3408 |
| ![alt text](http://pbs.twimg.com/profile_images/1163838161111437312/_NAzdS1x_normal.jpg "foto do usuário") [Olavo de Carvalho](https://twitter.com/OlavoOpressor) | 08/07/2016 | 21980.1 (439602/20) | 2293 |
| ![alt text](http://pbs.twimg.com/profile_images/1353657155224801280/DrzxKuTC_normal.jpg "foto do usuário") [Mita Guimarães](https://twitter.com/mitags) | 15/03/2011 | 3.629 (135784/37418) | 251857 |
| ![alt text](http://pbs.twimg.com/profile_images/1268965048967483392/JqgpsGzk_normal.jpg "foto do usuário") [HELLO THERE](https://twitter.com/JulioCesar20069) | 20/07/2015 | 0.233 (196/842) | 5321 |
| ![alt text](http://pbs.twimg.com/profile_images/1350629387734016001/j3kDQ2yg_normal.jpg "foto do usuário") [William Bonfim 🇧🇷😎👉](https://twitter.com/WilliamBonfim2) | 09/10/2017 | 0.596 (982/1648) | 14365 |
| ![alt text](http://pbs.twimg.com/profile_images/1128947439896059904/_DoMMcbs_normal.jpg "foto do usuário") [Jesse Araujo](https://twitter.com/Helleyser) | 20/01/2011 | 1.467 (132/90) | 5385 |
| ![alt text](http://pbs.twimg.com/profile_images/1312388322380124160/TEWzvpJd_normal.jpg "foto do usuário") [DT](https://twitter.com/DenisT90328942) | 07/07/2009 | 0.264 (207/785) | 6308 |
| ![alt text](http://pbs.twimg.com/profile_images/1355403126464000001/XtG4MdDy_normal.jpg "foto do usuário") [Júnior Gama](https://twitter.com/JuniorGama38) | 18/05/2020 | 0.081 (14/173) | 1470 |
| ![alt text](http://pbs.twimg.com/profile_images/1354806017385615361/lpI2KIMp_normal.jpg "foto do usuário") [GiL Espírito Santo](https://twitter.com/G_i_l_m_a_r) | 10/08/2012 | 0.619 (216/349) | 9795 |
| ![alt text](http://pbs.twimg.com/profile_images/1103461158873374720/dWEf_T61_normal.png "foto do usuário") [🚩🚩Silvia Mergulhão Lula Gigante 🇧🇷🇵🇹🇦🇷🇺🇸](https://twitter.com/Sil_Mergulhao) | 17/04/2015 | 1.416 (15581/11005) | 56867 |
| ![alt text](http://pbs.twimg.com/profile_images/1352101292550844416/W1mmrSjD_normal.jpg "foto do usuário") [Van Bolsonaro 🇧🇷🇧🇷🇧🇷🇧🇷](https://twitter.com/Van_Artioli) | 22/08/2010 | 0.647 (1795/2775) | 21498 |
| ![alt text](http://pbs.twimg.com/profile_images/1213071035316293632/aZRFkdkH_normal.jpg "foto do usuário") [Frederico Untar](https://twitter.com/fredericountar) | 26/07/2009 | 0.207 (375/1811) | 9828 |
| ![alt text](http://pbs.twimg.com/profile_images/1263169667570503680/gtWlgtjv_normal.jpg "foto do usuário") [Sabrina 😎🇧🇷](https://twitter.com/TheTerror32) | 29/02/2020 | 0.554 (996/1799) | 23980 |
| ![alt text](http://pbs.twimg.com/profile_images/1210738694941859843/a_KDqMZW_normal.jpg "foto do usuário") [Lia 🔆🇧🇷🇺🇸🇮🇹](https://twitter.com/melo_livi) | 10/09/2017 | 0.375 (271/722) | 6111 |
| ![alt text](http://pbs.twimg.com/profile_images/1279990178703163394/OXgl4v9c_normal.jpg "foto do usuário") [KinGui📜🔨](https://twitter.com/kinG_KGZ) | 31/07/2015 | 0.209 (33/158) | 740 |
| ![alt text](http://pbs.twimg.com/profile_images/1252944975790309379/xHE9Fc5g_normal.jpg "foto do usuário") [Cristiane 🇧🇷](https://twitter.com/mlenira80) | 04/07/2013 | 1.023 (2110/2062) | 14754 |
| ![alt text](http://pbs.twimg.com/profile_images/1333468561390653440/pIwr519f_normal.jpg "foto do usuário") [Leandro Felix 🇧🇷](https://twitter.com/_leandrofelixx) | 08/05/2019 | 3.188 (985/309) | 967 |
| ![alt text](http://pbs.twimg.com/profile_images/1232818999597182977/qGxGU_nk_normal.jpg "foto do usuário") [Dois Mil e Vixi Hum](https://twitter.com/Rudriguo) | 04/04/2011 | 6.968 (5874/843) | 192227 |
| ![alt text](http://pbs.twimg.com/profile_images/1355214831033458690/kr-JBzdx_normal.jpg "foto do usuário") [🇧🇷Rafael Hott🇺🇸🇬🇧🇦🇺🇮🇹🇧🇷](https://twitter.com/RafaelHott2) | 28/05/2018 | 0.976 (2734/2802) | 3158 |
| ![alt text](http://pbs.twimg.com/profile_images/1288208543523405824/IN9_m098_normal.jpg "foto do usuário") [Fernando Collor ⏳](https://twitter.com/Collor) | 17/06/2009 | 186.771 (72654/389) | 17276 |
| ![alt text](http://pbs.twimg.com/profile_images/1260576666138574851/bkPhOc2R_normal.jpg "foto do usuário") [Léo Santos](https://twitter.com/LEODumont1899) | 20/02/2018 | 0.819 (1539/1879) | 18438 |
| ![alt text](http://pbs.twimg.com/profile_images/1349808526743511041/yVHodq1f_normal.jpg "foto do usuário") [FPP](https://twitter.com/jfelippejr) | 18/08/2011 | 0.112 (53/474) | 18872 |
| ![alt text](http://pbs.twimg.com/profile_images/1342950736397791233/15bSjd77_normal.jpg "foto do usuário") [TB12 going for SB#7 Lets Go!!!!!!!](https://twitter.com/up4nething45) | 25/03/2017 | 0.352 (538/1527) | 26729 |
| ![alt text](http://pbs.twimg.com/profile_images/1352705320808755200/WHv7WzOe_normal.jpg "foto do usuário") [Thiago](https://twitter.com/goianoAncap) | 18/06/2019 | 0.629 (122/194) | 2704 |
| ![alt text](http://pbs.twimg.com/profile_images/1105434897/Twitter_normal.jpg "foto do usuário") [leovieira_fln](https://twitter.com/cmtevieira) | 02/07/2009 | 0.888 (340/383) | 22269 |
| ![alt text](http://pbs.twimg.com/profile_images/1277983497068531713/XHhnLJiF_normal.jpg "foto do usuário") [Leandro Narloch](https://twitter.com/lnarloch) | 08/10/2008 | 82.98 (79910/963) | 3390 |
| ![alt text](http://pbs.twimg.com/profile_images/1296286595897864192/OfwqrT7k_normal.jpg "foto do usuário") [Marcia 🇧🇷🇧🇷](https://twitter.com/Marcia_Ctno) | 15/10/2014 | 1.19 (1891/1589) | 53325 |
| ![alt text](http://pbs.twimg.com/profile_images/1057995138650267650/ruSUBemq_normal.jpg "foto do usuário") [JC](https://twitter.com/JPettan) | 07/08/2013 | 0.836 (133/159) | 20305 |
| ![alt text](http://pbs.twimg.com/profile_images/1292898099946565632/I9Y4hHcJ_normal.jpg "foto do usuário") [Pepê 👉🇧🇷](https://twitter.com/PortoCpaulo) | 03/11/2009 | 0.899 (1011/1125) | 18185 |
| ![alt text](http://pbs.twimg.com/profile_images/914803450390736896/qeGqGJKY_normal.jpg "foto do usuário") [Mariana R Silva 🧂👌🐸](https://twitter.com/maryanaprs) | 03/11/2016 | 0.205 (62/302) | 3873 |
| ![alt text](http://pbs.twimg.com/profile_images/1347833537051975683/-D_4gxWE_normal.jpg "foto do usuário") [Fernando Barbosa](https://twitter.com/FernandoBRMA) | 06/03/2020 | 0.764 (1806/2364) | 5002 |
| ![alt text](http://pbs.twimg.com/profile_images/1350522814542082048/db1zg5vH_normal.jpg "foto do usuário") [Márcio Bolsonaro 👉👉👉👉🇧🇷🇧🇷🇧🇷🇧🇷](https://twitter.com/Marcio_ProAct) | 21/05/2009 | 0.758 (1269/1675) | 3082 |
| ![alt text](http://pbs.twimg.com/profile_images/1298962815374557189/jCis0Pql_normal.jpg "foto do usuário") [Jailton Lucena](https://twitter.com/JailtonLucena1) | 20/01/2012 | 0.402 (248/617) | 5136 |
| ![alt text](http://pbs.twimg.com/profile_images/1324323559683067906/B9JXcubK_normal.jpg "foto do usuário") [#GoTrump 🇧🇷🇺🇸](https://twitter.com/freud_nao) | 26/03/2020 | 0.731 (607/830) | 22815 |
| ![alt text](http://pbs.twimg.com/profile_images/1256593053843931136/KNmxSv2X_normal.jpg "foto do usuário") [E jr](https://twitter.com/edilsonprocto) | 29/03/2018 | 0.8 (3889/4864) | 9173 |
| ![alt text](http://pbs.twimg.com/profile_images/1190604807528157184/CiXCMQEn_normal.jpg "foto do usuário") [a.lourenco](https://twitter.com/aljbh) | 04/06/2012 | 0.086 (9/105) | 498 |
| ![alt text](http://pbs.twimg.com/profile_images/1343024788902719488/xvZElv2__normal.jpg "foto do usuário") [denise mendes](https://twitter.com/_Denise_Mendes_) | 31/10/2011 | 0.44 (66/150) | 2533 |
| ![alt text](http://pbs.twimg.com/profile_images/1292171863016312840/8yNQ9QrU_normal.jpg "foto do usuário") [Rosiel Gondim 🇧🇷🙏🕰🌍🌈☄🇧🇷](https://twitter.com/GondimRosiel) | 09/11/2019 | 0.518 (612/1181) | 3348 |
| ![alt text](http://pbs.twimg.com/profile_images/1260970895717400579/cyno4u4X_normal.jpg "foto do usuário") [Marcos™ JB/38 2022🇧🇷🇧🇷](https://twitter.com/Marcosvt65) | 05/08/2015 | 1.654 (1621/980) | 18631 |
| ![alt text](http://pbs.twimg.com/profile_images/1198700984832274432/g6dLsYVY_normal.jpg "foto do usuário") [Lia Crespo #LiberdadeParaOswaldo](https://twitter.com/liacrespo) | 11/08/2009 | 23.486 (49697/2116) | 232898 |
| ![alt text](http://pbs.twimg.com/profile_images/1233597060450000898/czzRah49_normal.jpg "foto do usuário") [Mandrágora](https://twitter.com/Mandrgo03718042) | 17/12/2010 | 0.894 (690/772) | 20416 |
| ![alt text](http://pbs.twimg.com/profile_images/1186302678122618885/EkZ1ozAH_normal.jpg "foto do usuário") [Adeliana Rezende](https://twitter.com/AdelianaRezende) | 04/08/2011 | 0.892 (701/786) | 4880 |
| ![alt text](http://pbs.twimg.com/profile_images/1343739547289604097/LFw0Qq9A_normal.jpg "foto do usuário") [Nani Barbosa 🦋](https://twitter.com/nanibarbosalima) | 11/08/2009 | 0.865 (730/844) | 29341 |
| ![alt text](http://pbs.twimg.com/profile_images/1188915898490523654/LWuv4-Qp_normal.jpg "foto do usuário") [DezLai](https://twitter.com/Dezyr9) | 07/02/2013 | 0.783 (601/768) | 6120 |
| ![alt text](http://pbs.twimg.com/profile_images/593790602531237888/YjkgFkEY_normal.jpg "foto do usuário") [Carlos Wizard](https://twitter.com/CarlosWMartins) | 03/09/2009 | 6.654 (9102/1368) | 3118 |
| ![alt text](http://pbs.twimg.com/profile_images/1351767582966214657/4N9gIXkG_normal.jpg "foto do usuário") [Firmão Constantino🇧🇷RJ](https://twitter.com/FirmaoConservad) | 01/06/2020 | 5.068 (11181/2206) | 2250 |
| ![alt text](http://pbs.twimg.com/profile_images/1453241992/DSC02182_normal.jpg "foto do usuário") [Rodrigo G. Falcão](https://twitter.com/paulista_falcao) | 09/03/2010 | 0.094 (112/1194) | 1066 |
| ![alt text](http://pbs.twimg.com/profile_images/1165935840230596608/qYHHMr3s_normal.jpg "foto do usuário") [JEAN TRENTO](https://twitter.com/JEANTRENTO) | 17/02/2010 | 0.133 (88/664) | 1916 |
| ![alt text](http://pbs.twimg.com/profile_images/811388593834954752/LrMiJ7zw_normal.jpg "foto do usuário") [Wally Ness](https://twitter.com/wallyness007) | 21/12/2016 | 0.37 (177/479) | 10400 |
| ![alt text](http://pbs.twimg.com/profile_images/1355255250706440192/8_1MFsL1_normal.jpg "foto do usuário") [Freedom🤡 🇧🇷 🇺🇸 🇮🇱💚🤘](https://twitter.com/metalintheheart) | 22/06/2015 | 0.522 (835/1601) | 51294 |
| ![alt text](http://pbs.twimg.com/profile_images/1332510339024498689/4P36cpmh_normal.jpg "foto do usuário") [SANTOLINO](https://twitter.com/santolino2020) | 01/01/2015 | 0.347 (834/2401) | 6653 |
| ![alt text](http://pbs.twimg.com/profile_images/1136089155199479808/xNeWGI4k_normal.png "foto do usuário") [Sérgio Barros](https://twitter.com/sergiobarrosaju) | 13/01/2011 | 0.672 (749/1115) | 11399 |
| ![alt text](http://pbs.twimg.com/profile_images/1106632229147590656/E2k8QeFx_normal.jpg "foto do usuário") [Nelson🇧🇷🏴‍☠️🇺🇸](https://twitter.com/MontagnaNelson) | 18/09/2014 | 0.457 (715/1563) | 22016 |
| ![alt text](http://pbs.twimg.com/profile_images/1259114107711696898/2x81cnTU_normal.jpg "foto do usuário") [🇧🇷 Suely Pinheiro 🇧🇷🇺🇸🇮🇱](https://twitter.com/SuelyPinheiro5) | 16/01/2013 | 0.602 (216/359) | 2376 |
| ![alt text](http://pbs.twimg.com/profile_images/1348041861580124161/AUTHO5iU_normal.jpg "foto do usuário") [Insider_d0_P@ss@d0](https://twitter.com/InsiderPassado) | 14/01/2020 | 0.509 (28/55) | 1414 |
| ![alt text](http://pbs.twimg.com/profile_images/1222573854335406080/5gsCjv7k_normal.jpg "foto do usuário") [Ana Carolina](https://twitter.com/AnaCaro57469834) | 12/09/2018 | 0.721 (839/1164) | 38431 |
| ![alt text](http://pbs.twimg.com/profile_images/1256765104776937483/3mDFMYIo_normal.jpg "foto do usuário") [Fim Da Linha 2.0](https://twitter.com/FimDaLinha201) | 25/04/2020 | 0.217 (53/244) | 2622 |
| ![alt text](http://pbs.twimg.com/profile_images/1107975191844532224/TyUnyKv4_normal.jpg "foto do usuário") [Neto Samora 🇧🇷🇧🇷🇧🇷🇧🇷](https://twitter.com/NetoSamora) | 03/07/2009 | 0.073 (12/164) | 134 |
| ![alt text](http://pbs.twimg.com/profile_images/1293660578007920641/6gsfEfHC_normal.jpg "foto do usuário") [Rose bombom](https://twitter.com/RoseBombom17) | 08/09/2018 | 0.681 (1774/2605) | 10285 |
| ![alt text](http://pbs.twimg.com/profile_images/1314381476058804224/DwLUgt3g_normal.jpg "foto do usuário") [Elaine](https://twitter.com/peresbio) | 09/02/2019 | 0.432 (118/273) | 980 |
| ![alt text](http://pbs.twimg.com/profile_images/1331005992193187840/ZkRrtjcO_normal.jpg "foto do usuário") [🔸 𝒎𝒍𝒌 𝒏𝒆𝒖𝒕𝒓𝒐 🐍](https://twitter.com/fckpepo) | 31/01/2011 | 3.169 (545/172) | 31897 |
| ![alt text](http://pbs.twimg.com/profile_images/656782328770011136/tyu1bv_p_normal.jpg "foto do usuário") [silasolliveira](https://twitter.com/silasolliveira) | 23/02/2012 | 0.292 (14/48) | 3512 |
| ![alt text](http://pbs.twimg.com/profile_images/1259817255531151366/uSK5FraQ_normal.jpg "foto do usuário") [Sou a Verdade](https://twitter.com/SouaVerdade3) | 11/05/2020 | 0.455 (65/143) | 2747 |
| ![alt text](http://pbs.twimg.com/profile_images/1268748554392211456/tru6tM_P_normal.jpg "foto do usuário") [Eduardo](https://twitter.com/Edu_Ferre_SP) | 29/03/2020 | 0.258 (17/66) | 862 |
| ![alt text](http://pbs.twimg.com/profile_images/1264315873256497152/jNPJqzd4_normal.jpg "foto do usuário") [Perfil Político de direita,Bolsonarista e Patriota](https://twitter.com/SoumaisB) | 20/04/2020 | 0.872 (436/500) | 357 |
| ![alt text](http://pbs.twimg.com/profile_images/1073245273760194560/eYg_W19X_normal.jpg "foto do usuário") [aloisio sales](https://twitter.com/sales_aloisio) | 02/01/2018 | 0.528 (284/538) | 1378 |
| ![alt text](http://pbs.twimg.com/profile_images/1296528416930496513/5E-5LJp5_normal.jpg "foto do usuário") [Luciane GFMC](https://twitter.com/solbrilhante06) | 02/07/2010 | 0.226 (72/319) | 4088 |
| ![alt text](http://pbs.twimg.com/profile_images/1343982959712464898/vDIQPL5q_normal.jpg "foto do usuário") [Vaiolaldo](https://twitter.com/vaiolaldo) | 30/05/2020 | 0.0 (0/63) | 88 |
| ![alt text](http://pbs.twimg.com/profile_images/1351976616285659144/JUV4NBsS_normal.jpg "foto do usuário") [Araújo](https://twitter.com/MVA1975) | 16/10/2010 | 1.856 (232/125) | 30203 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Jose](https://twitter.com/Josecbf74) | 08/10/2018 | 3.5 (49/14) | 8547 |
| ![alt text](http://pbs.twimg.com/profile_images/1350828201472368643/HPRRAq6A_normal.jpg "foto do usuário") [Arthur Falcão 🇧🇷🦅🇺🇸](https://twitter.com/arturfalcaao) | 14/08/2016 | 0.895 (1362/1521) | 20880 |
| ![alt text](http://pbs.twimg.com/profile_images/1007684929755533313/L2m1uJNI_normal.jpg "foto do usuário") [Carlos Robbi](https://twitter.com/carlos_robbi) | 07/05/2015 | 0.581 (1596/2746) | 4414 |
| ![alt text](http://pbs.twimg.com/profile_images/1277755244424966145/2b5j0y6p_normal.jpg "foto do usuário") [Fê Mininelli](https://twitter.com/FelipeMininelli) | 31/07/2009 | 0.933 (223/239) | 1740 |
| ![alt text](http://pbs.twimg.com/profile_images/525457242464587776/OyVVl698_normal.jpeg "foto do usuário") [Giovanni Silvax](https://twitter.com/gioex7) | 21/10/2014 | 0.475 (84/177) | 5119 |
| ![alt text](http://pbs.twimg.com/profile_images/1188771740085825536/AtwQeO_Z_normal.jpg "foto do usuário") [José Carlos](https://twitter.com/josejcsv) | 19/06/2013 | 0.926 (577/623) | 8171 |
| ![alt text](http://pbs.twimg.com/profile_images/1268861156367773698/JY6Z9nUX_normal.jpg "foto do usuário") [gloria esperança🇧🇷🇧🇷](https://twitter.com/GloriaS83664242) | 09/11/2019 | 0.929 (26/28) | 3845 |
| ![alt text](http://pbs.twimg.com/profile_images/1257083644449034245/EesSNGty_normal.jpg "foto do usuário") [Marilia Lisboa](https://twitter.com/MariliaLisboa6) | 03/05/2020 | 0.718 (150/209) | 10145 |
| ![alt text](http://pbs.twimg.com/profile_images/1256065680346054662/v18IQ3Tt_normal.jpg "foto do usuário") [Defensor do Brasil](https://twitter.com/BrasilDefensor) | 01/05/2020 | 0.01 (14/0) | 567 |
| ![alt text](http://pbs.twimg.com/profile_images/1283266291521007616/wgZvyFau_normal.jpg "foto do usuário") [Rafael Caixeta](https://twitter.com/rafael1_caixeta) | 04/06/2010 | 0.128 (34/266) | 62 |
| ![alt text](http://pbs.twimg.com/profile_images/1269484018678091782/8ebe2CQZ_normal.jpg "foto do usuário") [Alexandre Lima](https://twitter.com/Alexandrez3rw) | 23/07/2017 | 0.381 (8/21) | 77 |
| ![alt text](http://pbs.twimg.com/profile_images/1348596651183771649/VCKtRn-6_normal.jpg "foto do usuário") [SeifertZen](https://twitter.com/NobleSixN096) | 05/11/2019 | 0.781 (236/302) | 10470 |
| ![alt text](http://pbs.twimg.com/profile_images/1301691578617155584/OEJqfCv5_normal.jpg "foto do usuário") [Alefe N7 # MassEffect](https://twitter.com/AlefeMil) | 03/06/2020 | 0.263 (25/95) | 109 |
| ![alt text](http://pbs.twimg.com/profile_images/1348351871614820352/Tt6Y43_j_normal.jpg "foto do usuário") [τeryn](https://twitter.com/dev0_t) | 29/08/2013 | 0.53 (231/436) | 8591 |
| ![alt text](http://pbs.twimg.com/profile_images/1338136673822117900/z989IHCP_normal.jpg "foto do usuário") [NewLogcy | PERFECT DARK = Xbox](https://twitter.com/NLogcy) | 27/04/2020 | 0.521 (38/73) | 1597 |
| ![alt text](http://pbs.twimg.com/profile_images/1267903195159945229/4rv_vp4o_normal.jpg "foto do usuário") [Marcos Valim](https://twitter.com/marcosvlim) | 22/04/2009 | 1.124 (308/274) | 24075 |
| ![alt text](http://pbs.twimg.com/profile_images/1325543337710002180/Z9QAHZiL_normal.jpg "foto do usuário") [riddle](https://twitter.com/basedriddle) | 24/09/2019 | 0.652 (359/551) | 3205 |
| ![alt text](http://pbs.twimg.com/profile_images/1353016064167325697/ahyuo02B_normal.jpg "foto do usuário") [PabloDrifter310](https://twitter.com/PabloDrifter310) | 09/04/2020 | 0.707 (53/75) | 420 |
| ![alt text](http://pbs.twimg.com/profile_images/1321807312030490624/9II3ZoLW_normal.jpg "foto do usuário") [Emmanuel Penha](https://twitter.com/EmmanuelPenha) | 23/05/2019 | 0.543 (69/127) | 3338 |
| ![alt text](http://pbs.twimg.com/profile_images/1300635654112632833/9j0MphlL_normal.jpg "foto do usuário") [Filipe Reis](https://twitter.com/FilipinhoAFLDR) | 29/12/2014 | 1.014 (73/72) | 9952 |
| ![alt text](http://pbs.twimg.com/profile_images/1091202050296348672/sZv-uGlH_normal.jpg "foto do usuário") [Paulo Smack](https://twitter.com/PauloSmack) | 23/05/2013 | 0.438 (28/64) | 659 |
| ![alt text](http://pbs.twimg.com/profile_images/801435770095628288/IxvUCjiD_normal.jpg "foto do usuário") [bruno machado](https://twitter.com/brunomachadohc) | 10/08/2012 | 0.044 (8/182) | 162 |
| ![alt text](http://pbs.twimg.com/profile_images/1347752696099598339/YlpRD_C3_normal.jpg "foto do usuário") [BOLSOQUINA 2022 🇧🇷](https://twitter.com/deconauta) | 25/09/2009 | 1.534 (1552/1012) | 19308 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Matheus Augusto Da Silva CamCampo pos](https://twitter.com/augusto_pos) | 23/01/2020 | 0.083 (1/12) | 26 |
| ![alt text](http://pbs.twimg.com/profile_images/1337608170169110530/CQ2r7bTq_normal.jpg "foto do usuário") [fabrizio](https://twitter.com/sambajapones) | 01/10/2019 | 4.191 (1249/298) | 10629 |
| ![alt text](http://pbs.twimg.com/profile_images/1298646408715698181/DaqLnObF_normal.jpg "foto do usuário") [Astro](https://twitter.com/Td_Astro) | 17/01/2016 | 0.016 (2/122) | 448 |
| ![alt text](http://pbs.twimg.com/profile_images/1346951145881792514/QeaFwA-x_normal.jpg "foto do usuário") [Stian Bjørnes(Eivør fan)❤](https://twitter.com/StianbjornesFar) | 26/12/2015 | 0.249 (177/710) | 609 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Tiago Queiroz](https://twitter.com/_TiagoQueiroz_) | 22/10/2010 | 0.088 (16/181) | 492 |
| ![alt text](http://pbs.twimg.com/profile_images/1057315523753635841/6Y-qwt5V_normal.jpg "foto do usuário") [Lord Fael](https://twitter.com/LordFael1) | 11/02/2018 | 0.164 (64/390) | 728 |
| ![alt text](http://pbs.twimg.com/profile_images/1348749975170248705/wfSEHSM6_normal.jpg "foto do usuário") [Igor Rolim](https://twitter.com/igoranjosrolim) | 24/12/2018 | 0.125 (13/104) | 7 |
| ![alt text](http://pbs.twimg.com/profile_images/1221984959486943238/R9JDCo9R_normal.jpg "foto do usuário") [André Silveira #Not2013](https://twitter.com/SuperbPlace_20) | 16/07/2013 | 0.842 (170/202) | 3385 |
| ![alt text](http://pbs.twimg.com/profile_images/1268041517660352514/IypOQKxD_normal.jpg "foto do usuário") [Zanca_vitor](https://twitter.com/Zancavitor1) | 03/06/2020 | 0.5 (1/2) | 3 |
| ![alt text](http://pbs.twimg.com/profile_images/1350976812394958854/GN6d16w-_normal.jpg "foto do usuário") [Sem ideia do que colocar aqui 🇧🇷](https://twitter.com/na0imp0rta) | 12/07/2014 | 0.388 (78/201) | 1253 |
| ![alt text](http://pbs.twimg.com/profile_images/1351583026669645824/adfmn8GK_normal.png "foto do usuário") [Inglaterra #paisverso (cel quebrou to inativo)](https://twitter.com/InglaterraPV) | 12/05/2015 | 0.746 (211/283) | 1943 |
| ![alt text](http://pbs.twimg.com/profile_images/1279898716040761352/0FgizhLK_normal.jpg "foto do usuário") [Ana](https://twitter.com/AnaValentine123) | 27/04/2020 | 4.955 (332/67) | 1158 |
| ![alt text](http://pbs.twimg.com/profile_images/1304850241041072129/EpzjV7Qk_normal.jpg "foto do usuário") [Matheus Oliveira](https://twitter.com/Mathzi9) | 29/08/2019 | 0.08 (12/150) | 2572 |
| ![alt text](http://pbs.twimg.com/profile_images/1184609791357964290/k8PAdm9X_normal.jpg "foto do usuário") [Alexandre Reges](https://twitter.com/AlexandreReges4) | 17/06/2019 | 0.221 (34/154) | 204 |
| ![alt text](http://pbs.twimg.com/profile_images/1349188715894157314/lSDlW_eK_normal.jpg "foto do usuário") [Franciel](https://twitter.com/FrancielBorges_) | 04/09/2012 | 1.408 (1432/1017) | 5604 |
| ![alt text](http://pbs.twimg.com/profile_images/1293231614810628096/RJbsv4n8_normal.jpg "foto do usuário") [Kurokami - Chaotic Good](https://twitter.com/LoboDireita) | 26/09/2016 | 0.75 (144/192) | 4480 |
| ![alt text](http://pbs.twimg.com/profile_images/1348856299480604681/rw-hfOL2_normal.png "foto do usuário") [Chief 👑](https://twitter.com/Chief117Br) | 28/08/2016 | 314.475 (43712/139) | 4520 |
| ![alt text](http://pbs.twimg.com/profile_images/814242642330611712/g0Aa86Rf_normal.jpg "foto do usuário") [Anderson Luis🇧🇷🇺🇸🎮❎](https://twitter.com/Derso_LuiS) | 29/10/2010 | 0.204 (44/216) | 1313 |
| ![alt text](http://pbs.twimg.com/profile_images/1035214451689979904/Vd_Gb834_normal.jpg "foto do usuário") [EJE](https://twitter.com/sanfran_972) | 30/01/2013 | 0.295 (1284/4350) | 165287 |
| ![alt text](http://pbs.twimg.com/profile_images/1349039328241078277/_JlQGNAY_normal.jpg "foto do usuário") [Pᴀʙʟᴏ Gᴏɴçᴀʟᴠᴇs🇧🇷™](https://twitter.com/pablogoncalve80) | 28/04/2014 | 0.132 (658/4985) | 41825 |
| ![alt text](http://pbs.twimg.com/profile_images/1192916241830334464/wks9KUYX_normal.jpg "foto do usuário") [Francisco Carneiro Neto](https://twitter.com/FraCNeto) | 08/11/2019 | 0.593 (344/580) | 12789 |
| ![alt text](http://pbs.twimg.com/profile_images/1190010737751732225/TiO9mJ7Q_normal.jpg "foto do usuário") [Gabrielle Corrêa](https://twitter.com/gabriellepaco) | 07/02/2018 | 0.821 (138/168) | 1665 |
| ![alt text](http://pbs.twimg.com/profile_images/1347910070856773634/uu-EPN_W_normal.jpg "foto do usuário") [Alex Ferreira⚡️](https://twitter.com/AlexFerraris__) | 24/02/2016 | 0.0 (0/188) | 1 |
| ![alt text](http://pbs.twimg.com/profile_images/1353862927812583425/3JpgtHGM_normal.jpg "foto do usuário") [BOLSORINGA TERROR DOS COMUNISTAS🇧🇷](https://twitter.com/BleekerJeminah) | 18/10/2015 | 0.428 (207/484) | 6546 |
| ![alt text](http://pbs.twimg.com/profile_images/1241071203508502531/00PzKMoV_normal.jpg "foto do usuário") [Erick (Balu)](https://twitter.com/ErickBalu) | 19/07/2009 | 0.674 (830/1232) | 9262 |
| ![alt text](http://pbs.twimg.com/profile_images/1209900409537601537/PXO1Zpx0_normal.jpg "foto do usuário") [Paulo Cesar](https://twitter.com/PauloCe92415842) | 25/12/2019 | 0.151 (14/93) | 63 |
| ![alt text](http://pbs.twimg.com/profile_images/1267782913061457927/s7uSIKuO_normal.jpg "foto do usuário") [Renato R 🇧🇷](https://twitter.com/Renatojrs81) | 07/08/2018 | 0.16 (210/1315) | 7893 |
| ![alt text](http://pbs.twimg.com/profile_images/1190919098785566720/ig0AGFq1_normal.jpg "foto do usuário") [Liana Carvalho 🔰](https://twitter.com/Liana91268928) | 23/05/2019 | 0.829 (1509/1821) | 13956 |
| ![alt text](http://pbs.twimg.com/profile_images/1350105608205324289/BIs-XVl9_normal.jpg "foto do usuário") [Marcia Camello](https://twitter.com/_MarciaCamello_) | 04/07/2014 | 0.884 (1419/1605) | 64285 |
| ![alt text](http://pbs.twimg.com/profile_images/1287048482453434368/WJSyfK-c_normal.jpg "foto do usuário") [ECS( Pátria Amada Brasil)](https://twitter.com/ESTERCR57993904) | 18/05/2019 | 0.884 (2343/2651) | 6059 |
| ![alt text](http://pbs.twimg.com/profile_images/1251921088868745217/P-tv8tR3_normal.jpg "foto do usuário") [Oliveira josafa](https://twitter.com/OJosafa) | 19/04/2020 | 0.71 (822/1158) | 22009 |
| ![alt text](http://pbs.twimg.com/profile_images/1256227502911115264/usF4QJPL_normal.jpg "foto do usuário") [Claudio Palhares .˙.](https://twitter.com/cmpalhares) | 09/03/2013 | 1.459 (13562/9296) | 29153 |
| ![alt text](http://pbs.twimg.com/profile_images/1351380213066821633/ma7moFwX_normal.jpg "foto do usuário") [MarvicT](https://twitter.com/TimMarvic) | 19/06/2018 | 1.83 (344/188) | 31835 |
| ![alt text](http://pbs.twimg.com/profile_images/1248323174112145408/Pak0_xDO_normal.jpg "foto do usuário") [Elaine Aparecida Monteiro](https://twitter.com/Elaine_tuti) | 01/02/2018 | 0.265 (77/291) | 572 |
| ![alt text](http://pbs.twimg.com/profile_images/1352903506664034304/-p24f9dt_normal.jpg "foto do usuário") [Francisco Costa](https://twitter.com/francoal10) | 08/11/2010 | 0.905 (3963/4380) | 41254 |
| ![alt text](http://pbs.twimg.com/profile_images/1281927430329053186/79kRZIDe_normal.jpg "foto do usuário") [Kiko](https://twitter.com/direitaSOS) | 16/11/2019 | 0.672 (654/973) | 1949 |
| ![alt text](http://pbs.twimg.com/profile_images/1310704832827871232/45nFttCP_normal.jpg "foto do usuário") [Waléria](https://twitter.com/WaleriaAL) | 30/12/2012 | 0.156 (110/706) | 603 |
| ![alt text](http://pbs.twimg.com/profile_images/1130661786577985537/WRoD7uYr_normal.png "foto do usuário") [Toca do Tux](https://twitter.com/tocadotux) | 07/07/2014 | 3.034 (1587/523) | 3654 |
| ![alt text](http://pbs.twimg.com/profile_images/1347928550494625798/FaDyqiJn_normal.jpg "foto do usuário") [Caipira🇧🇷](https://twitter.com/MRao1802) | 22/03/2019 | 1.15 (2050/1782) | 79164 |
| ![alt text](http://pbs.twimg.com/profile_images/1347745745538068482/3EJFemLc_normal.jpg "foto do usuário") [conservativebr 🇧🇷](https://twitter.com/conservativebr9) | 21/05/2020 | 0.154 (76/493) | 2360 |
| ![alt text](http://pbs.twimg.com/profile_images/1216150539127398400/954oOI97_normal.jpg "foto do usuário") [Afonso Raimundo](https://twitter.com/AfonsoRaimundo7) | 23/06/2017 | 0.551 (787/1429) | 20412 |
| ![alt text](http://pbs.twimg.com/profile_images/1355525480129187842/CeokZoDE_normal.jpg "foto do usuário") [Galo1908 🇧🇷🐔](https://twitter.com/galoconserv1908) | 23/07/2009 | 1.0 (498/498) | 57178 |
| ![alt text](http://pbs.twimg.com/profile_images/1248107733749989376/ln7oHcJ9_normal.jpg "foto do usuário") [Enquanto durar 3..2..1](https://twitter.com/Rafael87030471) | 09/04/2020 | 0.487 (56/115) | 3375 |
| ![alt text](http://pbs.twimg.com/profile_images/1129376515978878976/QnM52HkI_normal.png "foto do usuário") [José Antônio Ceres](https://twitter.com/ceres_jose) | 17/05/2019 | 0.641 (139/217) | 7956 |
| ![alt text](http://pbs.twimg.com/profile_images/1343573294566531078/MwbeaeM0_normal.jpg "foto do usuário") [Matheus 🦅](https://twitter.com/matheuszicapjl) | 18/09/2016 | 0.256 (77/301) | 4419 |
| ![alt text](http://pbs.twimg.com/profile_images/1265396858135904262/wmkKqefs_normal.jpg "foto do usuário") [Mario Xavier](https://twitter.com/xvianna1) | 25/07/2014 | 0.708 (226/319) | 1921 |
| ![alt text](http://pbs.twimg.com/profile_images/1350097220901740545/LlcoxOCZ_normal.jpg "foto do usuário") [RONÉRIA SOUZA](https://twitter.com/RONERIASOUZA) | 21/03/2019 | 1.012 (1718/1697) | 32437 |
| ![alt text](http://pbs.twimg.com/profile_images/1266561578507403264/aMSKTpF9_normal.jpg "foto do usuário") [Jéssica Scaramussa](https://twitter.com/JssicaScaramus1) | 17/07/2019 | 1.012 (174/172) | 6026 |
| ![alt text](http://pbs.twimg.com/profile_images/1353878853404553216/JlTCv7gu_normal.jpg "foto do usuário") [Paty Peña #BolsopetismoNao 🐮🚫🇧🇷](https://twitter.com/PatriciaADavis) | 18/03/2011 | 0.62 (1761/2839) | 40296 |
| ![alt text](http://pbs.twimg.com/profile_images/1334640409394503680/PbkD4zO__normal.jpg "foto do usuário") [Eva Brasileira Muta🇧🇷®](https://twitter.com/muta_eva) | 07/03/2019 | 1.013 (403/398) | 16922 |
| ![alt text](http://pbs.twimg.com/profile_images/1303151562794049536/c1IYZYK0_normal.jpg "foto do usuário") [Lorenzo Fontoura](https://twitter.com/rellfy) | 04/06/2011 | 6.765 (1211/179) | 411 |
| ![alt text](http://pbs.twimg.com/profile_images/1346432786622767104/iER8H0Bs_normal.jpg "foto do usuário") [Eric|の伝説](https://twitter.com/ericxlive) | 01/03/2012 | 0.229 (244/1067) | 7514 |
| ![alt text](http://pbs.twimg.com/profile_images/1135682861829447680/C2Op7QY1_normal.jpg "foto do usuário") [Matheus](https://twitter.com/matheus50859974) | 03/06/2019 | 0.159 (21/132) | 3456 |
| ![alt text](http://pbs.twimg.com/profile_images/378800000559726830/c1bc2f302892fd75bbacc2172a608f0f_normal.jpeg "foto do usuário") [Titto](https://twitter.com/tittorocha) | 19/09/2013 | 0.136 (90/662) | 1103 |
| ![alt text](http://pbs.twimg.com/profile_images/1058338873309302785/ukIJYNbe_normal.jpg "foto do usuário") [Fernando Eidt 🇧🇷🇪🇪🌞](https://twitter.com/fernandoeidt) | 19/02/2010 | 1.061 (984/927) | 77948 |
| ![alt text](http://pbs.twimg.com/profile_images/1307743655126593544/4clfbU6l_normal.jpg "foto do usuário") [Sandro Garcia](https://twitter.com/Sandromgc) | 01/07/2009 | 0.469 (130/277) | 926 |
| ![alt text](http://pbs.twimg.com/profile_images/1238795751788089344/rvFxlza9_normal.jpg "foto do usuário") [Enoque do Carmo](https://twitter.com/enoquecarmo) | 04/11/2009 | 0.169 (22/130) | 524 |
| ![alt text](http://pbs.twimg.com/profile_images/911295345950380032/SDXrPAkf_normal.jpg "foto do usuário") [Rubens Barbosa Gonça](https://twitter.com/gonca_rubens) | 22/09/2017 | 0.14 (31/221) | 8253 |
| ![alt text](http://pbs.twimg.com/profile_images/662463853540732928/iA1NqgYr_normal.png "foto do usuário") [Volerm](https://twitter.com/VidyaVolerm) | 21/11/2011 | 0.053 (18/340) | 1314 |
| ![alt text](http://pbs.twimg.com/profile_images/1044407099176964096/ow7cOkmo_normal.jpg "foto do usuário") [Elizeu Chiodi](https://twitter.com/ChiodiElizeu) | 21/09/2018 | 0.083 (48/576) | 7265 |
| ![alt text](http://pbs.twimg.com/profile_images/1330933285262864385/gFkfRjjZ_normal.jpg "foto do usuário") [Thu🇧🇷](https://twitter.com/thuanny88) | 30/11/2016 | 0.741 (748/1010) | 22664 |
| ![alt text](http://pbs.twimg.com/profile_images/1165709013226573831/cRfz5nrZ_normal.jpg "foto do usuário") [Edbrasilia🇧🇷](https://twitter.com/Edbrasilia) | 03/07/2010 | 0.079 (224/2842) | 13695 |
| ![alt text](http://pbs.twimg.com/profile_images/1311837133796265984/SQu6QoV8_normal.jpg "foto do usuário") [Sandra Assunçao🌸🐈🐩👊](https://twitter.com/sandraassu) | 10/06/2010 | 0.208 (333/1601) | 10763 |
| ![alt text](http://pbs.twimg.com/profile_images/1290489737157832707/9DUX5_-J_normal.jpg "foto do usuário") [Victor Miyamura](https://twitter.com/Victorkazoo) | 25/10/2009 | 0.503 (567/1127) | 9937 |
| ![alt text](http://pbs.twimg.com/profile_images/959949518711205888/SycWVCPk_normal.jpg "foto do usuário") [Fabio Gongora](https://twitter.com/Fabio_Gongora) | 06/02/2012 | 0.641 (393/613) | 87052 |
| ![alt text](http://pbs.twimg.com/profile_images/1352695614929301505/vLP9mKRV_normal.jpg "foto do usuário") [condensolino](https://twitter.com/AlcebiadesJusto) | 22/03/2020 | 0.91 (5548/6098) | 7710 |
| ![alt text](http://pbs.twimg.com/profile_images/1319964969266536448/yzZqm34F_normal.jpg "foto do usuário") [=Paulo](https://twitter.com/paulocnf) | 01/01/2011 | 6.604 (6881/1042) | 139468 |
| ![alt text](http://pbs.twimg.com/profile_images/1327363300032700420/ZnVPapZ0_normal.jpg "foto do usuário") [DD.Muniz 🇧🇷🇧🇷🇧🇷 DIA 16/08 EU VOU](https://twitter.com/DDMuniz2) | 11/02/2020 | 0.466 (268/575) | 6562 |
| ![alt text](http://pbs.twimg.com/profile_images/1350176038945484800/8N7dsGuc_normal.jpg "foto do usuário") [Ventos Frios 🔺](https://twitter.com/tiabili) | 02/07/2013 | 1.187 (1597/1345) | 105139 |
| ![alt text](http://pbs.twimg.com/profile_images/1308041716017041408/nv0C3xe3_normal.jpg "foto do usuário") [Nikolas Ferreira](https://twitter.com/nikolas_dm) | 15/08/2012 | 379.292 (139200/367) | 4257 |
| ![alt text](http://pbs.twimg.com/profile_images/1257831024723218434/7OI4o62z_normal.jpg "foto do usuário") [Gomes Nasser](https://twitter.com/GomesNasser1) | 06/05/2020 | 0.912 (125/137) | 1255 |
| ![alt text](http://pbs.twimg.com/profile_images/1338702317944791041/pyko04Kk_normal.jpg "foto do usuário") [Cadu ℗🇵🇹](https://twitter.com/cadusuda) | 27/12/2014 | 1.249 (446/357) | 7507 |
| ![alt text](http://pbs.twimg.com/profile_images/1175916259352989697/jbO9mI3S_normal.jpg "foto do usuário") [Rogerio Tavares](https://twitter.com/ROGERIO_TAVARES) | 25/06/2009 | 0.288 (91/316) | 1241 |
| ![alt text](http://pbs.twimg.com/profile_images/1242844919091380225/rrbvxZpu_normal.jpg "foto do usuário") [Germano Júnior 🇧🇷🇧🇷🇧🇷🇧🇷🇧🇷🇧🇷](https://twitter.com/yoga365fla) | 14/04/2014 | 0.194 (41/211) | 3656 |
| ![alt text](http://pbs.twimg.com/profile_images/1111825036/OgAAAI6jLGxhdSg7em6LiDHDtS-3W_2rpeBVVIjV85p1nhCXvkP70GeLvJSHoBpSx622mv-tZIOC1AVSCJTMn4wCyV0Am1T1UAlSLMouloa1RAblKEW_sKNerWrG_normal.jpg "foto do usuário") [Alexandre freitas](https://twitter.com/alegfreitas) | 22/08/2010 | 0.426 (78/183) | 2424 |
| ![alt text](http://pbs.twimg.com/profile_images/1034283213114564608/gFYbbNgy_normal.jpg "foto do usuário") [Barbosa Valeria](https://twitter.com/BarbosaValeria4) | 28/08/2018 | 0.102 (20/197) | 2136 |
| ![alt text](http://pbs.twimg.com/profile_images/1232279326772477952/L7XlfiYp_normal.jpg "foto do usuário") [Ricardo Cavalcanti](https://twitter.com/CAVALCANTIBJJ) | 07/06/2009 | 1.163 (1351/1162) | 11096 |
| ![alt text](http://pbs.twimg.com/profile_images/1317752588935323649/Y3KTMhG7_normal.jpg "foto do usuário") [IaraGB 🐒💨☭ 👉👉🇧🇷](https://twitter.com/iaragb) | 03/05/2010 | 3.886 (52542/13521) | 125854 |
| ![alt text](http://pbs.twimg.com/profile_images/1347772238028808193/C4e2wGyB_normal.jpg "foto do usuário") [Jouberth Souza](https://twitter.com/Jouberth19) | 07/08/2011 | 141.635 (138094/975) | 39171 |
| ![alt text]( "foto do usuário") [](https://twitter.com/bernardopkuster) | 16/03/2015 | 551.706 (369091/669) | 12001 |
| ![alt text](http://pbs.twimg.com/profile_images/1312050367979565059/RPEjMJ9q_normal.jpg "foto do usuário") [Sandra Costa](https://twitter.com/sandralvesc) | 07/03/2019 | 0.34 (277/814) | 6089 |
| ![alt text](http://pbs.twimg.com/profile_images/1331625492856909824/OwjiyR-D_normal.jpg "foto do usuário") [VirtualSexMachine](https://twitter.com/Mozinha40998886) | 02/04/2020 | 0.209 (27/129) | 1674 |
| ![alt text](http://pbs.twimg.com/profile_images/1346252263480840192/8TqzizJg_normal.jpg "foto do usuário") [Gian Fleck ➡️🇧🇷](https://twitter.com/FleckGian) | 25/11/2019 | 0.583 (374/641) | 28246 |
| ![alt text](http://pbs.twimg.com/profile_images/1354771624470392834/PqVzJMcN_normal.jpg "foto do usuário") [Luiz Baruk](https://twitter.com/Barukluiz) | 18/05/2010 | 0.907 (1073/1183) | 39332 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [taciana neves](https://twitter.com/taciana_neves) | 29/10/2012 | 0.145 (8/55) | 621 |
| ![alt text](http://pbs.twimg.com/profile_images/871914522864492544/CjaVhNg1_normal.jpg "foto do usuário") [Maria Rosa](https://twitter.com/mmros) | 11/11/2010 | 0.304 (108/355) | 6214 |
| ![alt text](http://pbs.twimg.com/profile_images/850914657464455168/ye3b4-K9_normal.jpg "foto do usuário") [Jefferson Rossi](https://twitter.com/krieger_deutsch) | 14/07/2016 | 0.492 (1135/2306) | 31419 |
| ![alt text](http://pbs.twimg.com/profile_images/1348308494009692160/ERQr7lEm_normal.jpg "foto do usuário") [Soumaria🇧🇷](https://twitter.com/smchoh1) | 01/09/2009 | 1.062 (647/609) | 35154 |
| ![alt text](http://pbs.twimg.com/profile_images/1328721992132988929/2yP3zu6J_normal.jpg "foto do usuário") [ANDERSON BOURNER](https://twitter.com/ANDERSONBOURNER) | 25/03/2010 | 2.272 (1752/771) | 62576 |
| ![alt text](http://pbs.twimg.com/profile_images/1348970393357479937/DYPmCI3e_normal.jpg "foto do usuário") [VLOGDOLISBOA🇧🇷🇮🇱🇺🇸 O BRASIL JÁ DEU CERTO 👍](https://twitter.com/VlogdoLisboa) | 23/04/2012 | 21.496 (100668/4683) | 18710 |
| ![alt text](http://pbs.twimg.com/profile_images/1265092337304305671/rFqNHWQd_normal.jpg "foto do usuário") [Mauricio Sotero](https://twitter.com/Mauriciokriok) | 30/03/2011 | 0.386 (61/158) | 602 |
| ![alt text](http://pbs.twimg.com/profile_images/1324513947089801216/dCQV7JgV_normal.jpg "foto do usuário") [Jalapeno - Fight for freedom!](https://twitter.com/WillowJalapeno) | 27/04/2020 | 0.654 (3134/4790) | 98474 |
| ![alt text](http://pbs.twimg.com/profile_images/1229785076600360960/asfhBppy_normal.jpg "foto do usuário") [Jamerson](https://twitter.com/Jamerso14717746) | 25/06/2019 | 0.054 (13/239) | 169 |
| ![alt text](http://pbs.twimg.com/profile_images/1139918813925924870/dE_b2Ye-_normal.jpg "foto do usuário") [sara everton cutrim](https://twitter.com/isabella_arthur) | 26/11/2015 | 0.625 (65/104) | 221 |
| ![alt text](http://pbs.twimg.com/profile_images/1243657138083430409/RV4O5KIG_normal.jpg "foto do usuário") [Tony](https://twitter.com/Tony__Bravo) | 15/07/2017 | 0.7 (604/863) | 4438 |
| ![alt text](http://pbs.twimg.com/profile_images/1244548313942196226/Bd9_Rr-s_normal.jpg "foto do usuário") [Sebástian Justo 🇧🇷 🔴⚫](https://twitter.com/justo_sebastian) | 30/03/2020 | 0.542 (632/1166) | 9588 |
| ![alt text](http://pbs.twimg.com/profile_images/1204569751466455040/eTGENVB9_normal.jpg "foto do usuário") [Thiagomourat77](https://twitter.com/thiagomourat77) | 11/12/2019 | 0.068 (26/385) | 379 |
| ![alt text](http://pbs.twimg.com/profile_images/829103356610277380/ZAZrsXs3_normal.jpg "foto do usuário") [elapresta](https://twitter.com/elapresta) | 09/01/2009 | 2.41 (470/195) | 9600 |
| ![alt text](http://pbs.twimg.com/profile_images/1347886069249961984/-IZOcwUz_normal.jpg "foto do usuário") [🇧🇷 Leonardo 📚 📖 🇧🇷 🇮🇱](https://twitter.com/Leo_SF86) | 24/11/2014 | 0.875 (574/656) | 5263 |
| ![alt text](http://pbs.twimg.com/profile_images/1332348562903093250/5t0sgDFd_normal.jpg "foto do usuário") [Cezar Leite](https://twitter.com/cezarleiteofc) | 04/01/2017 | 24.776 (3097/125) | 2135 |
| ![alt text](http://pbs.twimg.com/profile_images/1317913915477659649/8Dwup46L_normal.jpg "foto do usuário") [*Q*](https://twitter.com/superperdedor) | 26/09/2018 | 0.277 (392/1413) | 11933 |
| ![alt text](http://pbs.twimg.com/profile_images/1353517384364077058/vSijM9df_normal.jpg "foto do usuário") [Wagner Reis Bastos](https://twitter.com/WagnerReisBast4) | 08/03/2017 | 0.625 (2992/4790) | 5713 |
| ![alt text](http://pbs.twimg.com/profile_images/1258782793884209152/9yiva4gq_normal.jpg "foto do usuário") [Teresa Acetto](https://twitter.com/AcettoTeresa) | 04/04/2019 | 0.874 (2580/2953) | 15894 |
| ![alt text](http://pbs.twimg.com/profile_images/1320558325105332224/qmLfJhlK_normal.jpg "foto do usuário") [Vem Tretar](https://twitter.com/vemtretar1) | 27/03/2020 | 0.298 (125/420) | 12724 |
| ![alt text](http://pbs.twimg.com/profile_images/1347734744436535298/v0lXlayE_normal.jpg "foto do usuário") [Fabio Holanda 🇧🇷](https://twitter.com/FMZoso) | 24/09/2018 | 1.137 (1051/924) | 40430 |
| ![alt text](http://pbs.twimg.com/profile_images/1220797065061654528/litpQ7Gl_normal.jpg "foto do usuário") [sonia maria evangelista](https://twitter.com/s89m1962) | 19/06/2013 | 75.0 (225/3) | 8586 |
| ![alt text](http://pbs.twimg.com/profile_images/1329602971752157187/U4tqQ8da_normal.jpg "foto do usuário") [Mateus Fernando](https://twitter.com/MFernando_03) | 20/03/2020 | 0.227 (49/216) | 827 |
| ![alt text](http://pbs.twimg.com/profile_images/1268224256439173121/yIcfLZI1_normal.jpg "foto do usuário") [Negro Bolsonaro um rapaz latino americano](https://twitter.com/GERSON52721425) | 28/04/2019 | 0.961 (2418/2517) | 1885 |
| ![alt text](http://pbs.twimg.com/profile_images/1241946482581831681/nvBraowI_normal.jpg "foto do usuário") [Ana Paula](https://twitter.com/souzapaula11) | 12/03/2012 | 1.408 (573/407) | 12162 |
| ![alt text](http://pbs.twimg.com/profile_images/1348981562914856962/zNP6JJoS_normal.jpg "foto do usuário") [FB News](https://twitter.com/fbnewsoficial) | 06/12/2019 | 43.179 (20294/470) | 2633 |
| ![alt text](http://pbs.twimg.com/profile_images/1349032358775762944/bQzlrCfn_normal.jpg "foto do usuário") [PsXetra](https://twitter.com/PsXetra) | 30/01/2018 | 0.583 (2881/4940) | 109096 |
| ![alt text](http://pbs.twimg.com/profile_images/1232450620524814337/NQPCbmUh_normal.jpg "foto do usuário") [Andrea Mito 2020 3️⃣8️⃣🇧🇷🇺🇸🇮🇱👉](https://twitter.com/mito_2020) | 31/12/2019 | 1.428 (8787/6153) | 11461 |
| ![alt text](http://pbs.twimg.com/profile_images/1348204655843618818/xh6nGIyo_normal.jpg "foto do usuário") [Lela Cohen Xavier🇧🇷🇧🇷](https://twitter.com/lelacohen) | 16/08/2009 | 1.971 (6849/3475) | 407644 |
| ![alt text](http://pbs.twimg.com/profile_images/1289061743117897728/XySPKWfd_normal.jpg "foto do usuário") [Victor Figueiredo (procurando o que fazer...)](https://twitter.com/VictorF1428) | 20/04/2012 | 0.087 (39/450) | 3966 |
| ![alt text](http://pbs.twimg.com/profile_images/1297400359447597057/AKWivTIG_normal.jpg "foto do usuário") [Fernando, o jovem nova era #FreeLucasHype](https://twitter.com/jovemnovaera) | 06/06/2014 | 20.322 (24427/1202) | 26742 |
| ![alt text](http://pbs.twimg.com/profile_images/1263104833696854018/65xwd-Rv_normal.jpg "foto do usuário") [Johnny Bolsonaro](https://twitter.com/JohnnyBolsonar1) | 10/05/2020 | 0.659 (145/220) | 1970 |
| ![alt text](http://pbs.twimg.com/profile_images/1317245286125850624/NhP1MgkO_normal.jpg "foto do usuário") [Robson87180285](https://twitter.com/Robson871802851) | 03/05/2020 | 0.644 (1530/2377) | 6244 |
| ![alt text](http://pbs.twimg.com/profile_images/1267859430051401731/Ga5lSWiN_normal.jpg "foto do usuário") [...](https://twitter.com/tea_i_go) | 21/08/2019 | 0.425 (229/539) | 1244 |
| ![alt text](http://pbs.twimg.com/profile_images/1328900122370060289/Cxj4J9FQ_normal.jpg "foto do usuário") [👑 R. Reina 🧠💡](https://twitter.com/Reina_Moreira) | 07/09/2011 | 0.554 (722/1304) | 3649 |
| ![alt text](http://pbs.twimg.com/profile_images/1311234001433227264/xSVJXun4_normal.jpg "foto do usuário") [Fada 🇧🇷3️⃣8️⃣💚💛](https://twitter.com/Fadamajor) | 22/02/2020 | 1.152 (1311/1138) | 11654 |
| ![alt text](http://pbs.twimg.com/profile_images/1277435948775682048/23LvCVWW_normal.jpg "foto do usuário") [🇧🇷Lisner](https://twitter.com/gk_storeLi) | 09/03/2020 | 3.746 (1255/335) | 15853 |
| ![alt text](http://pbs.twimg.com/profile_images/1336113045748244480/omaENyMU_normal.jpg "foto do usuário") [Junqueira, la leggenda...🐷🏆🇮🇹🇧🇷😎](https://twitter.com/NorbertoJunque1) | 12/10/2017 | 0.662 (628/948) | 10255 |
| ![alt text](http://pbs.twimg.com/profile_images/1253901359365197824/-aeFyR5g_normal.jpg "foto do usuário") [Dionísio zuchi](https://twitter.com/DionisioZuchi) | 25/04/2020 | 0.367 (36/98) | 402 |
| ![alt text](http://pbs.twimg.com/profile_images/1239919373655199750/GqtWNZRO_normal.jpg "foto do usuário") [Jc Rosa](https://twitter.com/Foia_c) | 15/10/2014 | 0.61 (615/1009) | 2929 |
| ![alt text](http://pbs.twimg.com/profile_images/1286187069648363521/Mjh7X9bc_normal.jpg "foto do usuário") [Cláudio Moura](https://twitter.com/claudiomoura26) | 18/05/2015 | 0.556 (5/9) | 2686 |
| ![alt text](http://pbs.twimg.com/profile_images/1258026194991112193/VwlPS0g2_normal.jpg "foto do usuário") [Terraqueo 20O% 🇧🇷 vô conservador](https://twitter.com/terraqueo0520) | 06/05/2020 | 0.617 (1374/2228) | 6408 |
| ![alt text](http://pbs.twimg.com/profile_images/1159478217/twitter_normal.png "foto do usuário") [Autrônica](https://twitter.com/autronica) | 04/11/2010 | 2.471 (257/104) | 17704 |
| ![alt text](http://pbs.twimg.com/profile_images/1286015308092903432/m1DzNwUd_normal.jpg "foto do usuário") [Ricardo Aguiar 🇧🇷🇧🇷🇧🇷](https://twitter.com/ricardogaguiar) | 18/04/2009 | 1.042 (321/308) | 1425 |
| ![alt text](http://pbs.twimg.com/profile_images/1324908335943081985/hmFTTrUu_normal.jpg "foto do usuário") [🇪🇪 Max Lopes 🇪🇪](https://twitter.com/MaxLopes19_09) | 24/01/2012 | 0.272 (1199/4407) | 11593 |
| ![alt text](http://pbs.twimg.com/profile_images/1327658603684241408/lUheL4F2_normal.jpg "foto do usuário") [Gilmar Gambá Rodrigues #BOLSORINGA 🤡](https://twitter.com/Grfuracao) | 26/04/2017 | 0.916 (4124/4501) | 92934 |
| ![alt text](http://pbs.twimg.com/profile_images/1329208408461938695/_t9ePuym_normal.jpg "foto do usuário") [Sem nome](https://twitter.com/jonhaegon) | 15/08/2010 | 1.076 (550/511) | 143 |
| ![alt text](http://pbs.twimg.com/profile_images/1350602830311268354/CUu5LHDb_normal.jpg "foto do usuário") [Flávio Gordon](https://twitter.com/flaviogordon) | 25/06/2009 | 129.635 (110060/849) | 30124 |
| ![alt text](http://pbs.twimg.com/profile_images/1251294164614098946/UhTHFn_b_normal.jpg "foto do usuário") [JORNAL BRASIL DE DIREITA](https://twitter.com/JORNALBRASILDE1) | 08/04/2020 | 1.565 (6493/4150) | 8500 |
| ![alt text](http://pbs.twimg.com/profile_images/1354831131363995651/VwAV9_66_normal.jpg "foto do usuário") [ana](https://twitter.com/anacrisalmeidaa) | 10/05/2020 | 0.439 (373/850) | 25793 |
| ![alt text](http://pbs.twimg.com/profile_images/1352610933068206087/iagMT58C_normal.jpg "foto do usuário") [MSantos 🇮🇱🇧🇷🇺🇸](https://twitter.com/MouzarSantos) | 04/11/2018 | 0.736 (1048/1424) | 7676 |
| ![alt text](http://pbs.twimg.com/profile_images/1347852060998463488/EhkGoiFp_normal.jpg "foto do usuário") [Tadeu Pena](https://twitter.com/TadeuPena2) | 14/03/2017 | 0.104 (15/144) | 1308 |
| ![alt text](http://pbs.twimg.com/profile_images/1341866349186969601/8iw9wHiK_normal.jpg "foto do usuário") [Hyper - Fortnite Leaks](https://twitter.com/FortniteLeaks_H) | 05/10/2018 | 3.14 (942/300) | 3414 |
| ![alt text](http://pbs.twimg.com/profile_images/1351909457220018176/UcrKfwIU_normal.jpg "foto do usuário") [Anderson Souza](https://twitter.com/Andssouz) | 02/01/2010 | 2.444 (1442/590) | 149159 |
| ![alt text](http://pbs.twimg.com/profile_images/1242964588141916161/jboP5dim_normal.jpg "foto do usuário") [🇧🇷Lon Couto ◤✠◢ 🐂🚫](https://twitter.com/LonCouto) | 26/01/2016 | 0.346 (55/159) | 1552 |
| ![alt text](http://pbs.twimg.com/profile_images/1351612568004145152/MEKfDGwv_normal.jpg "foto do usuário") [davi](https://twitter.com/davilimaz) | 05/10/2015 | 1.275 (195/153) | 20521 |
| ![alt text](http://pbs.twimg.com/profile_images/1353443523190616065/T2tBvAzW_normal.jpg "foto do usuário") [Robson Nascimento 🇧🇷 🇳🇿](https://twitter.com/RobsonVN) | 24/06/2009 | 0.245 (25/102) | 2122 |
| ![alt text](http://pbs.twimg.com/profile_images/1341371009375612928/19G2MeVt_normal.jpg "foto do usuário") [Trocamos presidente por vacina](https://twitter.com/Brunosouza25) | 09/02/2010 | 0.535 (549/1026) | 104094 |
| ![alt text](http://pbs.twimg.com/profile_images/1259639427841896449/XaOsIeHE_normal.jpg "foto do usuário") [Alessandro Mendes🔴⚫️](https://twitter.com/tataiufc) | 19/08/2010 | 0.159 (89/561) | 28481 |
| ![alt text](http://pbs.twimg.com/profile_images/1285308738405113857/EFYC9wM9_normal.jpg "foto do usuário") [Celso Daniel](https://twitter.com/Alexand62127136) | 13/05/2020 | 0.0 (0/103) | 333 |
| ![alt text](http://pbs.twimg.com/profile_images/661581329159598080/vaHtM7OP_normal.jpg "foto do usuário") [Eduardo Souza](https://twitter.com/edusouza131) | 03/11/2015 | 0.333 (16/48) | 3664 |
| ![alt text](http://pbs.twimg.com/profile_images/1350388224309473281/31lDdqgC_normal.jpg "foto do usuário") [Adv. Erick Nilson Souto 🇧🇷](https://twitter.com/ericksouto) | 29/09/2009 | 0.425 (783/1843) | 1567 |
| ![alt text](http://pbs.twimg.com/profile_images/1347716877733289988/F7M4eUXu_normal.jpg "foto do usuário") [Paraíso Brasileiro 🇧🇷](https://twitter.com/ParasoBrasilei1) | 14/02/2020 | 0.621 (470/757) | 24203 |
| ![alt text](http://pbs.twimg.com/profile_images/1221798315995648001/OYej1vjZ_normal.jpg "foto do usuário") [Jose Luiz](https://twitter.com/JLuizPR) | 14/03/2014 | 0.547 (624/1140) | 14021 |
| ![alt text](http://pbs.twimg.com/profile_images/731627965881192449/nR-_q9rC_normal.jpg "foto do usuário") [Marcos Dantas](https://twitter.com/mmm_dantas) | 14/05/2016 | 0.184 (7/38) | 62 |
| ![alt text](http://pbs.twimg.com/profile_images/1254871677219016711/HPsbqsiy_normal.jpg "foto do usuário") [Dinho](https://twitter.com/ODinho_) | 27/06/2015 | 0.649 (133/205) | 4107 |
| ![alt text](http://pbs.twimg.com/profile_images/1253888997014810624/c0EQU7Cq_normal.jpg "foto do usuário") [Bolerage](https://twitter.com/Bolerage4) | 25/04/2020 | 0.108 (64/592) | 9613 |
| ![alt text](http://pbs.twimg.com/profile_images/1245139775478267910/Ok8IBdUL_normal.jpg "foto do usuário") [Carvalho](https://twitter.com/jalexandrefc) | 24/03/2020 | 0.571 (544/953) | 23411 |
| ![alt text](http://pbs.twimg.com/profile_images/1324553469664153600/WnsQXVRY_normal.jpg "foto do usuário") [charles 🇧🇷](https://twitter.com/charlesftc) | 30/05/2011 | 2.872 (810/282) | 47783 |
| ![alt text](http://pbs.twimg.com/profile_images/1150770816092688384/pK1a8MB0_normal.jpg "foto do usuário") [plinio1964](https://twitter.com/plinio19641) | 15/07/2019 | 0.689 (210/305) | 5380 |
| ![alt text](http://pbs.twimg.com/profile_images/1274864298704220162/vizF1tZx_normal.jpg "foto do usuário") [Pobre de Direita G.D.O 🇧🇷](https://twitter.com/Marcelo62598620) | 19/04/2020 | 0.533 (64/120) | 3880 |
| ![alt text](http://pbs.twimg.com/profile_images/1329926562670665729/xzep9xzc_normal.jpg "foto do usuário") [Ediberto Alves ➡🇧🇷](https://twitter.com/edibertoalves) | 14/04/2010 | 0.894 (709/793) | 5316 |
| ![alt text](http://pbs.twimg.com/profile_images/1318996261094109184/L2fUUEUr_normal.jpg "foto do usuário") [Marcio Machado](https://twitter.com/machado722) | 15/06/2011 | 0.108 (23/212) | 1285 |
| ![alt text](http://pbs.twimg.com/profile_images/1338578277422817281/VygJgT3G_normal.jpg "foto do usuário") [AleX ConServaDor®](https://twitter.com/AlexConservador) | 24/07/2009 | 3.661 (864/236) | 2333 |
| ![alt text](http://pbs.twimg.com/profile_images/1269331394947420162/XxpvM92b_normal.jpg "foto do usuário") [andrey silva](https://twitter.com/andreysilva21) | 02/01/2013 | 0.216 (29/134) | 918 |
| ![alt text](http://pbs.twimg.com/profile_images/1197095225870766081/dErVXab__normal.jpg "foto do usuário") [FamíliaDireitaBrasil](https://twitter.com/BrazilFight) | 11/03/2019 | 10.472 (167386/15984) | 35040 |
| ![alt text](http://pbs.twimg.com/profile_images/1096925329023795200/zTlhBuP7_normal.jpg "foto do usuário") [Gilga](https://twitter.com/Gilgatzu) | 05/11/2011 | 0.084 (73/874) | 4710 |
| ![alt text](http://pbs.twimg.com/profile_images/1195649049589952512/J64OMZbr_normal.jpg "foto do usuário") [🇧🇷Mirian Dias🇧🇷🇮🇱🇺🇸](https://twitter.com/MirianDias41) | 29/10/2019 | 0.959 (375/391) | 7733 |
| ![alt text](http://pbs.twimg.com/profile_images/822999099129679873/FvC_TwEj_normal.jpg "foto do usuário") [Ricardo Pereira](https://twitter.com/caconpereira) | 31/03/2011 | 0.23 (246/1070) | 21187 |
| ![alt text](http://pbs.twimg.com/profile_images/1227409794719518725/Qwvd8yrh_normal.jpg "foto do usuário") [Luis](https://twitter.com/Luis55962330) | 09/10/2019 | 0.936 (6234/6657) | 5997 |
| ![alt text](http://pbs.twimg.com/profile_images/1254926237585244161/fnMi19Mj_normal.jpg "foto do usuário") [Armandão, O Bão!](https://twitter.com/AlFaCoimbra72) | 29/09/2019 | 0.37 (144/389) | 1998 |
| ![alt text](http://pbs.twimg.com/profile_images/547355005292789760/ZRM_0-70_normal.jpeg "foto do usuário") [Renato Noronha](https://twitter.com/RenatoNoronhaJP) | 23/12/2014 | 0.105 (88/836) | 432 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [thiago.monico](https://twitter.com/monicothiago) | 22/06/2019 | 0.015 (1/67) | 434 |
| ![alt text](http://pbs.twimg.com/profile_images/1347740857940779010/job3Zg-N_normal.jpg "foto do usuário") [Jairo Marins3](https://twitter.com/JMarins3) | 24/12/2019 | 0.428 (248/579) | 21950 |
| ![alt text](http://pbs.twimg.com/profile_images/1224384842328170498/MzZp9lSf_normal.jpg "foto do usuário") [Melck Alexandre 🔰🇧🇷](https://twitter.com/alexandre_melck) | 10/02/2019 | 0.836 (250/299) | 6940 |
| ![alt text](http://pbs.twimg.com/profile_images/1342242332746375168/bQx5_ydN_normal.jpg "foto do usuário") [Glauber Galo🇧🇷🇧🇷🇧🇷🤘🤘🤘](https://twitter.com/glaubergalo) | 28/12/2012 | 0.422 (1045/2477) | 10645 |
| ![alt text](http://pbs.twimg.com/profile_images/1348271139781541895/q92jPKf-_normal.jpg "foto do usuário") [Marcos Alves](https://twitter.com/MarcosAlves_L) | 17/08/2010 | 0.398 (727/1828) | 31032 |
| ![alt text](http://pbs.twimg.com/profile_images/1353812812850749440/0Q2HANWr_normal.jpg "foto do usuário") [carlos eduardo freit](https://twitter.com/edu0475) | 01/08/2010 | 0.265 (68/257) | 4208 |
| ![alt text](http://pbs.twimg.com/profile_images/1354558705375846406/dmndn0cw_normal.jpg "foto do usuário") [Marcus Costa](https://twitter.com/marcusmineiro13) | 03/12/2014 | 0.853 (214/251) | 5420 |
| ![alt text](http://pbs.twimg.com/profile_images/1267242528987852801/5CN7O80i_normal.jpg "foto do usuário") [liberdade mesmo que tarde! 🚮](https://twitter.com/riporip) | 12/04/2011 | 0.313 (1564/4998) | 237515 |
| ![alt text](http://pbs.twimg.com/profile_images/1287041518260441088/Mz95TiH-_normal.jpg "foto do usuário") [André Gravina 🇧🇷](https://twitter.com/ALLG_BR) | 30/04/2020 | 0.606 (114/188) | 1635 |
| ![alt text](http://pbs.twimg.com/profile_images/378800000020321942/04bd7d400768c25d7b434fd544ad71d3_normal.jpeg "foto do usuário") [Anderson L Rodrigues](https://twitter.com/joseandersonrod) | 08/04/2013 | 0.296 (24/81) | 507 |
| ![alt text](http://pbs.twimg.com/profile_images/1226958718354575360/MtLQeyTu_normal.jpg "foto do usuário") [Alberto](https://twitter.com/Alberto97687507) | 10/02/2020 | 0.601 (119/198) | 3737 |
| ![alt text](http://pbs.twimg.com/profile_images/1266096258835533824/P0Br1KSJ_normal.jpg "foto do usuário") [Andre Luís da Silva](https://twitter.com/Dr_AndreLuis) | 26/06/2017 | 0.824 (42/51) | 3166 |
| ![alt text](http://pbs.twimg.com/profile_images/1349161053968588800/r5IA8-o__normal.jpg "foto do usuário") [Rodrigo](https://twitter.com/RodrigoCaetan27) | 26/12/2012 | 0.217 (147/677) | 6688 |
| ![alt text](http://pbs.twimg.com/profile_images/1309882710048071681/l86Zvk9k_normal.jpg "foto do usuário") [nnnnnn](https://twitter.com/EuDependodeDeus) | 21/01/2020 | 0.838 (145/173) | 4706 |
| ![alt text](http://pbs.twimg.com/profile_images/1347568421169487872/di8cs8Se_normal.jpg "foto do usuário") [Giuliano Schneider🇧🇷🇺🇸🇮🇱🇵🇱](https://twitter.com/giuschneider1) | 27/01/2010 | 1.746 (2193/1256) | 115230 |
| ![alt text](http://pbs.twimg.com/profile_images/1347732823709511682/-g1CPMgd_normal.jpg "foto do usuário") [Fábio decaⓟ](https://twitter.com/fabio13do11) | 25/01/2013 | 0.107 (89/828) | 4565 |
| ![alt text](http://pbs.twimg.com/profile_images/1342640109590634496/ymqV82Mr_normal.jpg "foto do usuário") [Vanessa: sai daqui jumento falador de bosta](https://twitter.com/milicianaa) | 21/02/2020 | 21.534 (27779/1290) | 10104 |
| ![alt text](http://pbs.twimg.com/profile_images/1217549578578415616/nUMRmJ2l_normal.jpg "foto do usuário") [Roberto](https://twitter.com/Roberto14110) | 17/06/2010 | 0.646 (847/1311) | 35234 |
| ![alt text](http://pbs.twimg.com/profile_images/1343944445390172160/cmCA-L1j_normal.jpg "foto do usuário") [Júnior Costa](https://twitter.com/Juninho9978) | 05/11/2018 | 1.489 (472/317) | 1915 |
| ![alt text](http://pbs.twimg.com/profile_images/1284573537269886977/ybD6_1Kq_normal.jpg "foto do usuário") [Naldo](https://twitter.com/Naldo99739848) | 16/06/2019 | 0.542 (818/1510) | 5696 |
| ![alt text](http://pbs.twimg.com/profile_images/1355257912671805449/LEMxcha6_normal.jpg "foto do usuário") [Gilson Silva bolsonaro2022 🇧🇷](https://twitter.com/GilsonNosslig) | 06/04/2019 | 0.638 (1384/2168) | 14118 |
| ![alt text](http://pbs.twimg.com/profile_images/1255272012487983104/VL6hdKdG_normal.jpg "foto do usuário") [Palhaço Clown](https://twitter.com/Acampos24320487) | 19/03/2020 | 0.464 (84/181) | 3150 |
| ![alt text](http://pbs.twimg.com/profile_images/1039308697313456128/2fckwERq_normal.jpg "foto do usuário") [Luciano M. Caixeta](https://twitter.com/luttimendes) | 13/12/2009 | 0.16 (13/81) | 1123 |
| ![alt text](http://pbs.twimg.com/profile_images/1263841678743318528/ClY7uciA_normal.jpg "foto do usuário") [ᕈᖾɩꙆɩρ ᖇɩᑯᥱɾ - 🇧🇷 🇦🇺](https://twitter.com/PewPhillip) | 04/08/2019 | 0.425 (99/233) | 3512 |
| ![alt text](http://pbs.twimg.com/profile_images/1336124820577280006/6mtNdpTp_normal.jpg "foto do usuário") [Löwe1976🇧🇷🇩🇪](https://twitter.com/MADel231276) | 18/05/2019 | 0.589 (356/604) | 7295 |
| ![alt text](http://pbs.twimg.com/profile_images/1303478167320092672/6Ko6mqfp_normal.jpg "foto do usuário") [Akitando.com](https://twitter.com/AkitaOnRails) | 10/04/2007 | 68.313 (26437/387) | 30564 |
| ![alt text](http://pbs.twimg.com/profile_images/1254472980299685888/nRndLJpt_normal.jpg "foto do usuário") [Kélice](https://twitter.com/Klice93946418) | 26/04/2020 | 0.261 (12/46) | 81 |
| ![alt text](http://pbs.twimg.com/profile_images/1275448880214061056/vXtOb2WA_normal.jpg "foto do usuário") [GilvâniaR](https://twitter.com/GilvniaR1) | 27/10/2019 | 0.482 (239/496) | 1197 |
| ![alt text](http://pbs.twimg.com/profile_images/1223041578014576640/3bw6dxB4_normal.jpg "foto do usuário") [O Pensador](https://twitter.com/O_Pensador64) | 31/01/2020 | 1.201 (359/299) | 17732 |
| ![alt text](http://pbs.twimg.com/profile_images/1349371353217040384/mGIo2gsi_normal.jpg "foto do usuário") [@paulinho-PJK](https://twitter.com/PauloRi43090258) | 14/05/2012 | 0.195 (304/1560) | 5809 |
| ![alt text](http://pbs.twimg.com/profile_images/1272682103746985984/x5wlcylh_normal.jpg "foto do usuário") [Robson Tiger Mariano](https://twitter.com/robtigers) | 08/02/2011 | 0.235 (319/1356) | 14572 |
| ![alt text](http://pbs.twimg.com/profile_images/1263614101038813185/uxLhpFG5_normal.jpg "foto do usuário") [#FechadoComBolsonaro](https://twitter.com/Keide26192892) | 26/03/2020 | 0.391 (36/92) | 843 |
| ![alt text](http://pbs.twimg.com/profile_images/1352369487698407424/E0ntOpv8_normal.jpg "foto do usuário") [Itamar Roriz. 🇧🇷🇺🇲🇪🇸🇮🇹](https://twitter.com/roriz_itamar) | 16/11/2018 | 0.749 (448/598) | 7531 |
| ![alt text](http://pbs.twimg.com/profile_images/1287556168273891328/1Esz-_YZ_normal.jpg "foto do usuário") [Monica Leal Abrahão](https://twitter.com/LealAbrahao) | 02/04/2012 | 1.09 (470/431) | 9472 |
| ![alt text](http://pbs.twimg.com/profile_images/1089145947895013376/tCunR99S_normal.jpg "foto do usuário") [Patrick Melo](https://twitter.com/melo_patrick) | 11/07/2011 | 0.45 (412/916) | 10319 |
| ![alt text](http://pbs.twimg.com/profile_images/1258443655628697600/KzAKJhaD_normal.jpg "foto do usuário") [Amynthas Dias](https://twitter.com/AmynthasD) | 12/10/2018 | 0.263 (20/76) | 639 |
| ![alt text](http://pbs.twimg.com/profile_images/1263319339500998657/If7P6fya_normal.jpg "foto do usuário") [Nelio.Jr Lima](https://twitter.com/NlioJnior1) | 09/01/2018 | 0.153 (40/261) | 1188 |
| ![alt text](http://pbs.twimg.com/profile_images/1239263045655937024/EV1Se1vU_normal.jpg "foto do usuário") [Business Latino](https://twitter.com/BusinessLatino1) | 15/03/2020 | 0.124 (26/209) | 3208 |
| ![alt text](http://pbs.twimg.com/profile_images/1235233759559061504/Qrm3dS0W_normal.jpg "foto do usuário") [igor silva](https://twitter.com/igor45689677) | 04/03/2020 | 0.103 (15/145) | 101 |
| ![alt text](http://pbs.twimg.com/profile_images/1043229448554930177/Vmadjq2L_normal.jpg "foto do usuário") [Toni Breitenbach](https://twitter.com/Toni_Breite) | 01/12/2015 | 0.418 (105/251) | 2611 |
| ![alt text](http://pbs.twimg.com/profile_images/491738122238308352/3mwABdmB_normal.jpeg "foto do usuário") [Jairo Coesi](https://twitter.com/jairocoesi) | 10/09/2009 | 0.22 (40/182) | 17 |
| ![alt text](http://pbs.twimg.com/profile_images/1350455111953342469/_Mb6C6Qa_normal.jpg "foto do usuário") [CanárioPistola👉👊🇧🇷♥️](https://twitter.com/MouraoBreno) | 06/05/2015 | 1.154 (764/662) | 14181 |
| ![alt text](http://pbs.twimg.com/profile_images/752176168057597953/vfksco8x_normal.jpg "foto do usuário") [Gio Menegati 🇧🇷🎸🚘](https://twitter.com/giomenegati) | 19/06/2011 | 1.277 (1715/1343) | 10958 |
| ![alt text](http://pbs.twimg.com/profile_images/1227632108279037957/U4PURKBs_normal.jpg "foto do usuário") [Erick Barros](https://twitter.com/erickbarros19) | 27/10/2009 | 0.939 (77/82) | 3382 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Pedro Aguinaldo](https://twitter.com/PedroAguinaldo8) | 03/04/2020 | 0.128 (5/39) | 2264 |
| ![alt text](http://pbs.twimg.com/profile_images/1124491611172429826/7AdTFbIB_normal.jpg "foto do usuário") [Rodrigo BORGES DE CARVALHO](https://twitter.com/Rodrigo18637365) | 04/05/2019 | 0.409 (137/335) | 12858 |
| ![alt text](http://pbs.twimg.com/profile_images/1348497260141797377/4fVbd4Xi_normal.jpg "foto do usuário") [HenriqueASilva](https://twitter.com/HenriqueASilva6) | 19/03/2019 | 0.135 (82/607) | 3920 |
| ![alt text](http://pbs.twimg.com/profile_images/1242470852681240578/8QMvs0tP_normal.jpg "foto do usuário") [Sandro Freitas🇧🇷🇺🇲🙏](https://twitter.com/sandromatchball) | 16/11/2011 | 0.719 (582/810) | 31103 |
| ![alt text](http://pbs.twimg.com/profile_images/1345312308663365637/jJrz-axB_normal.jpg "foto do usuário") [Enelu](https://twitter.com/eneidaluciacar1) | 06/03/2019 | 0.82 (2299/2805) | 90932 |
| ![alt text](http://pbs.twimg.com/profile_images/1347936645333594112/WB7XvlZS_normal.jpg "foto do usuário") [ⓟ Gerson Souza⚽️🏀🐽💚🇧🇷](https://twitter.com/Gerson__Souza) | 10/07/2009 | 0.79 (1750/2215) | 107259 |
| ![alt text](http://pbs.twimg.com/profile_images/1347231926709592065/GUS1o1ms_normal.jpg "foto do usuário") [fatima peixoto🇧🇷🇧🇷#💯%Bolsonaro.](https://twitter.com/peixoto507) | 31/03/2012 | 0.975 (1797/1843) | 3713 |
| ![alt text](http://pbs.twimg.com/profile_images/1254182993935175681/FyPMhwXK_normal.jpg "foto do usuário") [Emanuelle 🇧🇷](https://twitter.com/emanuelletenori) | 25/04/2020 | 0.822 (134/163) | 365 |
| ![alt text](http://pbs.twimg.com/profile_images/1355075261784608771/Ly4NzLtk_normal.jpg "foto do usuário") [Ramon](https://twitter.com/Rah_coffee) | 09/03/2019 | 3.861 (641/166) | 15287 |
| ![alt text](http://pbs.twimg.com/profile_images/1254139780176240642/Ly35aKr0_normal.jpg "foto do usuário") [Thiago Correia🔴⚫](https://twitter.com/Th_SilvaCRF) | 29/10/2018 | 0.709 (376/530) | 2097 |
| ![alt text](http://pbs.twimg.com/profile_images/1349215851900239874/8NV3q3Du_normal.jpg "foto do usuário") [Benedito](https://twitter.com/BeneditoSilind1) | 09/03/2020 | 1.046 (91/87) | 13707 |
| ![alt text](http://pbs.twimg.com/profile_images/1323284212372459522/Pdvlobvo_normal.jpg "foto do usuário") [Paulo henrique 🇧🇷🇺🇸🇬🇧🇺🇦🇸🇪](https://twitter.com/paulo17hen) | 20/11/2019 | 0.842 (1876/2227) | 19227 |
| ![alt text](http://pbs.twimg.com/profile_images/1255194949529763845/FJu-yDmj_normal.jpg "foto do usuário") [Felipe Vianna](https://twitter.com/PhilippusCaesar) | 22/08/2013 | 1.043 (973/933) | 6931 |
| ![alt text](http://pbs.twimg.com/profile_images/1349000602748121090/4cd4RbVx_normal.jpg "foto do usuário") [Fabricio Lopes](https://twitter.com/flopes_com) | 05/08/2018 | 0.466 (76/163) | 10862 |
| ![alt text](http://pbs.twimg.com/profile_images/1189294632921894914/Lpt3vJqe_normal.jpg "foto do usuário") [Diogo R](https://twitter.com/ManoDoBrasilis) | 21/12/2014 | 0.412 (73/177) | 7577 |
| ![alt text](http://pbs.twimg.com/profile_images/1286794064/DSC00468_normal.JPG "foto do usuário") [Marco Aurélio](https://twitter.com/MamfMotta) | 25/03/2011 | 0.348 (196/563) | 2402 |
| ![alt text](http://pbs.twimg.com/profile_images/1348035661689999362/1LIHAuuv_normal.jpg "foto do usuário") [Joao Carlos Gama](https://twitter.com/viotrgama) | 24/05/2010 | 0.439 (435/991) | 15733 |
| ![alt text](http://pbs.twimg.com/profile_images/1342514202892709891/8kEKwzRf_normal.jpg "foto do usuário") [Ana Helena Mofatto 🇧🇷👊💚](https://twitter.com/aninhamofatto) | 14/06/2010 | 1.022 (5207/5094) | 137410 |
| ![alt text](http://pbs.twimg.com/profile_images/1288621053502271489/L3Lw0cwe_normal.jpg "foto do usuário") [Adriana Oliveira](https://twitter.com/Adriana86984280) | 29/09/2018 | 0.49 (348/710) | 1529 |
| ![alt text](http://pbs.twimg.com/profile_images/1231359273952825345/Jc25kNHh_normal.jpg "foto do usuário") [Tiago Hernan🇧🇷⚖️](https://twitter.com/Ragnar_Anvil) | 22/02/2020 | 0.665 (189/284) | 5973 |
| ![alt text](http://pbs.twimg.com/profile_images/1034467768421240832/zciYixO6_normal.jpg "foto do usuário") [Guilherme Fiuza](https://twitter.com/GFiuza_Oficial) | 04/10/2014 | 694.325 (677661/976) | 11916 |
| ![alt text](http://pbs.twimg.com/profile_images/659878843369566208/j6WDBwO8_normal.jpg "foto do usuário") [Alexandra Martini](https://twitter.com/xandinhamartini) | 29/10/2015 | 0.582 (410/705) | 4310 |
| ![alt text](http://pbs.twimg.com/profile_images/1241033729646243843/BMEeBvQg_normal.jpg "foto do usuário") [neuza](https://twitter.com/neuzaalmeidao) | 20/03/2020 | 0.524 (86/164) | 1554 |
| ![alt text](http://pbs.twimg.com/profile_images/1252218689522413569/RVNgiZ5O_normal.jpg "foto do usuário") [Julio](https://twitter.com/JulioRaminho) | 08/07/2011 | 0.073 (8/110) | 72 |
| ![alt text](http://pbs.twimg.com/profile_images/1352078679095058434/VUtB7HYq_normal.jpg "foto do usuário") [Lilly Van Pelt](https://twitter.com/lilianmgmota) | 15/07/2016 | 2.064 (933/452) | 58087 |
| ![alt text](http://pbs.twimg.com/profile_images/1323216703371825152/p262c10M_normal.jpg "foto do usuário") [Rogério 🇧🇷](https://twitter.com/rogeriobdolive1) | 09/10/2019 | 8.605 (370/43) | 11512 |
| ![alt text](http://pbs.twimg.com/profile_images/1256032820700614656/0J47FQRs_normal.jpg "foto do usuário") [Alinne 🌸✨](https://twitter.com/linepolo) | 30/12/2009 | 2.336 (1051/450) | 14300 |
| ![alt text](http://pbs.twimg.com/profile_images/1244994865227862021/RVgpJ4Ju_normal.jpg "foto do usuário") [Ed](https://twitter.com/eduhaas) | 22/05/2009 | 0.16 (97/607) | 3459 |
| ![alt text](http://pbs.twimg.com/profile_images/1348031814854713346/hvwB1ZDM_normal.jpg "foto do usuário") [Marcos Alberto 🇮🇹🇧🇷](https://twitter.com/MarcosA74382174) | 17/08/2017 | 0.95 (1424/1499) | 4138 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [coruja](https://twitter.com/coruja25251764) | 31/10/2018 | 0.104 (17/163) | 7831 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Mauricio Alves](https://twitter.com/Maurici95108576) | 25/10/2018 | 0.456 (26/57) | 474 |
| ![alt text](http://pbs.twimg.com/profile_images/1250635254559318017/PyzE9ijc_normal.jpg "foto do usuário") [Renan Bolsonaro](https://twitter.com/renan_bolsonaro) | 21/06/2016 | 719.19 (45309/63) | 101 |
| ![alt text](http://pbs.twimg.com/profile_images/1346907054871601155/4SGcQqsW_normal.jpg "foto do usuário") [Metamorfina](https://twitter.com/Metamorfina01) | 30/04/2020 | 0.333 (143/430) | 6524 |
| ![alt text](http://pbs.twimg.com/profile_images/1189538159652167682/CzaOPtFo_normal.jpg "foto do usuário") [Gusfring](https://twitter.com/Gusfringmal) | 25/02/2012 | 0.079 (54/681) | 2526 |
| ![alt text](http://pbs.twimg.com/profile_images/1295423155314532364/VH_dFLHa_normal.jpg "foto do usuário") [◤✠◢Wedson Lima🇧🇷](https://twitter.com/wedsonlcosta) | 22/12/2016 | 0.268 (177/661) | 8159 |
| ![alt text](http://pbs.twimg.com/profile_images/1199096314669215744/sP2KMsBL_normal.jpg "foto do usuário") [GC Manhães🇧🇷🙏](https://twitter.com/gcmanhaes34) | 27/10/2014 | 0.055 (17/307) | 1420 |
| ![alt text](http://pbs.twimg.com/profile_images/1254396076615925762/_yCw_F4e_normal.jpg "foto do usuário") [Paulo Gontijo](https://twitter.com/Paulinho_81) | 10/08/2009 | 1.247 (288/231) | 33310 |
| ![alt text](http://pbs.twimg.com/profile_images/1293655630218252294/iCghMc3C_normal.jpg "foto do usuário") [Deixa o MOÇONARO te leitar JOHN-TEXX9 🇧🇷 ☦️🛡⚔️](https://twitter.com/DoTexxx9) | 22/07/2014 | 0.696 (561/806) | 11870 |
| ![alt text](http://pbs.twimg.com/profile_images/1347847413365616642/dlZ1Dg-D_normal.jpg "foto do usuário") [Danielle](https://twitter.com/daniballet_78) | 15/06/2016 | 0.359 (334/930) | 24690 |
| ![alt text](http://pbs.twimg.com/profile_images/1254604124873785344/YH0RXHiE_normal.jpg "foto do usuário") [TIA DO ZAPZAP](https://twitter.com/Tiadozapzapyah1) | 27/04/2020 | 0.482 (227/471) | 303 |
| ![alt text](http://pbs.twimg.com/profile_images/1306320048223641600/kDKpWuCG_normal.jpg "foto do usuário") [🔜MACLEURE🔙⚫🔴ᶜʳᶠ░░░](https://twitter.com/macleure_) | 02/06/2014 | 0.99 (6845/6914) | 23383 |
| ![alt text](http://pbs.twimg.com/profile_images/1287002082256576514/MlUQB7zy_normal.jpg "foto do usuário") [Niltomar Jesus](https://twitter.com/niltom96) | 18/04/2012 | 0.66 (215/326) | 424 |
| ![alt text](http://pbs.twimg.com/profile_images/1326696950788460548/1cxfQBa__normal.jpg "foto do usuário") [🌙n](https://twitter.com/Comiafodase01) | 20/10/2013 | 0.217 (68/313) | 4154 |
| ![alt text](http://pbs.twimg.com/profile_images/1299175686192730119/jrFobw13_normal.jpg "foto do usuário") [J.Peterson🇧🇷🇮🇱🇺🇸](https://twitter.com/gabinete_d_amor) | 29/04/2019 | 0.58 (1346/2322) | 4628 |
| ![alt text](http://pbs.twimg.com/profile_images/1244321318167883777/zOTL8Z1Y_normal.jpg "foto do usuário") [Ivone Brum](https://twitter.com/IvoneBrum1) | 29/03/2020 | 0.0 (0/46) | 1772 |
| ![alt text](http://pbs.twimg.com/profile_images/1348432244625592321/Pe_9l8Zc_normal.jpg "foto do usuário") [Maria Dobis 🇧🇷🇸🇻](https://twitter.com/maria_dobis) | 18/02/2018 | 0.109 (18/165) | 1604 |
| ![alt text](http://pbs.twimg.com/profile_images/1228504372260360193/812OvUz5_normal.jpg "foto do usuário") [NIOBIO](https://twitter.com/niobio8) | 15/02/2020 | 0.081 (60/738) | 4753 |
| ![alt text](http://pbs.twimg.com/profile_images/1245743322947297283/BpdLV24S_normal.jpg "foto do usuário") [Sr.Eidson](https://twitter.com/SrEidson) | 25/12/2011 | 0.119 (15/126) | 380 |
| ![alt text](http://pbs.twimg.com/profile_images/1267170502939983875/Rma8KTdQ_normal.jpg "foto do usuário") [Barreto 🇧🇷](https://twitter.com/BarretoPolitica) | 28/04/2020 | 0.997 (2317/2324) | 1833 |
| ![alt text](http://pbs.twimg.com/profile_images/1233943987293229057/OMCVTg1C_normal.jpg "foto do usuário") [ZeRinaldo](https://twitter.com/ZRinaldo49) | 04/12/2019 | 0.04 (9/226) | 1199 |
| ![alt text](http://pbs.twimg.com/profile_images/1302666270580629512/xF-dYVDz_normal.jpg "foto do usuário") [Júlio Frank Moreira Marquês Bastos](https://twitter.com/jfrankbolsonaro) | 02/08/2019 | 0.45 (532/1181) | 708 |
| ![alt text](http://pbs.twimg.com/profile_images/1354808196536254465/YOQmHHj5_normal.jpg "foto do usuário") [inimigo do felipe neto](https://twitter.com/thenotoriousgh) | 28/11/2019 | 1.444 (78/54) | 76 |
| ![alt text](http://pbs.twimg.com/profile_images/1347878742849433600/wm5AlBhV_normal.jpg "foto do usuário") [Castelarneto](https://twitter.com/Castelarneto) | 26/10/2011 | 0.413 (320/775) | 1499 |
| ![alt text](http://pbs.twimg.com/profile_images/1289206399/tu_normal.jpg "foto do usuário") [Josse Vale](https://twitter.com/JosseVale) | 28/01/2010 | 1.12 (28/25) | 1211 |
| ![alt text](http://pbs.twimg.com/profile_images/1348919850572406784/oV42ylV1_normal.jpg "foto do usuário") [🇧🇷 Hélio Freire - S.P. - 🇧🇷](https://twitter.com/HlioFreire5) | 05/01/2019 | 0.669 (1628/2432) | 64319 |
| ![alt text](http://pbs.twimg.com/profile_images/1351101258137022466/O08dxTQq_normal.jpg "foto do usuário") [Jackson S.F. Taschner 🇧🇷 🙏](https://twitter.com/SF74T) | 24/03/2009 | 0.842 (654/777) | 12203 |
| ![alt text](http://pbs.twimg.com/profile_images/1057608259505475585/npwGifgk_normal.jpg "foto do usuário") [Anderson Silva](https://twitter.com/anderson_gs1) | 05/04/2018 | 0.904 (47/52) | 1303 |
| ![alt text](http://pbs.twimg.com/profile_images/1347734790552907777/QnsIZcnf_normal.jpg "foto do usuário") [Ghost](https://twitter.com/Cristia90191822) | 07/03/2019 | 0.592 (365/617) | 25637 |
| ![alt text](http://pbs.twimg.com/profile_images/1252089794705985537/FESmaCKG_normal.jpg "foto do usuário") [Mariana Montagna](https://twitter.com/MontagnaMariana) | 05/04/2020 | 0.444 (171/385) | 1684 |
| ![alt text](http://pbs.twimg.com/profile_images/1182991583156813824/coZ0KoAI_normal.jpg "foto do usuário") [Daniel Francisco](https://twitter.com/Danielfrancis29) | 02/08/2011 | 0.074 (18/242) | 1849 |
| ![alt text](http://pbs.twimg.com/profile_images/1259496530022731776/3jrUhTmP_normal.jpg "foto do usuário") [Alan Paixão 🇧🇷](https://twitter.com/AlanOPaixao) | 15/05/2014 | 0.33 (38/115) | 559 |
| ![alt text](http://pbs.twimg.com/profile_images/1113833709860421632/KGdPAlrB_normal.jpg "foto do usuário") [Jederson](https://twitter.com/Jedersonqg) | 05/12/2018 | 0.154 (6/39) | 93 |
| ![alt text](http://pbs.twimg.com/profile_images/1258940642048311296/Ws4pXBbc_normal.jpg "foto do usuário") [Dr.Walter Faria Adv. (Mestre Abá)](https://twitter.com/MESTREABASEED) | 31/08/2011 | 0.238 (152/638) | 474 |
| ![alt text](http://pbs.twimg.com/profile_images/1233063997164920833/J9DLirmU_normal.jpg "foto do usuário") [@Diasblankk1](https://twitter.com/EdsonDiasSouza1) | 13/04/2018 | 0.936 (1356/1448) | 17160 |
| ![alt text](http://pbs.twimg.com/profile_images/1353847395579273216/2QE2v8Ce_normal.jpg "foto do usuário") [🇧🇷🇧🇷PequenaBolsoMITO③⑧ 🇧🇷🇧🇷](https://twitter.com/pequenagardenal) | 08/03/2014 | 1.267 (36218/28580) | 103108 |
| ![alt text](http://pbs.twimg.com/profile_images/1347734291262877699/gEnCboYM_normal.jpg "foto do usuário") [TiagoSG 🇧🇷🇧🇷🇧🇷](https://twitter.com/TiagoSG22) | 02/06/2009 | 0.951 (802/843) | 81529 |
| ![alt text](http://pbs.twimg.com/profile_images/1354470498189647873/LJuMBMmk_normal.jpg "foto do usuário") [#Chaperinga38 💋🎩💜](https://twitter.com/nzmendes1) | 04/07/2014 | 0.972 (33136/34090) | 470597 |
| ![alt text](http://pbs.twimg.com/profile_images/1171576602297294851/KyGGngyw_normal.jpg "foto do usuário") [TeAtualizei 🇧🇷👊🏻❤️](https://twitter.com/taoquei1) | 13/01/2013 | 316.961 (409513/1292) | 27828 |
| ![alt text](http://pbs.twimg.com/profile_images/1348347002170572801/Nub0pjz8_normal.jpg "foto do usuário") [Abelando 6% 🍀🐷](https://twitter.com/vna100) | 21/06/2016 | 1.226 (716/584) | 22288 |
| ![alt text](http://pbs.twimg.com/profile_images/1277256455402504192/oiTSw8c9_normal.jpg "foto do usuário") [Garcia 🇧🇷](https://twitter.com/Deo_GJ) | 21/06/2013 | 0.799 (187/234) | 1149 |
| ![alt text](http://pbs.twimg.com/profile_images/1354217246705508352/ZaJ4y_Fs_normal.jpg "foto do usuário") [SFC (2015 SERÁ VINGADO) 4%🐳](https://twitter.com/DaniloJCReina) | 04/04/2018 | 0.01 (259/0) | 11432 |
| ![alt text](http://pbs.twimg.com/profile_images/1288052357264281601/NS7GXK7U_normal.jpg "foto do usuário") [Kaneka Muck](https://twitter.com/guigamuck) | 17/06/2009 | 1.448 (740/511) | 64064 |
| ![alt text](http://pbs.twimg.com/profile_images/1069347406137958402/m1RWqKr3_normal.jpg "foto do usuário") [Maramouradebortoli](https://twitter.com/Mara70963148) | 29/11/2018 | 0.209 (14/67) | 226 |
| ![alt text](http://pbs.twimg.com/profile_images/1255510434116964353/Wln_jg1L_normal.jpg "foto do usuário") [Katia Marine](https://twitter.com/MarineKatia) | 20/10/2018 | 0.464 (77/166) | 3648 |
| ![alt text](http://pbs.twimg.com/profile_images/1287042943832985600/_RqqGTjC_normal.jpg "foto do usuário") [Marcelo](https://twitter.com/MarceloPain) | 17/08/2009 | 0.597 (145/243) | 5654 |
| ![alt text](http://pbs.twimg.com/profile_images/1350593122871468032/LciKEIv7_normal.jpg "foto do usuário") [Carla Zambelli](https://twitter.com/CarlaZambelli38) | 17/03/2018 | 3450.416 (1135187/329) | 19336 |
| ![alt text](http://pbs.twimg.com/profile_images/1179517015951904768/7mlSuCSR_normal.jpg "foto do usuário") [RafaelCP 🐸](https://twitter.com/rcp80) | 19/08/2011 | 0.664 (281/423) | 16080 |
| ![alt text](http://pbs.twimg.com/profile_images/1182270300211286017/DIFD94vS_normal.jpg "foto do usuário") [Elzira #Bolsonaro2022](https://twitter.com/netodepaula) | 21/07/2009 | 0.413 (2046/4957) | 22249 |
| ![alt text](http://pbs.twimg.com/profile_images/1182057652056137728/oTo0rcYM_normal.jpg "foto do usuário") [Cosmos](https://twitter.com/CosmoSantos_) | 11/12/2010 | 0.59 (851/1442) | 35420 |
| ![alt text](http://pbs.twimg.com/profile_images/1222590732118249474/RAP99hPw_normal.jpg "foto do usuário") [Guchi maria balboa](https://twitter.com/MariaBe40049617) | 29/01/2020 | 0.302 (48/159) | 3616 |
| ![alt text](http://pbs.twimg.com/profile_images/859852029384151040/C-4bcJ8o_normal.jpg "foto do usuário") [Marcelo Reina](https://twitter.com/ThiReina) | 03/05/2017 | 0.255 (76/298) | 4970 |
| ![alt text](http://pbs.twimg.com/profile_images/1051775514229264385/i4hwCHqW_normal.jpg "foto do usuário") [Elielton Silva](https://twitter.com/Elielton_coach) | 15/10/2018 | 0.801 (113/141) | 1470 |
| ![alt text](http://pbs.twimg.com/profile_images/1288430508507123714/u5J5QesH_normal.jpg "foto do usuário") [Lucano](https://twitter.com/leonthomasburke) | 12/08/2008 | 0.867 (852/983) | 14508 |
| ![alt text](http://pbs.twimg.com/profile_images/1203890794890960897/RbYCpXn__normal.jpg "foto do usuário") [Ana Paula Inácio](https://twitter.com/anapinacio) | 10/08/2010 | 0.673 (296/440) | 2093 |
| ![alt text](http://pbs.twimg.com/profile_images/1251471345076051968/_eoJJoZb_normal.jpg "foto do usuário") [Eu, Robot.](https://twitter.com/SidNunes1) | 14/03/2020 | 0.215 (32/149) | 6002 |
| ![alt text](http://pbs.twimg.com/profile_images/1303018359911522304/cMvCYpgS_normal.jpg "foto do usuário") [João Aristóteles 🤡 🇧🇷🇺🇸🇬🇧🇦🇺🇮🇹](https://twitter.com/AristotelesVia) | 01/11/2018 | 0.433 (912/2106) | 80372 |
| ![alt text](http://pbs.twimg.com/profile_images/1352234516644061186/4cekvDe0_normal.jpg "foto do usuário") [#AbortoNão - 🇻🇦🇧🇷🇺🇸🦅](https://twitter.com/vhscoffee) | 16/11/2013 | 2.537 (2309/910) | 71413 |
| ![alt text](http://pbs.twimg.com/profile_images/1191732378156355587/dL_3LBx7_normal.jpg "foto do usuário") [🇧🇷🇧🇷Vilmarbueno🇧🇷🇧🇷](https://twitter.com/VilmarBueno3) | 05/11/2019 | 0.582 (224/385) | 4846 |
| ![alt text](http://pbs.twimg.com/profile_images/1348253406557851650/9JJ3jVjU_normal.jpg "foto do usuário") [🇧🇷🇧🇷🇧🇷SILIANY🇧🇷🇧🇷🇧🇷 O POVO NO PODER](https://twitter.com/g_siliany) | 09/11/2016 | 0.495 (615/1242) | 23574 |
| ![alt text](http://pbs.twimg.com/profile_images/1351954800838123520/5RMTL1Q8_normal.jpg "foto do usuário") [りﾉムﾉｲﾑﾚ　ﾶﾉﾚﾉｲﾉﾑ 🇧🇷 38 😎 👉 👉](https://twitter.com/honklerBRA) | 05/01/2016 | 0.281 (78/278) | 3227 |
| ![alt text](http://pbs.twimg.com/profile_images/1278934300289904641/RPBwWijr_normal.jpg "foto do usuário") [Mormat 🇧🇷](https://twitter.com/MMormat) | 20/08/2013 | 0.401 (116/289) | 977 |
| ![alt text](http://pbs.twimg.com/profile_images/1240825939065483266/CmLyA3pO_normal.jpg "foto do usuário") [Punho_de_prata](https://twitter.com/Silver_punch_FW) | 16/09/2019 | 0.098 (13/133) | 2542 |
| ![alt text](http://pbs.twimg.com/profile_images/824024016121958406/kIjY1rej_normal.jpg "foto do usuário") [Beto](https://twitter.com/betooficiall) | 23/11/2011 | 0.102 (35/342) | 556 |
| ![alt text](http://pbs.twimg.com/profile_images/1201644964314275841/VqAnCzjt_normal.jpg "foto do usuário") [...EU SOU O QUE SOU. 🇧🇷🕎🇨🇱](https://twitter.com/toyniahi) | 18/07/2012 | 0.349 (321/921) | 6786 |
| ![alt text](http://pbs.twimg.com/profile_images/1348454191732322309/ITtYAKO5_normal.jpg "foto do usuário") [Paulo Serafim 🇧🇷🤝🇺🇸🤝🇮🇱🙏🇪🇺🦚](https://twitter.com/PauloSerafimBR) | 22/06/2019 | 0.796 (1581/1986) | 15118 |
| ![alt text](http://pbs.twimg.com/profile_images/1348591141973843968/FIYWGpTT_normal.jpg "foto do usuário") [Duchar](https://twitter.com/Diessil) | 11/06/2013 | 0.096 (300/3131) | 2083 |
| ![alt text](http://pbs.twimg.com/profile_images/1355575989317881863/knU9cSh0_normal.jpg "foto do usuário") [Maria P](https://twitter.com/damadanoite14) | 22/10/2014 | 0.921 (6420/6974) | 25608 |
| ![alt text](http://pbs.twimg.com/profile_images/986776133621477376/PplCatzw_normal.jpg "foto do usuário") [Rômulo Viel](https://twitter.com/rmviel) | 24/02/2009 | 0.55 (255/464) | 34453 |
| ![alt text](http://pbs.twimg.com/profile_images/1281090958814318592/jfhXhOyJ_normal.jpg "foto do usuário") [🇧🇷🇧🇷gilbertto ton🇧🇷🇧🇷](https://twitter.com/MitoPaviuCurto) | 24/09/2018 | 0.805 (2186/2715) | 24142 |
| ![alt text](http://pbs.twimg.com/profile_images/1347910558759211008/E33mcBd9_normal.jpg "foto do usuário") [Wiliam Osmar](https://twitter.com/WiliamOsmar) | 19/05/2019 | 0.715 (2316/3239) | 51399 |
| ![alt text](http://pbs.twimg.com/profile_images/1337546730796146701/YjX4AnJ0_normal.jpg "foto do usuário") [eduardo lima](https://twitter.com/DuddududuLima) | 19/09/2014 | 0.057 (61/1064) | 6660 |
| ![alt text](http://pbs.twimg.com/profile_images/1350641088030269442/56fReufS_normal.jpg "foto do usuário") [ALCÁÇOVA DO BONORO🎯🏰💯%BOLSONARO🇧🇷🇺🇸🇮🇱](https://twitter.com/GondimTiberio) | 17/08/2014 | 0.978 (1932/1975) | 1489 |
| ![alt text](http://pbs.twimg.com/profile_images/1318010350067945472/0PwKHdUN_normal.jpg "foto do usuário") [Hugo Santos](https://twitter.com/hugorsantos) | 05/08/2009 | 0.296 (131/442) | 4297 |
| ![alt text](http://pbs.twimg.com/profile_images/1174431574860992512/G1wpJiCz_normal.jpg "foto do usuário") [jackson](https://twitter.com/jacksonnfilho) | 23/12/2017 | 0.529 (199/376) | 5879 |
| ![alt text](http://pbs.twimg.com/profile_images/1294635627703611393/-NLtWGy9_normal.jpg "foto do usuário") [Luna](https://twitter.com/Luna10G) | 12/05/2011 | 0.164 (26/159) | 10261 |
| ![alt text](http://pbs.twimg.com/profile_images/1351573933842178054/p1NHtK_n_normal.jpg "foto do usuário") [Rafael Cavalcanti](https://twitter.com/liberatorafinh) | 24/08/2010 | 0.179 (100/559) | 10481 |
| ![alt text](http://pbs.twimg.com/profile_images/1244431773859287043/85oFi4Mv_normal.jpg "foto do usuário") [Luiz Leston](https://twitter.com/luiz_leston) | 22/06/2009 | 0.462 (12/26) | 5836 |
| ![alt text](http://pbs.twimg.com/profile_images/1339676596685434889/0t4UODaW_normal.jpg "foto do usuário") [Paulo Alexandre Babum](https://twitter.com/BabumRj) | 20/09/2013 | 0.412 (77/187) | 1183 |
| ![alt text](http://pbs.twimg.com/profile_images/1351571431008722944/lVQV303o_normal.jpg "foto do usuário") [Estácio de Sá. BOLSONARO. 38](https://twitter.com/Ricozagueiro) | 27/12/2010 | 0.447 (149/333) | 918 |
| ![alt text](http://pbs.twimg.com/profile_images/1326697405933346821/Wjgeb_3Y_normal.jpg "foto do usuário") [Ray 🇧🇷😎](https://twitter.com/RayRRRRay) | 02/02/2012 | 0.515 (848/1647) | 9083 |
| ![alt text](http://pbs.twimg.com/profile_images/1332062884290064387/hH-zh4n5_normal.jpg "foto do usuário") [Felipe G](https://twitter.com/GiannellaFelipe) | 28/01/2016 | 0.486 (220/453) | 9639 |
| ![alt text](http://pbs.twimg.com/profile_images/1220162091736272897/0camIyV8_normal.jpg "foto do usuário") [Artur Cassiano](https://twitter.com/CassianoArtur) | 23/01/2020 | 0.159 (10/63) | 286 |
| ![alt text](http://pbs.twimg.com/profile_images/1251100176019853312/aQTO_wwa_normal.jpg "foto do usuário") [Angie Saint](https://twitter.com/AngieSaint4) | 24/03/2020 | 0.07 (3/43) | 268 |
| ![alt text](http://pbs.twimg.com/profile_images/1342023418997334018/626SEp7i_normal.jpg "foto do usuário") [Asther](https://twitter.com/_Lytch) | 31/10/2019 | 0.029 (7/240) | 72 |
| ![alt text](http://pbs.twimg.com/profile_images/1216736157985333248/WS1wC7T8_normal.jpg "foto do usuário") [Kadmiel Cândido Chagas](https://twitter.com/KadmielCandido) | 29/10/2019 | 0.017 (2/116) | 61 |
| ![alt text](http://pbs.twimg.com/profile_images/1350284955906138113/ifu9FidJ_normal.jpg "foto do usuário") [Neves](https://twitter.com/depaulaneves) | 01/02/2013 | 0.431 (552/1282) | 2413 |
| ![alt text](http://pbs.twimg.com/profile_images/1251631615886929926/AnJOZgSe_normal.jpg "foto do usuário") [Rodrigo Bari](https://twitter.com/RodrigoBari3) | 18/04/2020 | 0.01 (0/0) | 20 |
| ![alt text](http://pbs.twimg.com/profile_images/1354796352895660034/GNzeSk-W_normal.jpg "foto do usuário") [Joana](https://twitter.com/Joana41858862) | 06/02/2020 | 0.4 (24/60) | 15151 |
| ![alt text](http://pbs.twimg.com/profile_images/1120693911964585987/En7uHOF9_normal.jpg "foto do usuário") [Renar Esppenchutz 🇧🇷🇧🇷🇧🇷](https://twitter.com/renaravante) | 02/08/2013 | 0.257 (127/495) | 2542 |
| ![alt text](http://pbs.twimg.com/profile_images/1251609272586326016/WK7sG6Rb_normal.jpg "foto do usuário") [Saymon Gomes](https://twitter.com/eydsaymon) | 27/10/2010 | 0.445 (441/990) | 14486 |
| ![alt text](http://pbs.twimg.com/profile_images/1280702479508832260/pnGY43Ih_normal.jpg "foto do usuário") [jnery](https://twitter.com/joelnferreira1) | 20/01/2015 | 0.224 (173/771) | 15588 |
| ![alt text](http://pbs.twimg.com/profile_images/1333247912508317696/GGIgEpAg_normal.jpg "foto do usuário") [Paulo Batista](https://twitter.com/itsphbatista) | 16/01/2020 | 0.277 (41/148) | 1548 |
| ![alt text](http://pbs.twimg.com/profile_images/1258558105291493376/sC8lHZFv_normal.jpg "foto do usuário") [Peterson Smith](https://twitter.com/P3t3rsonSmith) | 10/04/2020 | 0.587 (91/155) | 2854 |
| ![alt text](http://pbs.twimg.com/profile_images/1084290432832598017/a6Pn5h3__normal.jpg "foto do usuário") [Cebola](https://twitter.com/Cebola33255649) | 13/01/2019 | 0.343 (322/938) | 11676 |
| ![alt text](http://pbs.twimg.com/profile_images/1260943765616943104/jDWZfyXT_normal.jpg "foto do usuário") [Emerson](https://twitter.com/Rafael93118781) | 25/02/2020 | 0.039 (14/359) | 952 |
| ![alt text](http://pbs.twimg.com/profile_images/1253401744727584769/drLMyuvf_normal.jpg "foto do usuário") [VG8712](https://twitter.com/VGA1987) | 16/03/2020 | 0.021 (20/975) | 1417 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [A FAVOR DE JESUS](https://twitter.com/FavorJesus) | 04/04/2020 | 0.0 (0/54) | 1528 |
| ![alt text](http://pbs.twimg.com/profile_images/1346407445640441856/jhiLfsOj_normal.jpg "foto do usuário") [Ícaro Henrique](https://twitter.com/iczro) | 12/02/2018 | 3.884 (1946/501) | 30106 |
| ![alt text](http://pbs.twimg.com/profile_images/1340085891075862535/aOcBQ62s_normal.jpg "foto do usuário") [Suf 🇧🇦](https://twitter.com/iPimba21) | 13/05/2015 | 2.134 (937/439) | 26491 |
| ![alt text](http://pbs.twimg.com/profile_images/1344984992145879040/vzS7fqWJ_normal.jpg "foto do usuário") [Marcelo Xavier](https://twitter.com/marcelohxavier) | 02/11/2009 | 0.341 (329/965) | 22610 |
| ![alt text](http://pbs.twimg.com/profile_images/1284213056118099968/xt4wSE-b_normal.jpg "foto do usuário") [Regina Reis](https://twitter.com/ReginaReiis) | 24/02/2018 | 0.962 (2308/2398) | 20282 |
| ![alt text](http://pbs.twimg.com/profile_images/1347885790735556612/ATYCaepo_normal.jpg "foto do usuário") [Romano](https://twitter.com/Maurici40563688) | 07/09/2018 | 0.425 (256/603) | 11966 |
| ![alt text](http://pbs.twimg.com/profile_images/1349686729003905024/IN_jUPer_normal.jpg "foto do usuário") [Charles Silva](https://twitter.com/charlinhojan) | 16/02/2011 | 0.125 (32/255) | 7085 |
| ![alt text](http://pbs.twimg.com/profile_images/1336209574400040961/MzBJ96W9_normal.jpg "foto do usuário") [João Carlos Figueira](https://twitter.com/jccf00) | 15/03/2011 | 0.548 (338/617) | 18464 |
| ![alt text](http://pbs.twimg.com/profile_images/685181909098446849/1fVWaW2__normal.jpg "foto do usuário") [miriam](https://twitter.com/misalomao) | 20/08/2009 | 0.168 (62/368) | 2477 |
| ![alt text](http://pbs.twimg.com/profile_images/1157485049551495168/3Qu_bMWr_normal.jpg "foto do usuário") [Medo do Seo Peru - (completo, menos ar)](https://twitter.com/mano_quem) | 10/11/2018 | 0.732 (172/235) | 4948 |
| ![alt text](http://pbs.twimg.com/profile_images/1139755119870918656/2dyLx1uE_normal.jpg "foto do usuário") [Adailton Batista](https://twitter.com/Adailto92872795) | 15/06/2019 | 0.221 (70/317) | 2602 |
| ![alt text](http://pbs.twimg.com/profile_images/1321783456381153281/iTdGosUz_normal.jpg "foto do usuário") [Cearense Com Bolsonaro🇧🇷🇮🇱🇺🇸🇧🇷](https://twitter.com/cearacombonoro) | 18/03/2020 | 0.837 (1150/1374) | 5243 |
| ![alt text](http://pbs.twimg.com/profile_images/750120521744969729/dtSg39AB_normal.jpg "foto do usuário") [Akan Filip](https://twitter.com/akanfilip23) | 05/12/2012 | 1.132 (43/38) | 1728 |
| ![alt text](http://pbs.twimg.com/profile_images/1249342921310187520/RUp0O2m6_normal.jpg "foto do usuário") [Rômulo Almeida 🇭🇺🇧🇷](https://twitter.com/RomuloAlmeida17) | 24/06/2009 | 0.634 (347/547) | 6208 |
| ![alt text](http://pbs.twimg.com/profile_images/565963504507580416/k4xohx5N_normal.jpeg "foto do usuário") [SPECTRE1961](https://twitter.com/SPECTRE1961) | 03/12/2008 | 0.237 (730/3076) | 9789 |
| ![alt text](http://pbs.twimg.com/profile_images/1354391530400854018/6w6YsdGj_normal.jpg "foto do usuário") [#QueroBolsonaroAte2026💍🇧🇷 3️⃣8️⃣ 🤡](https://twitter.com/Ricardo44788581) | 18/09/2019 | 0.841 (1708/2032) | 46526 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [marcos alonge](https://twitter.com/AlongeMarcos) | 21/03/2018 | 0.255 (60/235) | 225 |
| ![alt text](http://pbs.twimg.com/profile_images/1348324832719548421/xheNyJL2_normal.jpg "foto do usuário") [Técio Melo](https://twitter.com/Tecio_Melo) | 05/04/2020 | 11.786 (10737/911) | 19481 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Fisiconabolsa](https://twitter.com/fisiconabolsa) | 10/12/2018 | 0.411 (78/190) | 2836 |
| ![alt text](http://pbs.twimg.com/profile_images/1205974318477434886/wTAPGJrd_normal.jpg "foto do usuário") [Juliano Cé Coelho](https://twitter.com/JulianoOnco) | 17/09/2016 | 0.24 (95/396) | 514 |
| ![alt text](http://pbs.twimg.com/profile_images/1325496343243198469/l40r-3PO_normal.jpg "foto do usuário") [JJ Bombarda](https://twitter.com/JJBOMBARDA) | 06/01/2020 | 0.585 (230/393) | 3558 |
| ![alt text](http://pbs.twimg.com/profile_images/1353095660652924928/-BfnBrMX_normal.jpg "foto do usuário") [Regina Jacob 🇧🇷](https://twitter.com/JacobRegina1968) | 07/03/2012 | 0.54 (412/763) | 24315 |
| ![alt text](http://pbs.twimg.com/profile_images/1345289475526692869/PXcj8UBY_normal.jpg "foto do usuário") [Celia alianca](https://twitter.com/MeloCelia) | 23/07/2011 | 0.475 (96/202) | 2216 |
| ![alt text](http://pbs.twimg.com/profile_images/1264232461543845892/JP7xS4KG_normal.jpg "foto do usuário") [Paulo 🇧🇷🇧🇷🇧🇷💪💪💪](https://twitter.com/cura_paulo) | 20/10/2018 | 0.626 (1803/2880) | 27581 |
| ![alt text](http://pbs.twimg.com/profile_images/2283453935/image_normal.jpg "foto do usuário") [Elias Nosow](https://twitter.com/Enosow) | 19/09/2009 | 0.65 (715/1100) | 22033 |
| ![alt text](http://pbs.twimg.com/profile_images/1268149435428507648/oPANuBJF_normal.jpg "foto do usuário") [Josué Patriota 🇧🇷](https://twitter.com/JosuePatriota) | 07/02/2019 | 490.039 (50474/103) | 2385 |
| ![alt text](http://pbs.twimg.com/profile_images/1347955741840318468/_x2dfedT_normal.jpg "foto do usuário") [Irado, furioso com tudo!](https://twitter.com/Julioseibei) | 21/10/2017 | 0.747 (1857/2487) | 72469 |
| ![alt text](http://pbs.twimg.com/profile_images/1354818833312190468/ECgP2IPX_normal.jpg "foto do usuário") [Helem](https://twitter.com/HelemAzevedo) | 26/04/2009 | 28.16 (20078/713) | 69210 |
| ![alt text](http://pbs.twimg.com/profile_images/1277572778988900353/doLj3WNS_normal.jpg "foto do usuário") [Tudo vai bem](https://twitter.com/Adenilc38079596) | 26/03/2020 | 0.315 (78/248) | 5430 |
| ![alt text](http://pbs.twimg.com/profile_images/1276114969365528576/HjpD_wS7_normal.jpg "foto do usuário") [🅰🅽🅳🆁🅴 🅱🆁🅰🆂🅸🅻](https://twitter.com/andrepelobrasil) | 20/01/2020 | 0.362 (200/552) | 8728 |
| ![alt text](http://pbs.twimg.com/profile_images/1251696500465373184/ZOqSpiW8_normal.jpg "foto do usuário") [fernando tavares](https://twitter.com/corinthians_fe) | 11/10/2018 | 0.292 (362/1238) | 2076 |
| ![alt text](http://pbs.twimg.com/profile_images/896693354045616128/Xcqeqhg3_normal.jpg "foto do usuário") [Francisco Pereira](https://twitter.com/UeldimarPereira) | 13/08/2017 | 0.172 (17/99) | 861 |
| ![alt text](http://pbs.twimg.com/profile_images/1347728002860384257/FUpwdJ4a_normal.jpg "foto do usuário") [Chibi Lover #Bolsonaro2022 🇧🇷 #FreeSpeech](https://twitter.com/Sunset28) | 29/05/2009 | 0.711 (1354/1905) | 17664 |
| ![alt text](http://pbs.twimg.com/profile_images/1351330616843898887/dn_CZ8LK_normal.jpg "foto do usuário") [Nany Dias](https://twitter.com/NayaneGonalves2) | 23/10/2012 | 1.227 (653/532) | 2252 |
| ![alt text](http://pbs.twimg.com/profile_images/1349168661626499073/XwO-mDuA_normal.jpg "foto do usuário") [Re](https://twitter.com/Renata33225236) | 04/04/2019 | 0.823 (2201/2673) | 15365 |
| ![alt text](http://pbs.twimg.com/profile_images/2197720016/twitrocar2_normal.jpg "foto do usuário") [Luiz Alberto](https://twitter.com/caterre) | 20/10/2008 | 0.534 (589/1102) | 13731 |
| ![alt text](http://pbs.twimg.com/profile_images/1199329059051847683/1U1CLHV1_normal.jpg "foto do usuário") [Hélio camolezi junio](https://twitter.com/PRHELIOCAMOLEZI) | 30/08/2010 | 0.544 (777/1427) | 25799 |
| ![alt text](http://pbs.twimg.com/profile_images/1225720620429848581/_wAb0hKf_normal.jpg "foto do usuário") [Adeilson Sousa🎸🎶](https://twitter.com/Itamar21asSousa) | 01/10/2014 | 0.119 (43/360) | 1844 |
| ![alt text](http://pbs.twimg.com/profile_images/880231714576052224/9oGgQytr_normal.jpg "foto do usuário") [Piquet🇧🇷](https://twitter.com/Piquetslz) | 02/07/2009 | 1.812 (696/384) | 4339 |
| ![alt text](http://pbs.twimg.com/profile_images/1245704414654017540/DSSUo9ma_normal.jpg "foto do usuário") [HeitorFederal](https://twitter.com/FederalHeitor) | 20/11/2019 | 0.612 (82/134) | 4632 |
| ![alt text](http://pbs.twimg.com/profile_images/1240050291321507841/pyP4JNP5_normal.jpg "foto do usuário") [Arnaldo Pitombo](https://twitter.com/ArnaldoPitombo) | 17/03/2020 | 0.033 (4/123) | 3852 |
| ![alt text](http://pbs.twimg.com/profile_images/1231342856188694529/OmQ1AODv_normal.jpg "foto do usuário") [Everton 🇧🇷 Brasil](https://twitter.com/Everton49827848) | 07/07/2018 | 0.104 (12/115) | 1279 |
| ![alt text](http://pbs.twimg.com/profile_images/1161244997733298179/57lX4OmI_normal.jpg "foto do usuário") [Esdras Santos](https://twitter.com/esdrasvendasmsf) | 06/07/2015 | 0.094 (50/531) | 1308 |
| ![alt text](http://pbs.twimg.com/profile_images/981335733607727104/2Ed7BlU-_normal.jpg "foto do usuário") [iran mello](https://twitter.com/iran_mello) | 21/11/2010 | 0.153 (186/1212) | 2689 |
| ![alt text](http://pbs.twimg.com/profile_images/1342266507238268930/sfkFdfI__normal.jpg "foto do usuário") [Enzo original](https://twitter.com/malak00i) | 26/12/2016 | 0.073 (89/1227) | 6331 |
| ![alt text](http://pbs.twimg.com/profile_images/817401202140999687/Z2iROpay_normal.jpg "foto do usuário") [@jp_bart](https://twitter.com/jp_bart1) | 04/04/2014 | 0.054 (54/995) | 280 |
| ![alt text](http://pbs.twimg.com/profile_images/1268731408253665290/hkxiHn7Z_normal.jpg "foto do usuário") [Sandman](https://twitter.com/54ndm4n5) | 04/07/2014 | 0.738 (245/332) | 12614 |
| ![alt text](http://pbs.twimg.com/profile_images/1313859586940694531/d1a5eLJs_normal.jpg "foto do usuário") [Revista Metró](https://twitter.com/paginasdametro) | 02/12/2016 | 54.446 (9637/177) | 19424 |
| ![alt text](http://pbs.twimg.com/profile_images/1004436052239618049/LIpnVk5Y_normal.jpg "foto do usuário") [Rstallone7](https://twitter.com/rstallone7) | 06/06/2018 | 0.136 (9/66) | 92 |
| ![alt text](http://pbs.twimg.com/profile_images/1352791686775250945/N4GEa0FY_normal.jpg "foto do usuário") [likinha](https://twitter.com/kalikinha) | 14/02/2011 | 1.132 (667/589) | 24697 |
| ![alt text](http://pbs.twimg.com/profile_images/1347573801568137219/au82QhD0_normal.jpg "foto do usuário") [Metrópole Litoral](https://twitter.com/Metro_Litoral) | 07/01/2018 | 68.589 (11180/163) | 15969 |
| ![alt text](http://pbs.twimg.com/profile_images/1347728386689527809/VwYBm_om_normal.jpg "foto do usuário") [Leoj Ojuara](https://twitter.com/Leoj_Ojuara) | 27/06/2015 | 0.349 (130/373) | 9734 |
| ![alt text](http://pbs.twimg.com/profile_images/1274859563179794432/FEdUaF3y_normal.jpg "foto do usuário") [Marcelo C](https://twitter.com/Mcalcagno2012) | 20/12/2016 | 0.328 (182/555) | 9694 |
| ![alt text](http://pbs.twimg.com/profile_images/920405527548649473/HHb7LYC2_normal.jpg "foto do usuário") [wallison morais](https://twitter.com/wallisonmorais1) | 23/10/2013 | 0.095 (60/631) | 7528 |
| ![alt text](http://pbs.twimg.com/profile_images/1351691440016019456/yLekuwnA_normal.jpg "foto do usuário") [Rafael](https://twitter.com/Fael_rodriguezz) | 03/07/2018 | 1.342 (487/363) | 6082 |
| ![alt text](http://pbs.twimg.com/profile_images/1301959388568203265/fODqmtbQ_normal.jpg "foto do usuário") [G B ⚽😍](https://twitter.com/7Gbrll_7) | 20/04/2019 | 0.149 (637/4266) | 38446 |
| ![alt text](http://pbs.twimg.com/profile_images/1348408759052365826/11uST7Pm_normal.jpg "foto do usuário") [Daniel Lancellott](https://twitter.com/Lancellott2) | 19/01/2018 | 0.231 (724/3129) | 14777 |
| ![alt text](http://pbs.twimg.com/profile_images/1353735120084234249/PbHbiKVX_normal.jpg "foto do usuário") [Ф £ Д T Í](https://twitter.com/DomOrleans) | 17/06/2010 | 2.892 (3737/1292) | 104445 |
| ![alt text](http://pbs.twimg.com/profile_images/1347771962693718017/M2Y30BGR_normal.jpg "foto do usuário") [Diana 🇧🇷👏🦀🦀](https://twitter.com/DianaBrasilBR) | 13/08/2009 | 0.735 (1377/1874) | 17265 |
| ![alt text](http://pbs.twimg.com/profile_images/645288703594766336/DhLpfqts_normal.jpg "foto do usuário") [Júlio Oliveira](https://twitter.com/juliooolliveira) | 12/03/2011 | 1.515 (197/130) | 1755 |
| ![alt text](http://pbs.twimg.com/profile_images/1348906504708108288/3BZispA-_normal.jpg "foto do usuário") [🇧🇷 Alexandre Soares 🇧🇷](https://twitter.com/ale_bsoares) | 16/06/2016 | 0.787 (3846/4887) | 5615 |
| ![alt text](http://pbs.twimg.com/profile_images/1270687374398443520/zOR9Esu3_normal.jpg "foto do usuário") [Anderson⚫️⚪️⭐️ 🇮🇪](https://twitter.com/andersonncalice) | 08/04/2010 | 0.729 (624/856) | 19795 |
| ![alt text](http://pbs.twimg.com/profile_images/1347737742344663040/oPG5l7Fb_normal.jpg "foto do usuário") [Hank](https://twitter.com/HenryRearden15) | 01/04/2020 | 0.308 (272/884) | 10947 |
| ![alt text](http://pbs.twimg.com/profile_images/982604924134612992/JES6PhRn_normal.jpg "foto do usuário") [Carlinhos🇧🇷](https://twitter.com/C4rl1nh0562) | 14/07/2016 | 0.814 (219/269) | 8658 |
| ![alt text](http://pbs.twimg.com/profile_images/1294028595611029504/z_-DaA5g_normal.jpg "foto do usuário") [Me Tire Daqui](https://twitter.com/MeTireDaqui) | 06/11/2010 | 0.589 (654/1110) | 753 |
| ![alt text](http://pbs.twimg.com/profile_images/1165750358813085701/0QD51HCQ_normal.jpg "foto do usuário") [O Corvo](https://twitter.com/0C0RV0) | 14/03/2019 | 5.782 (99093/17138) | 8640 |
| ![alt text](http://pbs.twimg.com/profile_images/1220698947355803655/L4nMb6dI_normal.jpg "foto do usuário") [Thaynnara Moreira](https://twitter.com/ThaynnaraMorei2) | 11/01/2016 | 0.371 (36/97) | 358 |
| ![alt text](http://pbs.twimg.com/profile_images/1158123664358989824/qqHlsj3I_normal.jpg "foto do usuário") [Figueredo](https://twitter.com/AdrianoFiguer16) | 25/09/2018 | 0.778 (605/778) | 6881 |
| ![alt text](http://pbs.twimg.com/profile_images/1274334232349941760/AYsw0n5D_normal.jpg "foto do usuário") [Claudio Sales 🇧🇷🇮🇱🇺🇸🔰🔰🔰](https://twitter.com/claudiosalesfer) | 27/05/2012 | 0.725 (1476/2035) | 3315 |
| ![alt text](http://pbs.twimg.com/profile_images/1227795837373353984/86RazBUv_normal.jpg "foto do usuário") [🇧🇷Marcos Pontes🇧🇷38🇧🇷](https://twitter.com/_MarcosPontes) | 05/08/2019 | 0.953 (1625/1705) | 18349 |
| ![alt text](http://pbs.twimg.com/profile_images/1210664455715119107/BhZMsz4Q_normal.jpg "foto do usuário") [José Alcides](https://twitter.com/josealcides) | 02/05/2009 | 0.579 (2163/3735) | 17373 |
| ![alt text](http://pbs.twimg.com/profile_images/1234228227134181378/GeyIvMoN_normal.jpg "foto do usuário") [SampaGalo](https://twitter.com/GalodoidoR49) | 13/12/2017 | 0.172 (129/749) | 3945 |
| ![alt text](http://pbs.twimg.com/profile_images/1347731864010764290/T-frGyvP_normal.jpg "foto do usuário") [Sexy Lula Molusco](https://twitter.com/adolfdohrea) | 12/03/2020 | 0.908 (167/184) | 8533 |
| ![alt text](http://pbs.twimg.com/profile_images/1246942457083899904/EO2kgNBY_normal.jpg "foto do usuário") [Miguel Brasil Honesto 🇧🇷](https://twitter.com/miguel_cwb) | 15/03/2011 | 0.169 (13/77) | 691 |
| ![alt text](http://pbs.twimg.com/profile_images/1297962137076326403/xOOxaatQ_normal.jpg "foto do usuário") [Arthur Weintraub](https://twitter.com/ArthurWeint) | 16/12/2018 | 2709.113 (577041/213) | 6506 |
| ![alt text](http://pbs.twimg.com/profile_images/1227193236260872192/wtwUi3pL_normal.jpg "foto do usuário") [André Menezes](https://twitter.com/AndrMen16821795) | 16/04/2018 | 0.015 (5/331) | 4088 |
| ![alt text](http://pbs.twimg.com/profile_images/1192820058151628801/VA-BAmsl_normal.jpg "foto do usuário") [Vinicius Lazari](https://twitter.com/ViniciusLazari8) | 08/11/2019 | 0.74 (3421/4624) | 4326 |
| ![alt text](http://pbs.twimg.com/profile_images/1347864195249930245/fCVfWLQN_normal.jpg "foto do usuário") [Jaque Luz](https://twitter.com/Jaqueluz82) | 10/06/2019 | 1.014 (1469/1449) | 6121 |
| ![alt text](http://pbs.twimg.com/profile_images/1192474742885928961/pHF4TlSH_normal.jpg "foto do usuário") [Alex Reis](https://twitter.com/AlexRei35785975) | 07/11/2019 | 0.013 (2/154) | 139 |
| ![alt text](http://pbs.twimg.com/profile_images/1324355883485302790/GZN-Kwp6_normal.jpg "foto do usuário") [Antonio Carlos Cardoso](https://twitter.com/Antonio46684810) | 21/03/2019 | 1.463 (18202/12440) | 22132 |
| ![alt text](http://pbs.twimg.com/profile_images/1238651819930288130/zzZL871W_normal.jpg "foto do usuário") [CyborgNacional01](https://twitter.com/CNacional01) | 04/12/2019 | 0.609 (814/1337) | 10182 |
| ![alt text](http://pbs.twimg.com/profile_images/1132445814880722944/5agg0fnj_normal.jpg "foto do usuário") [Gabriel Pinto](https://twitter.com/gabpintoo) | 21/09/2016 | 0.081 (233/2874) | 14185 |
| ![alt text](http://pbs.twimg.com/profile_images/1029833089801961477/Qiei4bXz_normal.jpg "foto do usuário") [Emilson Nunes Costa](https://twitter.com/EmilsonNunesCo2) | 15/08/2018 | 0.292 (850/2910) | 29847 |
| ![alt text](http://pbs.twimg.com/profile_images/1274141178297024512/9s90sjzG_normal.jpg "foto do usuário") [Assis PF 🇧🇷](https://twitter.com/Assis_PF) | 02/10/2017 | 0.414 (275/664) | 848 |
| ![alt text](http://pbs.twimg.com/profile_images/1354234504299339778/OXF8U83y_normal.jpg "foto do usuário") [𝓐𝓷𝓰𝓮𝓵 ♥️🇧🇷](https://twitter.com/fide_honorisPF) | 14/09/2018 | 2.789 (45598/16352) | 116500 |
| ![alt text](http://pbs.twimg.com/profile_images/1267770513713233921/6gn3DEZc_normal.jpg "foto do usuário") [⚔️ 👽Resistência Psicodélica 👽⚔️](https://twitter.com/TiagoGo45627664) | 23/07/2019 | 0.38 (261/686) | 1063 |
| ![alt text](http://pbs.twimg.com/profile_images/1349844242705895427/d3v0TBRY_normal.jpg "foto do usuário") [Agápê Brasil](https://twitter.com/agapefpim) | 07/12/2009 | 0.975 (19395/19886) | 13531 |
| ![alt text](http://pbs.twimg.com/profile_images/1300374510798082048/sJF_PQfT_normal.jpg "foto do usuário") [🇧🇷PERN@MBUC@NO🇧🇷](https://twitter.com/GomesDinaldo) | 29/11/2018 | 0.709 (3504/4944) | 13492 |
| ![alt text](http://pbs.twimg.com/profile_images/1326673595070869505/q8lw1SGQ_normal.jpg "foto do usuário") [Leonardo Lopes](https://twitter.com/leonardo1opes) | 28/06/2010 | 17.979 (8702/484) | 16332 |
| ![alt text](http://pbs.twimg.com/profile_images/1248375223230988289/6_wpp8YM_normal.jpg "foto do usuário") [Sergio Viana](https://twitter.com/SergioV18636901) | 02/03/2020 | 0.576 (238/413) | 1219 |
| ![alt text](http://pbs.twimg.com/profile_images/1215676932542672897/K0EqcDgr_normal.jpg "foto do usuário") [michel c](https://twitter.com/mc1154) | 27/11/2009 | 0.042 (40/951) | 8574 |
| ![alt text](http://pbs.twimg.com/profile_images/1297689239078002689/n3Dstl_0_normal.jpg "foto do usuário") [Junior](https://twitter.com/JuniorCorreia) | 22/03/2009 | 0.064 (178/2801) | 4805 |
| ![alt text](http://pbs.twimg.com/profile_images/1331791714336567296/G9-qgiAI_normal.jpg "foto do usuário") [#CriminalizaComunismoBrasil 在巴西將共產主義定為刑事犯罪](https://twitter.com/JhonyRostras) | 16/01/2018 | 0.477 (1585/3320) | 29377 |
| ![alt text](http://pbs.twimg.com/profile_images/1297426794749014017/DLnYz-m1_normal.jpg "foto do usuário") [🇧🇷🇷🇸🇭🇷Dragan Dragutinovic](https://twitter.com/dragandragu) | 29/02/2020 | 0.365 (100/274) | 1467 |
| ![alt text](http://pbs.twimg.com/profile_images/1193613144293330946/te7SbqWA_normal.jpg "foto do usuário") [Escabroso](https://twitter.com/Escabroso_1) | 11/10/2019 | 0.198 (17/86) | 1244 |
| ![alt text](http://pbs.twimg.com/profile_images/1278735060141776897/9OkPXt6x_normal.jpg "foto do usuário") [🇧🇷 DRI 🇧🇷](https://twitter.com/ADRIANE35) | 03/12/2009 | 0.975 (5904/6057) | 37057 |
| ![alt text](http://pbs.twimg.com/profile_images/1263918266906542083/remcVh7-_normal.jpg "foto do usuário") [Lourdes Maria](https://twitter.com/Lourdes40431925) | 22/07/2019 | 0.757 (452/597) | 2945 |
| ![alt text](http://pbs.twimg.com/profile_images/1083676648761946113/hpfKEtFC_normal.jpg "foto do usuário") [Márcio Ribeiro](https://twitter.com/maalelimas) | 25/12/2018 | 0.539 (265/492) | 10855 |
| ![alt text](http://pbs.twimg.com/profile_images/1273651038558588933/oX7hHbSb_normal.jpg "foto do usuário") [Mauro Fagundes](https://twitter.com/maurofagundess) | 23/05/2019 | 93.608 (43247/462) | 6288 |
| ![alt text](http://pbs.twimg.com/profile_images/1353158610247966721/U5eBO273_normal.jpg "foto do usuário") [Le reaça, da Direita🇧🇷](https://twitter.com/goulart_lenita) | 23/07/2017 | 3.019 (40096/13280) | 50165 |
| ![alt text](http://pbs.twimg.com/profile_images/1354335329034133504/oMqLUvYp_normal.jpg "foto do usuário") [𝕽𝖔𝖉𝖊𝖗𝖎𝖈𝖐 𝕮𝖆𝖛𝖆𝖑𝖈𝖆𝖓𝖙𝖊 ⚔️🦅](https://twitter.com/Roderick_Cvlcnt) | 17/11/2018 | 7.464 (209/28) | 8594 |
| ![alt text](http://pbs.twimg.com/profile_images/1168629086564098048/Z3Wsone6_normal.jpg "foto do usuário") [Isabelle Restani 👉🏻🇧🇷👍🏻🇧🇷💕🦚🦚](https://twitter.com/Isarestani) | 20/08/2009 | 0.912 (1722/1888) | 9616 |
| ![alt text](http://pbs.twimg.com/profile_images/1350460931021615105/HKa9GX3Z_normal.jpg "foto do usuário") [Fabiana Barroso](https://twitter.com/fabifbbr) | 19/08/2009 | 192.252 (136307/709) | 49587 |
| ![alt text](http://pbs.twimg.com/profile_images/1273034422728654849/mbj7znMZ_normal.jpg "foto do usuário") [Unknownuser  🇧🇷 🇮🇱 🇺🇲](https://twitter.com/phdigitos) | 03/04/2009 | 0.207 (245/1182) | 9384 |
| ![alt text](http://pbs.twimg.com/profile_images/1239495273828814849/5ANGlbj8_normal.jpg "foto do usuário") [Tô_de_olho_em_SLZ](https://twitter.com/TDeOlhoNoBr1) | 16/03/2020 | 0.016 (1/61) | 151 |
| ![alt text](http://pbs.twimg.com/profile_images/1350590849114107910/9V3POqCX_normal.jpg "foto do usuário") [DIREITA OPRESSORA!! 🤡](https://twitter.com/brunove15563373) | 06/03/2019 | 0.691 (429/621) | 5720 |
| ![alt text](http://pbs.twimg.com/profile_images/1239553738496450560/SbXTRgg5_normal.jpg "foto do usuário") [©old gu¥](https://twitter.com/caffimade) | 27/11/2019 | 0.4 (56/140) | 1181 |
| ![alt text](http://pbs.twimg.com/profile_images/1294055810671157248/wMhTsWsJ_normal.jpg "foto do usuário") [Weslen Gomes](https://twitter.com/wdgomes) | 04/01/2020 | 0.379 (36/95) | 214 |
| ![alt text](http://pbs.twimg.com/profile_images/1352380139041153026/mvv2_MrQ_normal.jpg "foto do usuário") [Paulo 👀🇧🇷🗽🇺🇸](https://twitter.com/brasilmelhor38) | 24/09/2018 | 0.476 (233/489) | 2075 |
| ![alt text](http://pbs.twimg.com/profile_images/1350288951664402433/P_7lThkL_normal.jpg "foto do usuário") [Cloris Portes 🇧🇷®️](https://twitter.com/CPortesa) | 07/07/2019 | 0.907 (3590/3957) | 11661 |
| ![alt text](http://pbs.twimg.com/profile_images/1264479649133998080/P96bkx-I_normal.jpg "foto do usuário") [Jeison Brasil](https://twitter.com/jeisonsanches4) | 08/01/2012 | 0.797 (1027/1289) | 3649 |
| ![alt text](http://pbs.twimg.com/profile_images/1298804392079044609/6dMCW8FB_normal.jpg "foto do usuário") [lee](https://twitter.com/frank3b7) | 26/10/2014 | 1.763 (827/469) | 8081 |
| ![alt text](http://pbs.twimg.com/profile_images/1233130142496624640/rO5C7ntO_normal.jpg "foto do usuário") [Dr Enéias Carneiro](https://twitter.com/EneiasDr) | 27/02/2020 | 0.118 (24/203) | 398 |
| ![alt text](http://pbs.twimg.com/profile_images/1197113164783063040/tUrN6PAf_normal.jpg "foto do usuário") [silvinhofenix](https://twitter.com/silvinhofenix) | 25/11/2011 | 0.383 (397/1036) | 1866 |
| ![alt text](http://pbs.twimg.com/profile_images/1322976091208896513/jOOFfwhj_normal.jpg "foto do usuário") [Julio Cesar Teixeira](https://twitter.com/jctm1) | 21/04/2009 | 2.779 (3213/1156) | 261037 |
| ![alt text](http://pbs.twimg.com/profile_images/1346825353092878337/A8gYtSyg_normal.jpg "foto do usuário") [🕇Inriel🕇](https://twitter.com/Inrielz) | 06/01/2020 | 0.165 (38/231) | 166 |
| ![alt text](http://pbs.twimg.com/profile_images/1307824127596732416/ig9GDC61_normal.jpg "foto do usuário") [MITO🇧🇷🇮🇪FLUZÃO🇺🇸🇮🇱BIBI](https://twitter.com/17marka17) | 10/04/2018 | 0.605 (2006/3314) | 12766 |
| ![alt text](http://pbs.twimg.com/profile_images/2676075958/d81f7d20c84e3475a163f4191c577570_normal.jpeg "foto do usuário") [Paulo Tavares](https://twitter.com/paulovtn) | 19/09/2012 | 0.091 (38/416) | 470 |
| ![alt text](http://pbs.twimg.com/profile_images/1229981009568915456/MXJH8Ipm_normal.jpg "foto do usuário") [Duke DeBear 🇺🇲](https://twitter.com/DukeDebear) | 11/11/2018 | 0.152 (127/836) | 12552 |
| ![alt text](http://pbs.twimg.com/profile_images/1257112955331756032/Ql0Edv4D_normal.jpg "foto do usuário") [🐸 Motoboy da Treta 🇧🇷](https://twitter.com/Supertramp68) | 11/04/2010 | 0.632 (426/674) | 30706 |
| ![alt text](http://pbs.twimg.com/profile_images/914002863382286336/BDlqhdUY_normal.jpg "foto do usuário") [Natasha Macedo 💮](https://twitter.com/Natasha_Hortela) | 30/09/2017 | 0.703 (1169/1664) | 50 |
| ![alt text](http://pbs.twimg.com/profile_images/1234193264372256770/l-S2Cge7_normal.jpg "foto do usuário") [O Mago Libertário](https://twitter.com/OMAGOLIBERTARIO) | 21/12/2018 | 67.377 (37192/552) | 22466 |
| ![alt text](http://pbs.twimg.com/profile_images/1293653597788536837/7ruLuuE7_normal.jpg "foto do usuário") [NEYBONARO 🇧🇷🇧🇷](https://twitter.com/CaoPara) | 02/02/2020 | 0.406 (736/1812) | 13945 |
| ![alt text](http://pbs.twimg.com/profile_images/1354456282498002945/ZAvlr_a3_normal.jpg "foto do usuário") [Flávio . ' . 🇧🇷🇵🇹](https://twitter.com/portuga_flavio) | 24/05/2011 | 0.595 (827/1390) | 14911 |
| ![alt text](http://pbs.twimg.com/profile_images/1079024123588870146/4JOE9KY0_normal.jpg "foto do usuário") [🇧🇷🇧🇷🇺🇸🇮🇱 ZÉ GAVIÃO 🇧🇷🇺🇸🇮🇱🇧🇷🇧🇷](https://twitter.com/GaviaoZe) | 28/12/2018 | 0.83 (4110/4949) | 79578 |
| ![alt text](http://pbs.twimg.com/profile_images/1306611719423262720/ZXa6c5X2_normal.jpg "foto do usuário") [Paulo Cruz](https://twitter.com/PauloCr90284717) | 17/11/2017 | 0.815 (358/439) | 1609 |
| ![alt text](http://pbs.twimg.com/profile_images/1226992403426545665/b_EsjV-J_normal.jpg "foto do usuário") [Dudu1981](https://twitter.com/laborao1) | 16/05/2011 | 0.107 (64/598) | 1399 |
| ![alt text](http://pbs.twimg.com/profile_images/968827441992142848/Qdqr3vMS_normal.jpg "foto do usuário") [Mestre Cardoso 🇧🇷🇮🇱🇺🇸🇨🇰🇰🇷🇧🇳](https://twitter.com/rdacardoso) | 29/06/2009 | 0.101 (23/227) | 684 |
| ![alt text](http://pbs.twimg.com/profile_images/1349111305572147205/yBEqjrAw_normal.jpg "foto do usuário") [rj2021](https://twitter.com/brasil2506) | 31/10/2010 | 0.513 (2324/4529) | 78981 |
| ![alt text](http://pbs.twimg.com/profile_images/1101567158042193920/F6iEq20E_normal.png "foto do usuário") [Francisco Salgado](https://twitter.com/chicosal491) | 26/03/2018 | 0.159 (14/88) | 1805 |
| ![alt text](http://pbs.twimg.com/profile_images/1335958417278689281/f8bljCl-_normal.jpg "foto do usuário") [Marco André 🇧🇷🇵🇱 (Sarcasmo não Mata!!! )](https://twitter.com/ma_kaval) | 23/02/2010 | 0.175 (174/994) | 13115 |
| ![alt text](http://pbs.twimg.com/profile_images/1083789646935531520/eQ9aIi18_normal.jpg "foto do usuário") [Mauro](https://twitter.com/Mauro37451328) | 11/01/2019 | 0.14 (13/93) | 1736 |
| ![alt text](http://pbs.twimg.com/profile_images/1239335627574870019/K2YmKNyQ_normal.jpg "foto do usuário") [1S3NTO ________________________Ora pois, veja bem!](https://twitter.com/1s3nto) | 26/02/2020 | 0.647 (22/34) | 2011 |
| ![alt text](http://pbs.twimg.com/profile_images/1030222252254683136/cK-Yod-a_normal.jpg "foto do usuário") [Andre Batista Silva 🇧🇷](https://twitter.com/AndreBatista_9) | 07/03/2012 | 0.483 (427/884) | 39952 |
| ![alt text](http://pbs.twimg.com/profile_images/1275915098956206080/GOdc98iP_normal.jpg "foto do usuário") [Moro Presidente 2022](https://twitter.com/elisa_guarita) | 15/08/2019 | 0.912 (156/171) | 8532 |
| ![alt text](http://pbs.twimg.com/profile_images/1214893771965550592/2rkRi3VP_normal.jpg "foto do usuário") [NTC 🇹🇼 🇭🇰](https://twitter.com/NKT010) | 04/05/2013 | 1.066 (292/274) | 8034 |
| ![alt text](http://pbs.twimg.com/profile_images/1302926976206995462/kap8dZ0c_normal.jpg "foto do usuário") [Adeir Pereira Marinh](https://twitter.com/adeir_marinh) | 17/10/2017 | 0.841 (2378/2829) | 134500 |
| ![alt text](http://pbs.twimg.com/profile_images/1337672949290192896/jZdDPJ6N_normal.jpg "foto do usuário") [𝐎𝐒𝐄𝐈𝐀𝐒 & 𝕄𝕒𝕣𝕖𝕤𝕚𝕒𝕤🌊🏄‍♂️🤡](https://twitter.com/PradoOseias) | 17/09/2017 | 0.832 (1951/2344) | 58017 |
| ![alt text](http://pbs.twimg.com/profile_images/880598334385291264/yR_q_5zM_normal.jpg "foto do usuário") [Antonio Chalhub](https://twitter.com/ChalhubAntonio) | 30/06/2017 | 0.894 (1617/1808) | 101422 |
| ![alt text](http://pbs.twimg.com/profile_images/1234541935999823873/4tSu874j_normal.jpg "foto do usuário") [MCCampos](https://twitter.com/Mariado90423288) | 20/03/2019 | 0.756 (1228/1625) | 6829 |
| ![alt text](http://pbs.twimg.com/profile_images/1260659633523482624/kiTA6Xfv_normal.jpg "foto do usuário") [cardoso](https://twitter.com/Cardoso) | 18/03/2007 | 181.413 (73291/404) | 654631 |
| ![alt text](http://pbs.twimg.com/profile_images/1122960446938648576/-vxgxm8i_normal.jpg "foto do usuário") [Rose Martins](https://twitter.com/RoseMar79044400) | 07/04/2019 | 0.832 (1192/1432) | 3893 |
| ![alt text](http://pbs.twimg.com/profile_images/1308102960539414531/l7U2mNQw_normal.jpg "foto do usuário") [I'm Jota! - O CUDIMUNDISTÃO É AQUI...](https://twitter.com/jotaefe2805) | 26/05/2010 | 2.159 (12803/5931) | 200376 |
| ![alt text](http://pbs.twimg.com/profile_images/1311288923436601344/hOUoRmJd_normal.jpg "foto do usuário") [japonazi](https://twitter.com/celso_matsuda) | 03/11/2009 | 0.334 (142/425) | 7016 |
| ![alt text](http://pbs.twimg.com/profile_images/1347867660302905346/RQRI2xwS_normal.jpg "foto do usuário") [Zeca ③⑧](https://twitter.com/JoseReldah) | 31/05/2010 | 0.909 (4523/4976) | 209151 |
| ![alt text](http://pbs.twimg.com/profile_images/1194382100184600576/t0ZcPIPL_normal.jpg "foto do usuário") [Marco Jardim](https://twitter.com/MarcoJardim15) | 19/10/2019 | 0.407 (168/413) | 20513 |
| ![alt text](http://pbs.twimg.com/profile_images/1337252028897243139/li0zDx_M_normal.jpg "foto do usuário") [Mariel 🇧🇷](https://twitter.com/mariel_mariel_m) | 26/06/2011 | 5.0 (35/7) | 5 |
| ![alt text](http://pbs.twimg.com/profile_images/1348957489321144320/5YiR1DR-_normal.jpg "foto do usuário") [#MaiaInimigoDoBrasil Botafogo](https://twitter.com/Direita_True) | 08/06/2017 | 5.576 (775/139) | 70387 |
| ![alt text](http://pbs.twimg.com/profile_images/1182333333801459717/FeckThbv_normal.jpg "foto do usuário") [Luís Fernando varges](https://twitter.com/vargesfernando) | 14/12/2014 | 0.1 (212/2129) | 2486 |
| ![alt text](http://pbs.twimg.com/profile_images/1284255536423358464/DizBqjOw_normal.jpg "foto do usuário") [RIBEIRO🇧🇷🇮🇱🇺🇸🇵🇱HCQN+AZ.Salva-Vacina-NÃO](https://twitter.com/Wal_Patriota) | 04/08/2018 | 0.985 (5295/5375) | 110668 |
| ![alt text](http://pbs.twimg.com/profile_images/1200180785808064522/NT1ewxhw_normal.jpg "foto do usuário") [🇧🇷TMarin10🇧🇷](https://twitter.com/marinho_thiago) | 07/03/2019 | 0.757 (712/941) | 34269 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [IvoHM](https://twitter.com/IvoHM) | 07/02/2010 | 0.034 (3/87) | 967 |
| ![alt text](http://pbs.twimg.com/profile_images/1808502859/361245_3002_normal.jpg "foto do usuário") [Andre L. T. Ramos](https://twitter.com/andreltr) | 24/03/2009 | 1.492 (176/118) | 27846 |
| ![alt text](http://pbs.twimg.com/profile_images/1291777851155415044/NSzN7trg_normal.jpg "foto do usuário") [Oriebir 🇧🇷🇧🇷](https://twitter.com/birollilo) | 16/10/2014 | 1.175 (322/274) | 6971 |
| ![alt text](http://pbs.twimg.com/profile_images/1321659449526931456/GYxGf9J0_normal.jpg "foto do usuário") [Cesar Luiz 🇧🇷🇺🇦](https://twitter.com/Cesar_Luiz020) | 15/03/2019 | 0.225 (206/914) | 9496 |
| ![alt text](http://pbs.twimg.com/profile_images/1223925339916849152/jk4XauDR_normal.jpg "foto do usuário") [Jandir Rodrigues](https://twitter.com/JandirRodrigu19) | 30/05/2019 | 0.786 (304/387) | 1798 |
| ![alt text](http://pbs.twimg.com/profile_images/1228714006145314816/usFYE7e7_normal.jpg "foto do usuário") [deiag73- ESQUERDA NÃO TEM VEZ E COMUNISTA MUITO -](https://twitter.com/deiag73) | 18/06/2010 | 0.449 (858/1910) | 6859 |
| ![alt text](http://pbs.twimg.com/profile_images/1183595549062250496/QbB2HZq-_normal.jpg "foto do usuário") [Diego Roger](https://twitter.com/diegowoodfx) | 11/04/2010 | 0.114 (55/483) | 4838 |
| ![alt text](http://pbs.twimg.com/profile_images/1189505104824717313/wZmYfm5p_normal.jpg "foto do usuário") [Cenoura Flamejante](https://twitter.com/cenouraemchamas) | 28/10/2019 | 0.406 (158/389) | 6733 |
| ![alt text](http://pbs.twimg.com/profile_images/1229960231762976768/Uu9J-ksE_normal.jpg "foto do usuário") [Edward Luz. Antropólogo & Consultor Parlamentar.](https://twitter.com/edwardluz) | 15/02/2009 | 0.54 (1217/2252) | 10052 |
| ![alt text](http://pbs.twimg.com/profile_images/1136977433423486976/TEg98DLv_normal.jpg "foto do usuário") [Diego244](https://twitter.com/Diegomartins244) | 01/04/2016 | 0.01 (1/0) | 753 |
| ![alt text](http://pbs.twimg.com/profile_images/1237538504428552192/3kBcwaRn_normal.jpg "foto do usuário") [Leandro Borges](https://twitter.com/leandroborges13) | 07/12/2009 | 0.139 (230/1657) | 3141 |
| ![alt text](http://pbs.twimg.com/profile_images/1304386239869616129/GyYCy_mp_normal.jpg "foto do usuário") [Rock🤘🐓🤘Galo!!! Já fez seu GNV?](https://twitter.com/BoaGalo) | 30/12/2013 | 0.996 (6070/6097) | 21865 |
| ![alt text](http://pbs.twimg.com/profile_images/1316546789755908096/0OCch-5-_normal.jpg "foto do usuário") [Colin Wright](https://twitter.com/SwipeWright) | 21/06/2018 | 179.956 (61905/344) | 24829 |
| ![alt text](http://pbs.twimg.com/profile_images/1235042914377568257/TF-0kXeP_normal.jpg "foto do usuário") [+5521988795401](https://twitter.com/EK40fZtwW5KneAM) | 22/04/2017 | 0.142 (18/127) | 3060 |
| ![alt text](http://pbs.twimg.com/profile_images/1347718812561498114/rBmn3Epy_normal.jpg "foto do usuário") [Guerra cultural 🇧🇷](https://twitter.com/nonducorduco7) | 02/07/2019 | 0.197 (236/1198) | 17317 |
| ![alt text](http://pbs.twimg.com/profile_images/1202374139778080773/72Bzzd3E_normal.jpg "foto do usuário") [Varini 🇧🇷 🇮🇱](https://twitter.com/VariniBrasil) | 13/08/2019 | 0.903 (664/735) | 6235 |
| ![alt text](http://pbs.twimg.com/profile_images/721739361637765120/A3edeUte_normal.jpg "foto do usuário") [maria del carmen rey - #Bolsonaro2022🙋🇧🇷](https://twitter.com/carmendelrey24) | 16/07/2014 | 0.714 (1450/2030) | 58149 |
| ![alt text](http://pbs.twimg.com/profile_images/1265090990169350145/wZjI2GLI_normal.jpg "foto do usuário") [PATRIOTA](https://twitter.com/DavidPatriota01) | 05/07/2019 | 0.01 (840/0) | 26723 |
| ![alt text](http://pbs.twimg.com/profile_images/1172574709290012674/2NFzaTIn_normal.jpg "foto do usuário") [Gabriel Marques](https://twitter.com/GabrielMar_ques) | 05/04/2019 | 0.686 (429/625) | 11535 |
| ![alt text](http://pbs.twimg.com/profile_images/1221684793039052801/Q66Ghw_L_normal.jpg "foto do usuário") [Br3n0🔴⚫](https://twitter.com/BrenoAlmeidaBF) | 12/10/2019 | 0.014 (1/69) | 211 |
| ![alt text](http://pbs.twimg.com/profile_images/1106400046663303169/W0VqrTKV_normal.jpg "foto do usuário") [Luciana Carvalho ](https://twitter.com/Lu_M_C) | 28/07/2014 | 0.189 (45/238) | 3149 |
| ![alt text](http://pbs.twimg.com/profile_images/1347717905421635589/YfmM000-_normal.jpg "foto do usuário") [Paulo Silva](https://twitter.com/paulo_silva2017) | 29/10/2017 | 0.988 (2244/2272) | 29975 |
| ![alt text](http://pbs.twimg.com/profile_images/1347947130862915587/E9Z5bEOD_normal.jpg "foto do usuário") [Sherlock - #Bolsonaro2022 🇧🇷](https://twitter.com/xerloquis) | 20/06/2018 | 0.985 (4715/4785) | 73768 |
| ![alt text](http://pbs.twimg.com/profile_images/1347807072201666560/nn5TOKn-_normal.jpg "foto do usuário") [viciado em viver 🇭🇺](https://twitter.com/________renan) | 18/01/2020 | 0.798 (67/84) | 8417 |
| ![alt text](http://pbs.twimg.com/profile_images/1171246014575120384/CxAc5Gx2_normal.jpg "foto do usuário") [Paulonail](https://twitter.com/paulonail) | 20/09/2018 | 0.594 (2214/3730) | 24695 |
| ![alt text](http://pbs.twimg.com/profile_images/1332358898024636417/bm9Jvp1t_normal.jpg "foto do usuário") [Kleber Teixeira 🇧🇷◤✠◢🇧🇷](https://twitter.com/klebersef) | 17/07/2009 | 0.991 (2548/2572) | 9142 |
| ![alt text](http://pbs.twimg.com/profile_images/1350994964654809094/hFUyjCk2_normal.jpg "foto do usuário") [Sirlei SCC](https://twitter.com/loiradedireita1) | 13/10/2018 | 0.986 (6910/7010) | 33800 |
| ![alt text](http://pbs.twimg.com/profile_images/1354122467888033792/tH6T3TOh_normal.jpg "foto do usuário") [Frank](https://twitter.com/jfrankrj) | 31/03/2012 | 0.873 (856/981) | 6484 |
| ![alt text](http://pbs.twimg.com/profile_images/1267598694653796352/HRE6PclC_normal.jpg "foto do usuário") [Dan](https://twitter.com/vireadireita20) | 20/09/2015 | 2.108 (2184/1036) | 50664 |
| ![alt text](http://pbs.twimg.com/profile_images/1187076510248849415/dM1bMgeS_normal.jpg "foto do usuário") [Juliana Garcia](https://twitter.com/Juliana84259162) | 07/09/2019 | 1.15 (17482/15207) | 24605 |
| ![alt text](http://pbs.twimg.com/profile_images/838691615019577345/C77tqrW7_normal.jpg "foto do usuário") [Carlos Alberto](https://twitter.com/berken70) | 17/01/2014 | 0.306 (52/170) | 1935 |
| ![alt text](http://pbs.twimg.com/profile_images/1302721962108579842/yu6qwT0e_normal.jpg "foto do usuário") [azuree](https://twitter.com/azuree8o8) | 13/02/2017 | 0.105 (41/392) | 1013 |
| ![alt text](http://pbs.twimg.com/profile_images/1353345552038195201/zhoct8Jj_normal.jpg "foto do usuário") [Amarelão fc.](https://twitter.com/EzequielPsilva1) | 03/12/2019 | 0.337 (766/2270) | 3585 |
| ![alt text](http://pbs.twimg.com/profile_images/1309192590735085570/0dczvBfy_normal.jpg "foto do usuário") [Moisés](https://twitter.com/MoisesLindis3) | 17/04/2019 | 0.176 (3/17) | 20 |
| ![alt text](http://pbs.twimg.com/profile_images/1131646033753182211/GHxOy2Nn_normal.jpg "foto do usuário") [Márcio Oliveira 🇾🇪 spfc](https://twitter.com/MrcioOl13025476) | 16/04/2019 | 0.063 (7/111) | 849 |
| ![alt text](http://pbs.twimg.com/profile_images/1352890141455622144/E92gvbk__normal.jpg "foto do usuário") [SushiDeCostela](https://twitter.com/sushidecostela) | 17/10/2018 | 1.037 (643/620) | 44930 |
| ![alt text](http://pbs.twimg.com/profile_images/1257677757196238849/r6gwEBW7_normal.jpg "foto do usuário") [Danny](https://twitter.com/dannstweets) | 22/05/2009 | 4.571 (1970/431) | 16375 |
| ![alt text](http://pbs.twimg.com/profile_images/1222876652998279169/Jr35v7en_normal.jpg "foto do usuário") [Αθήνα](https://twitter.com/atenas) | 20/09/2008 | 0.581 (274/472) | 20624 |
| ![alt text](http://pbs.twimg.com/profile_images/1200947581637058560/QgQ-qYHw_normal.jpg "foto do usuário") [G0ku](https://twitter.com/G0Kku_) | 01/12/2019 | 0.055 (4/73) | 25 |
| ![alt text](http://pbs.twimg.com/profile_images/1339962198794383360/XwwJNU8Z_normal.jpg "foto do usuário") [•Bruno - Impeachment já!](https://twitter.com/buninrj) | 20/03/2009 | 0.112 (287/2569) | 70384 |
| ![alt text](http://pbs.twimg.com/profile_images/1204601729104437248/FL3lqGPM_normal.jpg "foto do usuário") [Valeria Del Guercio](https://twitter.com/magalh_valeria) | 07/03/2017 | 0.618 (260/421) | 10697 |
| ![alt text](http://pbs.twimg.com/profile_images/3662085282/aef9411e85823f6847b7a9268d858312_normal.jpeg "foto do usuário") [Eduardo da Luz Pereira](https://twitter.com/elpbrasil) | 22/06/2010 | 0.349 (61/175) | 13028 |
| ![alt text](http://pbs.twimg.com/profile_images/907671173265330177/trCclwg5_normal.jpg "foto do usuário") [CaféLiberal☕️](https://twitter.com/liberalwyz) | 12/09/2017 | 1.087 (224/206) | 27115 |
| ![alt text](http://pbs.twimg.com/profile_images/1230129157331456000/Quy8eLI4_normal.jpg "foto do usuário") [Leandro Chaves](https://twitter.com/Leandro_chaves) | 14/11/2014 | 0.025 (37/1503) | 258 |
| ![alt text](http://pbs.twimg.com/profile_images/564129086113869824/u5VWtujL_normal.jpeg "foto do usuário") [loraodi](https://twitter.com/loraodi) | 14/08/2014 | 0.406 (43/106) | 25734 |
| ![alt text](http://pbs.twimg.com/profile_images/1346846885420609537/g_qFvrix_normal.jpg "foto do usuário") [Lion](https://twitter.com/liontherengar) | 08/05/2018 | 0.554 (82/148) | 1043 |
| ![alt text](http://pbs.twimg.com/profile_images/1227419384/belo05_normal.JPG "foto do usuário") [Mountain Madness](https://twitter.com/rey_belo) | 28/10/2009 | 0.102 (9/88) | 185 |
| ![alt text](http://pbs.twimg.com/profile_images/1351035881193435137/Is3Y54Me_normal.jpg "foto do usuário") [Norma](https://twitter.com/Norma47138802) | 25/10/2018 | 0.871 (1401/1609) | 126701 |
| ![alt text](http://pbs.twimg.com/profile_images/799999122371702784/CrqJTfHY_normal.jpg "foto do usuário") [AlexandreCarlosJung](https://twitter.com/Alexnrcarlosj) | 20/10/2015 | 0.15 (106/708) | 11107 |
| ![alt text](http://pbs.twimg.com/profile_images/1354455019001679872/07gEfpvd_normal.jpg "foto do usuário") [Marinho Rodrigo (DOC) 🇺🇸🇧🇷 🇵🇹](https://twitter.com/marinho_adv) | 12/08/2011 | 0.738 (217/294) | 2709 |
| ![alt text](http://pbs.twimg.com/profile_images/1341898363600572419/ZCeg0p98_normal.jpg "foto do usuário") [Lana](https://twitter.com/gatadedireita) | 20/11/2017 | 1.135 (993/875) | 16263 |
| ![alt text](http://pbs.twimg.com/profile_images/1355307002591932417/tlKMuiA4_normal.jpg "foto do usuário") [Chance, the Gardener](https://twitter.com/ZitoMaia1) | 15/10/2019 | 0.955 (276/289) | 11919 |
| ![alt text](http://pbs.twimg.com/profile_images/1053400997282897921/NItNbWDF_normal.jpg "foto do usuário") [Anderson M. G. 🇧🇷](https://twitter.com/goncaand) | 02/07/2014 | 0.807 (728/902) | 11152 |
| ![alt text](http://pbs.twimg.com/profile_images/1226236304763097089/gVKq-hR0_normal.jpg "foto do usuário") [Ana Onnis 🇧🇷](https://twitter.com/zogaonnis) | 12/11/2010 | 1.211 (4055/3348) | 40354 |
| ![alt text](http://pbs.twimg.com/profile_images/1168012378371448833/u1XQf_kf_normal.jpg "foto do usuário") [Paula 🇧🇷](https://twitter.com/Paula47843711) | 02/04/2019 | 0.514 (259/504) | 2440 |
| ![alt text](http://pbs.twimg.com/profile_images/714205937410699264/EM7QfJrG_normal.jpg "foto do usuário") [🍋 Limone 🇧🇷](https://twitter.com/crovislimone2) | 27/03/2016 | 0.831 (882/1062) | 32226 |
| ![alt text](http://pbs.twimg.com/profile_images/1160397778100609024/4XmXCCBj_normal.jpg "foto do usuário") [Zeca Francis (AB)🇧🇷🇵🇹🇮🇱🇺🇸](https://twitter.com/Zeca_Francis) | 08/08/2019 | 0.01 (343/0) | 5938 |
| ![alt text](http://pbs.twimg.com/profile_images/1253855460995858433/vIsENwbQ_normal.jpg "foto do usuário") [💚🇧🇷💛 Andrea](https://twitter.com/vix_andrea) | 04/02/2017 | 2.396 (1066/445) | 86236 |
| ![alt text](http://pbs.twimg.com/profile_images/1330793508697944067/1dkAz4Jv_normal.jpg "foto do usuário") [Pr.Paulo Braga M12 🇧🇷🇮🇱🇺🇸](https://twitter.com/PrPaulobraga) | 07/01/2015 | 0.682 (898/1316) | 9228 |
| ![alt text](http://pbs.twimg.com/profile_images/1348440901241229314/4tPUTExA_normal.jpg "foto do usuário") [Salomão 💙](https://twitter.com/Salomitto) | 02/06/2017 | 0.994 (4259/4286) | 11009 |
| ![alt text](http://pbs.twimg.com/profile_images/1343989093622022147/FEkoN8on_normal.jpg "foto do usuário") [Nadir4 🎓🔎🌐](https://twitter.com/NadiraSPFonseca) | 16/10/2019 | 0.077 (2/26) | 5 |
| ![alt text](http://pbs.twimg.com/profile_images/1118510319171788801/ioDcIFxL_normal.jpg "foto do usuário") [Monya](https://twitter.com/oOo_Monya_oOo) | 17/04/2019 | 0.153 (68/443) | 1253 |
| ![alt text](http://pbs.twimg.com/profile_images/1276814905497264129/SKbqc1uW_normal.jpg "foto do usuário") [LuQueiroz](https://twitter.com/jluqueiroz) | 05/08/2017 | 1.036 (2724/2630) | 142595 |
| ![alt text](http://pbs.twimg.com/profile_images/1045657047054905344/GRDWZLJR_normal.jpg "foto do usuário") [Renato Vieira](https://twitter.com/Renato29211889) | 28/09/2018 | 0.318 (85/267) | 2447 |
| ![alt text](http://pbs.twimg.com/profile_images/691594585626247168/ZtoZJsQG_normal.jpg "foto do usuário") [tonny](https://twitter.com/tonny_coxa) | 18/06/2010 | 0.997 (20623/20685) | 81493 |
| ![alt text](http://pbs.twimg.com/profile_images/1162774810222632960/fQlujBvs_normal.jpg "foto do usuário") [DEUS NO COMANDO](https://twitter.com/ScarduelliOsmar) | 07/07/2019 | 0.903 (4527/5012) | 16202 |
| ![alt text](http://pbs.twimg.com/profile_images/1184580127738515457/8Hv8KlAe_normal.jpg "foto do usuário") [Alan Naicson 🇧🇷](https://twitter.com/AlanNaicson) | 12/02/2013 | 0.131 (78/594) | 7232 |
| ![alt text](http://pbs.twimg.com/profile_images/1267841390924509187/avUgt9jD_normal.jpg "foto do usuário") [Fabio](https://twitter.com/FabioLima76) | 21/08/2011 | 0.493 (286/580) | 32650 |
| ![alt text](http://pbs.twimg.com/profile_images/470031024781803520/5X-hs4tA_normal.jpeg "foto do usuário") [Fernando Carneiro](https://twitter.com/1fernandoreal) | 02/05/2014 | 0.87 (456/524) | 43830 |
| ![alt text](http://pbs.twimg.com/profile_images/1274119450501971968/MKBcnx8t_normal.jpg "foto do usuário") [Joice Araújo](https://twitter.com/JoiceArajo16) | 30/09/2018 | 0.576 (110/191) | 10403 |
| ![alt text](http://pbs.twimg.com/profile_images/1305545591276142594/iNiYjQeo_normal.jpg "foto do usuário") [Luciana-15/03 eu Fui!!!🇧🇷👊](https://twitter.com/LucianaNoBot) | 18/09/2018 | 1.096 (949/866) | 17346 |
| ![alt text](http://pbs.twimg.com/profile_images/1199471535758741504/107S4xyB_normal.jpg "foto do usuário") [paulo](https://twitter.com/diversaumdanoet) | 14/07/2019 | 0.4 (14/35) | 403 |
| ![alt text](http://pbs.twimg.com/profile_images/1293568528096940032/objKNUtT_normal.jpg "foto do usuário") [Personagens da Disney com Bolsonaro](https://twitter.com/SeidlVann) | 30/07/2019 | 0.517 (46/89) | 4892 |
| ![alt text](http://pbs.twimg.com/profile_images/1330439937251041281/gcK8di7l_normal.jpg "foto do usuário") [Square Salvo](https://twitter.com/swedish_salvo) | 04/05/2018 | 0.072 (16/222) | 2404 |
| ![alt text](http://pbs.twimg.com/profile_images/1342667532499611649/D-XoWgiX_normal.jpg "foto do usuário") [\\C354R.exe](https://twitter.com/CesarNotFound) | 13/03/2019 | 0.131 (61/467) | 1497 |
| ![alt text](http://pbs.twimg.com/profile_images/1297165118699114496/5s6uWl6m_normal.jpg "foto do usuário") [Pericles](https://twitter.com/PERICLE54974122) | 13/02/2018 | 1.078 (843/782) | 6992 |
| ![alt text](http://pbs.twimg.com/profile_images/1347748372942364673/7vCsDua1_normal.jpg "foto do usuário") [É pavê ou pá comê?](https://twitter.com/epaveoucome) | 26/04/2017 | 0.784 (864/1102) | 48554 |
| ![alt text](http://pbs.twimg.com/profile_images/1332230789849882624/-RkxdU7n_normal.jpg "foto do usuário") [⚓️ MATRIX ⚓️](https://twitter.com/Marcos_Cesar_BR) | 29/10/2018 | 0.862 (1629/1889) | 15844 |
| ![alt text](http://pbs.twimg.com/profile_images/1348323568690593794/oY0XJrAb_normal.jpg "foto do usuário") [BRASIL ACIMA DE TUDO🇧🇷🇧🇷🇧🇷](https://twitter.com/cleonildopessoa) | 21/09/2015 | 0.591 (104/176) | 13316 |
| ![alt text](http://pbs.twimg.com/profile_images/1250441945643536387/K4C0dWRg_normal.jpg "foto do usuário") [sandra assuncao](https://twitter.com/sandrahostins) | 02/04/2011 | 0.983 (1247/1268) | 16930 |
| ![alt text](http://pbs.twimg.com/profile_images/633843038104756224/2kaftSrA_normal.jpg "foto do usuário") [Eliseu J Souza](https://twitter.com/EliseuJSouza) | 10/06/2012 | 0.127 (43/339) | 861 |
| ![alt text](http://pbs.twimg.com/profile_images/1133393822694727680/1pJosaBY_normal.png "foto do usuário") [SOL MAR MONTANHA JOVEM LUTE PELO BRASIL SEU FUTURO](https://twitter.com/SOLMARMONTANHA) | 30/05/2016 | 0.508 (1891/3719) | 60 |
| ![alt text](http://pbs.twimg.com/profile_images/1157469853403557888/8CG1kv4u_normal.jpg "foto do usuário") [Paulo Miguel Esdacheti](https://twitter.com/esdacheti) | 03/08/2019 | 0.253 (196/776) | 33411 |
| ![alt text](http://pbs.twimg.com/profile_images/1106455918823333888/rez_1ETP_normal.jpg "foto do usuário") [Rubens CM](https://twitter.com/rubensCMont) | 17/01/2018 | 0.177 (14/79) | 1583 |
| ![alt text](http://pbs.twimg.com/profile_images/1267802831634997248/fNIBdWfO_normal.jpg "foto do usuário") [Edvaldo Júnior](https://twitter.com/EdvaldoJunior85) | 16/06/2009 | 0.446 (202/453) | 4564 |
| ![alt text](http://pbs.twimg.com/profile_images/1273919599772413952/jW84SIqr_normal.jpg "foto do usuário") [Rafa Poerner 🗣️](https://twitter.com/Rafa_Poerner) | 25/10/2011 | 0.391 (212/542) | 11193 |
| ![alt text](http://pbs.twimg.com/profile_images/1268026416324542464/gALQ9E2e_normal.jpg "foto do usuário") [Fabio](https://twitter.com/PorumBrasilMe11) | 04/07/2019 | 0.469 (556/1185) | 8894 |
| ![alt text](http://pbs.twimg.com/profile_images/1350796243195322370/8fVPfaza_normal.jpg "foto do usuário") [observador 👮🏾‍♂️🇧🇷🇮🇱🇹🇼🇺🇸jacobju🐸gab.ai](https://twitter.com/juliocjacob) | 05/04/2011 | 0.838 (1098/1310) | 43348 |
| ![alt text](http://pbs.twimg.com/profile_images/1264961503809212416/Ew47h3jL_normal.jpg "foto do usuário") [Donbass - CRF 🔴⚫🔴⚫](https://twitter.com/DonbassRPD) | 26/07/2010 | 0.071 (53/744) | 8479 |
| ![alt text](http://pbs.twimg.com/profile_images/1075042777661083648/XwdXkEp-_normal.jpg "foto do usuário") [Diego](https://twitter.com/diega1n) | 28/07/2009 | 3.311 (586/177) | 771 |
| ![alt text](http://pbs.twimg.com/profile_images/1283126893999542276/Em9KpEFT_normal.jpg "foto do usuário") [Raffaello Fazzionni 🇧🇷🇧🇷🇧🇷](https://twitter.com/RaffaelloFazzi) | 04/05/2017 | 1.005 (6598/6563) | 10390 |
| ![alt text](http://pbs.twimg.com/profile_images/929518051057430530/NCbHs4ke_normal.jpg "foto do usuário") [JOÃO ANTONIO💧](https://twitter.com/Jamoraes39) | 25/10/2017 | 0.747 (574/768) | 6047 |
| ![alt text](http://pbs.twimg.com/profile_images/1312097831277285377/W5_LUBhL_normal.jpg "foto do usuário") [Van der ley](https://twitter.com/malitouno) | 18/08/2016 | 0.397 (87/219) | 5305 |
| ![alt text](http://pbs.twimg.com/profile_images/1165741600032612352/Eqqe82R-_normal.jpg "foto do usuário") [Mercury](https://twitter.com/mercury_reverso) | 23/01/2019 | 1.057 (130/123) | 8462 |
| ![alt text](http://pbs.twimg.com/profile_images/1259166803282006021/ichRTHb-_normal.jpg "foto do usuário") [👑Drunk Phillippe👑 Duke of Barley & Count of Hops](https://twitter.com/fbarc) | 23/04/2009 | 0.654 (1112/1700) | 9223 |
| ![alt text](http://pbs.twimg.com/profile_images/787661986679099392/qY38l8hr_normal.jpg "foto do usuário") [JAVIPOM](https://twitter.com/miratudo) | 15/10/2016 | 0.248 (166/670) | 5433 |
| ![alt text](http://pbs.twimg.com/profile_images/1208981114037133312/keIr1bpq_normal.jpg "foto do usuário") [Regi PdP](https://twitter.com/PdpRegi) | 01/12/2017 | 0.394 (39/99) | 3974 |
| ![alt text](http://pbs.twimg.com/profile_images/1297660044184625154/6se7UTaz_normal.jpg "foto do usuário") [João Zuba](https://twitter.com/JoaoZuba) | 14/02/2010 | 0.821 (239/291) | 8622 |
| ![alt text](http://pbs.twimg.com/profile_images/1266198576092327936/Ud6vb3_W_normal.jpg "foto do usuário") [FAÇA A COISA CERTA SEMPRE](https://twitter.com/WALTER_BKR) | 23/08/2011 | 0.239 (1059/4430) | 37694 |
| ![alt text](http://pbs.twimg.com/profile_images/1290682199591854082/jZsAovyZ_normal.jpg "foto do usuário") [Jonny Quest](https://twitter.com/JQuestReal) | 22/03/2019 | 0.412 (462/1122) | 734 |
| ![alt text](http://pbs.twimg.com/profile_images/1159863054445809664/gvr5mhSR_normal.jpg "foto do usuário") [Vinicius 🇧🇷](https://twitter.com/vleao96) | 31/07/2011 | 0.289 (65/225) | 4323 |
| ![alt text](http://pbs.twimg.com/profile_images/1281359870411907073/C3MEZe5v_normal.jpg "foto do usuário") [André Sant'' Anna](https://twitter.com/andrelu94331540) | 15/01/2013 | 0.086 (42/491) | 407 |
| ![alt text](http://pbs.twimg.com/profile_images/1337885343849320449/Q8L1YX01_normal.jpg "foto do usuário") [Patrick Oak](https://twitter.com/oak_patrick) | 01/10/2017 | 0.721 (2083/2889) | 3067 |
| ![alt text](http://pbs.twimg.com/profile_images/1258426186830688256/e1recQKM_normal.jpg "foto do usuário") [James🇧🇷](https://twitter.com/DEUSVULT33) | 23/09/2018 | 0.278 (229/823) | 2538 |
| ![alt text](http://pbs.twimg.com/profile_images/1149048501906628608/dLCaNXh7_normal.jpg "foto do usuário") [Adriano Souza](https://twitter.com/Adriano72942983) | 29/06/2019 | 0.037 (4/107) | 889 |
| ![alt text](http://pbs.twimg.com/profile_images/1082413805190168576/EM3wMRiv_normal.jpg "foto do usuário") [Dilmares](https://twitter.com/Dilmares1) | 07/01/2019 | 0.567 (101/178) | 6279 |
| ![alt text](http://pbs.twimg.com/profile_images/1343367668250894341/SY88g8fl_normal.jpg "foto do usuário") [🌸FleurDeDieu🌸](https://twitter.com/mfmbarr) | 27/07/2009 | 1.033 (45565/44094) | 35140 |
| ![alt text](http://pbs.twimg.com/profile_images/1120039032736632832/ru-w3SVP_normal.jpg "foto do usuário") [Sérgio Rodolfo Moreira](https://twitter.com/SrgioRodolfoMo2) | 19/04/2019 | 0.996 (5837/5858) | 21021 |
| ![alt text](http://pbs.twimg.com/profile_images/1139577784513245184/UKzh3HEQ_normal.jpg "foto do usuário") [Ana Gabriela](https://twitter.com/AnaGabr80951730) | 06/04/2019 | 0.708 (3026/4273) | 23785 |
| ![alt text](http://pbs.twimg.com/profile_images/1160538559121633280/JI8eiH3u_normal.jpg "foto do usuário") [Francisco Assis](https://twitter.com/chicodoparana) | 16/03/2019 | 0.947 (4599/4855) | 7238 |
| ![alt text](http://pbs.twimg.com/profile_images/1166315809037312001/cKYzmymQ_normal.jpg "foto do usuário") [KABULOZO🤙😋🤙](https://twitter.com/zeferorocha) | 08/07/2012 | 0.659 (539/818) | 17769 |
| ![alt text](http://pbs.twimg.com/profile_images/1301515021516787713/UHrNIKB1_normal.jpg "foto do usuário") [🇧🇷 𝔪卂ŕĆ𝓸ˢ 𝐑ό𝕊α 🇦🇺](https://twitter.com/marcosrosaaus) | 07/08/2010 | 0.907 (3031/3341) | 5857 |
| ![alt text](http://pbs.twimg.com/profile_images/1353380774196752384/TInus4dh_normal.jpg "foto do usuário") [Ana M.🇧🇷🇧🇷🇧🇷](https://twitter.com/AnaMBolsonaro) | 09/08/2018 | 1.002 (5023/5012) | 149907 |
| ![alt text](http://pbs.twimg.com/profile_images/1328486489731321856/dyM9fR3O_normal.jpg "foto do usuário") [Arthur do Val - Mamaefalei](https://twitter.com/arthurmoledoval) | 03/11/2015 | 1464.556 (547744/374) | 4796 |
| ![alt text](http://pbs.twimg.com/profile_images/1260055475799887872/TmoAkRLE_normal.jpg "foto do usuário") [CHARLIE BROWN](https://twitter.com/flavioobom) | 06/11/2009 | 0.477 (1048/2197) | 17735 |
| ![alt text](http://pbs.twimg.com/profile_images/1234935962020478977/B5vXM_TU_normal.jpg "foto do usuário") [JJᶜʳᶠ🔴⚫🤡](https://twitter.com/jjeffersonpb) | 19/03/2014 | 0.16 (511/3195) | 16616 |
| ![alt text](http://pbs.twimg.com/profile_images/1349037950198308872/dGJT9XzD_normal.jpg "foto do usuário") [Vitor A. R. Santos](https://twitter.com/vitorars) | 14/09/2009 | 11.445 (6100/533) | 53017 |
| ![alt text](http://pbs.twimg.com/profile_images/1343336164418347009/T1QF0ZOq_normal.jpg "foto do usuário") [🍀](https://twitter.com/Rayane130614) | 01/10/2017 | 0.31 (108/348) | 2282 |
| ![alt text](http://pbs.twimg.com/profile_images/1103409039604674573/vKlbaeXd_normal.jpg "foto do usuário") [Felipe Martins](https://twitter.com/FelpMartinS96) | 17/12/2017 | 0.356 (243/682) | 3604 |
| ![alt text](http://pbs.twimg.com/profile_images/1078337888906027008/dxuo2qO5_normal.jpg "foto do usuário") [Débora Sousa](https://twitter.com/dradeborasousa) | 09/12/2018 | 2.014 (421/209) | 81069 |
| ![alt text](http://pbs.twimg.com/profile_images/1237036162562306048/sSmJL1jo_normal.jpg "foto do usuário") [Gloria Silvestre Cozza](https://twitter.com/gloriasilvestre) | 27/12/2010 | 0.987 (22171/22471) | 15744 |
| ![alt text](http://pbs.twimg.com/profile_images/1114188129840390145/emjDnNwz_normal.jpg "foto do usuário") [Rodrigo Vilas Boas](https://twitter.com/RodrigoVilasB13) | 20/08/2018 | 0.018 (1/57) | 11 |
| ![alt text](http://pbs.twimg.com/profile_images/1294308904143388672/o3vKMjie_normal.jpg "foto do usuário") [ᑕᗩᖇᗰᗴᑎ ᗪᗴ ᗩᑎᗪᖇᗩᗪᗴ 3️⃣8️⃣ 🇧🇷](https://twitter.com/CarmendeAndrade) | 27/11/2010 | 1.025 (606/591) | 16645 |
| ![alt text](http://pbs.twimg.com/profile_images/1353082992416223232/TbhStKFj_normal.jpg "foto do usuário") [AlexBR 🇧🇷](https://twitter.com/AlexBRfour) | 12/08/2017 | 1.035 (17751/17149) | 22816 |
| ![alt text](http://pbs.twimg.com/profile_images/1348085223087632384/-d5ME3lR_normal.jpg "foto do usuário") [🇧🇷🌺 Rosane 🌺🇧🇷](https://twitter.com/DRosarts) | 07/11/2014 | 1.182 (5987/5066) | 70149 |
| ![alt text](http://pbs.twimg.com/profile_images/1347702026680074240/L0CK2lY3_normal.jpg "foto do usuário") [Raquel Stasiaki](https://twitter.com/RaquelStasiaki) | 25/05/2018 | 1.541 (154397/100204) | 5058 |
| ![alt text](http://pbs.twimg.com/profile_images/1348057956567416832/bg6fuM2Q_normal.jpg "foto do usuário") [Lauro Assunção](https://twitter.com/LauroAssuncao) | 09/03/2012 | 0.909 (1803/1983) | 3017 |
| ![alt text](http://pbs.twimg.com/profile_images/1347859452351946754/TGD8DCJU_normal.jpg "foto do usuário") [Marco Antonio🇧🇷🇵🇹🇺🇸🇮🇱🇯🇵](https://twitter.com/marcos_AntCost) | 28/11/2018 | 0.965 (19458/20161) | 18923 |
| ![alt text](http://pbs.twimg.com/profile_images/1347729406467387398/BUOgcWcJ_normal.jpg "foto do usuário") [severino🇧🇷🇧🇷🇺🇸🇺🇸🇮🇱🇮🇱 57.797.847](https://twitter.com/severinojlperei) | 22/09/2009 | 0.177 (724/4100) | 42593 |
| ![alt text](http://pbs.twimg.com/profile_images/2481907019/r8oi7p7hwxo7krp6bqpr_normal.jpeg "foto do usuário") [Gustavo Menezes](https://twitter.com/Gnaninho) | 17/07/2009 | 0.648 (1023/1579) | 2702 |
| ![alt text](http://pbs.twimg.com/profile_images/1295008733819478017/rRNrewXo_normal.jpg "foto do usuário") [solteiro rio das ostras RJ](https://twitter.com/gilbert31865331) | 21/01/2015 | 0.12 (25/208) | 2096 |
| ![alt text](http://pbs.twimg.com/profile_images/1242784468827586565/j28wMJ18_normal.jpg "foto do usuário") [Ruffus](https://twitter.com/laurindobzk) | 02/07/2010 | 0.13 (122/938) | 6888 |
| ![alt text](http://pbs.twimg.com/profile_images/1413056288/_ndice_normal.jpg "foto do usuário") [Os 3 Poderes](https://twitter.com/Os3Podreres) | 25/06/2011 | 0.545 (2124/3900) | 24371 |
| ![alt text](http://pbs.twimg.com/profile_images/1131220282465837061/8dsWsbu__normal.jpg "foto do usuário") [Renata Braga🇧🇷🇧🇷🇧🇷](https://twitter.com/RenataBraga74) | 16/03/2019 | 0.585 (138/236) | 2839 |
| ![alt text](http://pbs.twimg.com/profile_images/1293653560278822915/4-YlWc2c_normal.jpg "foto do usuário") [Leo V 🇭🇰](https://twitter.com/1leonca) | 08/10/2018 | 0.284 (182/641) | 5320 |
| ![alt text](http://pbs.twimg.com/profile_images/1347881714908073984/v4lOfhCJ_normal.jpg "foto do usuário") [Gaspa](https://twitter.com/gasplosion) | 01/07/2009 | 0.174 (334/1924) | 8455 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Jose Luiz Ferreira](https://twitter.com/ferreiraimbe1) | 22/08/2014 | 0.25 (3/12) | 7 |
| ![alt text](http://pbs.twimg.com/profile_images/480077522248294401/OBVftxBa_normal.jpeg "foto do usuário") [Dedé](https://twitter.com/Dede_Brasil) | 16/07/2011 | 4.5 (162/36) | 699 |
| ![alt text](http://pbs.twimg.com/profile_images/1089349993754963968/0xt-lYsQ_normal.jpg "foto do usuário") [FRANCISCO](https://twitter.com/opinionatico) | 26/01/2019 | 0.831 (564/679) | 5936 |
| ![alt text](http://pbs.twimg.com/profile_images/536531963747000320/wJDi6hgn_normal.jpeg "foto do usuário") [denize caputo](https://twitter.com/denizecaputo) | 23/09/2013 | 0.769 (30/39) | 1419 |
| ![alt text](http://pbs.twimg.com/profile_images/1397846036/Imagem_011_normal.jpg "foto do usuário") [Socorro Oliveira](https://twitter.com/socorrinho02) | 15/06/2011 | 0.202 (108/535) | 18741 |
| ![alt text](http://pbs.twimg.com/profile_images/697265499231625216/W4vjNRUA_normal.jpg "foto do usuário") [Joe](https://twitter.com/argusvalgard) | 15/01/2010 | 0.107 (3/28) | 202 |
| ![alt text](http://pbs.twimg.com/profile_images/1347905408694972416/vs8Ug37T_normal.jpg "foto do usuário") [Antônio Figueiredo](https://twitter.com/antoniofilh6921) | 20/01/2011 | 0.991 (320/323) | 4061 |
| ![alt text](http://pbs.twimg.com/profile_images/1353879863191613440/_jpN2KQ6_normal.jpg "foto do usuário") [arthurkkk](https://twitter.com/arthuraguii) | 29/03/2016 | 0.695 (153/220) | 3294 |
| ![alt text](http://pbs.twimg.com/profile_images/1818652548/mavitechi_normal.jpg "foto do usuário") [marco vinicio](https://twitter.com/mavitechi) | 28/01/2012 | 0.25 (11/44) | 1928 |
| ![alt text](http://pbs.twimg.com/profile_images/727320893974786048/pA4K37ep_normal.jpg "foto do usuário") [ROSA VON](https://twitter.com/RosalyVonp) | 21/06/2015 | 1.177 (686/583) | 31560 |
| ![alt text](http://pbs.twimg.com/profile_images/1342666292155834368/YIkiMWnA_normal.jpg "foto do usuário") [EricaOrnellas🇧🇷](https://twitter.com/ornellaserica) | 18/02/2014 | 0.656 (1160/1768) | 19668 |
| ![alt text](http://pbs.twimg.com/profile_images/1183573162874802178/xUinth5t_normal.jpg "foto do usuário") [Lu Pinheiro](https://twitter.com/LuPinheiro73) | 06/01/2019 | 0.662 (239/361) | 8202 |
| ![alt text](http://pbs.twimg.com/profile_images/900526966478163968/7lJsOXP2_normal.jpg "foto do usuário") [Jailço Jagunço](https://twitter.com/Jailcojagunco) | 28/02/2017 | 0.085 (347/4092) | 8914 |
| ![alt text](http://pbs.twimg.com/profile_images/1129038416845393920/S0sOrhOZ_normal.jpg "foto do usuário") [Lucs](https://twitter.com/Luc4355) | 05/11/2017 | 0.808 (413/511) | 6548 |
| ![alt text](http://pbs.twimg.com/profile_images/1293263952416309256/gw16tO8k_normal.jpg "foto do usuário") [🕊️ FELIPE LIMA🕊️VACINA JÁ 💉🇺🇳✊🏼](https://twitter.com/1FLP7) | 06/07/2009 | 0.909 (4944/5440) | 29313 |
| ![alt text](http://pbs.twimg.com/profile_images/1141904699014221827/79fW-PBl_normal.jpg "foto do usuário") [Contra o politicamente correto.](https://twitter.com/chatopracarakas) | 08/09/2018 | 0.315 (63/200) | 838 |
| ![alt text](http://pbs.twimg.com/profile_images/1058164014981832714/f1079tOB_normal.jpg "foto do usuário") [Vem tranquilo](https://twitter.com/raphilxvasco) | 04/10/2011 | 0.124 (32/258) | 7226 |
| ![alt text](http://pbs.twimg.com/profile_images/1345154041865768961/2arW_GDt_normal.jpg "foto do usuário") [Victor®](https://twitter.com/Victor_com) | 25/09/2009 | 2.4 (9340/3892) | 10120 |
| ![alt text](http://pbs.twimg.com/profile_images/1107271046854516736/dQpvyflu_normal.jpg "foto do usuário") [#Bettina](https://twitter.com/BettinaRica22) | 16/03/2019 | 2.31 (335/145) | 370 |
| ![alt text](http://pbs.twimg.com/profile_images/1351377043905249282/ziv66IZF_normal.jpg "foto do usuário") [RODRIGO CORRÊA](https://twitter.com/Rodrigo_Correaa) | 19/08/2009 | 0.474 (499/1053) | 8069 |
| ![alt text](http://pbs.twimg.com/profile_images/1268666767846539268/y_MdmukR_normal.jpg "foto do usuário") [Fernandinho  STZ](https://twitter.com/fernandinhoSTZ) | 10/07/2009 | 0.409 (414/1012) | 15691 |
| ![alt text](http://pbs.twimg.com/profile_images/1124850682597715969/vNCHDhZJ_normal.jpg "foto do usuário") [Armas da Liberdade 🇺🇦🦞🦞](https://twitter.com/ArmasLiberdade) | 27/08/2018 | 0.756 (668/884) | 13779 |
| ![alt text](http://pbs.twimg.com/profile_images/1131008739732021248/goMVgxnz_normal.png "foto do usuário") [Tupiniquim do Sul 🇧🇷 🇺🇸](https://twitter.com/TupiniquimS) | 16/12/2014 | 4.255 (5902/1387) | 266113 |
| ![alt text](http://pbs.twimg.com/profile_images/1302265866889949187/rwBgduj4_normal.jpg "foto do usuário") [Bolsonéas](https://twitter.com/Bolsoneas) | 13/04/2017 | 507.427 (242550/478) | 9905 |
| ![alt text](http://pbs.twimg.com/profile_images/1297883573840744449/KAuAD43o_normal.jpg "foto do usuário") [fruta do conde](https://twitter.com/carlaatta) | 16/05/2014 | 0.373 (224/600) | 2976 |
| ![alt text](http://pbs.twimg.com/profile_images/1342827966259208193/H0UqySaF_normal.jpg "foto do usuário") [╭⊱🌷⊱╯Zulєikα ❁╭⊱🌷⊱╯](https://twitter.com/_ZuleikaBrand_) | 21/10/2018 | 1.059 (3923/3706) | 30872 |
| ![alt text](http://pbs.twimg.com/profile_images/423822588758880256/SsvVGe-W_normal.jpeg "foto do usuário") [Renato ️🇧🇷 🇮🇹️ 🇺🇲️ 🇨🇦️ 🇳🇱️️ 🇩🇪️ 🇨🇭️](https://twitter.com/RenatoVix_) | 11/07/2009 | 1.174 (2846/2424) | 52615 |
| ![alt text](http://pbs.twimg.com/profile_images/1330319182332899333/4_c6ML0G_normal.jpg "foto do usuário") [Mister Eme -Bibliotecário e de direita!](https://twitter.com/Ismabiblio) | 09/11/2013 | 0.555 (227/409) | 1292 |
| ![alt text](http://pbs.twimg.com/profile_images/1106737022063050752/74jHwLEH_normal.png "foto do usuário") [Metal Core da Colina](https://twitter.com/narduccif5) | 22/12/2014 | 0.417 (221/530) | 15852 |
| ![alt text](http://pbs.twimg.com/profile_images/1114323873481281536/iuposKsd_normal.jpg "foto do usuário") [O BRASIL TEM PRESSA 🇧🇷🇧🇷🇧🇷](https://twitter.com/bitsagrado) | 06/04/2018 | 0.083 (58/697) | 902 |
| ![alt text](http://pbs.twimg.com/profile_images/788126445478477824/pXXRcEI7_normal.jpg "foto do usuário") [Alzira almeida](https://twitter.com/AlmeidaAlzira) | 07/02/2012 | 0.971 (5781/5956) | 336124 |
| ![alt text](http://pbs.twimg.com/profile_images/1283483475375423490/Yxz5eeAH_normal.jpg "foto do usuário") [joaquim](https://twitter.com/quimrj) | 16/11/2009 | 0.403 (255/633) | 8139 |
| ![alt text](http://pbs.twimg.com/profile_images/482591013333000192/btyDUd4n_normal.jpeg "foto do usuário") [João Luiz Vidigal](https://twitter.com/Chantecler) | 11/08/2009 | 0.588 (1701/2895) | 36681 |
| ![alt text](http://pbs.twimg.com/profile_images/703014663697604608/21aOl72c_normal.jpg "foto do usuário") [jose henrique](https://twitter.com/josehenriquejhp) | 06/12/2011 | 0.291 (57/196) | 18992 |
| ![alt text](http://pbs.twimg.com/profile_images/1189744075915833345/247UZ8wA_normal.jpg "foto do usuário") [Fe Zonzini](https://twitter.com/fe_zonzini) | 13/11/2015 | 1.021 (347/340) | 1728 |
| ![alt text](http://pbs.twimg.com/profile_images/1323741789774381056/MjL0dhbe_normal.jpg "foto do usuário") [Robson de Morais🇧🇷🇮🇱🇺🇸](https://twitter.com/MoraisRobsonS) | 18/11/2015 | 0.639 (1562/2445) | 9954 |
| ![alt text](http://pbs.twimg.com/profile_images/1271974284475404293/sZs_K70X_normal.jpg "foto do usuário") [Dom Vito Andolini](https://twitter.com/Dom_Andollini) | 13/01/2018 | 20.448 (28239/1381) | 64617 |
| ![alt text](http://pbs.twimg.com/profile_images/1238862720054804485/1Cwi_uPU_normal.jpg "foto do usuário") [🇧🇷 Ale Lagares 🇧🇷](https://twitter.com/alelagares) | 28/07/2009 | 0.956 (9978/10439) | 14658 |
| ![alt text](http://pbs.twimg.com/profile_images/1348632599867125763/gcIpJmaX_normal.jpg "foto do usuário") [ℭ𝔬𝔫𝔰𝔢𝔯𝔳𝔞𝔡𝔬𝔯 🇧🇷🔞](https://twitter.com/ConservadorBP) | 30/06/2010 | 1.768 (297/168) | 7539 |
| ![alt text](http://pbs.twimg.com/profile_images/1289749592880427009/pI-5ZFVB_normal.jpg "foto do usuário") [Cynthia YAUH 🇧🇷🇺🇸](https://twitter.com/cypessoa22) | 20/06/2014 | 0.613 (310/506) | 8349 |
| ![alt text](http://pbs.twimg.com/profile_images/1355525314458345473/akYPS-5G_normal.jpg "foto do usuário") [M.](https://twitter.com/joaomassari) | 21/01/2010 | 0.281 (263/937) | 8952 |
| ![alt text](http://pbs.twimg.com/profile_images/1303171194716389377/42RZKL0x_normal.jpg "foto do usuário") [ELIANNE O C R](https://twitter.com/ELIANNEOCR) | 18/10/2011 | 0.846 (766/905) | 21102 |
| ![alt text](http://pbs.twimg.com/profile_images/1352602635099111433/4Gpphek3_normal.jpg "foto do usuário") [HIDROXICLOROQUINA ABANDONADA](https://twitter.com/CloroquinaAband) | 24/03/2013 | 3.688 (3216/872) | 4939 |
| ![alt text](http://pbs.twimg.com/profile_images/1249218435093090304/cdTC5hH8_normal.jpg "foto do usuário") [ⓟ MÁRCIO 🐷 🔟🏆🇧🇷](https://twitter.com/MarcioPisos) | 06/07/2011 | 0.335 (372/1109) | 17965 |
| ![alt text](http://pbs.twimg.com/profile_images/1265965820934533120/O6VKDg7-_normal.jpg "foto do usuário") [Mauro Aliança pelo Brasil](https://twitter.com/Maurobr38) | 01/08/2011 | 0.739 (1719/2326) | 8683 |
| ![alt text](http://pbs.twimg.com/profile_images/1241824364338839552/3yvEOs-Q_normal.jpg "foto do usuário") [K@rinemmmsantos 🌹🇧🇷](https://twitter.com/Karinemmmsantos) | 01/01/2018 | 0.983 (5049/5138) | 24742 |
| ![alt text](http://pbs.twimg.com/profile_images/1144647206835806210/V0BAA9Jg_normal.jpg "foto do usuário") [alex🇧🇷🇺🇸🇮🇱 1️⃣7️⃣ 🧂👌🏼👑🐸](https://twitter.com/alexsandersche1) | 19/05/2018 | 0.706 (1260/1784) | 14586 |
| ![alt text](http://pbs.twimg.com/profile_images/1297724536780136455/dOYRHo61_normal.jpg "foto do usuário") [Andre RB](https://twitter.com/AndreRicBrasil) | 09/10/2009 | 3.516 (21822/6206) | 84895 |
| ![alt text](http://pbs.twimg.com/profile_images/1102782546692194304/Qdc1Nh-a_normal.png "foto do usuário") [Anderson Freitas](https://twitter.com/Anderso76840389) | 02/03/2019 | 0.207 (23/111) | 512 |
| ![alt text](http://pbs.twimg.com/profile_images/867343719984496641/CZblo_ye_normal.jpg "foto do usuário") [👉👉membro: F.O.D e GDO Miliciano Golpista✌🏻](https://twitter.com/gfcaa) | 08/07/2009 | 0.927 (5079/5481) | 67371 |
| ![alt text](http://pbs.twimg.com/profile_images/1351327476602048512/Xp_A5PZT_normal.jpg "foto do usuário") [Alessandra Terra 🥼🇧🇷](https://twitter.com/AleTerraSouza) | 18/10/2018 | 1.408 (3448/2448) | 30804 |
| ![alt text](http://pbs.twimg.com/profile_images/1253885926742339584/R6mWmjGn_normal.jpg "foto do usuário") [🇧🇷Antonio Soave🇧🇷](https://twitter.com/rurusoave) | 09/10/2016 | 0.728 (657/902) | 8988 |
| ![alt text](http://pbs.twimg.com/profile_images/1068294883897737216/7kMkMybc_normal.jpg "foto do usuário") [Sérgio Mota](https://twitter.com/Sergio18082013) | 18/08/2013 | 0.362 (88/243) | 25307 |
| ![alt text](http://pbs.twimg.com/profile_images/1300980779456040961/l9Hdh8mV_normal.jpg "foto do usuário") [Silvana Violi](https://twitter.com/Silvana07574917) | 18/09/2018 | 0.706 (579/820) | 4640 |
| ![alt text](http://pbs.twimg.com/profile_images/960186021274095616/zQnyagkP_normal.jpg "foto do usuário") [L.I.M.P.E  BR](https://twitter.com/BrasilLibre) | 11/05/2014 | 1.045 (1018/974) | 100935 |
| ![alt text](http://pbs.twimg.com/profile_images/1060143773584445440/19dZ_nUI_normal.jpg "foto do usuário") [Rozeli Borges Duarte](https://twitter.com/BorgesRozeli) | 12/07/2017 | 0.0 (0/69) | 77 |
| ![alt text](http://pbs.twimg.com/profile_images/612696192967782400/G6pij2Jz_normal.jpg "foto do usuário") [Globe Underground](https://twitter.com/globeUndergroun) | 21/06/2015 | 2.081 (1051/505) | 892 |
| ![alt text](http://pbs.twimg.com/profile_images/1337398388057399296/SsceZUYJ_normal.jpg "foto do usuário") [elizio figueiredo](https://twitter.com/elizioenfase) | 06/07/2009 | 0.89 (1062/1193) | 19819 |
| ![alt text](http://pbs.twimg.com/profile_images/888558155856318464/0ezeRmbj_normal.jpg "foto do usuário") [J. Sepúlveda](https://twitter.com/radardamidia) | 23/04/2008 | 28.51 (124390/4363) | 17276 |
| ![alt text](http://pbs.twimg.com/profile_images/1330953824824156164/9XtQmkuu_normal.jpg "foto do usuário") [Diogo Pires](https://twitter.com/Diogo_Pires_) | 25/07/2009 | 0.24 (99/412) | 1279 |
| ![alt text](http://pbs.twimg.com/profile_images/1298348157059899392/sSivLFPL_normal.jpg "foto do usuário") [𝓐𝓵𝓮𝓼𝓼𝓪𝓷𝓭𝓻𝓸 𝓒𝓮𝔃𝓪𝓻𝓲𝓸🇧🇷](https://twitter.com/cezarioale) | 09/10/2013 | 0.668 (3165/4736) | 5022 |
| ![alt text](http://pbs.twimg.com/profile_images/908113225845297154/fP0bE6OC_normal.jpg "foto do usuário") [Arrogante é o teu cu, eu sou é sincero](https://twitter.com/f_pedo) | 23/07/2015 | 0.422 (68/161) | 2294 |
| ![alt text](http://pbs.twimg.com/profile_images/1052978046867787776/_1NvBawf_normal.jpg "foto do usuário") [Marek Egles da Silva](https://twitter.com/IMarekyI) | 16/05/2018 | 0.328 (60/183) | 1078 |
| ![alt text](http://pbs.twimg.com/profile_images/1128104646944407555/iX6oSa_b_normal.png "foto do usuário") [Pedro Camargo🇧🇷®️😎👉](https://twitter.com/pecamargo) | 25/06/2009 | 0.908 (4654/5124) | 87442 |
| ![alt text](http://pbs.twimg.com/profile_images/1298036276969472000/Iftk-dzF_normal.jpg "foto do usuário") [Savio Dom 🇧🇷](https://twitter.com/saviodom) | 15/08/2009 | 0.967 (4755/4916) | 14796 |
| ![alt text](http://pbs.twimg.com/profile_images/1282078176852746240/w3omMV9r_normal.jpg "foto do usuário") [Sirley ⓟ 🇧🇷🇧🇷🇧🇷🇧🇷🇧🇷🇧🇷💚🐷](https://twitter.com/sirleyvolps) | 23/07/2014 | 0.837 (3252/3883) | 35765 |
| ![alt text](http://pbs.twimg.com/profile_images/1002718177422446592/P_tm2FqS_normal.jpg "foto do usuário") [João](https://twitter.com/jhoao) | 02/04/2009 | 0.853 (4064/4764) | 215066 |
| ![alt text](http://pbs.twimg.com/profile_images/1347865644344205314/qMPqnY7R_normal.jpg "foto do usuário") [( ͡° ͜ʖ ͡°)🇧🇷](https://twitter.com/murphybr2009) | 13/06/2009 | 2.886 (1241/430) | 200510 |
| ![alt text](http://pbs.twimg.com/profile_images/1329961797374373894/ziifyUrf_normal.jpg "foto do usuário") [Romário](https://twitter.com/serjiomiro) | 14/01/2017 | 0.202 (309/1529) | 56725 |
| ![alt text](http://pbs.twimg.com/profile_images/1337780400882638848/iFek1RcL_normal.jpg "foto do usuário") [leonel berto](https://twitter.com/leonelberto) | 04/02/2011 | 0.944 (1155/1223) | 9281 |
| ![alt text](http://pbs.twimg.com/profile_images/1165080661046300677/RqldYq77_normal.jpg "foto do usuário") [Fernando Grieco 🇧🇷](https://twitter.com/GriecoFernando) | 17/11/2018 | 0.764 (1322/1731) | 9994 |
| ![alt text](http://pbs.twimg.com/profile_images/796318927051694080/noa2EevC_normal.jpg "foto do usuário") [Maria Luiza Dentzien](https://twitter.com/Mluizadentzien) | 07/11/2016 | 0.61 (1199/1965) | 18305 |
| ![alt text](http://pbs.twimg.com/profile_images/1256266688397524996/tjfWDcFV_normal.jpg "foto do usuário") [FabMary](https://twitter.com/FabyanaMaria3) | 31/07/2017 | 0.562 (41/73) | 3293 |
| ![alt text](http://pbs.twimg.com/profile_images/428490377981460482/su3drVYh_normal.png "foto do usuário") [Rezar App](https://twitter.com/AppRezar) | 29/01/2014 | 0.01 (1169/0) | 10556 |
| ![alt text](http://pbs.twimg.com/profile_images/1052278332061085696/yN6PCeI7_normal.jpg "foto do usuário") [Sá Robô da Direita - trabalhando de graça](https://twitter.com/Samira11896041) | 08/10/2018 | 0.442 (327/740) | 6145 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [David](https://twitter.com/David44981181) | 21/03/2017 | 0.692 (240/347) | 4567 |
| ![alt text](http://pbs.twimg.com/profile_images/1084905884864704520/dIvouxFm_normal.jpg "foto do usuário") [Márcio](https://twitter.com/Mrcio05721560) | 14/01/2019 | 0.044 (2/45) | 639 |
| ![alt text](http://pbs.twimg.com/profile_images/1307159581320261633/NLn9159V_normal.jpg "foto do usuário") [Ragnedite](https://twitter.com/Ragnedite) | 07/07/2009 | 0.188 (173/918) | 5473 |
| ![alt text](http://pbs.twimg.com/profile_images/1329849712447533063/GFY5IGPR_normal.jpg "foto do usuário") [Hébão™ 🇧🇷](https://twitter.com/HebaoTM) | 03/12/2009 | 0.588 (137/233) | 3407 |
| ![alt text](http://pbs.twimg.com/profile_images/606577527155511296/-OFQdqaY_normal.jpg "foto do usuário") [MarcioM](https://twitter.com/MarcioA53993017) | 24/01/2015 | 0.25 (5/20) | 152 |
| ![alt text](http://pbs.twimg.com/profile_images/1080799342838063105/n5wnOBJD_normal.jpg "foto do usuário") [André Bento](https://twitter.com/AndrBen36332023) | 03/01/2019 | 0.289 (44/152) | 208 |
| ![alt text](http://pbs.twimg.com/profile_images/1164675286828556293/7Y34oWxg_normal.jpg "foto do usuário") [🇧🇷🇺🇸🇮🇱🇵🇱🇭🇺🇯🇵](https://twitter.com/suzuki_sk) | 12/07/2017 | 0.299 (129/431) | 9663 |
| ![alt text](http://pbs.twimg.com/profile_images/1015948339425218560/_rNAOdHl_normal.jpg "foto do usuário") [Wilson Salvador](https://twitter.com/WilsonS08039793) | 05/07/2018 | 2.37 (538/227) | 78426 |
| ![alt text](http://pbs.twimg.com/profile_images/938230224982028288/lK1TDxtt_normal.jpg "foto do usuário") [Tiamat](https://twitter.com/Tiamat_o_PT) | 22/11/2009 | 0.714 (140/196) | 14563 |
| ![alt text](http://pbs.twimg.com/profile_images/1001862065605267456/rdWiNCkU_normal.jpg "foto do usuário") [Fabio](https://twitter.com/Fabio68995622) | 26/05/2018 | 0.016 (17/1078) | 6892 |
| ![alt text](http://pbs.twimg.com/profile_images/1189898143174995973/4FKHW5uq_normal.jpg "foto do usuário") [Carlos Eduardo Miranda](https://twitter.com/eduardobuffalob) | 31/12/2017 | 0.345 (149/432) | 1246 |
| ![alt text](http://pbs.twimg.com/profile_images/1260996057867210753/Q1jAZPKd_normal.jpg "foto do usuário") [Newton Junior](https://twitter.com/newtonsilvajun) | 06/09/2016 | 0.135 (43/318) | 4339 |
| ![alt text](http://pbs.twimg.com/profile_images/1092422124013346817/HQmc38QD_normal.jpg "foto do usuário") [André Casteliano](https://twitter.com/andrecasteliano) | 12/03/2008 | 0.61 (1877/3079) | 30240 |
| ![alt text](http://pbs.twimg.com/profile_images/1328398773731680258/T8dCcS2y_normal.jpg "foto do usuário") [O POVO TEM QUE USAR O PODER QUE TEM!](https://twitter.com/RightPatriotaBr) | 25/03/2015 | 0.887 (1414/1595) | 16846 |
| ![alt text](http://pbs.twimg.com/profile_images/1183216515128188928/O3Wb9Xqb_normal.jpg "foto do usuário") [Cristiana Alexandrevna Menshova](https://twitter.com/CrisMenshova) | 14/10/2014 | 3.973 (63998/16107) | 45668 |
| ![alt text](http://pbs.twimg.com/profile_images/496029267931959296/9dc_XazJ_normal.jpeg "foto do usuário") [𝐶𝑒𝑠𝑎𝑟 𝑀𝑒𝑛𝑑𝑜𝑛ç𝑎 🇧🇷](https://twitter.com/cmendoncasp1) | 03/08/2014 | 0.896 (3831/4275) | 33579 |
| ![alt text](http://pbs.twimg.com/profile_images/1118167349234995207/eEjAiCsx_normal.jpg "foto do usuário") [Rodrigo Carlos Feitosa](https://twitter.com/Rodriggocfs) | 24/09/2017 | 0.163 (33/202) | 1474 |
| ![alt text](http://pbs.twimg.com/profile_images/1070555544690352128/JEMHaZLr_normal.jpg "foto do usuário") [GastãoSN](https://twitter.com/gastaosn) | 18/11/2016 | 1.021 (5033/4931) | 28378 |
| ![alt text](http://pbs.twimg.com/profile_images/1162847568117846016/-uPBRxUq_normal.jpg "foto do usuário") [🇬🇧 Saito Miyamoto 🏳‍🌈](https://twitter.com/NpdSaito) | 08/01/2013 | 0.657 (69/105) | 7027 |
| ![alt text](http://pbs.twimg.com/profile_images/1260343653425459201/5dBtmRAi_normal.jpg "foto do usuário") [Renan](https://twitter.com/renan_de) | 20/02/2010 | 0.506 (683/1350) | 29634 |
| ![alt text](http://pbs.twimg.com/profile_images/649588141238697984/0Dt_ViEQ_normal.jpg "foto do usuário") [Marcos Silva - gab.ai/MROBERTO2018](https://twitter.com/mroberto_2015) | 02/05/2010 | 0.338 (138/408) | 6761 |
| ![alt text](http://pbs.twimg.com/profile_images/1352433598113206274/pNb8tByO_normal.jpg "foto do usuário") [Kevin](https://twitter.com/deliriosdokevin) | 25/06/2010 | 1.714 (264/154) | 4650 |
| ![alt text](http://pbs.twimg.com/profile_images/1353738540195192833/sUU1POyU_normal.jpg "foto do usuário") [𝕮𝖍𝖆𝖔𝖙𝖎𝖈 𝕰𝖓𝖊𝖗𝖌𝖞](https://twitter.com/Drcaoz_) | 03/04/2018 | 0.246 (330/1343) | 34658 |
| ![alt text](http://pbs.twimg.com/profile_images/1151865373727367173/wn8hFsw7_normal.jpg "foto do usuário") [rafael weber](https://twitter.com/rafweber) | 07/10/2012 | 0.339 (444/1309) | 920 |
| ![alt text](http://pbs.twimg.com/profile_images/1046559546553106432/AaeKSQ7p_normal.jpg "foto do usuário") [Marcos barbosa](https://twitter.com/Marcosbmaradona) | 03/04/2018 | 0.105 (26/247) | 756 |
| ![alt text](http://pbs.twimg.com/profile_images/1047311615358590977/EX116yyH_normal.jpg "foto do usuário") [Jorge](https://twitter.com/Jorge93113625) | 10/08/2018 | 0.318 (61/192) | 574 |
| ![alt text](http://pbs.twimg.com/profile_images/1272130927242723330/TiAKTC-1_normal.jpg "foto do usuário") [®o 🚲](https://twitter.com/rtg_celestino) | 08/06/2010 | 0.293 (138/471) | 5294 |
| ![alt text](http://pbs.twimg.com/profile_images/986566831560380416/7SoQfEB1_normal.jpg "foto do usuário") [Alexandre Grilo](https://twitter.com/realmenteinutil) | 18/02/2008 | 0.294 (166/564) | 4558 |
| ![alt text](http://pbs.twimg.com/profile_images/1340829648633081856/HmARnKlL_normal.jpg "foto do usuário") [Lino Machado](https://twitter.com/LinoMachadoLM) | 22/12/2010 | 0.322 (118/366) | 3937 |
| ![alt text](http://pbs.twimg.com/profile_images/817010824/bender3_normal.jpg "foto do usuário") [joao zug](https://twitter.com/zugbr) | 04/06/2009 | 0.059 (54/922) | 2727 |
| ![alt text](http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png "foto do usuário") [Juvenil](https://twitter.com/NevesJuvenil) | 19/11/2016 | 1.162 (1467/1262) | 182422 |
| ![alt text](http://pbs.twimg.com/profile_images/1242924121656381442/zAQwe6WQ_normal.jpg "foto do usuário") [Teid 🇧🇷🇺🇦](https://twitter.com/0Teid) | 26/04/2009 | 1.087 (373/343) | 4125 |
| ![alt text](http://pbs.twimg.com/profile_images/962007896392282114/oyeHEX7E_normal.jpg "foto do usuário") [bernardorenault](https://twitter.com/bernardorenault) | 09/02/2018 | 0.151 (62/410) | 965 |
| ![alt text](http://pbs.twimg.com/profile_images/1355218979690844165/I0Ev2qcP_normal.jpg "foto do usuário") [Shelldon 🔴⚫](https://twitter.com/ShelldonCRF) | 15/06/2009 | 1.047 (2772/2647) | 95122 |
| ![alt text](http://pbs.twimg.com/profile_images/980911501392449536/m52rX82i_normal.jpg "foto do usuário") [Pavel Kohout](https://twitter.com/KohoutPavel) | 13/03/2012 | 5.43 (11272/2076) | 26528 |
| ![alt text](http://pbs.twimg.com/profile_images/1297936423/pedro2010_43_twitter_normal.jpg "foto do usuário") [Pedro Tomaz Alves](https://twitter.com/pedrotomazalves) | 04/04/2010 | 0.234 (396/1690) | 2125 |
| ![alt text](http://pbs.twimg.com/profile_images/1131278491784228865/KTNP9olJ_normal.jpg "foto do usuário") [Ilan Robson](https://twitter.com/ilan_robson) | 26/08/2009 | 0.553 (426/771) | 6482 |
| ![alt text](http://pbs.twimg.com/profile_images/973966059064713217/j3JLPq8q_normal.jpg "foto do usuário") [fhhhjggkgfhmch](https://twitter.com/gghhhdgvcbjj) | 14/03/2018 | 0.01 (0/0) | 0 |
| ![alt text](http://pbs.twimg.com/profile_images/1314800381218693121/LDO_H-VU_normal.jpg "foto do usuário") [Freud](https://twitter.com/ZecSant) | 13/08/2009 | 0.242 (284/1175) | 10119 |
| ![alt text](http://pbs.twimg.com/profile_images/2356226175/02_by_andyparkart_normal.jpg "foto do usuário") [Marcos Vinícius](https://twitter.com/marcos_mvcn) | 30/06/2012 | 0.116 (359/3088) | 1707 |
| ![alt text](http://pbs.twimg.com/profile_images/1355449527466078208/hx4LnrhZ_normal.jpg "foto do usuário") [Rodolfo](https://twitter.com/rytaufi) | 24/04/2015 | 2.615 (204/78) | 4527 |
| ![alt text](http://pbs.twimg.com/profile_images/1120403840929542147/QT0iX_KP_normal.jpg "foto do usuário") [Holybee](https://twitter.com/holybeesilver) | 18/05/2013 | 0.757 (427/564) | 4311 |
| ![alt text](http://pbs.twimg.com/profile_images/1202952508697694210/8l2EYn91_normal.png "foto do usuário") [฿tcandre](https://twitter.com/btcandre) | 05/06/2011 | 6338.364 (69722/11) | 58878 |
| ![alt text](http://pbs.twimg.com/profile_images/476741889727541248/P8Zk62sP_normal.jpeg "foto do usuário") [All About Travel](https://twitter.com/AllAbout_Travel) | 19/03/2009 | 0.977 (10913/11166) | 21437 |
| ![alt text](http://pbs.twimg.com/profile_images/1036293871897063424/aikUnJYJ_normal.jpg "foto do usuário") [Natalino Vegh](https://twitter.com/NatalinoVegh) | 15/01/2015 | 0.977 (126/129) | 5157 |
