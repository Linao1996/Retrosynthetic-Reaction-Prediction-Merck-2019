import re
from rdkit import Chem

def _smi2smi(string):
    string = re.sub(':\d*','',string)
    mol = Chem.MolFromSmiles(string)
    try:
        print(Chem.MolToSmiles(mol))
    except:
        print(string)
        raise
    return Chem.MolToSmiles(mol)

def smi2smi(string):
    string = re.sub(':\d*','',string)
    mol = Chem.MolFromSmiles(string)
    try:
        ret = Chem.MolToSmiles(mol)
    except:
        # print(string)
        ret = string
    return ret
    
def split_train_line(line):
    line = line.replace('\n', '')
    parts = line.split('>')
   
    reaction_id = parts[0].split(',')[0]
    reactant = parts[0].split(',')[1].split('.')
    
    reagent = parts[1].split('.')
    
    if len(parts[2].split(' ')) == 2:
        production = parts[2].split(' ')[0].split('.')
        xxx = parts[2].split(' ')[1]
    elif len(parts[2].split(' ')) == 1:
        production = [parts[2]]
        xxx = ''
    
    reaction = {
        'id': reaction_id,
        'reactant': list(map(smi2smi, reactant)),
        'reagent': list(map(smi2smi, reagent)),
        'production': list(map(smi2smi, production)),
        'xxx': xxx,
    }
    return reaction

def split_test_line(line):
    line = line.replace('\n', '')
    parts = line.split('>')
   
    reaction_id = parts[0].split(',')[0]
    reagent = parts[0].split(',')[1].split('.')

    if len(parts[1].split(' ')) == 2:
        production = parts[1].split(' ')[0].split('.')
        xxx = parts[1].split(' ')[1]
    elif len(parts[1].split(' ')) == 1:
        production = [parts[1]]
        xxx = ''
        
    reaction = {
        'id': reaction_id,
        'reagent': list(map(smi2smi, reagent)),
        'production': list(map(smi2smi, production)),
        'xxx': xxx,
    }
    return reaction