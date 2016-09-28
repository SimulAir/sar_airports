#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jsain
#
# Created:     18/08/2016
# Copyright:   (c) jsain 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import json
    from pprint import pprint

    with open('airport_data.json') as data_file:
        data = json.load(data_file)

    pprint(data)
    x=data['response']
    y=x[0]
    print(y)
    print('Done')

if __name__ == '__main__':
    main()
