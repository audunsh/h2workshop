#!/usr/bin/env python
# coding: utf-8

# # En modell basert på Newtons lover

# Vi skal nå utforme en modell basert på det som kalles klassisk fysikk. Vi kommer til å møte en del matematiske uttrykk her for å ikke gjemme bort detaljer, men ikke nøl med å hoppe rett til konklusjonen her og gå løs på simuleringen dersom det blir for mye.
# 
# ---
# 
# Vi har tidligere sett at den elektromagnetiske kraften mellom to ladde partikler, i vårt tilfelle elektronet $Q_e$ og protonet $Q_p$ kan utrykkes
# 
# $$
# \mathbf{F} = \frac{1}{4 \pi \varepsilon_0} \frac{Q_e Q_p}{r_{12}^2} \hat{\mathbf{r}}, 
# $$
# 
# Dermed kan vi for enhver avstand finne den tiltrekkende kraften mellom disse to partiklene. 
# 
# Om vi kombinerer dette med Newtons andre lov:
# 
# $$
# \mathbf{F} = m \mathbf{a} = \big{(}\frac{d}{dt} \big{)}^2 \mathbf{x}(t),
# $$
# 
# så får vi det som kalles en *differensiallikning* for $\mathbf{x}$:
# 
# $$
# \big{(}\frac{d}{dt} \big{)}^2 \mathbf{x}(t) = \frac{1}{4 \pi \varepsilon_0} \frac{Q_e Q_p}{r_{12}^2} \hat{\mathbf{r}}.
# $$
# 
# Vi har her også benyttet en <a href="https://no.wikipedia.org/wiki/Bevegelsesligning">klassisk bevegelseslikning</a>, som forteller oss at farten ved et tidspunkt $t$ ($\mathbf{v}$) er endring i posisjon ($\mathbf{x}$), og akselerasjon ($\mathbf{a}(t)$) er endring i fart:
# 
# $$
# \big{(}\frac{d}{dt} \big{)}^2 \mathbf{x}(t) = \frac{d}{dt} \mathbf{v}(t) = \mathbf{a}(t).
# $$
# 
# 
# Operasjonen $\frac{d}{dt}$ er en derivasjon (se ekstra materiale om nødvendig), og i uttrykket over gjør vi det to ganger:
# 
# $$
# \big{(}\frac{d}{dt} \big{)}^2 = \frac{d}{dt} \frac{d}{dt}.
# $$
# 
# # Konklusjon
# 
# Om vi overlater derivasjonsoperasjonen til datamaskinen kan vi finne et uttrykk for posisjonen til partiklene litt frem i tid. Du kan sammenlikne det med å gjøre følgende:
# 
# 1. Beregn kreftene som virker på elektronet og protonet. 
# 2. Finn akselerasjonen ved hjelp av Newtons annen lov.
# 3. Benytt akselerasjonen til å oppdatere farten til partikkelen.
# 4. Benytt farten til å oppdatere posisjonen til partikkelen.
# 5. For de nye posisjonene, gjenta punkt 1-5.
# 
# 
# 

# In[ ]:




