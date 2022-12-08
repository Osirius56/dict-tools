import json
import argparse
import operator

__version__ = "0.0.1"

def compare(o1,o2):
    keys_diff = {key for key in o1.keys()}.symmetric_difference({key for key in o2.keys()}) # compare keys list
    return keys_diff

def sort_by_value(data:dict,sort_key:str):
    # Define Sorter Matrix
    sorter_matrix = []
    sortedData = {}
    
    # transform keys path with dotted expression to list
    splitted_keys = sort_key.split('.')
    
    # Read value from sort_key expression
    if isinstance(data,dict):
        for entry,nfo in data.items():
            if len(splitted_keys)>1:
                path = [f"['{key}']" for key in splitted_keys]
                sorter_matrix.append({sort_key: eval(f"nfo{''.join(path)}"),"object":entry})

    for foo in sorted(sorter_matrix, key=operator.itemgetter(sort_key)):
        sortedData.update({foo['object']:data[foo['object']]})

    return sortedData

if __name__ == "__main__":
    print(f"dict_utils version: {__version__}")
    
    parser = argparse.ArgumentParser(prog="Dictionary sorter",add_help=True)
    gp_compare = parser.add_argument_group('DIFF MODE')
    gp_sort = parser.add_argument_group('SORT By Value')
    
    gp_compare.add_argument("-d","--diff-mode",help="Choose Compare mode to identify (d)ifferences between two dict.",action="store_true")
    gp_compare.add_argument("-r","--reference-file",help="Define reference file.")
    gp_compare.add_argument("-c","--compare-file",help="Define file to compare at reference.")
    
    gp_sort.add_argument("-s","--sort-by-value")
    gp_sort.add_argument("-f","--file",type=str)

    parser.add_argument("-o", "--output", help="Define output file. if None result juste printed.", default=None)
    args = parser.parse_args()
 
    if args.diff_mode:
        if args.reference_file and args.compare_file:
            output = compare(args.reference_file,args.compare_file)

    elif args.sort_by_value:
        with open(args.file) as fp:
            data = json.load(fp)
        output = sort_by_value(data,args.sort_by_value)

    if args.output:
        with open(args.output,"w") as fp:
            json.dump(output,fp,indent=4)