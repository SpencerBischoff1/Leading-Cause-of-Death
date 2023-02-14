import xml.etree.ElementTree as ET

def main():
    tree = ET.parse('leading_causes_of_death.xml')
    root = tree.getroot()
    year = input("please enter a year: ")
    cod_list = []

    for row in root[0]:
        cod_list.append(process_rows(row))
    print_rows(cod_list,year)

    return

def process_rows(row):
    mydict = {}
    mydict['_id'] = row.get('_id')

    for subelem in row:
        mydict[subelem.tag] = subelem.text
    return mydict

def print_rows(row_list,year):
    for index, record in enumerate(row_list):
        if record['year']==year:
            print("Record {} (id: {}): During {} the leading cause of death in {} was {}".
                    format(index,record['_id'],year, record['state'], record['cause_name']))

if __name__=='__main__':
    main()
