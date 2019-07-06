# RASA-projects
 Chatbots, contextual AI assistants

### **Prerequisites**
install anaconda 
###### Either create conda environment or use following commands on command line (terminal) directly
```
pip install rasa[spacy]
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```

### **Running of the Bot**
Use the following commands on the same command window
```
python training.py
python core.py
python -m rasa_core_sdk.endpoint --actions actions
```
Run this command on a fresh command window without closing the previous one
```
python runapp.py (on a new cmd window)
```
