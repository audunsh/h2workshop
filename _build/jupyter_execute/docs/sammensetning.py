#!/usr/bin/env python
# coding: utf-8

# # Bestanddelene i hydrogen
# 
# En viktig brikke i vår forståelse av hva som holder molekyler og atomer sammen er at *ladede objekter trekker og dytter på hverandre* - det som kalles elektrostatiske vekselvirkninger.
# 
# Allerede på tidlig 1800-tall kjente forskere til at ladede objekter vekselvirker gjennom <a href="https://no.wikipedia.org/wiki/Coulombs_lov">Coulombs lov</a>. Kreftene som virker mellom to ladninger $Q_1$ og $Q_2$, separert med en avstand $r_{12}$ kan uttrykkes
# 
# $$
# \mathbf{F}_1 = \frac{1}{4 \pi \varepsilon_0} \frac{Q_1 Q_2}{r_{12}^2} \hat{\mathbf{r}}, \tag{2}
# $$
# 
# hvor $r_{12} = \vert \mathbf{r}_{12} \vert = \vert \mathbf{r}_1 - \mathbf{r}_2 \vert$ er abstanden mellom objektene, vektoren $\hat{\mathbf{r}} = \frac{\mathbf{r}_1 - \mathbf{r}_2}{r_{12}}$ er retningen mellom objektene og $\varepsilon_0$ er den såkalte elektriske konstanten. 
# 
# Atomer er i seg selv nøytrale (ingen ladning), men som vi skal se kan de under visse betingelser splittes opp i mindre bestanddeler med ladning.

# # Oppdagelsen av elektronet
# 
# I 1897 observerte den britiske fysikeren Joseph John Thomson at atomer kan sende ut partikler med negativ ladning. Ved å måle hvordan stråling fra såkalte <a href="https://no.wikipedia.org/wiki/Bilder%C3%B8r">katodestrålerør</a> bøyde av i elektriske felter kunne han både avgjøre at partiklene hadde negativ ladning, samt anslag partiklenes masse til å være langt lavere enn atomet som helhet. Disse partiklene har i dag fått navnet *elektroner*.
# 
# ````{margin}
# ![Rosinbolle](./graphics/plum_pudding_nobeam.png)
# I rosinbollemodellen består atomet av en negativt ladde elektroner i et hav av positiv ladning.
# ````
# Videre, ettersom atomene opprinnelig hadde vært nøytrale (ingen ladning) antok Thomson at atomer bestod av negative partikler som badet i et "hav" av positivt ladde partikler. Denne modellen har fått navnet *rosinbollemodellen* (på engelsk: *plum-pudding model*), hvor elektronene er rosinen i bolla.

# # Oppdagelsen av atomkjernen
# 
# ````{margin}
# ![Atomkjernen](./graphics/figure_2_nobeam.png)
# En massiv positivt ladd kjerne omgitt av lette, negativt ladde elektroner.
# ````
# Det hersket ikke enighet om rosinbollemodellen, og enkelte spekulerte i om en modell som lignet mer på solsystemet kunne ha noe for seg - en massiv positivt ladd kjerne omgitt av lette, negative elektroner.  
# 
# For å avgjøre dette spørsmålet ble <a href="https://en.wikipedia.org/wiki/Geiger%E2%80%93Marsden_experiments">en serie eksperimenter</a> gjennomført mellom 1908 og 1913 av Ernst Rutherford, Hans Geiger og Ernest Marsden, hvor de bestrålte gullfolie med positivt ladede partikler, som vist i figuren under.
# 
# 
# ```{figure} ./graphics/figure_1.png
# ---
# height: 400px
# name: figure_1
# ---
# Geiger-Marsden eksperimentet: gullfolie bestråles med positivt ladde partikler.
# ```
# 
# Rutherford forventet at dersom den positive ladningen var spredt utover hele atomet så ville den innkommende strålingen svakt endre retning på sin ferd gjennom materialet. Om den positive ladningen derimot var konsentrert i en massiv kjerne forventet han å se det meste av strålingen passere uanfektet gjennom materialet, med unntak av noen få stråler som ble kraftig spredt i ulike retninger. 
# 
# Som vist i figuren over var ble strålingen spredt i alle mulige retninger, noe selv i samme retning som det kom fra, så Rutherford konkluderte basert på dette med at atomet bestod av en massiv, positiv kjerne omgitt av relativt lette, negative elektroner.
# 
# 
# ```{admonition} Diskuter
# - Hvordan forklarer du de to utfallene Rutherford så for seg i lys av Coulombs lov (likning 2)? 
# - Finnes det andre mulige tolkninger av Rutherfords eksperiment? Kan du se for deg en annen modell som gir samme resultat? 
# ```
# 
# 

# In[1]:


import bubblebox as bb
import evince as ev
import numpy as np

hydrogen = bb.showcase.classical_hydrogen(vel_electron = np.array([0, 1.43, 0.0]))
hydrogen.size = np.array([2,2,2])

#hydrogen.advance = hydrogen.advance_euler

hydrogen.dt = 0.001

#hydrogen.v()

b = ev.spotlight.SpotlightView(hydrogen)

b.window_scale = 0.5
b

