import unicodedata

def remove_non_ascii_normalized(string: str) -> str:
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()

if __name__ == "__main__":
    string = 'A	AGRICULTURA, PECUÁRIA, PRODUÇÃO FLORESTAL, PESCA E AQÜICULTURA	01	AGRICULTURA, PECUÁRIA E SERVIÇOS RELACIONADOS	01.7	 Caça e serviços relacionados	01.70-9	 Caça e serviços relacionados	0170-9/00 	Caça e serviços relacionados'
    
    print(string)
    print(remove_non_ascii_normalized(string))

