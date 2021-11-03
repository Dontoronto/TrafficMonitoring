#!/usr/bin/env python

import yaml
import re

class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)



with open("environment.yml", "r") as stream:
    try:
        
        print(type(stream))
        #print(yaml.safe_dump_all(stream, line_break="   "))
        '''
        a = dict(yaml.safe_load_all(stream))
        print(a)
        for elem, key in a.items():
            #print(elem)
            print(key)'''

        
        a = yaml.safe_load_all(stream)
        
        with open('testfile.yml', 'w') as p:
        
            #b = yaml.dump_all(a,p, Dumper=MyDumper, default_flow_style=False)

            b = yaml.dump_all(a,indent=2, allow_unicode=True, default_flow_style=False, width=4)

            pre_text = b.split("\n")
            print(pre_text)
            #print(pre_text)
            new_text = ""

            for i in range(len(pre_text)):
                #new_text = new_text + "  " + snippet
                #snippet = "  " + snippet
                

                if(re.search("^[a-z]", pre_text[i])):
                    pass
                else:
                    if(re.search("=.*",pre_text[i])):
                        pre_text[i] = re.sub("=.*", "", pre_text[i])
                    pre_text[i] = "  " + pre_text[i]
                #new_text.join(str(pre_text[i]))
                #new_text.join("  " + pre_text[i])
                


            print('------------')
            #print(new_text)
            #print(pre_text)

            #print("\n".join(pre_text))

            finished_text = "\n".join(pre_text).replace('"',"")
            #print(finished_text)

            




            #yaml.safe_dump_all(finished_text,p,)
            p.write(finished_text)




            #yaml.dump_all(new_text,p)

            #print(b)
            #print(type(b))

        #print(yaml.safe_load(stream))
        #print(len(yaml.safe_load(stream)))
        
    except yaml.YAMLError as exc:
        print(exc)