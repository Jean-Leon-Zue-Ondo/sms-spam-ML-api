 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
new file mode 100644
index 0000000000000000000000000000000000000000..939968d24e87cb16e6f6c3965f80976e4789be6c
--- /dev/null
+++ b/README.md
@@ -0,0 +1,46 @@
+# API de classification de SMS Spam
+
+Cette application expose un modèle de machine learning capable de classifier un message SMS comme **spam** ou **ham** (non-spam). Le modèle et le vectoriseur sont déjà enregistrés dans les fichiers `naive_bayes.pkl` et `vectorizer.pkl`.
+
+## Installation des dépendances
+
+Créez de préférence un environnement virtuel, puis installez les dépendances :
+
+```bash
+pip install -r requirements.txt
+```
+
+Si le fichier `requirements.txt` est vide, installez manuellement les dépendances essentielles :
+
+```bash
+pip install fastapi uvicorn scikit-learn joblib
+```
+
+## Lancement de l'API
+
+Démarrez l'API avec Uvicorn depuis la racine du projet :
+
+```bash
+uvicorn main:app --reload
+```
+
+L'API est alors disponible sur `http://localhost:8000`.
+
+## Exemple d'appel à l'endpoint `/predict`
+
+Envoyez une requête POST contenant un message SMS en JSON :
+
+```bash
+curl -X POST \
+  -H "Content-Type: application/json" \
+  -d '{"message": "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May"}' \
+  http://localhost:8000/predict
+```
+
+Réponse attendue :
+
+```json
+{"prediction": "spam"}
+```
+
+Cet exemple montre comment obtenir la prédiction ("spam" ou "ham") pour un message donné.
 
EOF
)
