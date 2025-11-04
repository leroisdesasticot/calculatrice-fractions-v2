<<<<<<< HEAD

import streamlit as st
from fractions import Fraction

st.set_page_config(page_title="Calculatrice Fractions", layout="centered")
st.title(" Calculatrice de fractions - Etapes Papier")
st.markdown("""
**Instructions :**  
- Entrez le numerateur et le denominateur de chaque fraction.  
- Choisissez l'operateur (+, -, *, /).  
- Les fractions s'afficheront avec des barres graphiques.
""")

# Colonnes pour les fractions
col1, col2 = st.columns([1,1])

with col1:
    a = st.number_input("Numerateur fraction 1", value=1, step=1)
    b = st.number_input("Denominateur fraction 1", value=1, min_value=1, step=1)

with col2:
    c = st.number_input("Numerateur fraction 2", value=1, step=1)
    d = st.number_input("Denominateur fraction 2", value=1, min_value=1, step=1)

op = st.selectbox("Operateur", ["+", "-", "*", "/"])

# Bouton pour calculer
if st.button("Calculer"):

    try:
        f1 = Fraction(a, b)
        f2 = Fraction(c, d)
        steps = f"**Calcul :**\n\n"

        # Affichage fraction graphique
        st.markdown(f"<div style='text-align:center; font-weight:bold;'>"
                    f"{a} / {b} {op} {c} / {d}</div>", unsafe_allow_html=True)

        # Calcul
        if op in ["+", "-"]:
            left = a*d
            right = b*c
            den = b*d
            sign = "+" if op=="+" else "-"
            result_num = left + right if op=="+" else left - right
            res = Fraction(result_num, den)
            steps += f"**Croisement :** {a}*{d} = {left}, {b}*{c} = {right}\n"
            steps += f"{left} {sign} {right}\n-----\n {den}\n"
            steps += f"= {result_num}/{den}\n"

        elif op == "*":
            num = a*c
            den = b*d
            res = Fraction(num, den)
            steps += f"**Multiplication :** {a}*{c}={num}, {b}*{d}={den}\n"
            steps += f"{num}\n-----\n{den}\n"

        else:  # Division
            num = a*d
            den = b*c
            if den == 0:
                st.error("Erreur : division par zero")
            res = Fraction(num, den)
            steps += f"**Division -> multiplier par l'inverse :** {a}/{b} * {d}/{c}\n"
            steps += f"{num}\n-----\n{den}\n"

        steps += f"\n**Resultat simplifie :** {res} = {res.numerator}/{res.denominator}\n"
        steps += f"**Decimal :** {float(res)}"

        st.markdown(f"<div style='background-color:#cce6ff; padding:10px; border-radius:10px; font-family:Courier;'>"
                    f"{steps.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)

    except Exception as e:
=======

import streamlit as st
from fractions import Fraction

st.set_page_config(page_title="Calculatrice Fractions", layout="centered")
st.title(" Calculatrice de fractions - Etapes Papier")
st.markdown("""
**Instructions :**  
- Entrez le numerateur et le denominateur de chaque fraction.  
- Choisissez l'operateur (+, -, *, /).  
- Les fractions s'afficheront avec des barres graphiques.
""")

# Colonnes pour les fractions
col1, col2 = st.columns([1,1])

with col1:
    a = st.number_input("Numerateur fraction 1", value=1, step=1)
    b = st.number_input("Denominateur fraction 1", value=1, min_value=1, step=1)

with col2:
    c = st.number_input("Numerateur fraction 2", value=1, step=1)
    d = st.number_input("Denominateur fraction 2", value=1, min_value=1, step=1)

op = st.selectbox("Operateur", ["+", "-", "*", "/"])

# Bouton pour calculer
if st.button("Calculer"):

    try:
        f1 = Fraction(a, b)
        f2 = Fraction(c, d)
        steps = f"**Calcul :**\n\n"

        # Affichage fraction graphique
        st.markdown(f"<div style='text-align:center; font-weight:bold;'>"
                    f"{a} / {b} {op} {c} / {d}</div>", unsafe_allow_html=True)

        # Calcul
        if op in ["+", "-"]:
            left = a*d
            right = b*c
            den = b*d
            sign = "+" if op=="+" else "-"
            result_num = left + right if op=="+" else left - right
            res = Fraction(result_num, den)
            steps += f"**Croisement :** {a}*{d} = {left}, {b}*{c} = {right}\n"
            steps += f"{left} {sign} {right}\n-----\n {den}\n"
            steps += f"= {result_num}/{den}\n"

        elif op == "*":
            num = a*c
            den = b*d
            res = Fraction(num, den)
            steps += f"**Multiplication :** {a}*{c}={num}, {b}*{d}={den}\n"
            steps += f"{num}\n-----\n{den}\n"

        else:  # Division
            num = a*d
            den = b*c
            if den == 0:
                st.error("Erreur : division par zero")
            res = Fraction(num, den)
            steps += f"**Division -> multiplier par l'inverse :** {a}/{b} * {d}/{c}\n"
            steps += f"{num}\n-----\n{den}\n"

        steps += f"\n**Resultat simplifie :** {res} = {res.numerator}/{res.denominator}\n"
        steps += f"**Decimal :** {float(res)}"

        st.markdown(f"<div style='background-color:#cce6ff; padding:10px; border-radius:10px; font-family:Courier;'>"
                    f"{steps.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)

    except Exception as e:
>>>>>>> 562c0b277f956f5d920f94b593761522750a6443
        st.error(f"Erreur : {e}")