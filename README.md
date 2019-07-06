# RASA-projects
 Chatbots, contextual AI assistants

### **Prerequisites**
1. install anaconda
Either create conda environment or use following commands on command line (terminal) directly
2. pip install rasa[spacy]
3. python -m spacy download en_core_web_md
4. python -m spacy link en_core_web_md en

### **Running of the Bot**
1. python training.py
2. python core.py
3. python -m rasa_core_sdk.endpoint --actions actions
4. python runapp.py (on a new cmd window)
